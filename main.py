"""Out-of-office entry: print the reply stored in entry.txt."""

from pathlib import Path


MAX_CHARS = 200


def load_reply() -> str:
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8").strip()


def check_reply(text: str) -> str:
    """Enforce the bounty gate: 1-200 non-blank UTF-8 characters."""
    cleaned = " ".join(text.split())
    if not cleaned:
        raise ValueError("entry.txt is blank")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"reply is {len(cleaned)} chars, over the {MAX_CHARS} limit")
    return cleaned


def main() -> None:
    print(check_reply(load_reply()))


if __name__ == "__main__":
    main()
