import os
import argparse
from plantcv import plantcv as pcv

class Crop:
    def __init__(self, input_dir, output_dir, x, y, width, height, debug=False, writeimg=False, result=None):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.debug = debug
        self.writeimg = writeimg
        self.result = result

    def crop_image(self, image_path):
        # Read the image
        img=  pcv.readimage(filename=image_path)
        
    
        # # Debug: check if img is a valid image array
        # if isinstance(img, tuple):
        #     print(f"Error reading image: {image_path}")
        #     return None  # or handle the error appropriately
        
        # Crop the image
        cropped_img = img[self.y:self.y + self.height, self.x:self.x + self.width]
        
        # Save the cropped image if writeimg is True
        if self.writeimg:
            filename = os.path.basename(image_path)
            output_path = os.path.join(self.output_dir, filename)
            pcv.print_image(cropped_img, output_path)
        
        return cropped_img

    def process_images(self):
        # List all files in the directory
        all_files = os.listdir(self.input_dir)
        # Filter for common image file extensions (add more if needed)
        image_files = [f for f in all_files if f.endswith(('.png', '.jpg', '.jpeg'))]
        # Iterate over each image and apply the cropping function
        for image_file in image_files:
            full_image_path = os.path.join(self.input_dir, image_file)
            cropped_img = self.crop_image(full_image_path)
            # Save the cropped image to the output directory
            output_path = os.path.join(self.output_dir, image_file)
            # pcv.print_image(cropped_img, output_path)
            print(f"Cropped image saved to {output_path}")
            # Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop images in a directory.")
    parser.add_argument("input_dir", help="Directory with input images.")
    parser.add_argument("output_dir", help="Directory to save cropped images.")
    parser.add_argument("x", type=int, help="X coordinate of the top-left corner of the crop box.")
    parser.add_argument("y", type=int, help="Y coordinate of the top-left corner of the crop box.")
    parser.add_argument("width", type=int, help="Width of the crop box.")
    parser.add_argument("height", type=int, help="Height of the crop box.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("--writeimg", action="store_true", help="Save cropped images.")
    args = parser.parse_args()
    cropper = Crop(args.input_dir, args.output_dir, args.x, args.y, args.width, args.height, args.debug, args.writeimg)
    cropper.process_images()
  