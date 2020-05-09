import cv2
import sys
import time

#cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
        time.sleep(1)  
    return 0
        

        
def net(x,y,w,h):
    timer=3
    check=1
    video_capt = cv2.VideoCapture(0)
    while True:
        
       # Capture frame-by-frame
        ret, frame = video_capt.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(20, 20),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        counters=0
        for (x1, y1, w1, h1) in faces:
            ++counters
            val=cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            ++counters
            if(counters ==4):
                print("Perfect")
                return 1
            if(val is  not None):
                time.sleep(3)
            else:
                counters=0
                      
        cv2.imshow('Video', frame)
        sleep(4)
        video_capt.release()
        cv2.destroyAllWindows()
        
        
def main():
    video_capture = cv2.VideoCapture(0)
    counter=0
    while True:
        
        # Capture frame-by-frame
        ret, frame = video_capture.read()

      #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(20, 20),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        counter =counter+1
        c=0
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            if(counter<40):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                counter=counter+1
                print (counter)
            else:
                
                for (x1, y1, w1, h1) in faces:
                    ++c
                    print ("counter1",c)
                    val=cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                    print ("hello")
                    ++c
                    print ("counter2",c)
                    if(c ==2):
                        print("Perfect")
                        return 1
                    if(val is  not None):
                        time.sleep(3)
                        exit(1)
                    else:
                        c=0
                        print ("counter3",c)
        # Display the resulting frame
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
if __name__=="__main__":
    main()
