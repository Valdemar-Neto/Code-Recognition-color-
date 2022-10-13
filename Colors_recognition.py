import cv2 # Importing of library opencv by python

cap = cv2.VideoCapture(0) # Initializing the cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400) # Format of frame - width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)# Format of frame - height

while True: # A loop to reading frames cam
    _, frame = cap.read() # To read frames
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting of frame from bgr to hsv
    height, width, _= frame.shape # Setting the format of frame

    cx = int(width/2) # coordinate in x of pixel center
    cy = int(height/2) # coordinate in y of pixel center

    pixel_center = hsv_frame[cy,cx] # Drawing the pixel_center at image center
    hue_value = pixel_center[0] # Receive the value of the first coordinate of the  pixel center

    color = "Undefined" # the variable of color

    ## THIS PART OF CODE IS DIRECTED TO CAPTURE COLOR ACCORDING TO HUE VALUE
    if hue_value < 5: # If the hue valor is less than 5, the color is red
        color = "RED"
    elif hue_value <22: # If the hue valor is less than 22, the color is orange
        color="ORANGE"
    elif hue_value <33: # If the hue valor is less than 33, the color is yellow
        color = "YELLOW"
    elif hue_value < 78: # If the hue valor is less than 78, the color is green
        color = "GREEN"
    elif hue_value < 134: # If the hue valor is less than 134, the color is blue
        color = "BLUE"
    elif hue_value < 145: # If the hue valor is less than 145, the color is purple
        color = "PURPLE"
    elif hue_value < 175: # If the hue valor is less than 175, the color is pink# If the hue valor is less than 5, the color is red
        color = "PINK"
    else: # if none of these values above , the color is red
        color = "RED"

    pixel_center_bgr = frame[cx, cy] # Drawing the pixel_center_bgr
    print(pixel_center_bgr) # Prints the values of the center brg at the terminal
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2]) # receive the of values of eachs coordinate for blue, green and red, respectively
    cv2.rectangle(frame, (cx-70, 85),(cx+90, 50), (255,255,255), -1) #Draw a rectangle on the sreen with 160px of width and 35px of height of white color
    cv2.putText(frame, color, (cx-60, 78),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(b,g,r), 2) # Writes on the screen the name of color being identified
    cv2.circle(frame, (cx, cy), 10, (25,25,25), 3) # Draw a circle of radius 10px

    cv2.imshow("frame", frame) #Show the read frame on the screen
    key = cv2.waitKey(1) #One millisecond refresh rate
    if key == 27: #Press ESC, the code stop
        break
cap.release()
cv2.destroyAllWindows() #Destroys all windows of code