import os
import caffe
import numpy as np
import matplotlib.pyplot as plt

# set display defaults for ipynb
$ %matplotlib inline
plt.rcParams['figure.figsize'] = (5, 5)
plt.rcParams['image.interpolation'] = 'nearest'

# set caffe mode
caffe.set_mode_cpu()

model_name = "CK_Tuning"
BATCH_SIZE = 4

model_def = "../models/deploy.prototxt"
model_weights = "../models/{0:}/{0:}.caffemodel".format(model_name)
model_mean = "../models/{0:}/mean.binaryproto".format(model_name)
labels = ['Neutral', 'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise']

images_fname = [
    os.path.join(root, fname) 
    for root, _, files in os.walk('../samples') 
    for fname in files
]
images = [caffe.io.load_image(image_fname) for image_fname in images_fname]

mean_values = [103.939, 116.779, 123.68]  # default vgg mean
with open(model_mean, 'rb') as meanfile:
    blob = caffe.proto.caffe_pb2.BlobProto()
    blob.ParseFromString(meanfile.read())
    mean_values = np.array(caffe.io.blobproto_to_array(blob))[0]
    mean_values = mean_values.transpose(1, 2, 0)
    mean_values = caffe.io.resize_image(mean_values, (224, 224), 2)
    mean_values = mean_values.transpose(2, 0, 1)

from caffe.classifier import Classifier
c = Classifier(
    model_def, 
    model_weights, 
    mean=mean_values,
    raw_scale=255,
    channel_swap=(2,1,0),
    image_dims=(256, 256)
)
c.blobs['data'].reshape(BATCH_SIZE, 3, 224, 224)
c.blobs['softmax'].reshape(BATCH_SIZE, 3)
c.reshape()

cls = c.predict(images)

for i in range(BATCH_SIZE):
    class_max = cls[i, :].argmax()
    plt.imshow(images[i])
    plt.title('Predicted: {} ({:.2f}%)'.format(labels[class_max], 100 * cls[i, class_max]))
    plt.axis('off')
    plt.show()