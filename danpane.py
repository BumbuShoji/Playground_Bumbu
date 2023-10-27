from PIL import Image

# Load the image
image_path=input("input_image_path:")
image = Image.open(image_path)
image = image.convert("RGB")

# Specify the number of rows and columns
num_rows = int(input("行の数:")) # Number of rows
subimage_height = int(image.height / num_rows)

# Calculate subimage size based on A4 dimensions
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

        # Save or process the subimage
        subimage.save(image_path + f"_sub_{row}_{col}.jpg")

#last_col
for row in range(num_rows):
    left = num_cols * subimage_width
    upper = row * subimage_height
    right = left + last_col
    lower = upper + subimage_height

    # Crop the subimage
    subimage = image.crop((left, upper, right, lower))

    # Save or process the subimage
    subimage.save(image_path + f"_sub_{row}_{num_cols}.jpg")


# save the divided and resized image parts
