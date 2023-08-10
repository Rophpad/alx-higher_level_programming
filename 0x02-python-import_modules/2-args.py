#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totalArgs = len(sys.argv) - 1

    def line_1(parameter):
        if (parameter == 0):
            print("{} arguments.".format(parameter))
        elif (parameter == 1):
            print("{} argument:".format(parameter))
        else:
            print("{} arguments:".format(parameter))
    line_1(totalArgs)

    def more_line(parameter):
        if (parameter > 0):
            for index in range(0, parameter):
                arg_index = index + 1
                print("{}: {}".format(arg_index, sys.argv[arg_index]))
    more_line(totalArgs)
