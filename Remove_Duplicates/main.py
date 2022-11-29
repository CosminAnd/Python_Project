import sys
import os


def solve():
    if len(sys.argv) != 2:
        raise Exception("[ERROR]- Invalid number of arguments!")
    folder_name = sys.argv[1]
    if os.path.isdir(folder_name) is False:
        raise Exception("[ERROR] - Is not folder!")
    if os.path.exists(folder_name) is False:
        raise Exception("[ERROR] - Folder not found!")
    dictionary = dict()
    duplicates = False
    for root, dir, files in os.walk(folder_name):
        for f in files:
            pass  # verificare continut fisiere
    if not duplicates:
        print("No duplicates")


if __name__ == "__main__":
    try:
        solve()
    except Exception as e:
        print(e)
