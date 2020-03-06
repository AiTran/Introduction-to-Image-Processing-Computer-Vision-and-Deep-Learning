import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from HW2_interface import Ui_Widget_HW2
import sys

# Define path dir
FolderImage = "./Image/"
ListImage = [f for f in os.listdir(FolderImage) if f.endswith(".bmp")]
# Define Interface
app = QtWidgets.QApplication(sys.argv)
Opencv_hw2 = QtWidgets.QWidget()
    
class TWSignals(QtCore.QObject):
	switch_window = QtCore.pyqtSignal(object)

class Process_Image(Ui_Widget_HW2):
    signals = TWSignals()
    def __init__(self):
        super(Process_Image,self).__init__()
        self.setupUi(Opencv_hw2)
      
        self.btn_disparity2.clicked.connect(lambda check: self.Disparity())
        self.btn_BS.clicked.connect(lambda check: self.Background_subtraction())
        self.btn_preprocessing.clicked.connect(lambda check: self.Preprocessing())
        self.btn_videotracking.clicked.connect(lambda check: self.videotracking())
        self.btn_AR.clicked.connect(lambda check: self.Augmented_Reality())
    
    def Disparity(self):
        imgL = cv2.imread( FolderImage + 'imL.png',0)
        imgR = cv2.imread( FolderImage + 'imR.png',0)

        window_size = 9
        left_matcher = cv2.StereoSGBM_create(
                minDisparity=0,
                numDisparities=64,            
                blockSize=9,
                P1=130,    
                P2=1900,
                disp12MaxDiff=1,
                uniquenessRatio=5,
                speckleWindowSize=200,
                speckleRange=3,
                # preFilterCap=30,
                mode=cv2.StereoSGBM_MODE_SGBM
            )
        disparity = left_matcher.compute(imgL,imgR)
        plt.imshow(disparity,'gray')
        plt.show()
    
###################################################################################   

    def Background_subtraction(self):
        cap = cv2.VideoCapture(FolderImage +  "bgSub.mp4")
        backSub = cv2.createBackgroundSubtractorMOG2(history = 50,	varThreshold = 150,detectShadows = True)
        kernel=np.ones((5,5),np.uint8)
        while True:
            ret, frame = cap.read()
            if ret:
                if frame is None:
                    break
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)
                
                fgMask = backSub.apply(gray_frame)
                
                cv2.imshow('Test1', frame)
                cv2.imshow('Test2', fgMask)
                
                keyboard = cv2.waitKey(10)
                if keyboard == 'q' or keyboard == 27:
                    break
            else:
                break
        cv2.waitKey(500)
        cv2.destroyAllWindows()



###################################################################################       

    def Augmented_Reality(self):
        corners = np.float32([[1, 1, 0], [1, 5, 0], [5, 5, 0], [5, 1, 0],[3, 3, -4]])
        camera_matrix = np.array([[2225.49585482, 0., 1025.5459589 ], [ 0., 2225.18414074, 1038.58518846], [ 0., 0., 1. ]])
        distortion_coefficient = np.array([[-0.12874225, 0.09057782, -0.00099125, 0.00000278, 0.0022925]])
        extrinsix = np.array([[[-0.97157425, -0.01827487, 0.23602862, 6.81253889], [ 0.07148055, -0.97312723, 0.2188925, 3.37330384], [ 0.22568565, 0.22954177, 0.94677165, 16.71572319]], 
                    [[-0.8884799, -0.14530922, -0.435303, 3.3925504 ], [ 0.07148066, -0.98078915, 0.18150248, 4.36149229], [-0.45331444, 0.13014556, 0.88179825, 22.15957429]], 
                    [[-0.52390938, 0.22312793, 0.82202974, 2.68774801], [ 0.00530458, -0.96420621, 0.26510046, 4.70990021], [ 0.85175749, 0.14324914, 0.50397308, 12.98147662]],
                    [[-0.63108673, 0.53013053, 0.566296, 1.22781875], [ 0.13263301, -0.64553994, 0.75212145, 3.48023006], [ 0.76428923, 0.54976341, 0.33707888, 10.9840538 ]], 
                    [[-0.87676843, -0.23020567, 0.42223508, 4.43641198], [ 0.19708207, -0.97286949, -0.12117596, 0.67177428], [ 0.43867502, -0.02302829, 0.89835067, 16.24069227]]])
        
        # List_Processimage, List_Objpoints, List_Imgpoints, image = Processing_Detect()
        # reprojection_error, camera_matrix, distortion_coefficient, rotation_v, translation_v = cv2.calibrateCamera(List_Objpoints, List_Imgpoints, image.shape[:2],None,None)
        text = ""
        print("-------Intrinsic:------- \n%s" %camera_matrix)
        print("-------Distortion:------- \n%s" %distortion_coefficient)
        List_image = []
        # out = cv2.VideoWriter('Augmented_Reality.avi',cv2.VideoWriter_fourcc(*'mp4v'), 1000,(int(image.shape[:2][0]*0.5), int(image.shape[:2][1]*0.5)))
        for index in range(5):
            # index = 0
            Rotation_Mtx= extrinsix[index][0:3,0:3]
            Translation_Mtx = extrinsix[index][0:3,3:]
            Extrinsic_matrix = extrinsix[index]
            pyramid_corners_2d,_ = cv2.projectPoints(corners,Rotation_Mtx,Translation_Mtx,camera_matrix,distortion_coefficient)
            
            print("-------Extrinsic of %s:------- \n%s" %(ListImage[index],Extrinsic_matrix))
            text += "Extrinsic of %s........ \n" %ListImage[index]
            # self.text_showvalue.setText(text)  
            ImagePath = FolderImage + ListImage[index]
            img=cv2.imread(ImagePath) #load the correct image
            line_width = 10
            red=(0,0,255) #red (in BGR)
            blue=(255,0,0) #blue (in BGR)
            cv2.line(img, tuple(pyramid_corners_2d[0][0]), tuple(pyramid_corners_2d[1][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[1][0]), tuple(pyramid_corners_2d[2][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[2][0]), tuple(pyramid_corners_2d[3][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[3][0]), tuple(pyramid_corners_2d[0][0]),red,line_width)

            cv2.line(img, tuple(pyramid_corners_2d[0][0]), tuple(pyramid_corners_2d[4][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[1][0]), tuple(pyramid_corners_2d[4][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[2][0]), tuple(pyramid_corners_2d[4][0]),red,line_width)
            cv2.line(img, tuple(pyramid_corners_2d[3][0]), tuple(pyramid_corners_2d[4][0]),red,line_width)
            resize_IMG = cv2.resize(img, (int(img.shape[:2][0]*0.4), int(img.shape[:2][1]*0.4))) 
            List_image.append(resize_IMG)
        count = 0
        while(1):
            for i in range(len(List_image)):
                cv2.imshow('Augmented_Reality',List_image[i])
                cv2.waitKey(700)
            if count == 2:
                break
            count += 1


###################################################################################   

    def Parameter_video_tracking():
        cap = cv2.VideoCapture(FolderImage +  "featureTracking.mp4")
        _, first_frame = cap.read()
        first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        first_frame_gray = cv2.GaussianBlur(first_frame_gray, (5, 5), 0)

        params = cv2.SimpleBlobDetector_Params()
        # Change thresholds
        params.minThreshold = 80
        params.maxThreshold = 300
        # Filter by Area.
        params.filterByArea = True
        params.minArea = 35
        params.maxArea = 55
        # Filter by Circularity
        params.filterByCircularity = True
        params.maxCircularity = 1
        params.minCircularity = 0.8
        params.filterByInertia = True
        params.minInertiaRatio = 0.4
        detector = cv2.SimpleBlobDetector()

        is_v2 = cv2.__version__.startswith("2.")
        if is_v2:
            detector = cv2.SimpleBlobDetector(params)
        else:
            detector = cv2.SimpleBlobDetector_create(params)
    
        keypoints = detector.detect(first_frame)
        List_point_all = []
        
        for i in range(len(keypoints)):
            x,y = np.int(keypoints[i].pt[0]),np.int(keypoints[i].pt[1])
            sz = np.int(keypoints[i].size)
            list_point = [[x,y]]
            List_point_all.append(list_point)
            if sz > 1:
                sz = np.int(sz/2)
            im_with_keypoints = cv2.rectangle(first_frame, (x-2-sz,y-2-sz), (x+10-sz,y+10-sz), color=(0,0,255), thickness=2)
        # cv2.imshow("First Frame", im_with_keypoints)
        # cv2.waitKey(0)
        return im_with_keypoints,List_point_all
        # cap.release()
        # cv2.destroyAllWindows()

###################################################################################   

    def Preprocessing(self):
        im_with_keypoints,List_point_all = Process_Image.Parameter_video_tracking()
        cv2.imshow("Preprocessing", im_with_keypoints)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

###################################################################################   

    def videotracking(self):
        cap = cv2.VideoCapture(FolderImage +  "featureTracking.mp4")

        lk_params = dict( winSize  = (21,21),
                        maxLevel = 2,
                        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

        # Create some random colors

        ret, old_frame = cap.read()
        old_frame,List_point_all = Process_Image.Parameter_video_tracking()
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        p0 = np.array(List_point_all,np.float32)
    
        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)

        while(1):
            ret,frame = cap.read()
            
            if (ret):
                # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                first_frame_blue = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                blueLower = (25,50,50)  #130,150,80
                blueUpper = (160,250,250) #250,250,120
                mask1 = cv2.inRange(first_frame_blue, blueLower, blueUpper)
                try:
                    contours, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
                except:
                    _,contours, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                frame_coppy = frame.copy()
                cv2.drawContours(frame_coppy, contours, -1, (255,0,0), 8)
                # cv2.imshow("sds",frame_coppy)
                frame_gray = cv2.cvtColor(frame_coppy, cv2.COLOR_BGR2GRAY)
                # cv2.imshow("89898",old_gray)
                # # calculate optical flow
                p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
                
                # # Select good points
                good_new = p1[st==1]
                good_old = p0[st==1]
                # draw the tracks
                for i,(new,old) in enumerate(zip(good_new,good_old)):
                    a,b = new.ravel()
                    c,d = old.ravel()
                    # print(a,b,c,d)
                    mask = cv2.line(mask, (a,b),(c,d), (0,0,255), 2)
                    frame = cv2.rectangle(frame, (int(a)-6,int(b)-6), (int(a)+7,int(b)+7), color=(0,0,255), thickness=-1)
                
                img = cv2.add(frame,mask)
                
                cv2.imshow('Video tracking ',img)
                k = cv2.waitKey(20) & 0xff

                if k == 27:
                    break

                # Now update the previous frame and previous points
                old_gray = frame_gray.copy()
                p0 = good_new.reshape(-1,1,2)
            else:
                break

        cv2.destroyAllWindows()
        cap.release()



###################################################################################   


def mainprocessing():
	ui = Process_Image()
	Opencv_hw2.show()
	sys.exit(app.exec_())

if __name__ == "__main__":         
    mainprocessing()




