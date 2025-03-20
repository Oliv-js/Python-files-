import os

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
else:
    modified_content = content.upper()
    
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}_modified{ext}"
    
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Successfully wrote modified content to {new_filename}")
    except PermissionError:
        print(f"Error: Permission denied to write to '{new_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")
