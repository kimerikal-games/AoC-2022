#!/usr/bin/python3
import argparse
import shutil
import json


def initialize_directory(day: int, title: str, config: dict) -> None:
    title = title.title()

    print(f"Initializing directory for day {day:02d}: {title}")

    try:
        shutil.copytree("00", f"{day:02d}")
    except FileExistsError:
        print("Directory already exists. Overwrite? [y/N]")
        response = input()
        if not response or response[0].lower() != "y":
            print("Aborting.")
            return

    with open(f"{day:02d}/program.py", "r") as f:
        program = f.read()
    program = (
        program
        .replace("{{ year }}", f"{config['year']}")
        .replace("{{ day }}", f"{day}")
        .replace("{{ title }}", title)
        .replace("{{ name }}", config["name"])
        .replace("{{ email }}", config["email"])
    )
    with open(f"{day:02d}/program.py", "w") as f:
        f.write(program)

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize the directory for new puzzle.")
    parser.add_argument("day", help="day number of puzzle", type=int)
    parser.add_argument("title", help="title of puzzle", type=str)

    args = parser.parse_args()
    day = args.day
    title = args.title
    try:
        config = json.load(open("config.json"))
    except FileNotFoundError:
        print("Please set up configuration file (config.json)")
        exit(1)

    initialize_directory(
        day=args.day,
        title=args.title,
        config=config,
    )
