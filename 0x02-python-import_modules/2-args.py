#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1

    if l == 0:
        print("{} arguements.".format(l))
    elif l == 1:
        print("{} arguement:".format(l))
    else:
        print("{} arguement:".format(l))

    if l >= 1:
        l = 0
        for arg in sys.argv:
            if l != 0:
                print("{}: {}".format(l, arg))
                l += 1
