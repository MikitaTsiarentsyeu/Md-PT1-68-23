def evenly_justify_text(text, max_line_length):
    if max_line_length <= 35:
        return "Maximum number of characters per line must be greater than 35."

    words = text.split()
    lines = []
    current_line = []
    current_line_length = 0

    for word in words:
        word_length = len(word)

        if current_line_length + len(current_line) + word_length <= max_line_length:
            current_line.append(word)
            current_line_length += word_length
        else:
            lines.append(current_line)
            current_line = [word]
            current_line_length = word_length

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for line in lines:
        if len(line) > 1:
            total_word_length = sum(len(word) for word in line)
            total_spaces_needed = max_line_length - total_word_length
            spaces_per_gap = total_spaces_needed // (len(line) - 1)
            extra_spaces = total_spaces_needed % (len(line) - 1)

            justified_line = line[0]
            for i in range(1, len(line)):
                gap_spaces = spaces_per_gap
                if extra_spaces > 0:
                    gap_spaces += 1
                    extra_spaces -= 1
                justified_line += ' ' * gap_spaces + line[i]

            justified_lines.append(justified_line)
        else:
            justified_lines.append(line[0])

    return '\n'.join(justified_lines)

# Prompt the user for input
user_input = input("Enter the text to be justified: ")

# Prompt the user for the maximum number of characters per line
try:
    max_line_length = int(input("Enter the maximum number of characters per line (greater than 35): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Check if the maximum number of characters per line is valid
if max_line_length <= 35:
    print("Maximum number of characters per line must be greater than 35.")
else:
    # Justify the text based on the specified maximum line length
    progres = evenly_justify_text(user_input, max_line_length)

    # Write the resulting text to a new file
    with open("progres.txt", "w") as file:
        file.write(progres)

    print("Text has been justified and written to 'progres.txt'.")
    