
# Smart Election Voting System with Face Recognition

## Overview
The **Smart Election Voting System** is a secure voting platform that leverages face recognition for voter authentication. This system ensures that each voter can cast their vote only once, enhancing security and streamlining the voting process. It uses machine learning, specifically the K-Nearest Neighbors (KNN) algorithm, to classify and recognize voter faces.

---

## Features
- **Face Detection:** Real-time detection using OpenCV's Haar Cascade.
- **Face Recognition:** Voter identification through the KNN algorithm.
- **Vote Recording:** Securely logs votes into a CSV file.
- **Duplicate Prevention:** Prevents voters from casting multiple votes.
- **Voice Feedback:** Provides auditory confirmations via a text-to-speech engine.

---

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - OpenCV: Face detection and image processing.
  - scikit-learn: KNN-based classification.
  - NumPy: Numerical computations.
  - win32com (Windows-specific): Text-to-speech functionality.
  - Pickle: Data serialization.
- **Dataset:** Custom face data collected during runtime.

---

## Setup Instructions
### 1. Prerequisites
Ensure Python 3.x is installed along with the required libraries:

```bash
pip install opencv-python scikit-learn numpy pywin32
```

### 2. Clone the Repository
Clone this project to your local machine:

```bash
git clone https://github.com/yourusername/face-recognition-voting.git
cd face-recognition-voting
```

### 3. Collect Face Data
Run the `add_faces.py` script to collect face data for voters:

```bash
python add_faces.py
```
- The system captures **1000 frames** of face data for each voter.
- Provide a **unique identifier** (e.g., Aadhaar number) for each voter.

### 4. Start the Voting System
Run the `give_vote.py` script to start the voting system:

```bash
python give_vote.py
```
- The system authenticates voters using face recognition.
- Voters can cast their votes by pressing:
  - `1` for BJP
  - `2` for Congress
  - `3` for AAP
  - `4` for NOTA

---

## How It Works
### 1. **Face Data Collection**
- Voter face data is captured, resized, and stored using `add_faces.py`.
- The data is serialized and saved as `.pkl` files.

### 2. **Voter Authentication**
- The `give_vote.py` script uses a pre-trained KNN classifier to recognize voter faces.
- Only authenticated voters can proceed to vote.

### 3. **Vote Casting**
- Voters select their choice by pressing the corresponding key.
- Votes are recorded in `Votes.csv` along with the voter's ID, date, and timestamp.

### 4. **Duplicate Vote Prevention**
- The system verifies `Votes.csv` to ensure no duplicate votes are cast.

---

## File Descriptions
- **`add_faces.py`:** Captures and stores face data for training the recognition system.
- **`give_vote.py`:** Manages real-time face recognition and vote recording.
- **`Votes.csv`:** Stores voting records, including voter ID, choice, date, and time.

---

## Limitations
- Requires a Windows system for text-to-speech functionality.
- Dependent on consistent lighting and camera quality for accurate face recognition.
- Assumes voters have unique identifiers (e.g., Aadhaar numbers).

---

## Future Enhancements
- Expand compatibility to non-Windows systems.
- Integrate live database support for real-time updates.
- Enhance recognition accuracy with deep learning techniques (e.g., CNNs).

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **[OpenCV](https://opencv.org/):** For robust computer vision tools.
- **[scikit-learn](https://scikit-learn.org/):** For machine learning functionalities.

---
