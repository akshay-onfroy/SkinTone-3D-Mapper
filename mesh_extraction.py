from pygltflib import GLTF2, ImageFormat
from PIL import Image as PILImage
import io

def extract_images_from_glb(filename):
    gltf = GLTF2().load(filename)
    # Convert the images to PNG format
    gltf.convert_images(ImageFormat.FILE)
    gltf.images[0].uri

