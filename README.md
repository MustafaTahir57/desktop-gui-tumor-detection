# Brain Tumor Detection Desktop Application

## Overview

This desktop application trains deep learning models on MRI/CT scan images for brain tumor detection. Key features include data preprocessing, augmentation, model training, evaluation metrics, and prediction capabilities. It achieves 99% accuracy in tumor detection, outperforming many existing approaches.

### Features:

- **Data Preprocessing**:
  - Noise Reduction
  - Skull Stripping
  - (Selection through checkboxes in the GUI)

- **Data Augmentation**:
  - Image Rotation
  - Scaling
  - Noise Injection
  - (Selection through checkboxes in the GUI)

- **Model Training**:
  - After training, the model is saved in the `model` directory for future use.
  
- **Model Evaluation**:
  - Accuracy, Precision, Recall, F1-Score, and Confusion Matrix are calculated and saved to a CSV file.
  - A Confusion Matrix image is generated using Matplotlib and displayed on the GUI.
  - Users can view the performance measures by clicking the "Performance Measure" button in the GUI.

- **Tumor Detection Prediction**:
  - Users can upload an MRI/CT scan image and check for the presence of a tumor.
  - If a tumor is detected, the application will output "Tumor Found!" along with the model's confidence.
  - If no tumor is detected, the output will be "No Tumor!" along with the model's confidence.

## How to Use the Application:

1. **Upload Dataset**: Use the provided GUI button to upload the dataset for model training.
2. **Select Preprocessing/Augmentation Options**: Choose the data preprocessing and augmentation techniques you wish to apply.
3. **Train Model**: After selecting the options, click the "Train Model" button to start training.
4. **Evaluate Model**: Once the model is trained, click "Performance Measure" to view the evaluation metrics.
5. **Predict Tumor**: After model evaluation, upload an MRI/CT scan image using the "Evaluate Tumor" button to see if a tumor is present.

## Requirements

- Python 3.11.0
- TensorFlow
- Pillow (PIL)
- Scikit-learn
- OpenCV
- Imutils
- Numpy
- Matplotlib
- CSV for data handling

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MustafaTahir57/desktop-gui-tumor-detection
    cd brain-tumor-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python dashboard.py
    ```

## File Structure

```bash
brain-tumor-detection/
├── Images/                    # Directory where Background images are saved for GUI
├── Dataset/                   # Directory for storing MRI/CT scan images dataset
├── model/                     # Directory where trained model is saved
├── model_evaluation/          # CSV files and confusion matrix images
├── dashboard.py               # Main GUI code
├── login.py                   # login window code 
├── data_augmentation.py       # data augmentation implementation
├── data_pre_processing.py     # data preprocessing implementation
├── model.py                   # model training and model evaluation implementation
├── predict.py                 # Classifies MRI/CT scan for tumor detection
├── requirements.txt           # all the requirements
└── README.md                  # Project documentation
```

## Example Workflow

1. **Preprocessing and Augmentation**: The user selects desired options like noise reduction, skull stripping, rotation, scaling, and noise injection before training the model.
   
2. **Model Training**: The model is trained based on the selected data processing steps, and the trained model is saved in the `model` directory for future predictions.

3. **Model Evaluation**: Evaluation metrics like accuracy, precision, recall, F1-score, and confusion matrix are calculated and stored in a CSV file, with a confusion matrix image displayed in the GUI.

4. **Prediction**: After selecting an MRI/CT scan image, the user clicks "Evaluate Tumor" to detect the presence of a tumor. The result is displayed in the GUI along with the model's confidence.

## Credits

- Developed by: [Muhammad Mustafa Tahir ](https://github.com/MustafaTahir57/desktop-gui-tumor-detection/)

## Note:
- The dataset directory should contain two subdirectories: `yes` for images with tumors and `no` for images without tumors.
