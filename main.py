import argparse
from multi_plantworkflow import MultiPlantWorkflow
from json_merger import JSONMerger

def parse_arguments():
    parser = argparse.ArgumentParser(description='Combine multiple tasks.')
    parser.add_argument('--input_dir', type=str, required=True, help='Input directory')
    parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('--result', type=str, required=True, help='Result file name')
    parser.add_argument('--merged_file', type=str, required=True, help='Output merged JSON file name')
    return parser.parse_args()

def main():
    args = parse_arguments()


    # Create an instance of MultiPlantWorkflow
    workflow = MultiPlantWorkflow(input_dir=args.input_dir, result=args.result, outdir=args.output_dir)
    workflow.run()

    # Create an instance of JSONMerger
    merger = JSONMerger(input_folder=args.output_dir, output_file=args.merged_file)
    merger.merge_json_files()

if __name__ == "__main__":
    main()