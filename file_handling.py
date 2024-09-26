# file_handling_assignment.py

# Step 1: Create a new text file and write to it
with open('my_file.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("The second line includes a number: 42.\n")
    file.write("Finally, here’s the third line: Python is great!\n")

# Step 2: Read the contents of the file and display them
print("Contents of my_file.txt:")
with open('my_file.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Step 3: Append additional lines to the file
with open('my_file.txt', 'a') as file:
    file.write("This is the fourth line added by appending.\n")
    file.write("Here’s the fifth line with another number: 100.\n")
    file.write("And this is the sixth line for good measure!\n")

# Display the updated contents
print("Updated contents of my_file.txt after appending:")
with open('my_file.txt', 'r') as file:
    updated_contents = file.read()
    print(updated_contents)
