import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# create database

path = 'Employees'
my_images = []
employee_names = []
employee_list = os.listdir(path)

for name in employee_list:
    current_image = cv2.imread(f'{path}/{name}')
    my_images.append(current_image)
    employee_names.append(os.path.splitext(name)[0])
print(employee_names)

# encode images
def encode(images):

    # create new list
    encoded_list = []

    # convert all images to RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # encode
        encoded = fr.face_encodings(image)[0]

        # add to list
        encoded_list.append(encoded)

    # return encoded list
    return encoded_list


# register entries
def register_entries(person):
    f = open('register.csv', 'r+')
    data_list = f.readline()
    registered_names = []
    for line in data_list:
        entry = line.split(',')
        registered_names.append(entry[0])

    if person not in registered_names:
        now = datetime.now()
        time_string = now.strftime('%H:%M:%S')
        f.writelines(f'\n{person}, {time_string}')


encoded_employee_list = encode(my_images)

# take an image from webcam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# read image from camera
success, image = capture.read()

if not success:
    print('Failed to capture image')
else:
    # recognize face in capture
    capture_face = fr.face_locations(image)

    # encode captured face
    capture_face_encoded = fr.face_encodings(image, capture_face)

    # look for matches
    for encoded_face, face_location in zip(capture_face_encoded, capture_face):
        matches = fr.compare_faces(encoded_employee_list, encoded_face)
        distances = fr.face_distance(encoded_employee_list, encoded_face)

        print(distances)

        match_index = numpy.argmin(distances)

        # show matches if any
        if distances[match_index] > 0.6:
            print('Does not match any of our employees')
        else:

            # find the name of the matched employee
            name = employee_names[match_index]

            y1, x2, y2, x1 = face_location
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            register_entries(name)

            # display the captured image
            cv2.imshow('Webcam Image', image)

            # keep window open
            cv2.waitKey(0)
