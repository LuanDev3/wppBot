#!/usr/bin/env/python

import pandas as pd
import os

class Schedule:
    
    #* Actual path of files
    dir_path = os.getcwd()
    pacients = os.path.join(dir_path, "files/pacients.csv")

    def __init__(self):
        self.pacients_csv = pd.read_csv(self.pacients)
        print(self.pacients_csv)

cal = Schedule()

