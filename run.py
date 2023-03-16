import cv2 as cv
import videoStream as vs

# give video path as an argument or int for webcam port (most likely 0, possible higher int if you have multiple cams)
cap = cv.VideoCapture('some_folder/some_video.mp4')
# name of the exercise, must be pullup, pushup or squat
exercise = 'pullup'

if exercise.lower() == 'pullup':
    counter = 0
    phase = None
elif exercise.lower() == 'pushup':
    counter = -1
    phase = "UP"
elif exercise.lower() == 'squat':
    counter = 0
    phase = "DOWN"
else:
    raise AttributeError("You have chosen an invalid exercise")    

vs.mp_stream(cap, exercise, counter, phase)

cap.release()
cv.destroyAllWindows()    
