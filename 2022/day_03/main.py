import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    data = [r.strip("\n") for r in raw]
    return data


if __name__ == "__main__":
    data = read_file("test_input.txt")
    print(data)