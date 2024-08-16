import os
import shutil
import scipy.io

# Define the paths
image_folder = '102flowers/dataset'  # Folder containing the images
label_file = 'imagelabels.mat'  # .mat file containing the labels
output_folder = 'dataset'  # Folder to store sorted images

# Load the labels from the .mat file
mat = scipy.io.loadmat(label_file)
labels = mat['labels'][0]  # Extract the labels (assuming labels are stored in a 1D array)

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over each image in the image folder
for i, label in enumerate(labels):
    # Create the label folder if it doesn't exist
    label_folder = os.path.join(output_folder, f'label_{label}')
    if not os.path.exists(label_folder):
        os.makedirs(label_folder)

    # Determine the image filename (assuming images are named sequentially)
    image_filename = f'image_{i+1:05d}.jpg'  # Adjust the file naming format as needed
    source_path = os.path.join(image_folder, image_filename)
    destination_path = os.path.join(label_folder, image_filename)

    # Move the image to the label folder
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
    else:
        print(f"Image {image_filename} not found.")

print("Images have been sorted and moved into label folders.")
