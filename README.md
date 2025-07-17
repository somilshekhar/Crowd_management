# Crowd Management System 🚶‍♂️🚶‍♀️

![Crowd Management Banner](https://via.placeholder.com/1200x300.png?text=Crowd+Management+System) <!-- Replace with actual banner image -->

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-brightgreen)](https://flask.palletsprojects.com/)
[![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-orange)](https://pjreddie.com/darknet/yolo/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📖 Overview

The **Crowd Management System** is a powerful tool for real-time crowd monitoring and management. Using **YOLO** for object detection and **Flask** for a user-friendly web interface, it analyzes video feeds from IP cameras or webcams to provide insights into crowd density, movement patterns, and safety concerns. Perfect for public spaces like malls, markets, and transportation hubs! 🏬🚉

🌟 **Key Features**:
- Real-time crowd detection and counting
- Visual crowd density maps with color-coded alerts
- Threshold-based overcrowding alerts
- Web-based interface for easy monitoring

## 🛠️ Technologies Used

- **Python** 🐍: Core programming language
- **YOLO** 🔍: Real-time object detection
- **OpenCV** 📷: Video and image processing
- **Flask** 🌐: Web framework for the interface
- **NumPy** 📊: Numerical computations

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- IP Camera (optional) or webcam
- Internet connection for dependency installation

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/somilshekhar/Crowd_management.git
   cd Crowd_management
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or use the provided batch file (Windows):
   ```bash
   dependencies.bat
   ```

3. **Configure IP Camera** (if using):
   - Install the "IP Camera" app from the Play Store.
   - Start the server on your mobile device to get the IP address.
   - Update `detection.py` with the IP:
     ```python
     camera_ip = "http://<your-ip-address>:8080/video"
     ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://localhost:5000`.

## 📺 Usage

1. **Video Input**:
   - Use an IP camera or your laptop’s webcam.
   - Ensure the camera captures the crowd area.

2. **Web Interface**:
   - View real-time crowd density maps 🌈
   - Monitor alerts for overcrowding 🚨
   - Analyze crowd behavior data 📈

3. **Customization**:
   - Adjust density thresholds in `detection.py`.
   - Modify Flask templates in the `templates/` folder for UI changes.

![Crowd Density Map](https://via.placeholder.com/600x400.png?text=Crowd+Density+Map+Example) <!-- Replace with actual screenshot -->

## 🎯 Applications

- **Public Safety**: Monitor crowds in markets, malls, or events.
- **Event Management**: Optimize crowd flow during concerts or festivals.
- **Business Optimization**: Analyze customer density in retail spaces.

## 📂 Project Structure

```plaintext
Crowd_management/
├── app.py              # Main Flask application
├── detection.py        # YOLO-based crowd detection logic
├── templates/          # HTML templates for the web interface
├── static/             # CSS, JS, and image assets
├── requirements.txt    # Python dependencies
├── dependencies.bat    # Batch file for dependency installation (Windows)
└── README.md           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! 🙌
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📸 Screenshots



---

⭐ **Star this repository if you find it useful!**  
For questions or feedback, contact [Somil Shekhar](https://github.com/somilshekhar).
