import sys
import os
import hashlib


def get_file_SHA1(filePath):
    try:
        m = hashlib.sha1()
        f = open(filePath, "rb")
        while True:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
        f.close()
        return m.hexdigest()
    except Exception("[ERROR] - Hash error!") as ex:
        print(ex)


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
            hst = get_file_SHA1(os.path.join(root, f))
            if hst in dictionary.keys():
                dictionary[hst].append(os.path.join(root, f))
                duplicates = True
            else:
                dictionary.update({hst: [os.path.join(root, f)]})
            # print(GetFileSHA1(os.path.join(root, f)))
    if not duplicates:
        print("No duplicates")
    for key, val in dictionary.items():
        if len(val) >= 2:
            print("The following files are identical:")
            for i in range(0, len(val)):
                print(str(i + 1) + ". " + val[i])
            kept_file = int(input("Please select the file you want to keep [1.." + str(len(val)) + "]? \n"))
            if 0 < kept_file > len(val):
                raise Exception("[ERROR] - File selected not is in list!")
            for i in range(0, len(val)):
                if i == kept_file - 1:
                    continue
                else:
                    os.remove(val[i])


if __name__ == "__main__":
    try:
        solve()
    except Exception as e:
        print(e)
