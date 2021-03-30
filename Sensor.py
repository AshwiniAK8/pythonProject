import serial
import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
ser = serial.Serial('COM4',9600)
while(1):
    bl = str(ser.readline())
    a = str(ser.readline())
    b = str(ser.readline())
    b1 = b.split()
    BPM = [b1[-1]]
    with open('HR.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(BPM)
    df = pd.read_csv("HR.csv")
    X = df.iloc[0:, 0].to_numpy()
    iso = IsolationForest(contamination=0.1)
    prf = iso.fit_predict(X.reshape(-1, 1))
    if prf[-1]==-1:
        bl1 = bl.split()
        a1 = a.split()
        lat1 = bl1[-1]
        long1 = a1[-1]
        gps = 'https://www.google.com/maps/search/?api=1&query=' + lat1[:-5] + ',' + long1[:-5]
        print("ALERT!")
    df.drop(df.tail(1).index,
            inplace=True)
    df.to_csv('HR.csv')