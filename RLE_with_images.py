# Complete code for the Project 2
import console_gfx # Importing a given file


# Function for displaying the menu
def display_menu():
    print("\nRLE Menu\n"
          "--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")


# Main function for interpreting the input correctly
def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    image_data = None

    while True: # Using a while loop to complete the program until input is 0
        display_menu()
        try:
            option = int(input("Select a Menu Option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 9.")
            continue

        if option == 0:
            break  # Exiting the program

        elif option == 1:  # Loading a file
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)

        elif option == 2:  # Loading a test image
            image_data = console_gfx.test_image
            print("Test image data loaded.")

        elif option == 3:  # Reading RLE String
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))

        elif option == 4:  # Reading RLE Hex String
            rle_hex_string = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex_string))

        elif option == 5:  # Reading Flat Hex String
            flat_hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex_string)

        elif option == 6:  # Displaying Image
            if image_data is None:
                print("No image data loaded.")
            else:
                print("Displaying image...") # Needed portion to correctly fulfill the requirements
                console_gfx.display_image(image_data)

        elif option == 7:  # Displaying RLE String in human-readable format
            if image_data is None:
                print("No image data loaded.")
            else:
                print(f"RLE representation: {to_rle_string(encode_rle(image_data))}")

        elif option == 8:  # Displaying RLE Hex Data
            if image_data is None:
                print("No image data loaded.")
            else:
                print(f"RLE hex values: {to_hex_string(encode_rle(image_data))}")

        elif option == 9:  # Displaying Flat Hex Data
            if image_data is None:
                print("No image data loaded.")
            else:
                print(f"Flat hex values: {to_hex_string(image_data)}")

        else: # If not any of the numbers were plugged in
            print("Invalid option! Please select a number between 0 and 9.")



# Function for the translating data to a hexadecimal string
def to_hex_string(data):
    hex_str = ''
    for num in data: # Using a for loop
        hex_str += format(num, 'x') # Converting each number to hexadecimal and adding to the string
    return hex_str


# Function for returning the number of runs of data in an image data set
def count_runs(flat_data):
    if not flat_data:
        return 0 # Handling an empty list if needed

    run_count = 1
    run_length = 1
    # Using a for loop
    for i in range(1, len(flat_data)): # Starting from the second item
        if flat_data[i] == flat_data[i - 1] and run_length < 15:
            run_length += 1
        else:
            run_count += 1
            run_length = 1

    return run_count


# Function for returning the encoding of the raw data passed in
def encode_rle(flat_data):
    if not flat_data:
        return []

    encoded = []
    run_length = 1
    # Using a for loop
    for i in range(1, len(flat_data)): # Starting from the second item
        if flat_data[i] == flat_data[i - 1] and run_length < 15:
            run_length += 1
        else:
            encoded.extend([run_length, flat_data[i - 1]])
            run_length = 1

    encoded.extend([run_length, flat_data[-1]])
    return encoded


# Function for the returning decompressed size RLE data
def get_decoded_length(rle_data):
    total_length = 0 # Using a for loop
    for i in range(0, len(rle_data), 2): # Iterating over the run lengths
        total_length += rle_data[i]
    return total_length


# Function for the returning of the decoded data set from RLE encoded data
def decode_rle(rle_data):
    decoded = [] # Using a for loop
    for i in range(0, len(rle_data), 2): # Iterating over the run lengths
        run_length = rle_data[i]
        pixel_value = rle_data[i + 1]
        decoded.extend([pixel_value] * run_length)
    return decoded


# Function for translating a string in a hexadecimal format into byte data
def string_to_data(hex_string):
    result = []
    for char in hex_string: # Using a for loop
        result.append(int(char, 16))
    return result


# Function for translating RLE data into a human-readable representation
def to_rle_string(rle_data):
    rle_string = ""

    for i in range(0, len(rle_data), 2): # Using a for loop to complete the function
        run_length = str(rle_data[i])
        run_value = hex(rle_data[i + 1])[2:].upper() # Running a hexadecimal
        rle_string += run_length + run_value
        if i + 2 < len(rle_data): # Delimiter between runs
            rle_string += ":"

    return rle_string


# Function for translating a string in human-readable RLE format into RLE byte data
def string_to_rle(rle_string):

    rle_string = rle_string.replace(":", " ")
    parts = [] # Creating a list
    current_part = ""


    for char in rle_string: # Using a for loop to reorder properly
        if char == " ":
            parts.append(current_part)
            current_part = ""
        else:
            current_part += char

    parts.append(current_part)


    rle_data = []
    for part in parts: # Using a for loop to complete the rest of the function
        run_length = int(part[:-1])
        run_value = int(part[-1], 16)
        rle_data.append(run_length)
        rle_data.append(run_value)

    return rle_data

if __name__ == "__main__": # Required final portion of the project
    main()