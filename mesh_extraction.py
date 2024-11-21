from pygltflib import GLTF2
import base64
import os

def extract_images_from_glb(glb_file, output_folder):
    gltf = GLTF2().load(glb_file)
    for idx, image in enumerate(gltf.images):
        #CHECKING ONLY THE SECOND IMAGE BECAUSE THAT IS WHAT WE WANT ALL THE TIME
        if idx == 1:
            try:
                if image.uri: 
                    if image.uri.startswith("data:image"):  
                        header, base64_data = image.uri.split(",", 1)
                        ext = header.split(";")[0].split("/")[1]  
                        image_data = base64.b64decode(base64_data)
                        output_path = os.path.join(output_folder, f"bodyMesh.png")
                        with open(output_path, "wb") as file:
                            file.write(image_data)
                        print(f"Extracted embedded image to: {output_path}")
                    else:
                        print(f"Image {idx} uses external reference: {image.uri}")
            
                elif image.bufferView is not None:
                    buffer_view = gltf.bufferViews[image.bufferView]
                    buffer_data = gltf.get_data_from_buffer_uri(gltf.buffers[buffer_view.buffer].uri)
                    start = buffer_view.byteOffset if buffer_view.byteOffset else 0
                    end = start + buffer_view.byteLength
                    image_data = buffer_data[start:end]
                    ext = "bin"
                    if image.mimeType:
                        ext = image.mimeType.split("/")[1]
                    output_path = os.path.join(output_folder, f"bodyMesh.png")
                    with open(output_path, "wb") as file:
                        file.write(image_data)
                    print(f"Extracted buffer-based image to: {output_path}")
                
            except Exception as e:
                print(f"Error extracting image {idx}: {str(e)}")
glb_file = "/Users/akshay/Documents/Work/Project_2(Blender mesh extracting)/mesh/BareBodyModel.glb"
output_folder = "/Users/akshay/Documents/Work/Project_1 (Colouring skin tones of mesh)/imgs"
extract_images_from_glb(glb_file, output_folder)