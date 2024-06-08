import os

# Define the directory path
directory_path = input("Enter directory: ")

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    # Construct the full file path
    full_file_path = os.path.join(directory_path, filename)
    
    # Check if it is a file (not a directory) and doesn't already have a .csv extension
    if os.path.isfile(full_file_path) and not filename.endswith('.csv'):
        # Create the new file name with .csv extension
        new_filename = filename + '.csv'
        new_full_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(full_file_path, new_full_file_path)

print("Renaming completed.")