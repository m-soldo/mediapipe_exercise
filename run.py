# Copyright 2019 The MediaPipe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
