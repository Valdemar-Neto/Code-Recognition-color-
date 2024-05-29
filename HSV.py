# Calculadora de Indices de cores hsv
# Irá medir as tonalidade das coresm
# A quantidade de cor em cada pixel
# O brilho

# Para a nossa aplicação irei utilizar a bilioteca opencv para python e a biblioteca numpy para a manipulação de array

#importando o open cv e numpy
import cv2
import numpy as np

# Irá simplesmente parar o código e quando chamada não irá fazer nada
def nothing(x):
    pass

# Trackbar: Limitand0 cada cor de acordo com a vontade do programador

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.createTrackbar("H", "frame", 0, 180, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", 'frame', 0, 255, nothing)

# Return a new array of given shape and types, filled with 0
img_hsv = np.zeros((250, 500, 3), np.uint8)

# Criar um laço para a obtençãio das cores em hsv
while True:
    # Cria uma linha com uma bolinha que podemos alterar os valores
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    #Pega os valores de ponta a ponta  da imagem em hsv
    img_hsv[:] = (h,s,v)
    #converte a imagem brg em hsv
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    #cria uma janela da camera onde vai passar as informações
    cv2.imshow("frame", img_bgr)
    key = cv2.waitKey(1)
    if key == 23:
        break

cv2.destroyAllWindows()
