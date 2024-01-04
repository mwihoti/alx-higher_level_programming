#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    word_arg = len(sys.argv) - 1

    if word_arg == 0:
        print("{} arguments.".format(word_arg))
    elif word_arg == 1:
        print("{} argument:".format(word_arg))
    else:
        print("{} arguments:".format(word_arg))

    if word_arg >= 1:
        word_arg = 0
        for arg in sys.argv:
            if word_arg != 0:
                print("{}: {}".format(word_arg, arg))
            word_arg += 1
