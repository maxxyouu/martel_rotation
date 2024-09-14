"""
step 1: this script mainly to merge the multi lesion label for each the patient volume
"""
import SimpleITK as sitk
import numpy as np
import os
import re

def load_mha_image(file_path):
    """Load a .mha image file."""
    return sitk.ReadImage(file_path)

def save_mha_image(image, output_path):
    """Save a .mha image file."""
    sitk.WriteImage(image, output_path)

def merge_segmentation_masks(mask_paths):
    """Merge (union) multiple segmentation masks."""
    merged_mask = None
    
    for mask_path in mask_paths:
        mask_image = load_mha_image(mask_path)
        mask_array = sitk.GetArrayFromImage(mask_image)
        
        if merged_mask is None:
            merged_mask = mask_array
        else:
            # Union of segmentation masks
            merged_mask = np.logical_or(merged_mask, mask_array)
    
    # Convert back to a SimpleITK image
    merged_image = sitk.GetImageFromArray(merged_mask.astype(np.uint8))
    
    # Copy the original image properties (spacing, origin, direction)
    merged_image.CopyInformation(load_mha_image(mask_paths[0]))
    
    return merged_image

def extract_patient_numeric(folder_name):
    """Extract the part of the folder name before the '_' character."""
    return folder_name.split('_')[0]

def process_patient_masks(review_folder, custom_name, output_folder):
    """Process all segmentation masks in the review folder and save in the specified output directory."""
    mask_files = [os.path.join(review_folder, f) for f in os.listdir(review_folder) if f.endswith('.mha') and 'mask' in f]
    
    if not mask_files:
        return False  # No mask files found, return False
    
    # Merge the segmentation masks
    merged_mask = merge_segmentation_masks(mask_files)
    
    # Define the output file name in the specified output folder
    output_file = os.path.join(output_folder, f"{custom_name}.mha")
    
    # Save the merged segmentation mask
    save_mha_image(merged_mask, output_file)
    return True  # Successfully processed and saved the volume

def clear_output_folder(output_folder):
    """Remove all files from the output folder."""
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Example usage
if __name__ == "__main__":
    base_folder = r"F:\amartel_data2__Breast__GE_project\breastMRI"
    output_folder = r"C:\Users\MaxYo\OneDrive\Desktop\MBP\martel\nnUNet_raw\Dataset011_GE\labelsTr"
    
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Clear existing files in the output folder
    clear_output_folder(output_folder)
    
    created_volumes = 0
    patients_without_masks = []

    # Traverse the directory structure
    for patient_folder in os.listdir(base_folder):
        patient_path = os.path.join(base_folder, patient_folder)
        
        if os.path.isdir(patient_path):
            for subdirectory in os.listdir(patient_path):
                subdirectory_path = os.path.join(patient_path, subdirectory)
                
                if os.path.isdir(subdirectory_path):
                    # Locate the review folder
                    review_folder = os.path.join(subdirectory_path, "review")
                    
                    if os.path.isdir(review_folder):
                        # Extract the part before '_' from the patient folder name
                        patient_numeric = extract_patient_numeric(patient_folder)
                        
                        # Custom name format: GE_{patient_numeric}
                        custom_name = f"GE_{patient_numeric}"
                        
                        # Process the masks and save the result to the specified output folder
                        if process_patient_masks(review_folder, custom_name, output_folder):
                            created_volumes += 1
                        else:
                            patients_without_masks.append(patient_folder)
    
    # Output results
    print(f"Number of volumes created: {created_volumes}")
    if patients_without_masks:
        print(f"Patients without masks: {', '.join(patients_without_masks)}")
    else:
        print("All patients had segmentation masks.")
