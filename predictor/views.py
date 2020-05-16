from django.conf import settings
from imageai.Detection import ObjectDetection
from imageai.Detection.Custom import CustomObjectDetection
import os
from .models import *
from imageai.Detection import VideoObjectDetection
from django.core.files.storage import default_storage
from django.shortcuts import render
# from .forms import FaceAdditionForm
# Create your views here.

def getResnet(request):
    if request.method == "POST":
        try:
            f = request.FILES['sentFile']  # here you get the files needed
        except:
            return render(request, 'homepage.html')

        execution_path = os.getcwd()
        detector = ObjectDetection()
        path = os.path.join(settings.MODELS, "resnet50_coco_best_v2.0.1.h5")
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(path)
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg',)
        item=[]
        object=''
        for eachObject in detections:
            item.append(eachObject["name"])
        if len(item)==0:
            return render(request, 'failPredictions.html')
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac=AdvertisementCategory.objects.filter(id__in=categoryName)
        ads=Advertisement.objects.filter(categoryName__in=ac)
        if len(ads)==0:
            return render(request, 'failPredictions.html')
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
        if len(item) == 0:
            return render(request, 'failPredictions.html')
        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac=AdvertisementCategory.objects.filter(id__in=categoryName)
        ads=Advertisement.objects.filter(categoryName__in=ac)
        if len(ads)==0:
            return render(request, 'failPredictions.html')
        context = {
            'ac':ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def getYolo(request):
    if request.method == "POST":
        try:
            f = request.FILES['sentFile']  # here you get the files needed
        except:
            return render(request, 'homepage.html')
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
        if len(item)==0:
            return render(request, 'failPredictions.html')

        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac = AdvertisementCategory.objects.filter(id__in=categoryName)
        ads = Advertisement.objects.filter(categoryName__in=ac)
        if len(ads)==0:
            return render(request, 'failPredictions.html')
        context = {
            'ac': ac,
            'ads': ads,
        }
        return render(request, 'predictions.html', context)
    else:
        return render(request, 'homepage.html')

def getCustom(request):
    if request.method == "POST":
        try:
            f = request.FILES['sentFile']  # here you get the files needed
        except:
            return render(request, 'homepage.html')
        execution_path = os.getcwd()
        modelPath = os.path.join(settings.MODELS,"detection_model.h5")
        configPath = os.path.join(settings.MODELS, "detection_config.json")
        detector = CustomObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(modelPath)
        detector.setJsonPath(configPath)
        detector.loadModel()
        try:
            detections = detector.detectObjectsFromImage(input_image=f,
                                                     output_image_path='media/imagetest.jpg')
        except:
            return  render(request, 'failPredictions.html')

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



def getVideo(request):
    if request.method == "POST":
        try:
            file = request.FILES['sentFile']  #
        except:
            return render(request, 'homepage.html')

        import uuid

        unique_filename = str(uuid.uuid4())
        file_name = default_storage.save(unique_filename, file)

        #  Reading file from storage
        file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)


        detector = VideoObjectDetection()
        detector.setModelTypeAsRetinaNet()
        path = os.path.join(settings.MODELS, "resnet50_coco_best_v2.0.1.h5")
        detector.setModelPath(path)
        detector.loadModel(detection_speed='faster')
        item = set()
        def forFrame(frame_number, output_array, output_count):
            for i in output_array:
                item.add(i['name'])








        video_path = detector.detectObjectsFromVideo(input_file_path='media/'+unique_filename,
                                                     output_file_path='media/imagetest_video'
                                                     , frames_per_second=20, log_progress=True,
                                                     minimum_percentage_probability=30,save_detected_video=True,per_frame_function=forFrame)

        categoryName = objectCategory.objects.filter(object__in=item).values_list('categoryName', flat=True)
        ac = AdvertisementCategory.objects.filter(id__in=categoryName)
        ads = Advertisement.objects.filter(categoryName__in=ac)
        if len(ads)==0:
            return render(request, 'failPredictions.html')
        context = {
            'ac': ac,
            'ads': ads,
        }

        return render(request, 'vid_predictions.html',context)
    else:
        return render(request, 'homepage2.html')
