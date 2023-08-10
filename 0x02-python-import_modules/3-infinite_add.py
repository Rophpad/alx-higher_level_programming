#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    adds = 0
    totalArgs = len(sys.argv) - 1
    for i in range(0, totalArgs):
        arg_index = i + 1
        adds += int(sys.argv[arg_index])
    print("{}".format(adds))
