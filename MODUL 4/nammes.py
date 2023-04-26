new_name = 'Luke'
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)

with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)