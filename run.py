import cv2 as cv
import mp_exercise_modul as mem


cap = cv.VideoCapture('1.mp4')
# width, height = cap.get(3), cap.get(4)
exercise = 'pullup'

if exercise == 'pullup':
    counter = 0
    phase = None
elif exercise == 'pushup':
    counter = -1
    phase = "UP"
elif exercise == 'squat':
    counter = 0
    phase = "DOWN"
else:
    raise AttributeError("You have chosen an invalid exercise")    

mem.mp_stream(cap, exercise, counter, phase)

cap.release()
cv.destroyAllWindows()    