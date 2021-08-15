# script for image recognition using facebook's resnet50 model

from imageai.Classification import ImageClassification
import os
execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "truck_1.jpg"), result_count=5)
for eachPrediction, eachPropability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachPropability)
