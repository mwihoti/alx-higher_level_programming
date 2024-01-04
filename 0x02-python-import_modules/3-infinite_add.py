#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for num in sys.argv:
        if num != sys.argv[0]:
            result += int(num)
    print(result)
