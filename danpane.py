from PIL import Image
import os

def danpane(image_path):
    # Load the image

    image = Image.open(image_path)
    image = image.convert("RGB")

    file_name_without_extension, file_extension = os.path.splitext(os.path.basename(image_path))
    parent_folder = os.path.dirname(image_path)
    output_folder = os.path.join(parent_folder, "Danpane_" + file_name_without_extension)
    os.makedirs(output_folder, exist_ok=True)



    # Specify the number of rows and columns
    num_rows = int(input("行の数:")) # Number of rows
    subimage_height = int(image.height / num_rows)

    # Calculate subimage size based on A4 dimensionspy
    a4_width = 210  # Width in mm
    a4_height = 297  # Height in mm

    # decide direction
    direction = input("方向（1:縦, 2:横）:")

    if direction == "1":
        subimage_width = int(subimage_height * a4_width / a4_height)
    elif direction == "2":
        subimage_width = int(subimage_height * a4_height / a4_width)
    else:
        print("error:input 1 or 2")

    num_cols = image.width // subimage_width
    last_col = image.width % subimage_width

    # Loop through the image and create subimages
    for row in range(num_rows):
        for col in range(num_cols):
            left = col * subimage_width
            upper = row * subimage_height
            right = left + subimage_width
            lower = upper + subimage_height

            # Crop the subimage
            subimage = image.crop((left, upper, right, lower))

            # Construct the subimage file name
            subimage_file_name = f"{file_name_without_extension}_sub_{row}_{col}.jpg"

            # Save the subimage to the output folder
            subimage.save(os.path.join(output_folder, subimage_file_name))

    #last_col
    for row in range(num_rows):
        left = num_cols * subimage_width
        upper = row * subimage_height
        right = left + last_col
        lower = upper + subimage_height

        # Crop the subimage
        subimage = image.crop((left, upper, right, lower))

        # Construct the subimage file name
        subimage_file_name = f"{file_name_without_extension}_sub_{row}_{num_cols}.jpg"

        # Save the subimage to the output folder
        subimage.save(os.path.join(output_folder, subimage_file_name))

    print(f"Subimages are saved in the '{output_folder}' folder.")


image_path=input("input_image_path:")

danpane(image_path)
"""

def process_images_in_folder(folder_path):
    # List all files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Filter image files (e.g., jpg, png, etc.)
    image_files = [f for f in image_files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'))]

    if not image_files:
        print("No image files found in the folder.")
        return

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        danpane(image_path)

# Input the folder path
folder_path = input("Enter the folder path containing image files: ")

if os.path.exists(folder_path):
    process_images_in_folder(folder_path)
else:
    print("Folder not found.")
"""