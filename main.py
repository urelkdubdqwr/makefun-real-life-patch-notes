import os

ENTRY_TEXT = (
    "v5.0.3: walking into a room no longer deletes the reason you walked in. "
    "The reason is now persisted. Retention: 4%.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as entry_file:
        entry_file.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
