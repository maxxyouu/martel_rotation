"""
step 3: this script mainly to sync the files between the labelsTr and the imagesTr directory
"""
import os

# Paths to the directories
images_dir = r'C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\imagesTr'
labels_dir = r'C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\labelsTr'

# Get list of file names in each directory (no extension)
images_files = set(os.listdir(images_dir))
labels_files = set(os.listdir(labels_dir))

# Track deleted files
deleted_from_images = []
deleted_from_labels = []

# Find common files in both directories (intersection)
common_files = images_files.intersection(labels_files)

# Delete files from images_dir that are not in labels_dir
for file_name in images_files:
    if file_name not in common_files:
        file_path = os.path.join(images_dir, file_name)
        print(f"Deleting {file_path} from images_dir")
        os.remove(file_path)
        deleted_from_images.append(file_name)

# Delete files from labels_dir that are not in images_dir
for file_name in labels_files:
    if file_name not in common_files:
        file_path = os.path.join(labels_dir, file_name)
        print(f"Deleting {file_path} from labels_dir")
        os.remove(file_path)
        deleted_from_labels.append(file_name)

# Output the deleted files from each directory
if deleted_from_images:
    print(f"\nDeleted {len(deleted_from_images)} file(s) from images_dir:")
    for file_name in deleted_from_images:
        print(file_name)
else:
    print("\nNo files were deleted from images_dir.")

if deleted_from_labels:
    print(f"\nDeleted {len(deleted_from_labels)} file(s) from labels_dir:")
    for file_name in deleted_from_labels:
        print(file_name)
else:
    print("\nNo files were deleted from labels_dir.")

# Count remaining files in each directory
remaining_images = os.listdir(images_dir)
remaining_labels = os.listdir(labels_dir)
print(f"\nNumber of files remaining in 'images_dir': {len(remaining_images)}")
print(f"Number of files remaining in 'labels_dir': {len(remaining_labels)}")

