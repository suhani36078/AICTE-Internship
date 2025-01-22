import cv2
import mediapipe as mp
mp_pose=mp.solutions.pose
mp_drawing=mp.solutions.drawing_utils

vedio_source=0
#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("dance.mp4")

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

with mp_pose.Pose(static_image_mode=False,model_complexity=0,enable_segmentation=False,min_detection_confidence=0.5,min_tracking_confidence=0.5)as pose:
    while cap.isOpened():
        ret,frame=cap.read()
        if not ret:
            print("Video Capture ended.")
            break

        frame=cv2.flip(frame,1)

        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        results=pose.process(frame_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0),thickness=2,circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,0,255),thickness=2,circle_radius=2)
                )
                
        display_frame=cv2.resize(frame,(960,540))# Adjust width and height as per your screen size 

        cv2.imshow('webcam',frame)
        if cv2.waitkey(0) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
            
                
