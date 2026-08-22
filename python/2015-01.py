#!/usr/bin/env python3
# https://adventofcode.com/2015/day/1
from pathlib import Path
from typing import Literal, cast

Instruction = Literal["(", ")"]


def part1(instructions: list[Instruction]) -> int:
    return sum(1 if instruction == "(" else -1 for instruction in instructions)


def part2(instructions: list[Instruction]) -> int:
    floor = 0
    for i, instruction in enumerate(instructions, start=1):
        floor += 1 if instruction == "(" else -1
        if floor < 0:
            break
    return i


def main(input_file: Path) -> None:
    input_data = input_file.read_text()

    instructions = cast(list[Instruction], list(input_data))

    print(part1(instructions))
    print(part2(instructions))


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent.parent / f"inputs/{Path(__file__).stem}.txt"
    main(input_file)
