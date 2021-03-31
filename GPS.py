import serial
ser = serial.Serial('COM4',9600)
#b = 'b Latitude in Decimal Degrees : 13.025846\r\n'
#a= 'b Longitude in Decimal Degrees : 43.245\r\n'
b=str(ser.readline())
a=str(ser.readline())
print(b)
print(a)
b1 = b.split()
a1 = a.split()
lat1 = b1[-1]
long1 = a1[-1]
print('https://www.google.com/maps/search/?api=1&query='+lat1[:-5]+','+long1[:-5])