import os
import shutil

def organize_images_by_item_number(directory, item_number_length):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    for file in files:
        # Extract the item number based on the specified length and strip trailing spaces
        item_number = file[:item_number_length].strip()

        # Create a directory for the item number if it doesn't exist
        item_directory = os.path.join(directory, item_number)
        if not os.path.exists(item_directory):
            os.makedirs(item_directory)

        # Move the file into the item directory
        shutil.move(os.path.join(directory, file), os.path.join(item_directory, file))

    print("Files have been organized successfully.")

if __name__ == "__main__":
    directory = input("Enter the path to the directory with jpg files: ")
    item_number_length = int(input("Enter the number of characters for the item number: "))
    organize_images_by_item_number(directory, item_number_length)
