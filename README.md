# Smart Driving Obstacle Detection System Based on YOLOv8

This project implements a smart driving obstacle detection system using the YOLOv8 object detection model, enhanced with custom modules like SlimNeck, GSConv, and GAM for improved performance. The system provides real-time object detection and distance estimation, all encapsulated within a user-friendly graphical interface built with PyQt6.

## Project Overview

In the realm of intelligent transportation systems and autonomous driving, accurate and real-time obstacle detection is paramount for ensuring safety and efficiency. This project addresses this critical need by leveraging the state-of-the-art YOLOv8 model, known for its balance of speed and accuracy. We further refine the model's capabilities by integrating novel architectural components (SlimNeck, GSConv, and GAM) to potentially boost detection performance in complex driving scenarios. The system features a PyQt6-based graphical user interface (GUI) that allows users to perform object detection on images and video streams, visualizing bounding boxes, class labels, and estimated distances to detected obstacles.

## Features

*   **YOLOv8-based Obstacle Detection:** Utilizes the powerful YOLOv8 model for efficient and accurate object detection.
*   **Enhanced Model Architecture:** Incorporates SlimNeck, GSConv, and GAM modules into the YOLOv8 architecture for potentially improved detection performance.
*   **Real-time Distance Estimation:** Calculates and displays the approximate distance to detected obstacles using camera intrinsic parameters.
*   **Graphical User Interface (GUI):** A user-friendly interface built with PyQt6 for easy interaction, allowing users to:
    *   Load images for object detection.
    *   Process video streams (from files or live camera feeds).
    *   Visualize detection results with bounding boxes, class labels, and distances.
    *   Display color-coded bounding boxes for vehicles based on their distance (e.g., red for close, orange for medium, green for far).
*   **Customizable Confidence Threshold:** Adjust the detection confidence threshold to fine-tune sensitivity.
*   **Configurable Training:** `train.py` provides options to configure training parameters like dataset path, image size, epochs, batch size, optimizer (SGD), and project/run names.

## Installation

To set up the project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Smart-Driving-Obstacle-Detection-System-Based-on-YOLOv8.git
    cd Smart-Driving-Obstacle-Detection-System-Based-on-YOLOv8
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The project relies on `ultralytics` for YOLOv8 and `PyQt6` for the GUI. You might also need `qt_material` for styling.
    ```bash
    pip install ultralytics==8.0.218 # Or the specific version used
    pip install PyQt6 qt_material opencv-python numpy
    ```
    *(Note: A `requirements.txt` file is not present in the initial file listing, so these are assumptions. It would be beneficial to create one.)*

## Usage

### Training the Model

The `train.py` script is used to train the YOLOv8 model with custom enhancements.

1.  **Prepare your dataset:** Ensure your obstacle detection dataset is in the YOLO format and you have a `obstacle.yaml` configuration file specifying dataset paths and class names. (Example: `ObstacleDataset/dataset/obstacle.yaml`)

2.  **Run training:**
    ```bash
    python train.py
    ```
    You can modify the training parameters directly in `train.py` (e.g., `epochs`, `batch`, `imgsz`, `device`). The model architecture is specified by `yolov8-SlimNeck+GSConv+GAM.yaml`.

### Running the GUI for Detection

The GUI allows you to perform real-time detection on images or videos.

1.  **Ensure you have a trained model weight file.** By default, `UI/yolo.py` looks for `../model/best.pt`. You should place your trained `best.pt` file in a `model` directory at the project root level, or update the `weights_path` in `UI/yolo.py`.

2.  **Start the application:**
    ```bash
    python UI/main.py
    ```

3.  **Interact with the GUI:**
    *   Load an image file for static detection.
    *   Select a video file or a camera feed for real-time detection.
    *   Observe bounding boxes, class labels, and distance estimations.
    *   Notice the color-coding for vehicles based on their proximity.

## Project Structure

```
.
├── CITATION.cff
├── LICENSE
├── README.md
├── mkdocs.yml
├── pyproject.toml
├── setup.py
├── train.py                          # Script for training the YOLOv8 model
├── UI/
│   ├── main.py                       # Main script to run the PyQt6 GUI
│   ├── mainwindow.py                 # PyQt6 main window logic
│   ├── mainwindow.ui                 # Qt Designer UI file for the main window
│   ├── ui_mainwindow.py              # Generated Python code from mainwindow.ui
│   └── yolo.py                       # YOLOv8 integration and detection logic
├── ultralytics/                      # Ultralytics YOLOv8 library (potentially modified or used as a module)
│   ├── cfg/                          # Configuration files for different YOLO models
│   ├── data/                         # Data loading and augmentation utilities
│   ├── engine/                       # Core components for training, prediction, etc.
│   ├── models/                       # Model definitions and specialized architectures (e.g., fastsam, rtdetr, sam, yolo)
│   ├── nn/                           # Neural network modules (e.g., blocks, convs, attention mechanisms like GAM, SlimNeck)
│   └── utils/                        # Utility functions (plotting, metrics, etc.)
├── yolov8-GAM.yaml                   # YOLOv8 configuration with GAM
├── yolov8-SlimNeck+GSConv.yaml       # YOLOv8 configuration with SlimNeck and GSConv
├── yolov8-SlimNeck+GSConv+GAM.yaml   # YOLOv8 configuration with SlimNeck, GSConv, and GAM (used in train.py)
└── model/                            # Directory for trained models (e.g., best.pt) - *create this directory*
```
*(Note: The `model/` directory is assumed for `best.pt` as per `yolo.py`. It's good practice to create it.)*


## Contact

If you have any questions or suggestions, please feel free to contact 1536825048@qq.com.
