import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception:
        print("Помилка при читанні файлу.")
        return []
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<16} | {counts.get(level, 0)}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу.")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()