"""Write one loading-screen tip to /output/entry.txt.

Deterministic, stdlib only, no network.
"""

TIP = "Loading… your agent has read 40 files, forgotten three, and is confidently typing anyway. You're both winging it."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")
    import os

    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
