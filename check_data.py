import signal
import threading
import pandas as pd
import re
import os
import sys
import ast

path_data = 'data/data.csv'

##
# INTERRUPT
#
def interrupt(signal, frame):
    print('')
    print('#'*50)
    print('Aborting checking!')
    print('#'*50)
    sys.exit(0)

##
# READ
#
def read():
    data = pd.read_csv(path_data, sep=';', header=0)

    amount = data.index
    ready = 1

    for name, item in data.iterrows():

        re_tokens = re.compile(r'\w+(?:\s|\.?)\-(?:\s)\w+|\(*\b[^\s,;#&]+[.)]*|\/\d+|[№][0-9]*', re.VERBOSE | re.UNICODE)

        print("#" * 50)
        print("# Checking data ({}/{})".format(ready, len(amount)))
        print("#" * 50)
        print("# Address: {}".format(item[0]))
        print("#" * 50)
        print("| {:<30} | {:<30}".format('String', 'Label'))

        for index, label in enumerate(ast.literal_eval(item[1])):
            print("| {:<30} | {:<30}".format(re_tokens.findall(item[0])[index], label))

        print("#" * 50)
        input("Next enter tap")
        
        os.system('clear')
        ready += 1

    print("#" * 50)
    print("# Finish")
    print("#" * 50)

    sys.exit(0)

##
# INIT
#
if __name__ == "__main__":
    os.system('clear')

    signal.signal(signal.SIGINT, interrupt)

    read()

    forever = threading.Event()
    forever.wait()