import os


def rename_images(start_number, folder_path, prefix=""):
    # Convert start_number to an integer to ensure proper increment
    current_number = int(start_number)

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Sort files to ensure renaming is done in order
    files.sort()

    for file in files:
        # Construct the new file name using the current number, preserving the file extension
        file_extension = os.path.splitext(file)[1]
        new_file_name = f"{prefix}{str(current_number).zfill(3)}{file_extension}"

        # Construct full old and new file paths
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_file_name}'")

        # Increment the number for the next file
        current_number += 1


# Example usage
folder = "../temp"
start = "001"
pre = "cube"
rename_images(start, folder, pre)
