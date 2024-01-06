import os
import cv2


def capture_face_detection():
    script_path = os.path.abspath(__file__)  # Get the absolute path of the script
    fr_path = os.path.join(script_path, "captured")

    # Create the 'captured' directory if it doesn't exist
    if not os.path.exists(fr_path):
        os.makedirs(fr_path)

    def detect_bounding_box(vid):
        gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.1, 15, minSize=(150, 150))
        return len(faces) > 0  # return True if a face was detected, False otherwise

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    video_capture = cv2.VideoCapture(0)
    frame_count = 0
    max_frames = 3

    while frame_count < max_frames:
        result, video_frame = video_capture.read()
        if not result:
            break

        if detect_bounding_box(video_frame):  # if a face was detected
            file_path = os.path.join(fr_path, f'00{frame_count}.jpg')
            cv2.imwrite(file_path, video_frame)  # save the frame as a jpg image
            frame_count += 1  # increment frame count

        cv2.imshow("Face Detection", video_frame)  # display the processed frame

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def capture_face_storing(foldername):
    script_path = os.path.abspath(__file__)  # Get the absolute path of the script
    fr_path = os.path.join(script_path, "datasets")
    folder_path = os.path.join(fr_path, foldername)

    # Create the 'captured' directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    def detect_bounding_box(vid):
        gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.1, 15, minSize=(150, 150))
        return len(faces) > 0  # return True if a face was detected, False otherwise

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    video_capture = cv2.VideoCapture(0)
    frame_count = 0
    max_frames = 3

    while frame_count < max_frames:
        result, video_frame = video_capture.read()
        if not result:
            break

        if detect_bounding_box(video_frame):  # if a face was detected
            file_path = os.path.join(folder_path, f'00{frame_count}.jpg')
            cv2.imwrite(file_path, video_frame)  # save the frame as a jpg image
            frame_count += 1  # increment frame count

        cv2.imshow("Face Detection", video_frame)  # display the processed frame

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()