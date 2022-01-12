from os import stat
import time
from scripts import status

def error(ID, message):
    print("\n" + str(message) + "\n" + "Code: " + str(ID))
    
    time.sleep(5)

def log(message):
    if (status.mustDebug):
        print("---LOG---\n" + str(message) + "\n---------\n")
        time.sleep(3)


headers = {}

def display_header(header_line):
    if (status.mustDebug):
        header_line = header_line.decode('iso-8859-1')

        if ':' not in header_line:
            return

        h_name, h_value = header_line.split(':', 1)

        h_name = h_name.strip()
        h_value = h_value.strip()
        h_name = h_name.lower()
        headers[h_name] = h_value