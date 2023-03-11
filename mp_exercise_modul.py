import mediapipe as mp
import numpy as np
import cv2 as cv
import mp_exercise_modul as mem

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def calc_angle(a: list, b: list, c: list) -> float:
    """Takes given points (arrays) from mediapipe pose solution
       and returns a relevant angle"""
    
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle


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
            func = getattr(mem, exercise)
            counter, phase  = func(image, landmarks, counter, phase)

            cv.imshow(exercise.capitalize(), image)
            if cv.waitKey(1) & 0xFF == 27:
                break


def pullup(image, landmarks, counter, phase) -> tuple[float, str]:
    """This function, if specified is called automaticaly by mp_stream function.\n 
    It tracks and returns count and phase for given exercise and also outputs \n
    those values as well as the relevant angle for given exercise onto video stream"""

    try:
        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        angle = calc_angle(shoulder, elbow, wrist)
        angle = round(angle, 2)
        
        if angle > 167:
            phase = 'UP'
        if angle < 70 and phase == 'UP':
            phase = 'DOWN'
            counter += 1    
        
        cv.putText(image, phase, (150, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (100,255,100), 3)
        cv.putText(image, str(counter), (50, 300), 0, 2, (248,183,7), 3)
        return counter, phase 
    except:
        pass    


def pushup(image, landmarks, counter, phase) -> tuple[float, str]:
    """This function, if specified is called automaticaly by mp_stream function.\n 
    It tracks and returns count and phase for given exercise and also outputs \n
    those values as well as the relevant angle for given exercise onto video stream"""
    
    try:
        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        angle = calc_angle(shoulder, elbow, wrist)
        angle = round(angle, 2)
        
        if angle > 167 and phase == 'UP':
            phase = 'DOWN'
            counter += 1    
        if angle < 43:
            phase = 'UP'
        
        cv.putText(image, phase, (300, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (100,255,100), 3)
        cv.putText(image, str(counter), (50, 300), 0, 2, (248,183,7), 3)
        return counter, phase 
    except:
        pass


def squat(image, landmarks, counter, phase) -> tuple[float, str]:
    """This function, if specified is called automaticaly by mp_stream function.\n 
    It tracks and returns count and phase for given exercise and also outputs \n
    those values as well as the relevant angle for given exercise onto video stream"""
    
    try:
        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

        angle = calc_angle(shoulder, elbow, wrist)
        angle = round(angle, 2)
        
        if angle > 167 and phase == 'UP':
            phase = 'DOWN'
            counter += 1    
        if angle < 60:
            phase = 'UP'
        
        cv.putText(image, phase, (150, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (100,255,100), 3)
        cv.putText(image, str(counter), (50, 300), 0, 2, (248,183,7), 3)
        return counter, phase 
    except:
        pass




 # cv.putText(image, str(angle),
        #             tuple(np.multiply(elbow, [width, height]).astype(int)),
        #             cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 1, cv.LINE_AA
        #             )