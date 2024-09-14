"""
step 2: This script mainly to preprocess the breastMRI dataset so that the format obey the
structure desired by nnUnet
"""

# #%% section to visualize the size of the image vols
# # Path to the folder containing the .mha files
# folder_path = "F:\\amartel_data2__Breast__GE_project\\nnUNet\\nnUNet_raw\\Dataset011_GE\\imagesTr"

# # Iterate through all the files in the folder
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.mha'):
#         # Full path to the .mha file
#         file_path = os.path.join(folder_path, file_name)
        
#         # Read the .mha image
#         image = sitk.ReadImage(file_path)
        
#         # Get the size (dimensions) of the image
#         size = image.GetSize()
        
#         # Print the size of the image
#         print(f'File: {file_name}, Size (Dimensions): {size}')
# "F:\amartel_data2__Breast__GE_project\breastMRI\0276_r\6952525\276CADPat_8054_20111231_6952525_3_LT.Sag.FSE.T2.FS.mha"

import os
import shutil

def clear_output_folder(output_folder):
    """Remove all files from the output folder."""
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Define the source and destination directories
source_dir = r'F:\\amartel_data2__Breast__GE_project\\breastMRI'  # Replace with the actual path
destination_dir = r'C:\\Users\\MaxYo\\OneDrive\\Desktop\\MBP\\martel\\nnUNet_raw\\Dataset011_GE\\imagesTr'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Clear existing files in the output folder
clear_output_folder(destination_dir)

# Initialize counters and tracking lists
total_copied = 0
patients_without_ph1sag = []

# Walk through all subdirectories in the source directory
for patient_folder in os.listdir(source_dir):
    patient_path = os.path.join(source_dir, patient_folder)

    if os.path.isdir(patient_path):
        # Extract the numeric part from the patient_folder name
        numeric_part = patient_folder.split('_')[0]
        if numeric_part:
            found_ph1sag = False
            for sub_folder in os.listdir(patient_path):
                sub_folder_path = os.path.join(patient_path, sub_folder)

                if os.path.isdir(sub_folder_path):
                    # Search for files with 'Ph1Sag' in the name
                    for file_name in os.listdir(sub_folder_path):
                        if 'Ph1Sag' in file_name and file_name.endswith('.mha'):
                            source_file = os.path.join(sub_folder_path, file_name)
                            new_file_name = f"GE_{numeric_part}.mha"
                            destination_file = os.path.join(destination_dir, new_file_name)
                            
                            # Copy the file to the destination directory with the new name
                            shutil.copy2(source_file, destination_file)
                            total_copied += 1
                            found_ph1sag = True
            
            if not found_ph1sag:
                patients_without_ph1sag.append(patient_folder)

# Output the results
print(f"Total volumes copied: {total_copied}")

if patients_without_ph1sag:
    print("Patients without 'Ph1Sag' images:")
    for patient in patients_without_ph1sag:
        print(patient)
else:
    print("All patients have 'Ph1Sag' images.")

# C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\labelsTr
# C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\imagesTr