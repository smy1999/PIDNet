# to be done
import os
import cv2
import glob

images_path = '/Users/smy1999/Desktop/index/leftImg8bit/demoVideo/stuttgart_00/'
images = glob.glob(images_path + '*.png')

video = cv2.VideoWriter('d:/image/test.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,(1280,720))  #定义保存视频目录名称及压缩格式，fps=10,像素为1280*720
for i in range(1,len(list)):
    img = cv2.imread('d:/image/'+list[i-1])  #读取图片
    img=cv2.resize(img,(1280,720)) #将图片转换为1280*720
    video.write(img)   #写入视频

video.release()
