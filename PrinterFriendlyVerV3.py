# Import the required modules
import os
import shutil
import hashlib

# Define the root folder of the repo
root_folder = input("Enter the root folder of the repo: ")

# Define the output folder where the single page and media files will be stored
output_folder = "output"

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Define a function to copy and rename the media files
def copy_media(file):
    # Get the file name and extension
    name, ext = os.path.splitext(file)

    # Open the file in binary mode and read its content
    with open(file, "rb") as f:
        content = f.read()

    # Generate a hash value based on the file content using md5 algorithm
    hash_value = hashlib.md5(content).hexdigest()

    # Generate a new name based on the hash value and the file extension
    new_name = hash_value + ext

    # Copy the file to the output folder with the new name
    shutil.copy(file, os.path.join(output_folder, new_name))

    # Return the new name of the file
    return new_name

# Define a function to update the references to the media files in the markdown content
def update_references(content):
    # Split the content by lines
    lines = content.split("\n")

    # Loop through each line
    for i, line in enumerate(lines):
        # Check if the line contains a reference to a media file
        if "!alt text[1].split(")")[0]

            # Get full path of old name by joining root folder and old name 
            old_path = os.path.join(root_folder, old_name)

            # Copy and rename media file to output folder 
            new_name = copy_media(old_path)

            # Replace the old name with the new name in the line
            line = line.replace(old_name, new_name)

            # Update the line in the content
            lines[i] = line

    # Join the lines back into a single string
    content = "\n".join(lines)

    # Return the updated content
    return content

# Define a function to generate a table of contents from the markdown content
def generate_toc(content):
    # Initialize an empty list to store the headings
    headings = []

    # Split the content by lines
    lines = content.split("\n")

    # Loop through each line
    for line in lines:
        # Check if the line starts with one or more '#'
        if line.startswith("#"):
            # Get the level of the heading based on the number of '#'
            level = len(line.split()[0])

            # Get the text of the heading by removing the '#'
            text = line.replace("#", "").strip()

            # Add a tuple of (level, text) to the headings list
            headings.append((level, text))

    # Initialize an empty string to store the table of contents
    toc = ""

    # Loop through each heading in the headings list
    for level, text in headings:
        # Generate an anchor link based on the text of the heading
        link = "#" + text.lower().replace(" ", "-")

        # Add a bullet point with indentation based on the level of the heading
        toc += "  " * (level - 1) + "- "

        # Add a hyperlink with the text and link of the heading
        toc += "" + text + "\n"

    # Return the table of contents as a string
    return toc

# Initialize an empty string to store the single page content
single_page = ""

# Use os.walk to recursively iterate through all subdirectories and files in root folder 
for dirpath, dirnames, filenames in os.walk(root_folder):
    
    # Loop through each file in filenames list 
    for file in filenames:

        # Check if file ends with ".md" extension 
        if file.endswith(".md"):

            # Get full path of file by joining dirpath and file 
            file_path = os.path.join(dirpath, file)

            # Print verbose step to console 
            print("Processing file: " + file_path)

            # Open file in read mode 
            with open(file_path, "r") as f:

                # Read file content as a string 
                content = f.read()

                # Update references to media files in content 
                content = update_references(content)

                # Add content to single page 
                single_page += content + "\n"

# Generate table of contents from single page content 
toc = generate_toc(single_page)

# Add table of contents to the beginning of single page content 
single_page = "# Table of Contents\n" + toc + "\n" + single_page

# Add a return to top link after each heading in single page content 
single_page = single_page.replace("\n#", "\nReturn to top\n#")

# Write single page content to a single_page.md file in output folder 
with open(os.path.join(output_folder, "single_page.md"), "w") as f:
    f.write(single_page)

# Print verbose step to console 
print("Single page created successfully in output folder")
