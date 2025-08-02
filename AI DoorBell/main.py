import cv2
import face_recognition
import playsound
import threading

# Initialize camera
cap = cv2.VideoCapture(0)
sound_played = False

# Function to play the doorbell sound
def ring_bell():
    playsound.playsound('doorbell.mp3')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame from BGR to RGB (face_recognition expects RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    faces = face_recognition.face_locations(rgb_frame)

    if faces and not sound_played:
        # Start sound in background
        threading.Thread(target=ring_bell, daemon=True).start()
        sound_played = True
    elif not faces and sound_played:
        # Reset sound trigger
        sound_played = False

    # Show the frame
    cv2.imshow('Smart Doorbell', frame)

    # Exit on 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
