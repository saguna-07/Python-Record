with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire file
    print(content)
    with open("example.txt", "r") as file:
        line1 = file.readline()
with open("example.txt", "r") as file:
    all_lines = file.readlines()
    for line in all_lines:
        print(line.strip())  # Using .strip() to remove the newline character

