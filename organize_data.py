#Organize data properly for CUB_200_2011
import os
import sys

"""
Create relevant directory structure
"""
def create_dirs():
    for dirName in ['train', 'test']:
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        else:    
            print("Directory " , dirName ,  " already exists")


"""
Split images into train and test set based on a precomputed split
(Also every train file starts off in the same cluster 0)
"""
def organize_data():
    image_split = {}
    with open('train_test_split.txt', 'r') as split_file:
        for line in split_file:
            line = line.strip()
            image_id, is_train = line.split()
            image_split[image_id] = is_train

    with open('images.txt', 'r') as images_file:
        images = images_file.readlines()

    train_file = open('train.txt', 'w')
    test_file = open('test.txt', 'w')

"""
This snippet builds directory structure according to README but code doesn't actually expect that
"""
    # for image in images:
    #     image_id, image_name = image.split()
    #     # If the precomputed split says this is a train image move it to train directory
    #     # and write file name and fake cluster to train.txt
    #     if int(image_split[image_id]) == 1:
    #         os.makedirs(os.path.dirname('train/' + image_name), exist_ok=True)
    #         os.rename('images/' + image_name, 'train/' + image_name)
    #         train_file.write(image_name + ' 0\n')
    #     else:
    #         os.makedirs(os.path.dirname('test/' + image_name), exist_ok=True)
    #         os.rename('images/' + image_name, 'test/' + image_name)
    #         test_file.write(image_name + ' 0\n')

"""
This snippet builds directory structure that seems to work (untested, needs to be confirmed)
"""
    for image in images:
        image_id, image_name = image.split()
        # Make the directory for this class
        os.makedirs(os.path.dirname('train/' + image_name), exist_ok=True)
        # Move the image to proper location
        os.rename('images/' + image_name, './' + image_name)

        # If the precomputed split says this is a train image write file name and fake cluster to train.txt
        if int(image_split[image_id]) == 1:
            train_file.write(image_name + ' 0\n')
        else:
            test_file.write(image_name + ' 0\n')


if __name__ == '__main__':
    create_dirs()
    organize_data()
