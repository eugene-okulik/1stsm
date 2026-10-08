import os
import argparse
from datetime import datetime
from collections import defaultdict


DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
DATE_LEN = 23

CONTEXT_WORDS = 5


def collect_files(path):
    if os.path.isfile(path):
        return [path]

    if os.path.isdir(path):
        log_files = []
        for file_name in os.listdir(path):
            full_path = os.path.join(path, file_name)
            if os.path.isfile(full_path):
                log_files.append(full_path)
        return log_files

    return []


def split_into_blocks(file_path):
    blocks = defaultdict(list)
    current_date = None

    with open(file_path, "r", encoding="utf-8") as logfile:
        for raw_line in logfile:
            clean_line = raw_line.rstrip("\n")

            if not clean_line.strip():
                continue

            date_part = clean_line[:DATE_LEN]

            try:
                block_date = datetime.strptime(date_part, DATE_FORMAT)
                current_date = block_date
                blocks[block_date].append(clean_line)
            except ValueError:
                if current_date is not None:
                    blocks[current_date].append(clean_line.strip())

    return blocks


def get_context(block_text, needle, context_words=CONTEXT_WORDS):
    all_words = block_text.split()

    for word_index, word in enumerate(all_words):
        if needle in word:
            start = max(0, word_index - context_words)
            end = min(len(all_words), word_index + context_words + 1)
            return " ".join(all_words[start:end])

    return None


def print_match(file_name, block_date, context):
    print(f"Файл: {file_name}")
    print(f"Время: {block_date}")
    print(f"Контекст: ...{context}...")
    print("-" * 60)


def analyze(path, needle):
    log_files = collect_files(path)

    if not log_files:
        print("Файлов не найдено по пути:", path)
        return 0

    matches_found = 0

    for file_path in log_files:
        blocks = split_into_blocks(file_path)
        file_name = os.path.basename(file_path)

        for block_date, lines in blocks.items():
            block_text = " ".join(lines)
            context = get_context(block_text, needle)

            if context is None:
                continue

            matches_found += 1
            print_match(file_name, block_date, context)

    return matches_found


def main():
    parser = argparse.ArgumentParser(description="Search for text in logs")
    parser.add_argument("path", help="Path to the log file or directory")
    parser.add_argument(
        "-t", "--text",
        required=True,
        help="Text to search for",
    )
    args = parser.parse_args()

    needle = args.text
    matches_found = analyze(args.path, needle)

    if matches_found == 0:
        print("Ничего не найдено")
    else:
        print(f"Всего совпадений: {matches_found}")


main()
