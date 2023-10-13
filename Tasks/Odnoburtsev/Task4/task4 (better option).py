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

    with open("new formatted text.txt", "w") as new:
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
                # or not. If yes, write the line in new. If not, continue searching
                elif i == 1 and lines[-i] == " ":
                    new.write(lines[:-i].strip() + "\n")
                    f.seek(f.tell())
                    lines = f.read(chunk_size+1)
                    break

                elif lines[-i] != " ":
                    continue
                
                # If the current symbol is a whitespace, slice the line before 
                # this index, search for whitespaces in the line and replace single 
                # whitespaces with required number of whitespaces taking into
                # account of the number of characters (i) moved to the next line. 
                # Record output in new_lines
                else:
                    gaps_number = len(lines[:-i].strip().split(" "))-1
                    all_spaces_number = chunk_size - len(lines[:-i].strip()) + gaps_number
                    spaces_per_gap = all_spaces_number // gaps_number
                    resid_spaces = all_spaces_number%gaps_number
                    new_lines = lines[:-i].strip().replace(" ", spaces_per_gap*" ")

                    # If the residue of whitespaces isn't equal 0 replace existing
                    # whitespaces with the number increased by 1. Perform this
                    # operation the number of times that is equal to resid_spaces.
                    # Write the output in the file new and return File Handle 
                    # in a required position.
                    new_lines = new_lines.replace(spaces_per_gap*" ", (spaces_per_gap+1)*" ", resid_spaces)
                    
                    new.write(new_lines + "\n")
                    f.seek(f.tell() - i+1)
                    lines = f.read(chunk_size+1)
                    break
         
            # Check the last line whose length is less than defined number (chunk).
            # Write it and break a loop 
            if len(lines) < chunk_size:
                new.write(lines)
                break

print(f"Your file with {chunk_size} characters per line is ready. \
Please open the file 'new formatted text.txt'!")

# end_time = time.time()
# print(end_time)
# print('done', end_time - start_time)