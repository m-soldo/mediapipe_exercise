import mediapipe as mp
import numpy as np
import cv2 as cv
import exercises as ex

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def mp_stream(cap, exercise, counter, phase) -> None:
    """Starts video stream with mediapipe pose solution.
    
       `cap`: ocv video capture object (video path, 0 for web cam)
       `exercise`: name of the desired exercise, will call according exercise function based on given name 
       `counter`, `phase`: produced automaticaly in the main script, exercise counter and phase  
    """
    with mp_pose.Pose(smooth_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # False znaci read only (array je nepromjenjiv u memoriji)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

            landmarks = results.pose_landmarks.landmark

            # ovdje se poziva funkcija za vjezbu
            func = getattr(ex, exercise)
            counter, phase  = func(image, landmarks, counter, phase)

            cv.imshow(exercise.capitalize(), image)
            if cv.waitKey(1) & 0xFF == 27:
                break
