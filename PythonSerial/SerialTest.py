import serial

ser = serial.Serial(port = 'COM6',baudrate = '9600')

data = [0,0,0,0,0]

while(1):
    A = ser.read(1)
    A = int.from_bytes(A,byteorder='little',signed=True)
    if (A == 83):
        A = ser.read(3)
        for x in range(0,5):
            A = ser.read(4)
            A = int.from_bytes(A,byteorder='little',signed=True)
            data[x] = A
        with open('data.txt','a') as file:
                file.write(str(data[0])+','+str(data[1])+','+str(data[2])+','+str(data[3])+','+str(data[4])+'\n')    
        print(data)

ser.close()

