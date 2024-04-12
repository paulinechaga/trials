# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write('This is line 1\n')
        file.write('This is line 2\n')
        file.write('The number is 3\n')

    # File Reading and Display
    with open('my_file.txt', 'r') as file:
        print(file.read())

   # File Appending
    with open('my_file.txt', 'a') as file:
        file.write('Appending line 1\n')
        file.write('Appending line 2\n')
        file.write('Appending line 3\n')

    # Display the final content
    with open('my_file.txt', 'r') as file:
        print(file.read())

except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution of the script has ended.")
