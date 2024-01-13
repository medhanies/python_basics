import time
import os
import pandas as pd

#while True:
    #if os.path.exists("vegetables.txt"):

      #  with open("vegetables.txt") as file:
           # print(file.read())
    #else:
     #   print("File does not exist.")
    #time.sleep(10)

while True:
    if os.path.exists("temps_today.csv"):
        data = pd.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)