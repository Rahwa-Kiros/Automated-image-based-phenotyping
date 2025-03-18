# Automated-image-based-phenotyping
This repository provides an automated image-based phenotyping system designed to analyze plant growth, health, and other phenotypic traits. plantCV and machine learning, the system processes images or videos of plants to extract critical data such as plant height, leaf area, RGB color.


## list of Libraries and packages used in the project
pandas: Data manipulation library. numpy: Numerical computation library. argparse: Command-line argument parsing.KNeighborsRegressor: plantcv: A Python package for image processing and analysis in plant science. os: to interact with the operating system. %matplotlib widget: to creating static, animated, and interactive visualizations. pandas:to analyzing, cleaning, exploring, and manipulating data. scipy. stats: used for probabilistic distributions and statistical operations. matplotlib and seaborn: used for data visualization. Json library: used to parse JSON from strings or files.

# Repository Structure

## python scripts

#### image_cropper.py
This script utilizes the PlantCV library to crop image for further analyses.
To run the code open teminal and execure the following command
##### "python <script_name>"

#### multi_plantworkflow.py
This script utilizes PlantCV, a Python library designed for multi plant image analysis, to process images in a specified directory. It performs tasks such as thresholding, masking, and size analysis. Results are saved in JSON format for each processed image.

#### json_merger.py
The script reads JSON files from a specified input directory, extracts metadata and observations from each file, and merges them into a consolidated JSON format. Each observation is tagged with its original file name for reference.
this scripte used to merge the file 

#### main.py
The main.py script serves as the entry point for running the entire image processing workflow. It orchestrates the execution of the other scripts by taking input arguments, such as the directories for input images and output results, as well as the filename for the merged JSON file. The script runs the cropping, multi-plant analysis, and JSON merging tasks in sequence, facilitating a streamlined processing pipeline.

To run this script, open the terminal and execute the following command:
###### "python <script_name> --input_dir <path_to_input_folder> --output_dir <path_to_output_folder> --result_file <result_directory> --merged_file  <out_put_file-name.json>"

    Where:
    --input_dir specifies the directory containing the input images.
    --output_dir specifies where to save the processed images.
    --result_file is the directory where the individual image results (in JSON format) will be saved.
    --merged_file is the filename for the final consolidated JSON output.

## Jupyter Notebook Files
    1. single_plant_processing.ipynb': Processing data obtained from multiple plant analysis methods using PlantCV for further analysis.
    2. json_data_processing.ipynb : process the json data obtained from multi_plantworkflow.


#### To run the Jupyter Notebook files above, open each file in a Jupyter Notebook environment and execute cells sequentially by selecting a cell and clicking the run button or running all cells simultaneously.

## Additional Considerations:
Python Version Compatibility
PlantCV version compatibility
