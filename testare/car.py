# -*- coding: utf-8 -*-

import cv2



def main():
    cascade_src = 'cars.xml'

    video_src = 'testare/video.mp4'

    cap = cv2.VideoCapture(video_src)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    car_cascade = cv2.CascadeClassifier(cascade_src)


    while True:
        ret, img = cap.read()
        fgbg.apply(img)
        if (type(img) == type(None)):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cars = car_cascade.detectMultiScale(gray, 1.1, 2)


        for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

        cv2.imshow('video', img)


        if cv2.waitKey(33) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
