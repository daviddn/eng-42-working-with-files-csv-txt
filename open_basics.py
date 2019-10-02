# Here we define our open/close functions

def open_read_file(file):
    try:
        opened_file = open(file, 'r')
        # print(type(opened_file)) # Not something we can work with
        file_lines_list = opened_file.readlines() # Something we can work with
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))

        opened_file.close() # Otherwise file is locked and can't be changed

    except FileNotFoundError as errmsg:
        print('File cannot be found. Please check your inputs', errmsg)
        raise
