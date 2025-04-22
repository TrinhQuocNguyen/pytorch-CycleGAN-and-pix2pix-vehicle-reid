import os
import shutil

def move_and_rename_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if "_fake_B" in filename:
            # Build full paths
            old_path = os.path.join(source_folder, filename)
            new_filename = filename.replace("_fake_B", "")
            new_path = os.path.join(destination_folder, new_filename)
            
            # Move and rename the file
            shutil.move(old_path, new_path)
            print(f"Moved and renamed: {filename} -> {new_filename}")

# Example usage
source_folder = "results/veri2vehicleid_small_cyclegan/test_latest/images"
destination_folder = "/old/home/ccvn/Workspace/trinh/data/reid/VehicleID/image_combine_gan"

move_and_rename_files(source_folder, destination_folder)
