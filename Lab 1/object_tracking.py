import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Create upper and lower HSV ranges for color mask
    lower_pink = np.array([170, 110, 110])
    upper_pink = np.array([180, 255, 255])

    # Create a mask using the inRange function
    mask = cv2.inRange(hsv, lower_pink, upper_pink)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Draw bounding box around object with largest contour
    if contours:
        box_color = (0, 255, 0)  # Green color in BGR
        box_thickness = 2
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, box_thickness)

    # Display the resulting frame
    cv2.imshow("Color Tracking", frame)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()