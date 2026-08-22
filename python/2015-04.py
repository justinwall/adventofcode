#!/usr/bin/env python3
# https://adventofcode.com/2015/day/4
import hashlib
from pathlib import Path


def part1(secret_key: str) -> int:
    i = 1
    while True:
        hash = hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()
        if hash.startswith("0" * 5):
            return i
        i += 1


def part2(secret_key: str) -> int:
    i = 1
    while True:
        hash = hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()
        if hash.startswith("0" * 6):
            return i
        i += 1


def main(input_file: Path) -> None:
    secret_key = input_file.read_text()

    print(part1(secret_key))
    print(part2(secret_key))


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent.parent / f"inputs/{Path(__file__).stem}.txt"
    main(input_file)
