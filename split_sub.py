import os
import shutil
import random

# Define paths
dataset_folder = 'dataset'  # Folder containing the 102 label sub-folders
train_folder = 'train'
val_folder = 'val'

# Create train and val directories if they don't exist
for folder in [train_folder, val_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Iterate over each sub-folder in the dataset folder
for label_folder in os.listdir(dataset_folder):
    label_path = os.path.join(dataset_folder, label_folder)
    
    if os.path.isdir(label_path):
        # List all images in the label folder
        images = os.listdir(label_path)
        
        # Shuffle images to ensure random distribution
        random.shuffle(images)
        
        # Determine the split index
        split_idx = int(0.8 * len(images))
        
        # Split the images into train and val sets
        train_images = images[:split_idx]
        val_images = images[split_idx:]
        
        # Create corresponding label sub-folders in train and val directories
        train_label_folder = os.path.join(train_folder, label_folder)
        val_label_folder = os.path.join(val_folder, label_folder)
        
        if not os.path.exists(train_label_folder):
            os.makedirs(train_label_folder)
        
        if not os.path.exists(val_label_folder):
            os.makedirs(val_label_folder)
        
        # Move images to the respective train/val sub-folder
        for image in train_images:
            shutil.move(os.path.join(label_path, image), os.path.join(train_label_folder, image))
        
        for image in val_images:
            shutil.move(os.path.join(label_path, image), os.path.join(val_label_folder, image))

print("Images have been split into train and val folders.")
