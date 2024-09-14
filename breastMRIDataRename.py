"""
rename the file inside a directory that follow the nnunet
"""

import os

def rename_files(directory):
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Split the file into name and extension
        file_name, file_extension = os.path.splitext(filename)
        
        # Check if '_0000' is already in the filename
        if not file_name.endswith('_0000'):
            # Create the new filename by appending '_0000'
            new_filename = f"{file_name}_0000{file_extension}"
            
            # Construct the full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    # Replace with the directory you want to process
    target_directory = r'C:\\Users\\MaxYo\\OneDrive\\Desktop\\MBP\\martel\\nnUNet_raw\\Dataset011_GE\\imagesTr'
    
    rename_files(target_directory)
