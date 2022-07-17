import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
pad=None
noiseth=800
x,y = 0,0

while(1):
    # Take each frame
    _, frame = cap.read()

    frame = cv.flip( frame, 1 )
    
    # Initialize the pad as  black image of  same size as the frame
    if pad is None:
        pad = np.zeros_like(frame)

    # Convert BGR to HSV  (Image segmentation)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
            
    lower_range  = np.array([110,50,50])
    upper_range = np.array([130,255,255])
    
    
    mask = cv.inRange(hsv, lower_range, upper_range)
    
    
    # Find Contours Contours can be explained simply as a curve joining all the continuous points (along the boundary),
    # having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.
    
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(mask, contours, 0, (0,255,0), 3)
    
    if contours and cv.contourArea(max(contours, 
                                 key = cv.contourArea)) > noiseth:
                
        c = max(contours, key = cv.contourArea) 
        M= cv.moments(c)           # moments are the average of the intensities of an image's pixels. use to find center of stylus.
        x1 = int(M['m10']/M['m00'])
        y1 = int(M['m01']/M['m00'])

        if x == 0 and y == 0:
            x,y= x1,y1
            
        else:
            # Draw the line on the pad
            pad = cv.line(pad, (x,y),(x1,y1), [255,0,0], 4)
        
        # After the line is drawn the new points become the previous points.
        x,y= x1,y1

    else:
        # If there were no contours detected then make x1,y1 = 0
        x,y =0,0
    

    
    cv.imshow('pad', pad)
    cv.imshow('frame',frame)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
        
    #Clear the board when pressed 'c'
    if k == ord('c'):
        pad = None

cap.release()
cv.destroyAllWindows()


    

