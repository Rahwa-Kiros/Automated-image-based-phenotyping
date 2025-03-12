import os
from plantcv import plantcv as pcv

class ImageCropper:
    def __init__(self, input_dir, output_dir, crop_coords):
        """
        Initialize the ImageCropper with input directory, output directory, and crop coordinates.
        
        :param input_dir: Directory where input images are stored.
        :param output_dir: Directory where cropped images will be saved.
        :param crop_coords: Tuple (x, y, h, w) for cropping the image.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.crop_coords = crop_coords
        
        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def get_image_files(self, folder_path):
        """List all image files in the input folder."""
        return [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.tiff'))]

    def crop_image(self, image_path):
        """Crop the image based on predefined coordinates."""
        img, path, filename = pcv.readimage(filename=image_path)
        
        # Crop the image using the given coordinates (x, y, h, w)
        x, y, h, w = self.crop_coords
        cropped_img = pcv.crop(img=img, x=x, y=y, h=h, w=w)
        
        return cropped_img

    def save_cropped_image(self, cropped_img, output_path):
        """Save the cropped image to the output folder."""
        pcv.print_image(cropped_img, output_path)
        print(f"Cropped image saved as: {output_path}")

    def process_images(self):
        """Process all the images in both BOTTOM and TOP folders."""
        # Initialize the counter to cycle through GA, GB, GC
        counter = 0
        
        # List all subdirectories inside the input directory (e.g., 'BOTTOM' and 'TOP')
        for folder_name in os.listdir(self.input_dir):
            folder_path = os.path.join(self.input_dir, folder_name)
            
            # Only process if it's a folder
            if os.path.isdir(folder_path):
                # Get all image files from the current folder
                image_files = self.get_image_files(folder_path)
                
                for image_file in image_files:
                    input_image_path = os.path.join(folder_path, image_file)

                    # Modify the filename based on the folder name
                    base_name, ext = os.path.splitext(image_file)
                    
                    # Folder-specific suffix and label cycling
                    if "BOTTOM" in folder_name.upper():
                        suffix = "_christa"
                    elif "TOP" in folder_name.upper():
                        suffix = "_eleven"
                    else:
                        suffix = ""

                    # Set the GA, GB, GC pattern
                    label = ['GA', 'GB', 'GC'][counter % 3]  # Cycle through GA, GB, GC

                    # Create the new file name by adding the timestamp, label, and suffix
                    new_image_name = f"{base_name}_{label}{suffix}{ext}"
                    new_image_path = os.path.join(self.output_dir, new_image_name)

                    # Crop the image
                    cropped_img = self.crop_image(input_image_path)

                    # Save the cropped image with the new filename
                    self.save_cropped_image(cropped_img, new_image_path)

                    print(f"Processed file: {image_file} -> {new_image_name}")

                    # Increment the counter and reset after 3 (GA, GB, GC cycle)
                    counter += 1
                    if counter == 3:
                        counter = 0  # Reset the counter after GC

# Example usage
if __name__ == "__main__":
    input_directory = "Seaweed biostimulant Rahwa"  # Root directory containing 'BOTTOM' and 'TOP' folders
    output_directory = "OUTPUT"  
    
    # Define crop coordinates (x, y, height, width)
    crop_coordinates = (820, 320, 850, 780)  # Update this as needed
 
     
    
    # Create an instance of ImageCropper with the specified directories and crop coordinates
    cropper = ImageCropper(input_dir=input_directory, output_dir=output_directory, crop_coords=crop_coordinates)
    
    # Process the images in the input folders ('BOTTOM' and 'TOP')
    cropper.process_images()