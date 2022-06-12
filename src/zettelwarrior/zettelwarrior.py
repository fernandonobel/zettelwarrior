import os
import sys

import yaml


def read_yaml_front_matter(filename):
    project_dir = os.path.realpath(".")
    filepath = os.path.join(project_dir, filename)

    with open(filepath, "r") as f:
        # Make a dict from the first YAML block
        result = next(yaml.load_all(f, Loader=yaml.FullLoader))

    return result


def main():
    filename = sys.argv[1]

    data = read_yaml_front_matter(filename)

    print(data)


if __name__ == "__main__":
    main()
