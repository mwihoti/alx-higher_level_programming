#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    word_arg = len(sys.argv) - 1

    if word_arg == 0:
        print("{} arguements.".format(l))
    elif word_arg == 1:
        print("{} arguement:".format(l))
    else:
        print("{} arguement:".format(l))

    if word_arg >= 1:
        word_arg = 0
        for arg in sys.argv:
            if word_arg != 0:
                print("{}: {}".format(word_arg, arg))
                word_arg += 1
