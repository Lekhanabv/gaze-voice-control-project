import cv2
import mediapipe as mp
import pyautogui

class GazeController:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        self.screen_w, self.screen_h = pyautogui.size()

    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if results.multi_face_landmarks:
            mesh_points = results.multi_face_landmarks[0].landmark
            # Right eye landmark (index 474 is usually on the iris)
            eye = mesh_points[474]
            x = int(eye.x * self.screen_w)
            y = int(eye.y * self.screen_h)
            pyautogui.moveTo(x, y, duration=0.1)

        return frame

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break

            frame = self.process_frame(frame)
            cv2.imshow("Eye Gaze Tracker", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.capture.release()
        cv2.destroyAllWindows()
