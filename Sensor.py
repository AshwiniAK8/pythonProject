import serial
import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
ser = serial.Serial('COM4',9600)
while(1):
    print("RUN")
    a = str(ser.readline())
    b = str(ser.readline())
    bl = str(ser.readline())
    b1 = bl.split()
    BPM1 = b1[-1].split()[0].split('\\')[0]
    if BPM1 == "*****":
        return
    BPM = int(BPM1)
    df = pd.read_csv("HR.csv")
    X = df.iloc[0:, 0].to_numpy()
    print(BPM)
    # X_last = X[-1]
    X[-1] = BPM
    iso = IsolationForest(contamination=0.1)
    prf = iso.fit_predict(X.reshape(-1, 1))
    if prf[-1] == -1:
        bl1 = b.split()
        a1 = a.split()
        lat1 = bl1[-1]
        long1 = a1[-1]
        gps = 'https://www.google.com/maps/search/?api=1&query=' + lat1[:-5] + ',' + long1[:-5]
        print("ALERT!")
