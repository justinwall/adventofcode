#!/usr/bin/env python3
# https://adventofcode.com/2015/day/3
from pathlib import Path
from typing import Literal, cast

Direction = Literal[">", "<", "^", "v"]


def move(x: int, y: int, direction: Direction) -> tuple[int, int]:
    if direction == ">":
        return x + 1, y
    if direction == "<":
        return x - 1, y
    if direction == "^":
        return x, y + 1
    if direction == "v":
        return x, y - 1


def part1(directions: list[Direction]) -> int:
    santa_x = santa_y = 0
    visited = [(0, 0)]

    for direction in directions:
        santa_x, santa_y = move(santa_x, santa_y, direction)
        if (santa_x, santa_y) not in visited:
            visited.append((santa_x, santa_y))

    return len(visited)


def part2(directions: list[Direction]) -> int:
    santa_x = santa_y = robot_x = robot_y = 0
    visited = [(0, 0)]

    dir_iter = iter(directions)
    for direction in dir_iter:
        santa_x, santa_y = move(santa_x, santa_y, direction)
        robot_x, robot_y = move(robot_x, robot_y, next(dir_iter))

        if (santa_x, santa_y) not in visited:
            visited.append((santa_x, santa_y))
        if (robot_x, robot_y) not in visited:
            visited.append((robot_x, robot_y))

    return len(visited)


def main(input_file: Path) -> None:
    input_data = input_file.read_text()

    directions = cast(list[Direction], list(input_data))

    print(part1(directions))
    print(part2(directions))


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    input_file = root_dir / "inputs" / f"{Path(__file__).stem}.txt"
    main(input_file)
