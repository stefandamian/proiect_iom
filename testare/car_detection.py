# car detection

import cv2


def main():
    haarcascade_car = cv2.CascadeClassifier('haarcascade/haarcascade_car.xml')
    video = cv2.VideoCapture('video.mp4')

    if video.isOpened() == False:
        print("Error opening video")
    else:
        while video.isOpened():
            ret, frame = video.read()

            if ret:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                detected_cars = haarcascade_car.detectMultiScale(gray_frame, 1.2, 5)

                for (x, y, width, height) in detected_cars:
                    print(x, y, width, height)
                    cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 255), 2)
                    cv2.imshow('Cars detection', frame)

                # for exit press 'q' on keyboard
                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break
            else:
                break


    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
   main()
