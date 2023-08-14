import os

# Set folder paths
folder1_path = "outputFilesneg"
folder2_path = "outputFiles"


# Get list of file names in each folder
folder1_files = os.listdir(folder1_path)
folder2_files = os.listdir(folder2_path)

# Check for missing files in folder2
missing_files = []
for file in folder1_files:
    if file not in folder2_files:
        missing_files.append(file)

# Print results
if len(missing_files) == 0:
    print("All files in folder1 exist in folder2.")
else:
    print("The following files in folder1 do not exist in folder2:")
    for file in missing_files:
        print(file)