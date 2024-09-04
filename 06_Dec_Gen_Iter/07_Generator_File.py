def read_file_generator():
    with open("./myfile.txt") as file:
        for line in file:
            yield line 

    
for line in read_file_generator():
    print(line)