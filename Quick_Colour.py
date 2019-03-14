import cv2
import numpy as np

# capturing video through webcam

cap = cv2.VideoCapture(1)

while(1):
    _, img = cap.read()

    # converting frame(img == BGR) to HSV(hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # red color

    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)

    # blue color

    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)

    # yellow color

    yellow_lower = np.array([22,60,200],np.uint8)
    yellow_upper = np.array([60,255,255],np.uint8)

    # white color

    white_lower = np.array([0,0,200],np.uint8)
    white_upper = np.array([180,20,255],np.uint8)

    # black color

    black_lower = np.array([0,0,0],np.uint8)
    black_upper = np.array([180,255,30],np.uint8)

	
    # Beaver brown color
    Beaver_lower = np.array([154, 124, 105],np.uint8)
    Beaver_upper = np.array([164, 143, 117],np.uint8)
    # Beige brown color
    Beige_lower = np.array([230, 200, 200],np.uint8)
    Beige_upper = np.array([255, 250, 240],np.uint8)
    # Buff brown color
    Buff_lower = np.array([235, 215, 125],np.uint8)
    Buff_upper = np.array([245, 225, 135],np.uint8)
    # Burnt brown color
    Burnt_lower = np.array([133, 46, 31],np.uint8)
    Burnt_upper = np.array([143, 56, 41],np.uint8)
    # Chestnut brown color
    Chestnut_lower = np.array([144, 64, 48],np.uint8)
    Chestnut_upper = np.array([154, 74, 58],np.uint8)
    # Chocolate brown color
    Chocolate_lower = np.array([118, 58, 0],np.uint8)
    Chocolate_upper = np.array([128, 68, 5],np.uint8)
    # Cocoa brown color
    Cocoa_lower = np.array([205, 100, 25],np.uint8)
    Cocoa_upper = np.array([215, 115, 35],np.uint8)
	
    # all color together

    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    white = cv2.inRange(hsv, white_lower, white_upper)
    black = cv2.inRange(hsv, black_lower, black_upper)
    Beaver = cv2.inRange(hsv, black_lower, black_upper)
    Beige = cv2.inRange(hsv, black_lower, black_upper)
    Buff = cv2.inRange(hsv, black_lower, black_upper)
    Burnt = cv2.inRange(hsv, black_lower, black_upper)
    Chestnut = cv2.inRange(hsv, black_lower, black_upper)
    Chocolate = cv2.inRange(hsv, black_lower, black_upper)
    Cocoa = cv2.inRange(hsv, black_lower, black_upper)

	
    # Morphological Transform, Dilation

    kernal = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernal)
    res_red = cv2.bitwise_and(img, img, mask = red)

    blue = cv2.dilate(blue, kernal)
    res_blue = cv2.bitwise_and(img, img, mask = blue)

    yellow = cv2.dilate(yellow, kernal)
    res_yellow = cv2.bitwise_and(img, img, mask = yellow)

    white = cv2.dilate(white, kernal)
    res_white = cv2.bitwise_and(img, img, mask = white)

    black = cv2.dilate(black, kernal)
    res_black = cv2.bitwise_and(img, img, mask = black)
	
    Beaver = cv2.dilate(Beaver, kernal)
    res_Beaver = cv2.bitwise_and(img, img, mask = Beaver)
    Beige = cv2.dilate(Beige, kernal)
    res_Beige = cv2.bitwise_and(img, img, mask = Beige)
    Buff = cv2.dilate(Buff, kernal)
    res_Buff = cv2.bitwise_and(img, img, mask = Buff)
    Burnt = cv2.dilate(Burnt, kernal)
    res_Burnt = cv2.bitwise_and(img, img, mask = Burnt)
    Chestnut = cv2.dilate(Chestnut, kernal)
    res_Chestnut = cv2.bitwise_and(img, img, mask = Chestnut)
    Chocolate = cv2.dilate(Chocolate, kernal)
    res_Chocolate = cv2.bitwise_and(img, img, mask = Chocolate)
    Cocoa = cv2.dilate(Cocoa, kernal)
    res_Cocoa = cv2.bitwise_and(img, img, mask = Cocoa)

    # Tracking red
    (_, contours, hierarchy)=cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))    

    # Tracking blue
    (_, contours, hierarchy)=cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
            

    # Tracking yellow
    (_, contours, hierarchy)=cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Yellow Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    ##Tracking white
    # (_, contours, hierarchy)=cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for pic, contour in enumerate(contours):
        # area = cv2.contourArea(contour)
        # if(area > 300):
            # x, y, w, h = cv2.boundingRect(contour)
            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            # cv2.putText(img, "White Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))

    ##Tracking black
    # (_, contours, hierarchy)=cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for pic, contour in enumerate(contours):
        # area = cv2.contourArea(contour)
        # if(area > 300):
            # x, y, w, h = cv2.boundingRect(contour)
            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            # cv2.putText(img, "Black Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    # Tracking Cocoa
    (_, contours, hierarchy)=cv2.findContours(Cocoa, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Cocoa Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    # Tracking Chocolate
    (_, contours, hierarchy)=cv2.findContours(Chocolate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Chocolate Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    # Tracking Chestnut
    (_, contours, hierarchy)=cv2.findContours(Chestnut, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Chestnut Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    # Tracking Burnt
    (_, contours, hierarchy)=cv2.findContours(Burnt, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Burnt Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))

    # Tracking Buff
    (_, contours, hierarchy)=cv2.findContours(Buff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Buff Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))

    # Tracking Beige
    (_, contours, hierarchy)=cv2.findContours(Beige, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Beige Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    # Tracking Beaver
    (_, contours, hierarchy)=cv2.findContours(Beaver, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 200):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 100), 2)
            cv2.putText(img, "Beaver Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 100))		
    
    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
