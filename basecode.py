
import cv2
import threading

def stream(add, windowName1):
    cv2.namedWindow(windowName1)
    capture1 = cv2.VideoCapture(add)  # laptop's camera
    if capture1.isOpened():  # check if feed exists or not for camera 1
        ret1, frame1 = capture1.read()
    else:
        ret1 = False

    while ret1:  # and ret2 and ret3:
        ret1, frame1 = capture1.read()
        cv2.imshow(windowName1, frame1)

        if cv2.waitKey(1) == 27:
            break

    capture1.release()
    cv2.destroyAllWindows()
    return 

def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Webcam"
        windowName2 = "Phone"
        windowName3 = "Phone2"
        cv2.namedWindow(windowName)
        cv2.namedWindow(windowName2)
        cv2.namedWindow(windowName3)

        capture1 = cv2.VideoCapture(0)  # 0 for laptop's camera, any other argument if there is an external camera
        capture2 = cv2.VideoCapture("http://10.130.14.110:8080/video")   # sample code for mobile camera video capture using IP camera
        capture3 = cv2.VideoCapture("stuff")

        # define size for recorded video frame for video 1
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        width2 = int(capture2.get(3))
        height2 = int(capture2.get(4))
        size2 = (width2, height2)

        width3 = int(capture2.get(3))
        height3 = int(capture2.get(4))
        size3 = (width3, height3)

        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'WebcamRecording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, size1) # 30 is the framerate here

        optputFile2 = cv2.VideoWriter(
            'PhoneRecording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, size2)

        optputFile3 = cv2.VideoWriter(
            'PhoneRecording2.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, size3)


        # check if feed exists or not for camera 1
        if capture1.isOpened():
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        if capture2.isOpened():
            ret2, frame2 = capture2.read()
        else:
            ret2 = False

        if capture3.isOpened():
            ret3, frame3 = capture3.read()
        else:
            ret3 = False


        while ret1 and ret2 and ret3:
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()
            # sample feed display from camera 1
            cv2.imshow(windowName, frame1)
            cv2.imshow(windowName2, frame2)
            cv2.imshow(windowName3, frame3)
            # saves the frame from camera 1
            optputFile1.write(frame1)
            optputFile2.write(frame2)
            optputFile3.write(frame3)

            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        capture2.release()
        capture3.release()
        optputFile1.release()
        optputFile2.release()
        optputFile3.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream
        windowName1 = "webcam"
        windowName2 = "phone"
        
        # cv2.namedWindow(windowName2)

        add1 = 0
        add2 = "http://10.130.14.110:8080/video"
        # # capture1 = cv2.VideoCapture(0)  # laptop's camera
        # capture2 = cv2.VideoCapture("http://10.130.14.110:8080/video") # phone camera
        # # t1 = threading.Thread(target=stream, args=(add1, windowName1,))
        # t2 = threading.Thread(target=stream, args=(add2, windowName2,))
        
        # # t1.start()
        # t2.start()

        cv2.namedWindow(windowName1)
        cv2.namedWindow(windowName2)
        capture1 = cv2.VideoCapture(add1)  # laptop's camera
        capture2 = cv2.VideoCapture(add2) # phone camera
        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        if capture2.isOpened():  # check if feed exists or not for camera 1
            ret2, frame2 = capture2.read()
        else:
            ret2 = False

        while ret1 and ret2:  # and ret2 and ret3:
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            cv2.imshow(windowName1, frame1)
            cv2.imshow(windowName2, frame2)
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        cv2.destroyAllWindows()
        return 

    else:
        print("Invalid option entered. Exiting...")

main()
