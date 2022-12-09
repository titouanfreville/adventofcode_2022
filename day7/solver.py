import re
from os import path
from typing import Dict, List, TypedDict, Union

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")


class Path(TypedDict):
    path: str
    size: int
    childs: Dict[str, "Path"]
    parent_path: Union["Path", None]


def new_path(
    path: str,
    parent_path: Path | None = None,
    size: int = 0,
    childs: Dict[str, Path] = None,
) -> Path:
    childs = childs or {}
    return {
        "path": path,
        "parent_path": parent_path,
        "size": size,
        "childs": childs,
    }


directory_tree: Path = new_path("/")
cmd_parsing = re.compile(r"\$ (?P<cmd>[a-z]+)(?: (?P<args>[a-z ./]+))*")

with open(FILE_NAME) as f:
    lines = f.readlines()

current_dir: Path = directory_tree
is_listing = False
for line in lines:
    line = line.strip("\n").strip("\r")
    is_cmd = line.startswith("$")

    if not is_cmd and not is_listing:
        raise ValueError("UnrecognizeCommand")

    if is_cmd:
        is_listing = False

        cmd_data = cmd_parsing.search(line).groupdict()

        match cmd_data["cmd"]:
            case "cd":
                cmd_arg = cmd_data["args"]
                if not cmd_arg or cmd_arg == current_dir["path"]:
                    continue

                match cmd_arg:
                    case "/":
                        current_dir = directory_tree

                    case "..":
                        if current_dir["parent_path"]:
                            current_dir = current_dir["parent_path"]
                        else:
                            raise ValueError("NoLowerLevel")

                    case _:
                        if cmd_arg not in current_dir["childs"]:
                            current_dir["childs"][cmd_arg] = new_path(
                                cmd_arg, current_dir
                            )

                        current_dir = current_dir["childs"][cmd_arg]
            case "ls":
                is_listing = True
    elif is_listing:
        a, b = line.split(" ", 1)

        if a == "dir" and b not in current_dir["childs"]:
            current_dir["childs"][b] = new_path(b, current_dir)

        else:
            a = int(a)
            current_dir["size"] += a

            tmp = current_dir
            while tmp["parent_path"]:
                tmp["parent_path"]["size"] += a
                tmp = tmp["parent_path"]


# Part 1
def get_directory_size_lower_than(
    parent: Path, matched_size: List[int], max_size_of_folder_in_sum: int = 100000
):
    if parent["size"] <= max_size_of_folder_in_sum:
        matched_size.append(parent["size"])

    for child in parent["childs"].values():
        get_directory_size_lower_than(child, matched_size, max_size_of_folder_in_sum)


res = []
get_directory_size_lower_than(directory_tree, res)
print(sum(res))

# Part 2
available_disk = 70000000
required_space = 30000000
to_free = required_space - (available_disk - directory_tree["size"])


def get_directory_size_higher_than(
    parent: Path, matched_size: List[int], min_size_of_folder_in_sum: int = 30000000
):
    if parent["size"] >= min_size_of_folder_in_sum:
        matched_size.append(parent["size"])

    for child in parent["childs"].values():
        get_directory_size_higher_than(child, matched_size, min_size_of_folder_in_sum)


to_del = []
get_directory_size_higher_than(directory_tree, to_del, to_free)
print(min(to_del))
