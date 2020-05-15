from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from imageai.Detection import ObjectDetection
import os
from .models import *
import cv2
import threading
from imageai.Detection import VideoObjectDetection
from django.core.files.storage import default_storage

from django.shortcuts import render
# from .forms import FaceAdditionForm
import cv2
import numpy as np
from django.http import StreamingHttpResponse

# Create your views here.

def getResnet(request):
    if request.method == "POST":
        f = request.FILES['sentFile']  # here you get the files needed
        execution_path = os.getcwd()
        detector = ObjectDetection()
        path = os.path.join(settings.MODELS, "resnet50_coco_best_v2.0.1.h5")
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(path)
        detector.loadModel()

        detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg')
        item=[]
        object=''
        for eachObject in detections:
            item.append(eachObject["name"])
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac=AdvertisementCategory.objects.filter(id__in=categoryName)
        ads=Advertisement.objects.filter(categoryName__in=ac)
        context = {
            'ac':ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def getYoloTiny(request):
    if request.method == "POST":
        f = request.FILES['sentFile']  # here you get the files needed
        execution_path = os.getcwd()
        detector = ObjectDetection()
        path = os.path.join(settings.MODELS, "yolo-tiny.h5")
        detector.setModelTypeAsTinyYOLOv3()
        detector.setModelPath(path)
        detector.loadModel()

        detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg')
        item=[]
        object=''
        for eachObject in detections:
            item.append(eachObject["name"])
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac=AdvertisementCategory.objects.filter(id__in=categoryName)
        ads=Advertisement.objects.filter(categoryName__in=ac)
        context = {
            'ac':ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def getYolo(request):
    if request.method == "POST":
        f = request.FILES['sentFile']  # here you get the files needed
        execution_path = os.getcwd()
        detector = ObjectDetection()
        path = os.path.join(settings.MODELS, "yolo.h5")
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(path)
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg')
        item = []
        object = ''
        for eachObject in detections:
            item.append(eachObject["name"])
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac = AdvertisementCategory.objects.filter(id__in=categoryName)
        ads = Advertisement.objects.filter(categoryName__in=ac)
        context = {
            'ac': ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def getCustom(request):
    if request.method == "POST":
        f = request.FILES['sentFile']  # here you get the files needed
        execution_path = os.getcwd()
        detector = ObjectDetection()
        path = os.path.join(settings.MODELS, "yolo.h5")
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(path)
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg')
        item = []
        object = ''
        for eachObject in detections:
            item.append(eachObject["name"])
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac = AdvertisementCategory.objects.filter(id__in=categoryName)
        ads = Advertisement.objects.filter(categoryName__in=ac)
        context = {
            'ac': ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def default(request):
    return render(request, 'base.html')


# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         image = self.frame
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
#
#
#
#
# def getResnet1(request):
#     if request.method == "POST":
#         file = request.FILES['sentFile']  #
#         import uuid
#
#         unique_filename = str(uuid.uuid4())
#         file_name = default_storage.save(unique_filename, file)
#
#         #  Reading file from storage
#         file = default_storage.open(file_name)
#         file_url = default_storage.url(file_name)
#
#
#         detector = VideoObjectDetection()
#         detector.setModelTypeAsRetinaNet()
#         path = os.path.join(settings.MODELS, "resnet50_coco_best_v2.0.1.h5")
#         detector.setModelPath(path)
#         detector.loadModel()
#         video_path = detector.detectObjectsFromVideo(input_file_path='media/'+unique_filename,
#                                                      output_file_path='media/imagetest_video'
#                                                      , frames_per_second=20, log_progress=True,
#                                                      minimum_percentage_probability=30,save_detected_video=True)
#         context = {
#             'video':1
#         }
#         return render(request, 'predictions.html',context)
#     else:
#         return render(request, 'homepage.html')
#
# def stopResnet(request):
#     print('in stop')
#     camera.release()
#     return render(request, 'predictions.html', context)