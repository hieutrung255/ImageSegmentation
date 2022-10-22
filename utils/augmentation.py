import torch
from torchvision import transforms
from PIL import Image, ImageOps, ImageFilter
import numpy as np

class Compose(object):
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, img, anno_class_img):
        for t in self.transforms:
            img, anno_class_img = t(img, anno_class_img)
        return img, anno_class_img

class Scale(object):
    def __init__(self, scale):
        self.scale = scale
    
    def __call__(self, img, anno_class_img):
        width = img.size[0]
        height = img.size[1]

        scale = np.random.uniform(self.scale[0], self.scale[1])

        scale_w = int(width*scale)
        scale_h = int(height*scale)

        img = img.resize((scale_w, ))