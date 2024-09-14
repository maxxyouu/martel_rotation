"""
step 5: keep the files that have the same spatial dimensions
"""
import os
import SimpleITK as sitk

# Paths to the directories
images_dir = r'C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\imagesTr'
labels_dir = r'C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\labelsTr'

# Get list of .mha files in each directory
images_files = {f for f in os.listdir(images_dir) if f.endswith('.mha')}
labels_files = {f for f in os.listdir(labels_dir) if f.endswith('.mha')}

# Find common files in both directories
common_files = images_files.intersection(labels_files)

# Track files with different dimensions
files_with_diff_dimensions = []

# Function to get image dimensions from an .mha file
def get_image_dimensions(file_path):
    image = sitk.ReadImage(file_path)
    return image.GetSize()  # Returns a tuple of the image dimensions

# Compare dimensions
for file_name in common_files:
    image_file_path = os.path.join(images_dir, file_name)
    label_file_path = os.path.join(labels_dir, file_name)
    
    # Get dimensions of the image and label
    image_dimensions = get_image_dimensions(image_file_path)
    label_dimensions = get_image_dimensions(label_file_path)
    
    # Check if dimensions differ
    if image_dimensions != label_dimensions:
        files_with_diff_dimensions.append(file_name)

# Remove files with differing dimensions from both directories
for file_name in files_with_diff_dimensions:
    image_file_path = os.path.join(images_dir, file_name)
    label_file_path = os.path.join(labels_dir, file_name)
    
    # Remove files from both directories
    print(f"Removing {file_name} from both directories.")
    os.remove(image_file_path)
    os.remove(label_file_path)

# Output files with different dimensions
if files_with_diff_dimensions:
    print(f"\nRemoved {len(files_with_diff_dimensions)} file(s) with differing dimensions:")
    for file_name in files_with_diff_dimensions:
        print(f"File: {file_name}")
else:
    print("\nNo files with differing dimensions were found.")

# Output the number of remaining files in both directories
remaining_images_files = {f for f in os.listdir(images_dir) if f.endswith('.mha')}
remaining_labels_files = {f for f in os.listdir(labels_dir) if f.endswith('.mha')}

print(f"\nNumber of files remaining in 'images_dir': {len(remaining_images_files)}")
print(f"Number of files remaining in 'labels_dir': {len(remaining_labels_files)}")
