import os
import random
import shutil

# Path to the Test folder containing fruit folders
test_folder_path = 'Test/'

# Path to the New Dataset folder where selected images will be copied
new_dataset_folder_path = 'New Dataset/'

# Function to randomly select and copy 3 images from the source folder to the destination folder
def copy_random_images(source_folder, destination_folder):
    selected_images = random.sample(os.listdir(source_folder), 3)
    for image_file in selected_images:
        image_path = os.path.join(source_folder, image_file)
        shutil.copy(image_path, destination_folder)

# Create the New Dataset folder if it doesn't exist
os.makedirs(new_dataset_folder_path, exist_ok=True)

# Loop through each fruit folder in the Test folder
for fruit_folder in os.listdir(test_folder_path):
    fruit_folder_path = os.path.join(test_folder_path, fruit_folder)
    if os.path.isdir(fruit_folder_path):
        # Create a corresponding folder in the New Dataset folder
        output_fruit_folder_path = os.path.join(new_dataset_folder_path, fruit_folder)
        os.makedirs(output_fruit_folder_path, exist_ok=True)

        # Copy 3 random images from the fruit folder to the New Dataset folder
        copy_random_images(fruit_folder_path, output_fruit_folder_path)
