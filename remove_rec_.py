import os
import re

def remove_images_with_rec(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return

        # Get a list of all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files
        for file_name in files:
            # Check if the file name contains '_rec_' and is an image
            if re.search(r"_rec_", file_name) and file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                # Construct full file path
                file_path = os.path.join(folder_path, file_name)

                # Remove the file
                os.remove(file_path)
                print(f"Removed: {file_name}")

        print("Operation completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'your/folder/path' with the actual folder path
folder_path = "results/veri2vehicleid_small_cyclegan/test_latest/images"
remove_images_with_rec(folder_path)