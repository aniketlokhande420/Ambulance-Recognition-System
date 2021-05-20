import cv2


cap = cv2.VideoCapture(r'E:/project/test1.mp4')
# capture frames from a video
#cap = cv2.VideoCapture(0)

# Trained XML classifiers describes some features of some object we want to detect
amb_cascade = cv2.CascadeClassifier(r'E:/project/cascade.xml')

# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    amb = amb_cascade.detectMultiScale(gray, 1.1, 2)
    for (x, y, w, h) in amb:
        #Create bounding box 
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 1)
        print("Ambulance detected")
    cv2.imshow('window', frames )
    #Hit Esc to close the window
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
