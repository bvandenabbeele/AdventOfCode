import pathlib
import requests


_base_dir = pathlib.Path(__file__).parent


def get_input(year: int, day: int) -> None:
    target_path = _base_dir / f"{year}/day_{str(day).zfill(2)}/input.txt"

    if not target_path.exists():
        problem_input = download_input(year, day)

        with open(target_path, "w") as f:
            f.write(problem_input)


def download_input(year: int, day: int) -> str:
    with open(_base_dir / "cookie.txt", "r") as f:
        cookie = f.read().strip()

    return requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie}).text

