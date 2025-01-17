import face_recognition as face
import re
import os

os.chdir(os.path.dirname(__file__))

def recognize_face_from_file():
    '''Compares the camera output to the reference images in this directory'''
    results = []
    for file in os.listdir("."):
        # print(file)
        if re.match(r"ref[0-9]+\.png", file):
            # Load the reference image properly
            ref_image = face.load_image_file(file)
            ref = face.face_encodings(ref_image)
            
            # Ensure at least one face encoding is detected
            if not ref:
                print(f"No face found in {file}")
                continue
            
            print("got here")

            # Load the temporary camera image properly
            cam_image = face.load_image_file("tempcam.png")
            camf = face.face_encodings(cam_image)

            # Ensure at least one face encoding is detected
            if not camf:
                print("No face found in tempcam.png")
                continue
            
            # Compare faces
            result = face.compare_faces(ref, camf[0])
            if result:
                results.append(file)

    os.remove("tempcam.png")
    return results
