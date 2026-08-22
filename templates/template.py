#!/usr/bin/env python3
# https://adventofcode.com/<year>/day/<day>
from pathlib import Path


def part1(input_data: str) -> None:
    pass


def part2(input_data: str) -> None:
    pass


def main(input_file: Path) -> None:
    input_data = input_file.read_text()

    print(part1(input_data))
    print(part2(input_data))


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent.parent / f"inputs/{Path(__file__).stem}.txt"
    main(input_file)
