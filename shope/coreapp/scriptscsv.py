with open('auto.csv', mode='r') as file1, \
        open('autonew.csv', mode='w') as file2:
    lines = file1.readlines()
    for line in lines:
        new_line = line[:len(line)-2] + '\n'
        file2.write(new_line)
