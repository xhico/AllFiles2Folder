# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
from glob import glob


def organize_files(main_folder):
    """
    Organize files in the specified main folder and its subfolders.

    Parameters:
    - main_folder (str): The path to the main folder containing files to be organized.
    """
    print("-----------------------")
    print("Organizing files in:", main_folder)

    # list to store subfolders
    subfolders = []
    all_files = [y for x in os.walk(main_folder) for y in glob(os.path.join(x[0], '*'))]

    for idx, src in enumerate(all_files):
        filename = os.path.basename(src)
        folder = os.path.dirname(src)
        print(f"{idx}: {folder} - {filename}")

        # Move file to main folder
        os.rename(src, os.path.join(main_folder, filename))

        # Add subfolder to subfolders
        if folder not in subfolders and folder != main_folder:
            subfolders.append(folder)

    # Delete subfolders
    for folder in subfolders:
        os.rmdir(folder)


def main():
    """
    Main function to execute file organization.
    """
    try:
        # Get user input for main folder
        main_folder = input("MAIN_FOLDER: ")
        organize_files(main_folder)

    except Exception as ex:
        print(f"An error occurred: {ex}")

    finally:
        print("END")


if __name__ == '__main__':
    main()
