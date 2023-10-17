
# Data validation taking into account the minimum possible number of characters
while True:
    chunk_size = input("Please enter the desired number of characters per line greater than 35:\n")
    # chunk_size = 54

    # import time
    # start_time = time.time()
    # print(start_time)
  
    try:
        chunk_size = int(chunk_size)
    except:
        print("The value entered must be a single integer number")
        continue

    if chunk_size <= 35:
        print("The number entered must be greater than 35")
        continue
    break

# Move to dir Task4 where a file text.txt is stored
# import os
# old_dir = os.getcwd()
# os.chdir("../../!!!Tasks/Task4")

# Open the file text.txt from dir Task4, return to the old_dir, read and write
# its content applying lines whose length depends on the number entered. 
with open("text.txt") as f:
    # os.chdir(old_dir)
    with open("formatted text.txt", "w") as new:
        lines = f.read(chunk_size+1)
        
        # Search for lines with '\n' symbol, define its index in a line and 
        # write the line before it. Return File Handle to the split position.
        # Read another line (chunk).
        while lines:
            for i in range(1, chunk_size):
                if "\n" in lines:
                    if lines[-i] == "\n":
                        new.write(lines[:-i].strip() + "\n")
                        f.seek(f.tell() - i+1)
                        lines = f.read(chunk_size+1)
                        break

                # Check if the current symbol starting from the end is a whitespace
                # or not. If not, continue searching
                elif lines[-i] != " ":
                    continue
                
                # If the current symbol is a whitespace, slice the line before 
                # this index, search for other whitespaces and replace single 
                # whitespaces with double taking into account of characters (i)
                # moved to the next line. Record output in new_lines
                else:
                    new_lines = ""
                    a = 0
                    for char in lines[:-i].strip():
                        if char == " ":
                            char = "  "
                            a += 1
                            if a >= i:
                                char = " "
                        new_lines += char                  
                    
                    # Check if new_lines is equal to defined line length (chunk). If so,
                    # write it, returtn File Handle taking into account the number of
                    # characters moved to the next line. Read another line (chunk)
                    if len(new_lines) == chunk_size:
                        new.write(new_lines + "\n")
                        f.seek(f.tell() - i+1)
                        lines = f.read(chunk_size+1)
                        break
                    
                    # If new_lines isn't equal to defined line length add whitespaces
                    # taking in to account the difference
                    else:
                        final_lines = ""
                        b = 0
                        for char in new_lines:
                            if char == " ":
                                char = "  "
                                b += 1
                                if b > (chunk_size - len(new_lines)):
                                    char = " "
                            final_lines += char

                        # Write the line obtained (final_lines), return File Handle
                        # taking into account the number of characters moved to the
                        # next line. Read another line (chunk)
                        new.write(final_lines + "\n")
                        f.seek(f.tell() - i+1)
                        lines = f.read(chunk_size+1)
                        break
            
            # Check the last line whose length is less than defined number (chunk).
            # Write it and break a loop 
            if len(lines) < chunk_size:
                new.write(lines)
                break

print(f"Your file with {chunk_size} characters per line is ready. \
Please open the file 'formatted text.txt'!")

# end_time = time.time()
# print(end_time)
# print('done', end_time - start_time)

                





