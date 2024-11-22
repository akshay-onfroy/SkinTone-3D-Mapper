from PIL import Image
import os

def resize(mesh_path):
    # Open the image
    image = Image.open(mesh_path)

    # Resize the image further if necessary
    new_size = (image.width // 3, image.height // 3)  # Reduce size by about a third
    resized_image = image.resize(new_size, Image.LANCZOS)

    # Save with higher compression
    resized_image.save("/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/output.png", format='PNG', optimize=True, compress_level=9)

    # Check the file size after compression
    file_size = os.path.getsize("/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/output.png")
    print(f"File size: {file_size / 1024:.2f} KB")
