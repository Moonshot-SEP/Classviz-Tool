# # Packages
import sys

def is_valid_json_file(file_path: str) -> bool:
    """Check if the input file at file_path is a valid JSON file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        bool: True if the file is a valid JSON file, False otherwise.
    """
    # Check if the file is ends with '.json'
    if not file_path.lower().endswith('.json'):
        print("The input file is not a JSON file.")
        return False
    # Check if the file is readable by Python
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return True
    except:
        print("The input file is readable.")
        return False

def copy_input_file_to_data_folder(input_file: str, output_file: str):
    """Copy content of user input JSON file to 'data/input.json'.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file ('data/input.json').
    """
    # for debugging
    # print(f'Input file: {input_file}')
    # print(f'Output file: {output_file}')

    # Get content of input file
    with open(input_file, 'r') as f:
        data = f.read()
        # Write content to output file
        with open(output_file, 'w') as f:
            f.write(data)

def main(argv):
    """Function that is executed first.

    Args:
        argv (list[type]]): Provided CLI arguments.
    """
    # Assign CLI arguments
    input_file, output_file = argv[1:3] 

    # Check for valid input file
    if not is_valid_json_file(input_file):
        sys.exit(1)
    
    # Copy input file to 'data/input.json'
    copy_input_file_to_data_folder(input_file, output_file)

if __name__ == "__main__":
    print("Copying input file to 'data/input.json'.")
    main(sys.argv)