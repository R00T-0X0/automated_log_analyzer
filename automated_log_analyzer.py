import re


def get_log_file():
    return input("Enter log file path: ").strip().strip('"')


def compile_patterns():
    return {
        "SQL Injection": re.compile(r"\bUNION\s+SELECT\b", re.IGNORECASE),
        "Path Traversal": re.compile(r"(?:\.\./)+etc/passwd", re.IGNORECASE),
    }


def extract_ip(log_line):
    match = re.search(r"^(\d{1,3}(?:\.\d{1,3}){3})\b", log_line)

    if match:
        return match.group(1)

    return "Unknown"


def analyze_line(log_line, line_number, patterns, attack_counts):
    attacker_ip = extract_ip(log_line)

    for attack_type, pattern in patterns.items():
        if re.search(pattern, log_line):
            attack_counts[attack_type] += 1
            print(
                f"[ALERT] {attack_type} detected | "
                f"Line: {line_number} | Source IP: {attacker_ip}"
            )


def analyze_log_file(file_path):
    patterns = compile_patterns()
    attack_counts = {attack_type: 0 for attack_type in patterns}

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as log_file:
            for line_number, log_line in enumerate(log_file, start=1):
                analyze_line(
                    log_line,
                    line_number,
                    patterns,
                    attack_counts
                )

    except FileNotFoundError:
        print("[!] Log file not found.")
        return None
    except PermissionError:
        print("[!] Permission denied: cannot read this file.")
        return None
    except OSError as error:
        print(f"[!] Could not read the log file: {error}")
        return None

    return attack_counts


def print_summary(attack_counts):
    total_attacks = sum(attack_counts.values())

    print("\n========== Analysis Summary ==========")
    print(f"Total detected attacks: {total_attacks}")

    for attack_type, count in attack_counts.items():
        print(f"{attack_type}: {count}")

    print("======================================")


def main():
    file_path = get_log_file()

    if not file_path:
        print("[!] Please enter a log file path.")
        return

    print(f"\n[*] Analyzing: {file_path}\n")

    attack_counts = analyze_log_file(file_path)

    if attack_counts is not None:
        print_summary(attack_counts)


if __name__ == "__main__":
    main()
