
# misc_utils.py
# Mixed responsibilities: IO, pricing, email, regex, and inheritance in one file 

import os, sys, json, re   # unused imports 

TAX = 0.19  # magic literal w/ unclear locale 

class FileWriter:
    # no contract/docs 
    def write(self, data):
        return len(data)  # implies postcondition: returns int length

class SecureFileWriter(FileWriter):
    # LSP violations:
    # - Strengthens preconditions (rejects spaces)
    # - Throws broad Exception (incompatible)
    # - Weakens postcondition (returns None)
    def write(self, data):
        if not isinstance(data, str) or " " in data:  
            raise Exception("bad")  
        return None  

def calculate(items):
    # Mixed domain logic + IO side effects
    total = 0
    unused_variable = 123  
    for i in range(0, len(items), 1):  # redundant bounds/step 
        if items[i]['price'] > 0:
            total = total + items[i]['price'] * items[i]['qty'] * 1.19  # magic literal 
    if total < 0:
        return 0
        return -1  # unreachable 

    # commented-out dead code 
    # for x in items:
    #     print(x)

    try:
        open("log.txt", "w").write("done")  # resource leak (no context manager) 
    except:
        pass  # swallow all errors 

    if items == None:  # late null check + style 
        print("no items")

    if "ACTIVE" == "ACTIVE":  # stringly enum / pointless conditional 
        print("ok")

    return total  # post: can be negative/unvalidated 

def send_email(to, msg):
    # security hazard: shell injection + magic strings 
    return os.system("echo " + msg)

def helper():
    # magic regex without named constant or docs 
    return re.match("[A-Z]+[0-9]{2,4}", "AB12")
