# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and
# extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count = count + 1 # Calculate the total number of value
        # Extraction of number
        find = line.find(':') # Index of number
        value = line[find+1:] # Value that lies in the above index. Added 1 so that it doesn't pick :
        strp = value.strip() # strip newlines and space after ':'
        fvalue = float(strp) # Convert the value into float
        tot= tot+fvalue # calculate the total
    line = line.rstrip() # to 'remove' the newline of each line.
    print(line)
print(count)
print(tot)
print("Average spam confidence:", tot/count)
