import serial
arquivo = "logger.csv"


arduino = serial.Serial('COM7', 9600)
arduino.flushInput()
print("Abrindo Serial")

amostra = 10
linha =0
while linha < amostra:

    data = str(arduino.readline().decode("utf-8"))
    print(data)
    file = open(arquivo, "a")
    print("Criando arquivo csv")
    file.write(data)
    linha = linha +1
print("Final de Leituras")
file.close()
arduino.close()