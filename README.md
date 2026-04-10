😴 Driver Drowsiness Detection System

A deep learning-based Driver Drowsiness Detection System that detects whether a driver's eyes are open or closed in real time using a webcam and alerts when drowsiness is detected.
The system uses Computer Vision, CNN, OpenCV, and TensorFlow to monitor eye movements and prevent accidents caused by driver fatigue.

This project helps improve road safety by providing real-time drowsiness alerts.

🌟 Features
👁️ Real-Time Eye Detection
Detects face using Haar Cascade
Detects eyes in real time
Classifies eye state (Open / Closed)
Displays status on screen
🚨 Drowsiness Alert System
Tracks continuous closed-eye frames
Shows DROWSY ALERT when eyes remain closed
Real-time monitoring using webcam
Lightweight and fast detection
🧠 Deep Learning Model
CNN-based model
Binary classification
Open Eyes
Closed Eyes
Trained on image dataset
🏗️ System Architecture
Input

Webcam video feed

↓

Face Detection

OpenCV Haar Cascade

↓

Eye Detection

OpenCV Eye Cascade

↓

CNN Model

TensorFlow / Keras Model

↓

Prediction

Open Eyes / Closed Eyes

↓

Alert

Drowsiness Warning

🛠️ Tools & Technologies
Programming Language
Python
Libraries
TensorFlow
Keras
OpenCV
NumPy
Matplotlib
Scikit-learn
Technologies
Deep Learning
Computer Vision
CNN
Image Processing
Haar Cascade
Development Environment
Google Colab
Python IDE
Webcam System
🧠 Model Information
Model Type

Convolutional Neural Network (CNN)

Architecture
Conv2D
MaxPooling2D
Conv2D
MaxPooling2D
Flatten
Dropout
Dense Layers
Sigmoid Output
Output
0 → Open Eyes
1 → Closed Eyes

Model File:

Drowsiness_model.h5
📂 Project Structure
Drowsiness-Detection/
│
├── train.py
├── testing.py
├── training.ipynb
├── Drowsiness_model.h5
├── data/
│   ├── train/
│   │   ├── Open_Eyes/
│   │   └── Closed_Eyes/
│   └── test/
│       ├── Open_Eyes/
│       └── Closed_Eyes/
│
└── README.md
⚙️ Installation & Setup
Prerequisites
Python 3.8+
Webcam
pip
Step 1: Clone Repository
git clone https://github.com/your-username/Drowsiness-Detection.git
cd Drowsiness-Detection
Step 2: Install Dependencies
pip install tensorflow
pip install opencv-python
pip install numpy
pip install matplotlib
pip install scikit-learn
▶️ How to Run
1️⃣ Train Model

Run:

python train.py

This will:

Load dataset
Train CNN model
Save model as Drowsiness_model.h5
2️⃣ Run Drowsiness Detection

Run:

python testing.py

This will:

Open webcam
Detect face and eyes
Predict Open or Closed
Show Drowsy Alert
Press ESC to exit
📊 Dataset

Dataset contains two classes:

Open Eyes
Closed Eyes
Folder Structure
train/
   Open_Eyes/
   Closed_Eyes/

test/
   Open_Eyes/
   Closed_Eyes/
Image Size
128 x 128
📈 Training Details
Parameter	Value
Image Size	128x128
Batch Size	16
Epochs	10
Optimizer	Adam
Loss Function	Binary Crossentropy
Output	Sigmoid
🚨 Drowsiness Alert Logic

If eyes remain closed continuously:

counter > 5

Then system shows:

DROWSY ALERT

on the screen.

🔮 Future Improvements
-Add alarm sound
-Add blink detection
-Improve CNN accuracy
-Add mobile camera support
-Deploy using Flask
-Deploy using Streamlit
-Add dashboard monitoring
-Integrate with vehicle system

You can:
-Fork the repository
-Improve model
-Add features
-Submit pull request
