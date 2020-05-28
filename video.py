import os
from cv2 import cv2
from settings import SKIPFRAME, THRESHOLD
from files import check_dir, check_file


def extract_images(file_name, extention):
    print("Start stracting image from {}".format(file_name + extention))
    if not check_file('videos/{}'.format(file_name + extention)):
        return False
    cap = cv2.VideoCapture('videos/{}'.format(file_name + extention))
    check_dir('images/{}'.format(file_name))
    ret, actual_frame = cap.read()
    last_saved = actual_frame
    i = 0
    image_number = 0
    while(cap.isOpened()):
        if ret == False:
            break
        diff1 = cv2.matchTemplate(
            last_saved, actual_frame, cv2.TM_CCOEFF_NORMED)[0][0]
        if not i or diff1 < THRESHOLD:
            cv2.imwrite(
                'images/{}/image{:03d}.jpg'.format(file_name, image_number), actual_frame)
            image_number += 1
            last_saved = actual_frame
        cap.set(1, SKIPFRAME*i)
        ret, actual_frame = cap.read()
        i += 1

    cap.release()
    cv2.destroyAllWindows()
    print("Saved {} images in images/{}".format(image_number, file_name))
    return image_number != 0
