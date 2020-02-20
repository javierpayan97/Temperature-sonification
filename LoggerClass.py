import csv
from prettytable import PrettyTable
import time
from datetime import datetime
from datetime import timedelta
class DataLogger:
    def __init__(obj,path,tSeconds):
        obj.dataName = []
        obj.tSeconds = tSeconds
        obj.path = path
        obj.samples = []
        obj.newdict = {}
        obj.DictNames = []
        
    def log(obj, dict1):
        samples = obj.samples
        samples.append(dict1)
        obj.newdict = dict1
        time.sleep(obj.tSeconds)
        
    def save(obj):
        # Open your file (create it)
        # loop in all the elements of samples
        table = PrettyTable()
        Num = 0
        n = 0
        counter = 0
        filepath = obj.path
        for key in obj.newdict.keys():
            obj.DictNames.append(key)
        for sample in obj.samples:
            for num in range (0,len(obj.DictNames)):      
                time1 = sample[obj.DictNames[num]]
                for key in sample.keys():
                    if counter ==0:
                        obj.dataName.append(key)
                counter = counter+1
        with open(filepath,'w',newline='') as f:
            file = csv.writer(f)
            Seconds = obj.tSeconds
            Name = obj.dataName #Array of the names of the data
            Num_Name = len(Name)
            Default_Array =['Index']
            for roww in range(0,Num_Name):
                Default_Array.append(Name[roww])
            file.writerow(Default_Array)
            table.field_names = Default_Array
            N = len(obj.DictNames)
            C = 0
            for sample in obj.samples:
                Default_Array2 = [Num]
                for i in range(0,N):
                    if C <= N-1:
                        time1 = sample[obj.DictNames[C]]
                        Default_Array2.append(time1)
                    C = C + 1
                if C > N-1:
                    C = 0
                    file.writerow(Default_Array2)
                    table.add_row(Default_Array2)
                    Num = Num + 1
                
            print(table)

