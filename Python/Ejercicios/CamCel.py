import cv2
#Link de la camara de la app IP Webcam
cap = cv2.VideoCapture("http://192.168.3.2:8080/video")

while(True):
    _, frame = cap.read()
    try:
        cv2.imshow('videoc', frame)
                   # cv2.resize(frame,(600,400)))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except cv2.error:
        print("end")
        break

cap.release()
cv2.destroyAllWindows()