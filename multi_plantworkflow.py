import os
import argparse
from plantcv import plantcv as pcv

class MultiPlantWorkflow:
    def __init__(self, input_dir, result, outdir, writeimg=False, debug=None):
        self.input_dir = input_dir
        self.result = result
        self.outdir = outdir
        self.writeimg = writeimg
        self.debug = debug
        self.results_list = []  # List to store results

    def setup(self):
        # Set up the debug and output directories
        pcv.params.debug_outdir = self.outdir
        pcv.params.debug = self.debug
         # Set plotting size (default = 100)
        pcv.params.dpi = 100
        # Increase text size and thickness for clarity
        pcv.params.text_size = 20
        pcv.params.text_thickness = 20
        pcv.params.line_thickness = 1

    def process_image(self, image_file):
        # Construct the full path to the image
        image_path = os.path.join(self.input_dir, image_file)

        try:
            # Read the image
            img, path, filename = pcv.readimage(filename=image_path)

            # Crop image if necessary. This is optional.
            croped_img = pcv.crop(img=img, x=70, y=70, h=650, w=490)

            # Rotate input image 90 degrees
            rotate_img = pcv.transform.rotate(croped_img, 90, False)

            # apply dual channels threshold
            l_v_thresh = pcv.threshold.dual_channels(rgb_img = rotate_img, x_channel = "v", y_channel = "l", points = [(40,80),(40,80)],above=True)
            
            # Fill in small objects if the above threshold looks like there are "holes" in the leaves
            a_fill_image = pcv.fill(bin_img=l_v_thresh, size=150)
          
            # Mask images
            mask = pcv.apply_mask(img=rotate_img, mask=a_fill_image, mask_color='black')

             # Find objects in the binary image
            # Make a grid of ROIs
            roi_objects =pcv.roi.multi(img=mask, coord=(70,90), radius=60, 
                                                spacing=(170, 150), nrows=3, ncols=4)
            # reate a labeled mask for use with analysis functions. this is different from the binary image
            labeled_mask, num_plants = pcv.create_labels(mask=a_fill_image, rois=roi_objects, roi_type="partial")

            
            # Analyze the shape of each plant 
            pcv.analyze.size(img=rotate_img, labeled_mask=labeled_mask, n_labels=num_plants, label="plant")

            # Analyze color
            pcv.analyze.color(rgb_img=rotate_img, labeled_mask=labeled_mask, n_labels=num_plants, colorspaces="HSV")

            # Save results in JSON format
            result = pcv.outputs.save_results(filename=f"{self.result}_{image_file}", outformat='json')

            # Append the result to the list
            self.results_list.append(result)

        except Exception as e:
            print(f"Error processing image {image_path}: {str(e)}")

    def run(self):
        # Set up the workflow
        self.setup()

        # Get a list of all files in the input folder
        image_files = [f for f in os.listdir(self.input_dir)]

        # Process each image in the folder
        for image_file in image_files:
            self.process_image(image_file)

# def parse_arguments():
#     # Argument parsing function
#     parser = argparse.ArgumentParser(description="PlantCV multi-plant workflow")
#     parser.add_argument("--input_dir", help="Input directory containing images", required=True)
#     parser.add_argument("--result", help="Results file", required=True)
#     parser.add_argument("--outdir", help="Output directory", required=True)
#     parser.add_argument("--writeimg", help="Save output images", action="store_true")
#     parser.add_argument("--debug", help="Set debug mode", default=None)
#     args = parser.parse_args()
#     return args

# def main():
#     # Parse arguments
#     args = parse_arguments()

#     # Create an instance of PlantCVWorkflow with the parsed arguments
#     workflow = multi_plantworkflow(
#         input_dir=args.input_dir,
#         result=args.result,
#         outdir=args.outdir,
#         writeimg=args.writeimg,
#         debug=args.debug
#     )

#     # Run the workflow
#     workflow.run()

# if __name__ == "__main__":
#     main()