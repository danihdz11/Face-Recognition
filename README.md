# Face Recognition Attendance System

This project uses facial recognition technology to register employee attendance using a webcam. The system compares the captured face with a database of employee images and logs the entry time of recognized employees.

## Libraries Required

To ensure the project works properly, you need to install the following libraries:

1. **dlib**
2. **cmake**
3. **face_recognition**
4. **cv2**
5. **numpy**
6. **os**
7. **datetime**

## Code Structure

1. **Image Capture**: The system loads employee images from the `Employees` folder, converts them to RGB format, and encodes them for facial recognition.

2. **Entry Registration**: Every time the system detects a registered face, it logs the employee's entry with the current time and saves it in a `register.csv` file.

3. **Real-time Facial Recognition**: When the script is executed, it opens the webcam, captures an image, and compares it with the registered images. If a matching face is detected, the employee’s name is displayed, and their entry is logged.

## Notes

- If the system does not find a match in the detected faces, it will display a message indicating that no employee was matched.
- The `register.csv` file is automatically created if it doesn't exist, and stores records in the format: `employee_name, entry_time`.
