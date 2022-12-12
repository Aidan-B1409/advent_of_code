import io


def parse_command_tree(cmd_buf: io.TextIOWrapper) -> list:
    files = []
    while True:
        cmd = cmd_buf.readline().strip("\n")
        if "$" in cmd:
            if "cd" in cmd:
                if ".." in cmd:
                    return files
                files.append(parse_command_tree(cmd_buf))
                continue
            if cmd == "$ ls":
                continue
        cmd = cmd.split()
        print(cmd)
        try:
            files.append(int(cmd[0]))
        except ValueError:
            continue
        except IndexError:
            return files


sum = 0
candidate = 30000000


def get_smallest_dirs(tree: list) -> int:
    global sum
    tmp = 0
    for e in tree:
        if isinstance(e, list):
            tmp2 = get_smallest_dirs(e)
            if tmp2 <= 100000:
                sum += tmp2
            tmp += tmp2
        else:
            tmp += e
    return tmp


def get_candidate_dir(tree: list, max: int) -> int:
    global candidate
    tmp = 0
    for e in tree:
        if isinstance(e, list):
            tmp2 = get_candidate_dir(e, max)
            if (70000000 - max) + tmp2 >= 30000000:
                if tmp2 < candidate:
                    candidate = tmp2
            tmp += tmp2
        else:
            tmp += e
    return tmp


def main() -> None:
    with open("input.txt") as input:
        fsystem = parse_command_tree(input)
        max = get_smallest_dirs(fsystem)
        get_candidate_dir(fsystem, max)


if __name__ == "__main__":
    main()
