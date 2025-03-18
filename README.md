# Automated-image-based-phenotyping
This repository provides an automated image-based phenotyping system designed to analyze plant growth, health, and other phenotypic traits. plantCV and machine learning, the system processes images or videos of plants to extract critical data such as plant height, leaf area, RGB color.


## list of Libraries and packages used in the project
pandas: Data manipulation library. numpy: Numerical computation library. argparse: Command-line argument parsing.KNeighborsRegressor: plantcv: A Python package for image processing and analysis in plant science. os: to interact with the operating system. %matplotlib widget: to creating static, animated, and interactive visualizations. pandas:to analyzing, cleaning, exploring, and manipulating data. scipy. stats: used for probabilistic distributions and statistical operations. matplotlib and seaborn: used for data visualization. Json library: used to parse JSON from strings or files.

# Repository Structure
### python scripts
#### crop_image.py
This script utilizes the PlantCV library to crop image for further analyses. the class in the scripet is import to the main function to run unsig srguments.

###### To run this script open terimal and execute "python <script_name> --input_dir <path_to_input_folder> --output_dir <path_to_output_folder> --result_file <result_directory> --merged_file  <out_put_file-name.json>"

