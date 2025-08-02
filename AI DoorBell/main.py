import cv2
import face_recognition
import playsound
import threading

cap = cv2.VideoCapture(0)
sound_played = False

def ring_bell():
    playsound.playsound('doorbell.mp3')

while True:
    ret , frame = cap.read()
    faces = face_recognition.face_locations(frame)
    if faces and not sound_played:
        threading.Thread(target=ring_bell).start()
        sound_played = True
    elif not faces and sound_played:
        sound_played = False
    cv2.imshow('Smart Doorbell', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
