from django.apps import AppConfig
from django.conf import settings
from imageai.Detection import ObjectDetection
import os


class PredictorConfig(AppConfig):
    name = 'predictor'



