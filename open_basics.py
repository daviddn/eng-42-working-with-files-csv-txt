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

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file: # Doesn't need close method
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('File cannot be found. Please check your inputs', errmsg)
        # raise
    finally:
        print('\n Execution completed')

def write_to_file(file, order_item):
    try:
        opened_file = open(file, 'w')
        opened_file.write(order_item)

        opened_file.close()
    except FileNotFoundError:
        print('File not found')