import os
import shutil
#1
def list_contents(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))
#2
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
#3
def check_path_info(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")
#4
def count_lines(file):
    with open(file, 'r') as f:
        print("Number of lines:", sum(1 for _ in f))
#5
def write_list_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(item + "\n")
    print("Data written to", filename)
#6
def generate_text_files():
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is {letter}.txt\n")
    print("Text files created.")
#7
def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")
#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} deleted")
    else:
        print("Cannot delete", path)

if __name__ == "__main__":
    path = "."
    list_contents(path)
    check_access(path)
    check_path_info("example.txt")
    write_list_to_file("sample.txt", ["Hello", "World"])
    count_lines("sample.txt")
    generate_text_files()
    copy_file("sample.txt", "copy_sample.txt")
    delete_file("sample.txt")

