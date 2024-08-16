# Fellowship AI Code Challenge

## Project Overview

This project is designed to organize a dataset of flower images into labeled folders and then split the dataset into training and validation sets. The steps below guide you through downloading the necessary data, organizing it, and preparing it for model training.

## Steps to Reproduce

### 1. Download the Dataset

Download the flower dataset and the `imagelabel.mat` file from the following link:

- [Flower Dataset - Oxford](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)

### 2. Organize Images by Labels

After downloading the dataset, organize the images into folders corresponding to their labels by following these steps:

1. Open the `sorted.py` script.
2. Adjust any parameters as necessary within the script.
3. Execute the script using the following command:

   ```bash
   python sorted.py
   ```

   This will automatically place the images into folders based on their respective labels.

### 3. Split Dataset into Training and Validation Sets

Once the images are sorted by label, split the dataset into training and validation sets:

1. Open the `split-sub.py` script.
2. Modify the parameters as needed to customize the split.
3. Run the script with the following command:

   ```bash
   python split-sub.py
   ```

   This will create two new folders, `train` and `val`, containing the split datasets.

### 4. Run the Model Notebook

With the dataset prepared, you can now run the provided Jupyter notebook to train your model:

1. Open the notebook in your preferred environment (e.g., Jupyter Lab, VS Code).
2. Follow the instructions within the notebook to execute the model training.

---

## Requirements

Ensure you have the following installed to run the scripts and notebook:

- Python 3.x
- Required Python libraries as listed in `requirements.txt` (if applicable)

## Conclusion

By following these steps, you'll have a well-organized dataset ready for model training, with a clear separation between training and validation data.
