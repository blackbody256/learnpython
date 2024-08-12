f = open('my_file.txt', 'w')#the 'w' is for write, you can even use r for read
f.write("Hello there!")
f.close()


#another  way to write in a file which is better coz it closes the object automatically
with open('my_file.txt', 'r') as f:
    file_data = f.read()
print(file_data)

#the one below reads with parameters of an integer
with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())


camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)