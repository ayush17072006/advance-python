input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    print("Total number of lines:", len(lines))

    first_two = lines[:2]

    with open(output_file, "w") as file:
        file.writelines(first_two)

    print("First two lines written successfully.")

except FileNotFoundError:
    print("Error: Input file not found.")