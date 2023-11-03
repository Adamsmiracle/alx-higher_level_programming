#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    size = len(args) - 1

    if size > 1:
        print(f"{} arguments".format(size))
        for i in range(size + 1):
            print(f"{}: {}".format(i, argv[i]))

    elif size == 0:
        print(f"{} arguments".format(size))

    else:
        print(f"{} arguments".format(size))
        print(f"{}: {}".format(size, argv[1]))
