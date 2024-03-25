# # Packages
import sys
import os

def is_valid_json_file(input_file: str) -> bool:
    """Check if the input file at file_path is a valid JSON file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        bool: True if the file is a valid JSON file, False otherwise.
    """
    # Check if the file is ends with '.json'
    if not input_file.lower().endswith('.json'):
        print("The input file is not a JSON file.")
        print(input_file.lower())
        return False
    # Check if the file is readable by Python
    try:
        with open(input_file, 'r') as f:
            data = f.read()
            return True
    except:
        print("The input file is readable.")
        return False

def rm_file(file_path: str):
    """Remove previous input file at file_path.

    Args:
        file_path (str): Path to the file.
    """
    os.system(f"rm {file_path}")

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

def build_http_server(tool_dir: str):
    """Build a HTTP server to host the visualization.
    Args:
        tool_dir (str): Path to the directory containing the visualization tool.
    """
    # Build the HTTP server
    os.system(f"python3 -m http.server -b 127.0.0.42 7800 -d {tool_dir}")

def main(argv):
    """Function that is executed first.

    Args:
        argv (list[type]]): Provided CLI arguments.
    """
    # Assign CLI arguments
    input_file, output_file, tool_dir = argv[1:4] 

    # Check for valid input file
    if not is_valid_json_file(input_file):
        sys.exit(1)
    
    # Remove previous input file if it exists - cause Galaxy is laggy
    rm_file(output_file)
    # Copy input file to 'data/input.json'
    copy_input_file_to_data_folder(input_file, output_file)
    # Build HTTP server to deploy ClassViz
    build_http_server(tool_dir)

if __name__ == "__main__":
    print("Running Visualization tool.")
    main(sys.argv)