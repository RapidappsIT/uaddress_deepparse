import signal
import threading
import sys
import re
import pandas as pd
import csv
import os
import improver
from labels import LABELS
from colored import fg, attr, bg
from deepparse.parser import AddressParser

path_data = 'data/data.csv'

address_parser = AddressParser(
    device=0,
    model_type="bpemb", 
    attention_mechanism=True,
    path_to_retrained_model="./data/uaddress.ckpt"
)

##
# INTERRUPT
#
def interrupt(signal, frame):
    print("")
    print('#' * 50)
    print('Aborting pretrain!')
    print('#' * 50)
    
    sys.exit()

##
# SHOW LABELS
#
def show_labels():
   
    print('#' * 50)
    print('Labels')
    print('#' * 50)

    print("| {:<10}| {:<30} |".format('ID', 'NAME'))
    for key, item in enumerate(LABELS):
        print("| {:<10}| {:<30} |".format(key + 1, item))

##
# CHECK VALID
#
def check_valid(str):
    os.system('clear')

    str = improver.improve_address(str)

    address = address_parser(str)

    print("#" * 77)
    print("# Address: {}".format(str))
    print("#" * 77)

    print("#" * 77)
    print("# {!s:35} | {!s:35} #".format('Label', 'String'))
    print("#" * 77)

    for label, str in address.to_dict().items():

        print("| {!s:35} | {!s:35} |".format(label, str))

    print("#" * 77)

    if input("Address is valid? (yes(enter), no(n)): ") == 'n':
        return False
    
    return True
##
# SHOW STRINGS
#
def show_strings(ready, amount, address, str):
    os.system('clear')

    show_labels()

    print("#" * 50)
    print("Address ({}/{}): {}".format(ready, len(amount), address))
    print("#" * 50)

    print("#" * 50)
    stringPos = str['span']
    print("Address: ", address[:stringPos[0]] + ('%s%s%s%s' % (fg(16), bg(11), str['string'], attr(0))) + address[stringPos[1]:])
    print("#")
    print("String: ", str['string'])
    print("#" * 50)

##
# FINISH
#
def finish():
    os.system('clear')

    print("#" * 50)
    print("# Finish")
    print("#" * 50)

    sys.exit()

##
# READ LIST
#
def read_list():
    data = pd.read_csv('data/raw.csv', sep=";", header=None)
    
    stop = False
    repeat = True
    next_address = False
    ready = 1
    amount = data.index

    for name, item in data.iterrows():
        address = improver.improve_address(item[0])

        if check_valid(address): 
            ready += 1
            continue
            
        re_tokens = re.compile(r'\w+(?:\s|\.?)\-(?:\s)\w+|\(*\b[^\s,;#&]+[.)]*|\/\d+|[№][0-9]*', re.VERBOSE | re.UNICODE)
        
        data = []

        for item in re.finditer(re_tokens, address):
            data.append({
                'string': item.group(),
                'span': item.span()
            })

        while repeat:
            for key, item in enumerate(data):
                while True:
                    show_strings(ready, amount, address, item)
                    try:
                        label = input("Enter label ID or (stop(s), repeat(r), next(n)): ")
                        if label == 'stop' or label == 's':
                            stop = True
                            repeat = False
                        elif not label:
                            repeat = False
                        elif label == 'repeat' or label == 'r':
                            repeat = True
                            break
                        elif label == 'next' or label == 'n':
                            next_address = True
                            repeat = False
                        else:
                            if re.match(r'^\d+$', label):
                                data[key]['label'] = LABELS[int(label) - 1]
                                stop = False
                                repeat = False
                                break
                            else:
                                raise IndexError
                    except IndexError:
                        print("#" * 50)
                        print("Error ID label. Please correct ID label enter")
                        continue
                
                    if stop or next_address:
                        break
        
                if stop or repeat or next_address:
                    break
            
        ##

        if next_address is not True:
            if stop is not True:
                save_data(address, data)
                ready += 1
            else:
                interrupt('', '')
        else:
            ready += 1
            repeat = True
            next_address = False
            print("#" * 50)
            print('Skip address')

        if ready > len(amount):        
            finish()
        else:
            repeat = True

    finish()

##
# SAVE DATA
#
def save_data(address, data):

    if os.path.exists(path_data):
        with open(path_data, 'a') as file:
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_ALL)
            
            columns = {
                'Address': address,
                'Tags': [item['label'] for item in data]
            }

            writer.writerow(columns.values())

    else:
        with open(path_data, 'w') as file:
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_ALL)
            
            columns = {
                'Address': address,
                'Tags': [item['label'] for item in data]
            }

            writer.writerow(columns.keys())
            writer.writerow(columns.values())

    os.system("cp data/data.csv data/test.csv")
            
##
# INIT
#
if __name__ == "__main__":
    os.system('clear')

    signal.signal(signal.SIGINT, interrupt)

    read_list()

    forever = threading.Event()
    forever.wait()