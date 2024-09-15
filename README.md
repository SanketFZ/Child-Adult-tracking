# Child-Adult Person Detection using YOLOv8

DeepSORT enhances object tracking by combining:
1. **Motion-based Tracking** using a Kalman Filter.
2. **Appearance-based Association** using deep learning feature descriptors.

## Workflow

### 1. Detection
- **Input:** Object detections from an object detection model (e.g., YOLO, Faster R-CNN).
- **Bounding Boxes:** Each detection provides bounding boxes with associated confidence scores.

### 2. Feature Extraction
- **Appearance Descriptor:** For each detected object, a feature vector is extracted using a deep neural network (typically a pre-trained CNN like ResNet).
- **Purpose:** The feature vector helps distinguish between objects of similar size and shape based on appearance.

### 3. Kalman Filter Prediction
- **Tracking State Prediction:** The Kalman Filter predicts the object's next position based on its past states (position and velocity).
- **Motion Model:** Assumes constant velocity for objects, predicting their next position in the absence of new observations.

### 4. Matching and Association
- **Cost Matrix Calculation:** 
  - **Appearance Feature Distance:** Computed using the Euclidean distance between feature vectors.
  - **Motion Distance:** Calculated using the Mahalanobis distance between the predicted state and new detection.
- **Assignment:** The Hungarian algorithm is used to solve the cost matrix, matching detections to existing tracks in a way that minimizes total cost.

### 5. Update
- **Track Update:** Kalman Filter states and appearance descriptors are updated with new detection data.
- **New Tracks:** If a detection does not match an existing track, a new track is initialized.
- **Track Management:** Tracks not matched with detections for several frames are removed.

### 6. Output
- **ID Assignment:** Each tracked object is assigned a unique ID, consistent across frames.
- **Tracking Results:** Outputs include IDs, bounding boxes, and metadata (e.g., confidence scores) for each tracked object.


## Dataset Preparation

1. **Data Collection**: 
   - Gathered a diverse dataset containing images of adults and kids in various environments and poses.

2. **Annotation **: 
   - Used  tool ROBOFLOW to label and create bounding boxes around each person.
   - Labeled the bounding boxes as either "adult" or "kid".

3. **Data Split**:
   -   training, validation, and test sets into following:
     - **Training Set**: 70%
     - **Validation Set**: 20%
     - **Test Set**: 10%

## Setting Up YOLO Environment

1. **Install YOLOv8**:
   - Clone the YOLOv8 repository and install the YOLO library
   ```python
   pip install -r requirements.txt for dependencies
   ```

2. **Preparing YOLO Config File**:
   - Modified the `data.yaml` file to specify the number of classes (2: "adult" and "kid") and the paths to your dataset.

## Training the Model

1. **Run the Training Script**:
   - Execute the training command using your dataset and the YOLOv8 model:

2. ** Recursive Training**:
   - By Tracking the training progress through logs and visualizations. Adjust hyperparameters if necessary.

## Model Evaluation

1. **Validation**:
   - After training,  the modelwas evaluated using the validation set.results are stored in runs.

2. **Test**:
   - Test the model on the test set to assess its generalization capabilities.

## Fine-Tuning and Iteration

1. **Fine-Tune**:
   - If the initial results are not satisfactory, fine-tune the model by adding more data or tweaking hyperparameters.

2. **Continuous Learning**:
   - Regularly update the dataset and retrain the model to maintain and improve accuracy and robustness.



## Folder Overview
1. **ExperimentalCode**:
contains Code for for two different model
2. **Output**:
video output saved in.mp4 format
3. **traindedModel**: notebook Containing Model 
following is the link to notebook [COLAB Notebbok](https://colab.research.google.com/drive/1c-JkX-xFKUlbtzA4uiN5StUQc4O1lCWW?usp=sharing)

note : change path of train, test,valid in data.yaml file while training the model in colab notebook



## Scripts Execution
1. **personTraing.py**: Track the model using the dataset and YOLOv8 model.
2. **ChildTracking.py**: Track the model using custom model i.e., best (1).pt
3. **video** : to download test video




Note:- check for updated or equal version requirements for smooth execution

#### **Thank You**
