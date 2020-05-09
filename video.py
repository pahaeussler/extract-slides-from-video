import os 
from cv2 import cv2
from settings import SKIPFRAME, THRESHOLD
from files import check_dir, check_file

def extract_images(file_name, extention):
    print("Start stracting image from {}".format(file_name + extention))
    if not check_file('videos/{}'.format(file_name + extention)):
        return False
    cap = cv2.VideoCapture('videos/{}'.format(file_name + extention))
    check_dir('pictures/{}'.format(file_name))
    ret, frame = cap.read()
    lastframe = frame

    i = 0
    image_number = 0
    while(cap.isOpened()):
        if ret == False:
            break
        res = cv2.matchTemplate(lastframe, frame, cv2.TM_CCOEFF_NORMED)
        if not i or res[0][0]<THRESHOLD:
            print('  -> Saved pictures/{}/image{}.jpg'.format(file_name, image_number))
            cv2.imwrite('pictures/{}/image{}.jpg'.format(file_name, image_number),frame)
            image_number += 1
        lastframe = frame
        cap.set(1, SKIPFRAME*i)
        ret, frame = cap.read()
        i += 1
    
    cap.release()
    cv2.destroyAllWindows()
    print("Saved {} images in pictures/{}".format(image_number, file_name))
    return image_number != 0