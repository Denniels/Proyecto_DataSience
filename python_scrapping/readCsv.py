import pandas as pd
import numpy as np
import csv

def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text

def replace(text):
    try:
        return text.replace(",", "")
    except AttributeError:
        return text
    
def readCsv(fileRoute, separator):        
    return pd.read_csv(fileRoute, sep=separator, converters={'State': strip}, skiprows=0)