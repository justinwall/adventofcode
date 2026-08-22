#!/usr/bin/env python3
# https://adventofcode.com/2015/day/2
from pathlib import Path

Present = list[int]


def part1(presents: list[Present]) -> int:
    wrapping_paper = 0
    for present in presents:
        l, w, h = sorted(present)
        surface_area = 2 * (l * w + l * h + w * h)
        smallest_area = l * w
        wrapping_paper += surface_area + smallest_area
    return wrapping_paper


def part2(presents: list[Present]) -> int:
    ribbon = 0
    for present in presents:
        l, w, h = sorted(present)
        volume = l * w * h
        smallest_perimeter = 2 * (l + w)
        ribbon += volume + smallest_perimeter
    return ribbon


def main(input_file: Path) -> None:
    input_data = input_file.read_text()

    presents = [
        [int(dimension.strip()) for dimension in line.split("x")]
        for line in input_data.splitlines()
    ]

    print(part1(presents))
    print(part2(presents))


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    input_file = root_dir / "inputs" / f"{Path(__file__).stem}.txt"
    main(input_file)
