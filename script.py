import os

def save_file_structure(root_dir, output_file):
    with open(output_file, 'w') as f:
        for foldername, _, filenames in os.walk(root_dir):
            print(foldername)
            if filenames:  # Only write the folder name if it contains files
                folder_name = os.path.basename(foldername)
                f.write(f"{folder_name}\n")
                for filename in filenames:
                    f.write(f"{filename}\n")
                f.write("\n")  # Add an extra line break between folders

# Replace 'your_root_directory' with the path of the directory you want to scan
root_directory = os.getcwd()
output_file = 'finish.txt'

save_file_structure(root_directory, output_file)
