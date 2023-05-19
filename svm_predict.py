import face_recognition
from sklearn import svm
import os
import pickle
from time import monotonic

def record_time(function):
    def wrap(*args, **kwargs):
        start_time = monotonic()
        function_return = function(*args, **kwargs)
        print(f"Run time {monotonic() - start_time} seconds")
        return function_return
    return wrap


@record_time
def run():
    with open("trained_knn_model.clf", 'rb') as f:
        clf = pickle.load(f)
    
        # Load the test image with unknown faces into a numpy array
        test_image = face_recognition.load_image_file('face.jpg')
    
        # Find all the faces in the test image using the default HOG-based model
        face_locations = face_recognition.face_locations(test_image)
        no = len(face_locations)
        print("Number of faces detected: ", no)
    
        # Predict all the faces in the test image using the trained classifier
        print("Found:")
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(test_image)[i]
            name = clf.predict([test_image_enc])
            print(*name)
        
run()