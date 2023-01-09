import os

# Creating a function to filter out comments and print to stripped_diff
def custom_diff(tag1, tag2, file_name):
  original_diff_file = open("original_diff", "w")
  print("Printing diff to original_diff...")
  if file_name == "":
 subprocess.call(['git', 'diff', tag1, tag2], stdout=original_diff_file) # Executing git diff via subprocess and printing to original_diff for all files
  else:
	subprocess.call(['git', 'diff', tag1, tag2, file_name], stdout=original_diff_file) # Executing git diff via subprocess and printing to original_diff for a given file
  write_path = "stripped_diff"
  read_path = "original_diff"
  flag = False # Creating an indicator for the beginning of a multi-line comment
  function_flag = False # Creating an indicator for when the user searches for a function
  line_counter = 0
  print("Stripping comments and sending to stripped_diff...")
  with open(read_path) as original_diff:  # Opening original_diff to be read
  	with open(write_path, 'w') as write_file: # Opening stripped_diff to be written in
      	for line in original_diff:
        	if args.function_name != "":
          	if line.find(args.function_name) != -1 and function_flag == False:
            	line_counter = 0
            	function_flag = True
          	if function_flag == True and line_counter < int(args.lines):
            	line_temp = line.replace(" ", "") # Creating a temporary whitespace-free line
            	if line_temp.startswith("+/**") or line_temp.startswith("-/**"):
              	flag = True
              	continue
            	if (line_temp.startswith("+*") or line_temp.startswith("-*")) and flag == True:
              	if line_temp.endswith("*/"):
                	flag = False
              	continue
            	if not (line_temp.startswith("+/*") or line_temp.startswith("-/*") or line_temp.startswith("/*")  or line_temp.startswith("+//") or line_temp.startswith("-//") or line_temp.startswith("+0x") or line_temp.startswith("-0x")):
                  	write_file.write(line)
                  	line_counter = line_counter + 1
        

	else:
          	line_temp = line.replace(" ", "") # Creating a temporary whitespace-free line
          	if line_temp.startswith("+/**") or line_temp.startswith("-/**"):
            	flag = True
            	continue
          	if (line_temp.startswith("+*") or line_temp.startswith("-*")) and flag == True:
            	if line_temp.endswith("*/"):
              	flag = False
            	continue
          	if not (line_temp.startswith("+/*") or line_temp.startswith("-/*") or line_temp.startswith("/*")  or line_temp.startswith("+//") or line_temp.startswith("-//") or line_temp.startswith("+0x") or line_temp.startswith("-0x")):
                	write_file.write(line)