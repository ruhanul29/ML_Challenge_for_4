#micro-1

with open("example.txt", "w") as f:
    f.write("Duck Duck Go\n")
    f.write("File Closed.")
    
#micro-2

with open('app.log', "a") as f:
    f.write("New log\n")  
    
#micro-3

with open("a.jpg", "rb") as f:
    image_bytes = f.read()
    
print(type(image_bytes))
print(len(image_bytes))

#micro-4

with open("d.txt", "r",encoding='utf-8') as f:
    text = f.read()        

#micro-5

import json

x = {"name": "Karim","age":5}      

with open("x.json","w",encoding='utf-8') as f:
    json.dump(x,f, indent=4)

#micro-6   

import csv

rows = []

with open ("xyz.csv", 'r',encoding="utf-8",newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

print(rows)

#micro-8

from pathlib import Path

folder = "C:\Users\mdruh\,.,.,.,\New folder (3)"
file = "C:\ML\DS_for4(2)\x.json"

path = Path(folder) / file

print(Path)   

#micro-9

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        end = time.time()
        print(f"Time taken: {end-self.start:.6f} seconds")

with Timer():
    total=0
    for i in range (1000000):
        total += i        
         
#micro-7

with open("abc.txt", "w", encoding="utf-8") as f:
    for i in range (1000000) :
        f.write(f"Line {i}\n")
        
#micro-10

......       