#import argv from sys
from sys import argv

# pass command line arguments to variable argv
script, filename = argv

#This process prompts if you'd like to rewrite the passed .txt file
print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C(^C).")
print("If you want that, hit RETURN.")

input("?")

#opens the .txt file passed into argv
print("Opening the file...")
target = open(filename, 'w')

#truncates file. 
# NB: Since we opened the file in write mode ('w') we actually do not need this.
print("Truncating the file.  Goodbye!")
target.truncate()

#Creates a 3 variables for new text that will be written on 3 lines in .txt file
print("Now I'm going to ask you for three lines.")

line1 = input("line 1:  ")
line2 = input("line 2:  ")
line3 = input("line 3:  ")

formatter = "{} {} {}"
# Writes the variables into the file. 
print("I'm going to write these to the file.")

target.write(formatter.format(line1+"\n", line2+"\n", line3+"\n"))

#closes the .txt file.
print("And finally, we close it.")
target.close()
