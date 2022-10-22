import os.path
import json
import random
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
import itertools
from typing import List
from skimage.transform import resize
import skimage.transform
from mpl_toolkits.axes_grid1 import ImageGrid

class ImageGenerator:
    index = 0
    epochs = 0
    
    def __init__(self, file_path: str, json_path: str, batch:int, image_size:List[int], rotation=False, mirroring=False, shuffle=False):
        self.file_path = file_path
        self.json_path = json_path
        self.batch = batch
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        
        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}
        # Note that the file names correspond to the dicts of the label dictionary.
        
    def next(self, resize_=False):
        with open(self.json_path) as json_file:
            data = json.load(json_file)  # Load json file as a dictionary
            if (self.shuffle==True):
                data_list = list(data.items()) # Ta kanw lista
                random.shuffle(data_list) # Ta kanw shuffle 
                data = dict(l) # To ksanakanw dictionary
                  
            size = len(data) # Ποσα ειναι τα δεδομενα
            if (self.batch<=size):
                if (size - ImageGenerator.index >= self.batch):
                    images = [] # Edw tha vazw ta imaeges
                    labels = [] # Edw ta labels
                    for i in range(ImageGenerator.index, ImageGenerator.index+self.batch):
                        current_image = np.load(self.file_path + str(list(data.keys())[i]) +'.npy')
                        images = images + [current_image]
                        label_number = list(data.values())[i] # Edw pairnw to noumero tis class
                        labels.append(label_number)
                    images = np.stack(images, axis=0)
                    ImageGenerator.index += self.batch
                    if (ImageGenerator.index==size+self.batch):
                        ImageGenerator.index == 0
                        ImageGenerator.epochs += 1
                else:
                    howmany = self.batch - size + ImageGenerator.index # Posa mou menoun extra
                    images = [] # Edw tha vazw ta imaeges
                    labels = [] # Edw ta labels
                    for i in range(ImageGenerator.index, size):
                        current_image = np.load(self.file_path + str(list(data.keys())[i]) +'.npy')
                        images = images + [current_image]
                        label_number = list(data.values())[i] # Edw pairnw to noumero tis class
                        labels.append(label_number)
                    for i in range(0, howmany):
                        current_image = np.load(self.file_path + str(list(data.keys())[i]) +'.npy')
                        images = images + [current_image]
                        label_number = list(data.values())[i] # Edw pairnw to noumero tis class
                        labels.append(label_number) 
                    images = np.stack(images, axis=0)
                    ImageGenerator.index = 0 
                    ImageGenerator.epochs += 1
                    
            #Resizing 
            if (resize_==True):
                resized_images = []
                for j in range(self.batch):
                    resized = resize(images[j], (self.image_size[0], self.image_size[1]))
                    resized_images = resized_images + [resized]
                
                images = np.stack(resized_images, axis=0)
                
            return images, labels
#             else:
#                 print("Batch size too big or no more batches to return")
                    

    
    def augment(self, img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function
        if (self.rotation==True):
            angles = [90, 180, 270]
            rotated_img = skimage.transform.rotate(test_img, angle=random.choice(angles))
            return rotated_img
        else:
            return img
        
        if (self.mirroring == True):
            will_mirror = random.choice([0,1])
            if will_mirror==1:
                 return img[:, ::-1]
            else:
                return img
        else:
            return img
        
    def current_epoch(self):
        # return the current epoch number
        return ImageGenerator.epochs

    def class_name(self, int_label):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[int_label]
    
    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        #TODO: implement show method
        if (self.batch>=9):
            im1, lb1 = self.next() # Generate a batch
            fig = plt.figure(figsize=(20, 20))

            rows = self.batch//3 if (self.batch%3)==0 else (self.batch//3) + 1

            grid = ImageGrid(fig, 111,
                     nrows_ncols=(rows, 3), 
                     axes_pad=0.5,
                     )

            for ax, im in zip(grid, range(im1.shape[0])):
                # Iterating over the grid returns the Axes.
                ax.imshow(im1[im])
                label_num = lb1[im]
                ax.title.set_text(self.class_name(label_num))
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)

            plt.show()
        