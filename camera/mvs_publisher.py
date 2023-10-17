import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import numpy as np

def publish_video():
    rospy.init_node('video_publisher', anonymous=True)

    image_pub = rospy.Publisher('/image', Image, queue_size=10)
    
    # 打开摄像头
    cap = cv2.VideoCapture(1)  # 0表示默认的摄像头
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    bridge = CvBridge()
    
    rate = rospy.Rate(10)  # fps
    kernel = np.ones((3,3), np.uint8)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)[:, :, 0]
            # frame [:, :, 1] = 127
            # frame [:, :, 2] = 127
            # frame = cv2.cvtColor(frame, cv2.COLOR_YUV2RGB)
            
            # frame = cv2.erode(frame, kernel, iterations = 2)
            # frame = cv2.dilate(frame, kernel, iterations = 1)
            
            # frame = 255 - frame

            #sobel
            # sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)  # 在水平方向上检测边缘
            # sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)  # 在垂直方向上检测边缘
            # frame = np.sqrt(sobel_x**2 + sobel_y**2)
            # frame = cv2.convertScaleAbs(frame)

            # #
            # dilated_image = cv2.dilate(frame, kernel, iterations=5)
            # #
            # eroded_image = cv2.erode(frame, kernel, iterations=5)

            # gradient_image = dilated_image - eroded_image
            # alpha = 0.7 
            # beta = 1.0 - alpha
            # frame = cv2.addWeighted(frame, alpha, gradient_image, beta, 0)

            # 将OpenCV图像转换为ROS图像消息
            header = Header()
            header.stamp = rospy.Time.now()
            # image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="mono8")
            image_msg.header = header
            
            # 发布图像消息到指定话题
            image_pub.publish(image_msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_video()
    except rospy.ROSInterruptException:
        pass