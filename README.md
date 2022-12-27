
Build
---

1.Building ORB-SLAM3

    git clone https://github.com/sam051200/ORB_SLAM3.git 
	cd ORB_SLAM3 
	chmod +x build.sh 
	./build.sh 
2.Building ORB-SLAM3 for ROS nodes 

    sudo apt install python-is-python3 
  	export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM3/Examples/ROS 
	chmod +x build_ros.sh 
   	./build_ros.sh
`PATH/ORB_SLAM3/Examples/ROS 請填入的絕對路徑`

使用
---
1.設定相機參數（yaml）
可參考 `ORB_SLAM3/Examples/ROS/mycam.yaml`

2.運行

	rosrun ORB_SLAM3 Mono ./ORB_SLAM3/Vocabulary/ORBvoc.txt ./ORB_SLAM3/Examples/ROS/mycam.yaml /image
`./ORB_SLAM3/Examples/ROS/mycam.yaml` 填入自己相機的設定檔位址

`/image`填入ROS 影像Topic的





   
