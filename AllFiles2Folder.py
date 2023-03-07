# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
from glob import glob


def main():
    print("-----------------------")
    MAIN_FOLDER = input("MAIN_FOLDER: ")

    # Find all files
    print("-----------------------")
    subFolders = []
    allFiles = [y for x in os.walk(MAIN_FOLDER) for y in glob(os.path.join(x[0], '*'))]
    for idx, src in enumerate(allFiles):
        filename = os.path.basename(src)
        folder = os.path.dirname(src)
        print(str(idx) + ": " + folder + " - " + filename)

        # Move file to MAIN_FOLDER
        os.rename(src, os.path.join(MAIN_FOLDER, filename))

        # Add subFolder to subFolders
        if folder not in subFolders and folder != MAIN_FOLDER:
            subFolders.append(folder)

    # Delete subFolders
    for folder in subFolders:
        os.rmdir(folder)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
        print("END")
