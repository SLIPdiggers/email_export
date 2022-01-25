# Paste email contacts into a text file and specify paths here.
# Script will pick out usernames and (over)write to a csv
import sys
import numpy as np

open_path = "C:\\Users\\Big\\Desktop\\allstaff.txt"
write_path = "usernames.csv"

user_array = np.array("Usernames")

try:
        with open(open_path, 'r') as f:
                tokens = f.read()
except:
        print("File not read! Does it exist?")
        sys.exit()
try:
        f = open(write_path, "w")
except:
        print("Cannot write to Destination File! Already open in another program?")
        sys.exit()
        

#print(tokens)

flag = False
user = ""

for char in tokens:
#        print("char = ", char)
#        print("user = ", user)
        if char == None:
                user += ""
        if char == '@':
                flag = False
        if flag == True:
                user += char
        if char == '<':
                flag = True
                user_array = np.append(user_array, user)
                user_array = np.append(user_array, ',')
                user_array = np.append(user_array, '\n')
                print(user)
                user = ""
#print(user_array)

try:
        for item in user_array:
                f.write(item)
except:
        print("Failed to write to file part way through. Open in another program?")
        sys.exit()

f.close()
print("\n\nOperation completed. Usernames from " + open_path + " extracted and written to " + write_path)

