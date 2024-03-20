# # Packages
import sys

def main(argv):
    """Put user input JSON file to data folder.

    Args:
        argv (list[type]]): Provided CLI arguments.
    """
    input_file = argv[1] # Assign CLI arguments
    print(f'Input file: {input_file}')
    with open(input_file, 'r') as f:
        data = f.read()
        with open('data/input.json', 'w') as f:
            f.write(data)

if __name__ == "__main__":
    print("Copying input file to 'input.json'.")
    main(sys.argv)