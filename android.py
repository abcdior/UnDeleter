import os
import shutil

def recover_deleted_files(root_dir):
    for root, directories, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".deleted"):
                print("Found deleted file: " + os.path.join(root, file))
                new_file_name = file[:-8]
                shutil.move(os.path.join(root, file), os.path.join(root, new_file_name))

def main():
    root_dir = input("Enter the location or path of the drive to search for deleted files: ")
    recover_deleted_files(root_dir)

if __name__ == "__main__":
    main()
