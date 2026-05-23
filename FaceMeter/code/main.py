import cv2
import mediapipe as mp
import numpy as np
from mediapipe.python.solutions.drawing_utils import DrawingSpec

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# Function to calculate the percentage of visible face landmarks
def calculate_face_visibility(landmarks):
    visible = 0
    for lm in landmarks:
        if 0 <= lm.x <= 1 and 0 <= lm.y <= 1:
            visible += 1
    return round((visible / len(landmarks)) * 100, 2)

# Start video capture from the default webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if frame not captured

    # Convert frame to RGB for MediaPipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_h, image_w, _ = frame.shape
    results = face_mesh.process(frame_rgb)

    detected = False

    # If face landmarks are detected
    if results.multi_face_landmarks:
        detected = True
        for face_landmarks in results.multi_face_landmarks:
            # Draw face mesh landmarks on the frame
            mp_drawing.draw_landmarks(
                frame, 
                face_landmarks, 
                mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=DrawingSpec(color=(0, 200, 0), thickness=1, circle_radius=1),
                connection_drawing_spec=DrawingSpec(color=(0, 150, 255), thickness=1)
            )
            landmarks = face_landmarks.landmark
            percent_visible = calculate_face_visibility(landmarks)
            text = f"Face Visible: {percent_visible}%"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.0
            thickness = 3
            # Calculate text size and position
            text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
            text_x, text_y = 30, 60
            # Draw background rectangle for text
            cv2.rectangle(
                frame,
                (text_x - 10, text_y - text_size[1] - 10),
                (text_x + text_size[0] + 10, text_y + 10),
                (30, 30, 30),
                -1
            )
            # Put the face visibility percentage text on the frame
            cv2.putText(
                frame,
                text,
                (text_x, text_y),
                font,
                font_scale,
                (0, 255, 180),
                thickness,
                cv2.LINE_AA
            )
    else:
        # If no face is detected, show "No Face Visible" in light red
        text = "No Face Visible"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.0
        thickness = 3
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
        text_x, text_y = 30, 60
        cv2.rectangle(
            frame,
            (text_x - 10, text_y - text_size[1] - 10),
            (text_x + text_size[0] + 10, text_y + 10),
            (30, 30, 30),
            -1
        )
        cv2.putText(
            frame,
            text,
            (text_x, text_y),
            font,
            font_scale,
            (102, 102, 255),  # light red (BGR)
            thickness,
            cv2.LINE_AA
        )

    # Display the frame with annotations
    cv2.imshow("Face Visibility", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Exit loop on 'q' key press

# Release resources
cap.release()
cv2.destroyAllWindows()