import os
import cv2

# Path to the New Dataset folder containing fruit folders
new_dataset_folder_path = 'SuperMinDataset'

# Path to the Masked New Dataset folder where masked images will be saved
masked_new_dataset_folder_path = 'Masked SuperMinDataset'

# Function to apply mask and save the masked image
def apply_mask_and_save(input_img_path, output_img_path):
    # Read the input image
    image = cv2.imread(input_img_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a mask (white for the fruit regions, black for other regions)
    ret, mask = cv2.threshold(gray_image, 247, 255, cv2.THRESH_BINARY)

    # Invert the mask to get black for the fruit regions and white for other regions
    masked_image = cv2.bitwise_not(mask)

    # Save the masked image
    cv2.imwrite(output_img_path, masked_image)



# Loop through each fruit folder in the New Dataset folder
for fruit_folder in os.listdir(new_dataset_folder_path):
    fruit_folder_path = os.path.join(new_dataset_folder_path, fruit_folder)
    if os.path.isdir(fruit_folder_path):
        # Create a corresponding folder in the Masked New Dataset folder
        output_fruit_folder_path = os.path.join(masked_new_dataset_folder_path, fruit_folder)
        os.makedirs(output_fruit_folder_path, exist_ok=True)

        # Loop through each image in the fruit folder
        for image_file in os.listdir(fruit_folder_path):
            image_path = os.path.join(fruit_folder_path, image_file)
            output_image_path = os.path.join(output_fruit_folder_path, image_file)

            # Apply mask and save the masked image
            apply_mask_and_save(image_path, output_image_path)
