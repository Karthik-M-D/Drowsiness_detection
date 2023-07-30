import os
import random
import shutil

# Define the root directory where the dataset is located
root_dir = 'data'
new_dir = 'processed_data_final'  # New directory for storing train and valid folders

# Define the directories for open and closed images
open_dir = os.path.join(root_dir, 'Open_Eyes')
closed_dir = os.path.join(root_dir, 'Closed_Eyes')

# Create the new directory
os.makedirs(new_dir, exist_ok=True)

# Define the directories for train and validation images within the new directory
train_dir = os.path.join(new_dir, 'train')
valid_dir = os.path.join(new_dir, 'valid')

# Create the train and validation directories within the new directory
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)

# Define the subdirectories for open and closed within the train and validation directories
train_open_dir = os.path.join(train_dir, 'open')
train_closed_dir = os.path.join(train_dir, 'closed')
valid_open_dir = os.path.join(valid_dir, 'open')
valid_closed_dir = os.path.join(valid_dir, 'closed')

# Create the open and closed subdirectories within the train directory
os.makedirs(train_open_dir, exist_ok=True)
os.makedirs(train_closed_dir, exist_ok=True)

# Create the open and closed subdirectories within the validation directory
os.makedirs(valid_open_dir, exist_ok=True)
os.makedirs(valid_closed_dir, exist_ok=True)

# Define the percentage split
train_split = 0.8

# Move open images to train and validation directories within the new directory
open_images = os.listdir(open_dir)
random.shuffle(open_images)
num_train = int(len(open_images) * train_split)

for img in open_images[:num_train]:
    src = os.path.join(open_dir, img)
    dst = os.path.join(train_open_dir, img)
    shutil.move(src, dst)

for img in open_images[num_train:]:
    src = os.path.join(open_dir, img)
    dst = os.path.join(valid_open_dir, img)
    shutil.move(src, dst)

# Move closed images to train and validation directories within the new directory
closed_images = os.listdir(closed_dir)
random.shuffle(closed_images)
num_train = int(len(closed_images) * train_split)

for img in closed_images[:num_train]:
    src = os.path.join(closed_dir, img)
    dst = os.path.join(train_closed_dir, img)
    shutil.move(src, dst)

for img in closed_images[num_train:]:
    src = os.path.join(closed_dir, img)
    dst = os.path.join(valid_closed_dir, img)
    shutil.move(src, dst)
