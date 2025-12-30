import os

def get_files_info(working_directory, directory="."):
    # Check if directory is a valid argument
    if os.path.isdir(directory) is False:
        print(f'Error: "{directory}" is not a directory')

    # Absolutize and normalize our working directory
    working_dir_abs = os.path.abspath(working_directory)

    # Construct the full path to the target directory
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Check if target_dir falls within the absolute working_directory path. Returns True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir is False:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    # List the contents of target_dir
    dir = os.listdir(target_dir)

    # Iterate over the items in the target directory
    for file in dir:
        is_dir = os.path.isdir(file)

        if is_dir is True:
            file_size = os.path.getsize(file)
            print(f"- {file}: file_size={file_size}, is_dir={is_dir}")
