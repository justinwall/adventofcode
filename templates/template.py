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
    root_dir = Path(__file__).resolve().parent.parent
    input_file = root_dir / "inputs" / f"{Path(__file__).stem}.txt"
    main(input_file)
