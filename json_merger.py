import os
import json
import argparse

class JSONMerger:
    def __init__(self, input_folder, output_file):
        self.input_folder = input_folder
        self.output_file = output_file

    def merge_json_files(self):
        # List all files in the folder
        files = [f for f in os.listdir(self.input_folder) if os.path.isfile(os.path.join(self.input_folder, f))]

        # Initialize an empty list to store data from each file
        all_data = []

        # Iterate over each file
        for file_name in files:
            file_path = os.path.join(self.input_folder, file_name)

            try:
                # Read data from the file
                with open(file_path, 'r') as file:
                    file_data = json.load(file)

                # Extract metadata and observations
                metadata = file_data.get("metadata", {})
                observations = file_data.get("observations", {})

                # Add filename to each observation
                observations_with_filename = {plant: {"filename": file_name, **traits} for plant, traits in observations.items()}

                # Append data to the list
                all_data.append({
                    "filename": file_name,
                    "metadata": metadata,
                    "observations": observations_with_filename
                })

            except Exception as e:
                print(f"Error processing file {file_path}: {str(e)}")

        # Write the merged data to a new JSON file
        with open(self.output_file, 'w') as output_file:
            json.dump(all_data, output_file, indent=2)

        print(f"Merged data saved to {self.output_file}")

#     @staticmethod
#     def parse_arguments():
#         parser = argparse.ArgumentParser(description='Merge JSON files containing plant observation data.')
#         parser.add_argument('--input_folder', type=str, required=True, help='Path to the folder containing JSON files.')
#         parser.add_argument('--output_file', type=str, required=True, help='Path to save the merged JSON file.')
#         return parser.parse_args()

# def main():
#     # Parse arguments
#     args = JSONMerger.parse_arguments()

#     # Create an instance of JSONMerger and merge the files
#     merger = JSONMerger(args.input_folder, args.output_file)
#     merger.merge_json_files()

# if __name__ == "__main__":
#     main()