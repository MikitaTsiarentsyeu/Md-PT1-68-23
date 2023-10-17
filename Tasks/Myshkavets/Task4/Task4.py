def format_text(input_file, output_file, max_line_length):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    formatted_lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) <= max_line_length:
            current_line += word + " "
        else:
            formatted_lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        formatted_lines.append(current_line.strip())

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in formatted_lines:
            words = line.split()
            if len(words) > 1:
                num_gaps = max_line_length - sum(len(word) for word in words)
                while num_gaps > 0:
                    for i in range(len(words) - 1):
                        words[i] += " "
                        num_gaps -= 1
                        if num_gaps == 0:
                            break
            f.write(" ".join(words) + '\n')

if __name__ == "__main__":
    max_line_length = int(input("Enter the maximum number of characters per line (more than 35): "))
    if max_line_length <= 35:
        print("The maximum number of characters must be greater than 35.")
    else:
        input_file = r'C:\Users\Maxim\Desktop\Md-PT1-68-23\Tasks\Myshkavets\Task4\text.txt'
        output_file = r'C:\Users\Maxim\Desktop\Md-PT1-68-23\Tasks\Myshkavets\Task4\formatted_text.txt'
        format_text(input_file, output_file, max_line_length)
        print("The text has been successfully formatted and saved in formatted_text.txt.")
