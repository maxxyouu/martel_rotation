"""
step 4: sanity check the merged label by visualize the patient that has multiple lesion, retrieved by the keyword "merged_mask"
"""
import os

def extract_patient_numeric(folder_name):
    """Extract the part of the folder name before the '_' character."""
    return folder_name.split('_')[0]

def find_patients_with_merged_mask(base_folder):
    """Find patients with 'merged_mask' in one of the files inside the review folder."""
    patients_with_merged_mask = []

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
                        # Check if any file contains 'merged_mask' in its name
                        for file in os.listdir(review_folder):
                            if 'merged_mask' in file:
                                # Extract the patient numeric part and add it to the list
                                patient_numeric = extract_patient_numeric(patient_folder)
                                patients_with_merged_mask.append(patient_numeric)
                                break  # No need to check further files for this patient
    
    return patients_with_merged_mask

# Example usage
if __name__ == "__main__":
    base_folder = r"F:\amartel_data2__Breast__GE_project\breastMRI"
    
    # Find patients with 'merged_mask' in one of the files in the review folder
    patients_with_merged_mask = find_patients_with_merged_mask(base_folder)
    
    # Output the results
    if patients_with_merged_mask:
        print(f"Patients with 'merged_mask': {', '.join(patients_with_merged_mask)}")
    else:
        print("No patients with 'merged_mask' found.")
