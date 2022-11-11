import serial
porta = "COM7"
baud = 9600
arquivo = "valores.py"

ardruino = serial.Serial(porta,baud)
ardruino.flushInput()
print("Abrindo Serial")

values = []
amostra = 10
linha = 0
while linha <= amostra:
    
    data = str(ardruino.readline().decode("utf-8"))
    values.append(data[:-2])
    linha += 1
print("Final de leituras")
file = open(arquivo,'a')
file.write("Valores="+str(values))
print(values)
file.close()
ardruino.close()