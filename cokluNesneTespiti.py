import cv2

trackers = cv2.MultiTracker_create()

cap = cv2.VideoCapture(0)

fps = 30#kamera yada videonun fps değeri
f = 0
while True:
    ret, frame = cap.read()
    # Yüksekliği ve Genişiği alma
    (H, W) = frame.shape[:2]
    frame = cv2.resize(frame, dsize = (960, 540))
    
    (success , boxes) = trackers.update(frame)# trackers her adımda update edilecek
  
 
    
    for box in boxes:#box takip sonucuna denk gelir
        (x, y, w, h) = [int(v) for v in box]#boxes değerleri int dönüştürdük
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("t"):
        #takip edeceğimiz bölge 
        box = cv2.selectROI("Frame", frame, fromCenter=False)
    
        tracker =cv2.TrackerMIL_create()
        trackers.add(tracker, frame, box)
    elif key == ord("q"):break

    f = f + 1
    
cap.release()
cv2.destroyAllWindows() 

