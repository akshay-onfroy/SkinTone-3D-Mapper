from pygltflib import GLTF2
import base64
import os

def extract_and_replace_images_from_glb(glb_file, output_folder, replacement_image_path):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Load the GLB file
    gltf = GLTF2().load(glb_file)
    
    # Read replacement image
    with open(replacement_image_path, 'rb') as image_file:
        replacement_image_data = image_file.read()
    
    for idx, image in enumerate(gltf.images):
        # Process only the second image (index 1)
        if idx == 1 and image.bufferView is not None:
            # Get current bufferView and buffer
            buffer_view = gltf.bufferViews[image.bufferView]
            buffer = gltf.buffers[buffer_view.buffer]
            
            # Get the full buffer data
            buffer_data = gltf.get_data_from_buffer_uri(buffer.uri)
            buffer_data = bytearray(buffer_data)
            
            # Extract original image data
            start = buffer_view.byteOffset if buffer_view.byteOffset else 0
            end = start + buffer_view.byteLength
            original_image_data = buffer_data[start:end]
            
            # Save original image
            output_path = os.path.join(output_folder, "bodyMesh.png")
            with open(output_path, "wb") as file:
                file.write(original_image_data)
            print(f"Extracted original image to: {output_path}")
            
            # Check sizes
            original_size = buffer_view.byteLength
            new_size = len(replacement_image_data)
            print(f"Original image size: {original_size} bytes")
            print(f"Replacement image size: {new_size} bytes")
            
            if new_size > original_size:
                raise ValueError("Replacement image is larger than original buffer space")
            
            # Calculate padding needed
            padding_size = original_size - new_size
            padding = b'\x00' * padding_size
            
            # Replace the data in the buffer, maintaining original size with padding
            buffer_data[start:start + new_size] = replacement_image_data
            buffer_data[start + new_size:start + original_size] = padding
            
            # Update the buffer in the GLTF object
            gltf.set_binary_blob(bytes(buffer_data))
            
            # Save the modified GLB
            gltf.save("/Users/akshay/Documents/Work/Project_3 ( Syncing proj 1 & 2)/glb/output.glb")
            print("Saved modified GLB with replaced image")
            
            return True
    
    return False
