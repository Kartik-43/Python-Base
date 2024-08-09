# To write in the file we need to change the mode to w...
# If file exists it will rewrite the whole file to the values provided by the user....

with open('My_File.txt', mode='w') as file:
    content = file.write('New_Text.')
    print(content)

# If file does not exist it will create the file from scratch...

with open('New_File.txt', mode='w') as file:
    content = file.write('New_Text.')
    print(content)
