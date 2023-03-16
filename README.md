# MediaPipe_Exercise
Tracking range of motion and number of repetitions for pullups, pushups and squats.

The human body is detected using mediapipe solutions from the mediapipe library. With appliance of mathematical methods, the algorithm is able to track how many repetitions of a given exercise were made and whether they were made with full range of motion (the algorithm won't count them otherwise).

Exercises covered so far are pullups, pushups and squats.

## How to use:

  1.) Create Python venv from reyuirments.txt
  
  2.) In the run.py file, as an argument for the VideoCapture method, in 'cap' variable, give a path for the video you want to process, or use 0 for webcam (if you           have multiple cameras connected to your hardware, it may be a different int). Then run run.py.

## Exercises:

### Pullup

   ![count_pullup](https://user-images.githubusercontent.com/100207531/224478501-c78f3cf1-1206-4841-b5ce-1ae0800b5aca.gif)

The algorithm is primarily focused on shoulder, elbow and wrist points from mediapipe pose solution. It uses those points to calculate the angle between the forearm and upper arm, then compares them to hardcoded thresholds to determine phase -> should one go up or down. After one full range of motion has been completed, the counter will be enlarged by one. Both phase and count are outputed on the video stream. 


### Pushup

![count_pushup](https://user-images.githubusercontent.com/100207531/224478557-75819f06-c90d-4c79-9ae9-722e8067e136.gif)

In the case of pushup, same points as with a pullup are deemed relevant (shoulder, elbow, wrist); only thresholds and starting values for phase and counter are set differently in the pushup function. Algoritham again checks for a relevant angle and compares it to hardcoded thresholds determining the phase and incrementing the counter after one full pushup has been made. Both phase and count are outputed on the video stream.


### Squat

![count_squat](https://user-images.githubusercontent.com/100207531/224478565-57b014ba-15da-4e13-aee0-76ed47a77a0c.gif)

For squat exercise, the algorithm will primarly focus on hip, knee and ankle points from mediapipe pose solution, generally following the same set of principles of checking relevant angles and based on them, determining the phase of the exercise (up/down) and incrementing the counter accordingly. Both phase and count are outputed on the video stream. 
