import os
import colour_extracting
import mesh_extraction
import writing
import resizing
#Extracting the mesh from glb file

files_to_remove = ["/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/0.jpg","/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/1.jpg","/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/2.jpg"]
for file in files_to_remove:
    try:
        os.remove(file)
    except FileNotFoundError:
        continue

mesh_extraction.extract_images_from_glb(filename="/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/BareBodyModel.glb")

# Finding the skin tone from the photo and replacing it instead of the existing mesh
colour_extracting.first_call(face_path='/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/test_1.jpg',mesh_path='/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/1.jpg')

resizing.resize(mesh_path="/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/extracted_mesh.png")

writing.extract_and_replace_images_from_glb(glb_file="/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/BareBodyModel.glb", output_folder="/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/", replacement_image_path="/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/imgs/output.png")


