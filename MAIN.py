import colour_extracting
import mesh_extraction

#Extracting the mesh from glb file
glb_file = "glb/BareBodyModel.glb"
output_folder = "imgs/"
mesh_extraction.extract_images_from_glb(glb_file, output_folder)

# Finding the skin tone from the photo and replacing it instead of the existing mesh
colour_extracting.first_call()


