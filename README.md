# Drishyam : Smart Payment Gateway

This project combines the power of **Object Detection**, **Voice Commands**, and **Gesture Recognition** to deliver a seamless and interactive user experience for managing transactions. It also includes real-time location detection and text-to-speech features.

---

## 🏗 **Architecture**
1. **Object Detection**:
   - Integrated with the **YOLO (You Only Look Once)** model for real-time object detection through a webcam.
   - Detected objects are announced using **Text-to-Speech (TTS)** for enhanced accessibility.

2. **Voice Commands**:
   - **Speech recognition** allows users to issue commands like "debit," "credit," "view balance," etc.
   - Facilitates hands-free operation for a better user experience.

3. **Gesture Recognition**:
   - Utilizes **MediaPipe** to detect hand gestures.
   - Gesture-based commands enable intuitive interaction.

4. **Account and Transaction Management**:
   - Includes features for debiting, crediting, viewing balance, and checking transaction history.

5. **Location Services**:
   - Integrated with **Geopy** for real-time location detection.
   - Displays user location and addresses dynamically.

---

## 💻 **Tech Stack**
- **Machine Learning**: YOLO (Object Detection), MediaPipe
- **Voice Processing**: SpeechRecognition, pyttsx3 (Text-to-Speech)
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Location Services**: Geopy

---

## 📂 **Project Structure**
```plaintext
.
├── static/
│   ├── index.html        # Frontend HTML file
│   ├── styles.css        # Styling for the frontend
├── app.py                # Flask backend application
├── object_detection.py   # YOLO-based object detection script
├── gesture_recognition.py # MediaPipe gesture recognition script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 **Features**
- **Object Detection**: Real-time detection of objects via webcam with voice-based announcements.
- **Voice Commands**: Execute actions like debiting, crediting, and balance inquiries using speech recognition.
- **Gesture Recognition**: Perform actions via hand gestures detected using MediaPipe.
- **Transaction Management**: Manage account balances and transaction history through intuitive inputs.
- **Location Detection**: Real-time location and address display using Geopy.

---

## 🛠 **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone "https://github.com/Kaap10/Drishyam.git"
   cd Drishyam
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   `http://127.0.0.1:5000/`

---

## 🌟 **Future Enhancements**
- Improve object detection accuracy by fine-tuning the YOLO model.
- Add more gestures and voice commands for enhanced functionality.
- Integrate cloud storage for transaction history.
- Deploy the application to a cloud platform for global accessibility.

---

## 🤝 **Contributing**
Contributions are welcome! Fork the repository and submit pull requests with your improvements.

---

## 📜 **License**
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 📬 **Contact**
For questions or suggestions, feel free to reach out via GitHub issues or email.
