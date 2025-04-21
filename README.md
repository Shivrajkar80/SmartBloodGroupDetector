![Logo](BLOOD%20GROUP%20DETECTION%20USING%20EDGE%20BASED%20IMAGE.LOGO.png)

# 🩸 Blood Group Detection using Image Processing

This is a final year engineering project that detects human blood groups from blood sample images using **pure image processing techniques** in Python. The system avoids machine learning and relies on color and pattern analysis to determine blood group type (A, B, AB, O with Rh factor + or -).

---

## 🎯 Objective

To develop a fast and accurate system that can detect blood groups from images of blood samples without the need for complex training or external datasets. This is especially useful in emergency medical scenarios or low-resource settings.

This final year project aims to automate the detection of human blood groups using Python and image processing. Unlike traditional approaches that rely on machine learning, this system uses color segmentation and pattern recognition to identify blood group types (A, B, AB, O) along with Rh factor (+/-). It is lightweight, fast, and accurate for academic and potential healthcare use. The project was developed collaboratively by a 3-member engineering team using tools like OpenCV and NumPy.

---

## 🧪 How It Works

1. **Image Input**: A microscope or test image of blood is captured or loaded.
2. **Preprocessing**:
   - Resize the image
   - Convert to grayscale or HSV
   - Apply thresholding and filtering
3. **Detection Logic**:
   - Analyze presence of clumping/agglutination patterns
   - Use predefined color ranges or shapes to detect reactions with anti-sera
4. **Output**: Displays the predicted blood group (e.g., A+, O-, etc.)

---

## 🛠️ Tech Stack

| Area                 | Tools & Libraries     |
|----------------------|-----------------------|
| Programming Language | Python                |
| Image Processing     | OpenCV, NumPy         |
| UI (optional)        | Tkinter (for GUI)     |
| Data Handling        | Basic file I/O        |
| Visualization        | Matplotlib (optional) |

---

## 🧱 Project Structure



Blood-Group-Detection/ │ ├── detector.py # Main script for blood group detection ├── preprocess.py # Image preprocessing functions ├── model.pkl # Trained ML model (exported from Weka or sklearn) ├── sample_images/ # Folder containing test images ├── README.md # Project documentation └── requirements.txt # Python dependencies
