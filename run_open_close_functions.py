from open_basics import *

# Here we'll run all our functions

# open_read_file('order.txt')
#
# open_read_file_using_with('order.txt')

write_to_file('order.txt', 'Cake')

open_read_file_using_with('order.txt')

list_order = ['Sea Bass Grilled', 'Champagne Sangria', 'Clams']

for item in list_order:
    write_to_file('order.txt', item)