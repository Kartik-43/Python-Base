''' Writes Or Appends the data given by user... '''

mode = input('What do you want to do Write or Append ("w" for write and "a" for append) :- ').lower()
d = input('Enter the name of the file you want to create or append :- ').lower()

f = open(f"{d}" , f'{mode}')

if mode == 'a':
    Start = input('Do you want to start appending from the new line? (y or n) : ').lower()
    if Start == 'y':
        z = input('Enter the text you want to add to file(ADD \\n for NEW LINE) :- ')
        f.write('\n'+ z)
    else:
        z = input('Enter the text you want to add to file(ADD \\n for NEW LINE) :- ')
        f.write(z)

f.close( )
