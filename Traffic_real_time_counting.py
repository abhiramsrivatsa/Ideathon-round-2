
# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting_api

input_video = "./Enter the traffic live feed here"

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28')

#object_counting_api.object_counting(input_video, detection_graph, category_index, 0) # for counting all the objects, disabled color prediction

#object_counting_api.object_counting(input_video, detection_graph, category_index, 1) # for counting all the objects, enabled color prediction


targeted_objects = "car,person,truck,bus" # (for counting targeted objects) change it with your targeted objects person relates to a two wheeler
is_color_recognition_enabled = 0

#object_counting_api.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects, fps, width, height) # targeted objects counting

object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled) # counting all the objects
