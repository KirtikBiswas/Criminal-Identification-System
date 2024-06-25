import cv2
from facerec import detect_faces

def registerCriminal(img, path, img_num):
    size = 2
    (im_width, im_height) = (112, 92)
    file_num = 2 * (img_num - 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    if len(faces) > 0:
        faces = sorted(faces, key=lambda x: x[3], reverse=True)  # sort based on height of image
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (im_width, im_height))

        print(f"Saving training sample {img_num}.1")
        cv2.imwrite(f'{path}/{file_num}.png', face)
        file_num += 1

        print(f"Saving training sample {img_num}.2")
        face = cv2.flip(face, 1)
        cv2.imwrite(f'{path}/{file_num}.png', face)
    else:
        print(f"img {img_num} : Face is not present")
        return img_num

    return None
