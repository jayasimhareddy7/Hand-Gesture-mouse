# Hand Gesture Mouse Controller - Complete Process Documentation

## Project Overview

This project implements a virtual mouse controlled by hand gestures using computer vision. Users can control their computer's cursor, perform clicks, and scroll using simple hand gestures captured through a webcam.

## Core Components

### 1. Main Application (`app.py`)
The core functionality that processes hand gestures and controls the mouse.

### 2. Streamlit Interface (`streamlit_app.py`)
A web-based GUI to easily start the gesture mouse controller.

## Technology Stack

- **OpenCV**: Computer vision library for video capture and image processing
- **MediaPipe**: Google's machine learning solution for hand tracking
- **PyAutoGUI**: Cross-platform GUI automation for mouse control
- **Streamlit**: Web application framework for the user interface

## Detailed Process Flow

### Step 1: Initialization
```
- Import required libraries (cv2, mediapipe, pyautogui, math)
- Set pyautogui.FAILSAFE = False to disable failsafe mode
- Initialize MediaPipe Hands solution
- Initialize webcam capture (VideoCapture(0))
- Get screen dimensions for cursor mapping
```

### Step 2: Video Capture Loop
```
- Continuously read frames from webcam
- Flip frame horizontally for mirror view
- Convert BGR color space to RGB for MediaPipe processing
- Process frame to detect hand landmarks
```

### Step 3: Hand Detection & Landmark Extraction
```
- MediaPipe detects hand landmarks (21 points per hand)
- Draw landmarks on the frame for visual feedback
- Extract specific landmark coordinates:
  * Index finger tip (landmark 8)
  * Other finger tips for gesture recognition
  * Thumb landmarks for scroll detection
```

### Step 4: Cursor Movement
```
- Map index finger tip coordinates to screen coordinates
- Scale camera frame coordinates to screen resolution
- Use pyautogui.moveTo() to move cursor smoothly
- Real-time tracking as hand moves
```

### Step 5: Gesture Recognition

#### Fist Gesture (Left Click)
```
- Check if all finger tips (index, middle, ring, pinky) are below palm base
- All landmarks 8, 12, 16, 20 must be lower than landmark 0 (wrist)
- When detected: Trigger pyautogui.click()
```

#### Thumbs Up (Scroll Up)
```
- Compare thumb tip (landmark 4) with thumb IP joint (landmark 3)
- If thumb tip is higher than IP joint: thumbs up detected
- When detected: pyautogui.scroll(20) to scroll up
```

#### Two Fingers Up (Scroll Down)
```
- Check if index finger (landmark 8) and middle finger (landmark 12) are extended
- Compare finger tip Y-coordinate with previous joint Y-coordinate
- When detected: pyautogui.scroll(-20) to scroll down
```

### Step 6: Display & Exit
```
- Display processed video feed with OpenCV window
- Wait for ESC key (key code 27) to break loop
- Release webcam resources
- Close all OpenCV windows
```

## Hand Landmark Reference

MediaPipe detects 21 hand landmarks:
- 0: Wrist
- 1-4: Thumb
- 5-8: Index finger
- 9-12: Middle finger
- 13-16: Ring finger
- 17-20: Pinky finger

Each finger has 4 landmarks:
- MCP (Metacarpophalangeal joint) - base
- PIP (Proximal Interphalangeal joint) - middle joint
- DIP (Distal Interphalangeal joint) - upper joint
- Tip - fingertip

## Installation Process

1. Create virtual environment:
   ```bash
   python -m venv mp_env
   source mp_env/bin/activate  # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   
   Or use Streamlit interface:
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage Instructions

### Basic Controls
1. **Move Cursor**: Point with your index finger
2. **Left Click**: Make a fist (all fingers down)
3. **Scroll Up**: Show thumbs up gesture
4. **Scroll Down**: Point with index and middle fingers

### Best Practices
- Ensure good lighting for accurate hand detection
- Keep hand within camera frame
- Maintain moderate distance from camera (30-60 cm)
- Allow 1-2 seconds for gesture detection
- Press ESC to exit the application

## Technical Details

### Coordinate Mapping
- Camera frame coordinates are normalized (0.0 to 1.0)
- Multiplied by screen width/height to get pixel coordinates
- X-axis: index_finger.x * screen_w
- Y-axis: index_finger.y * screen_h

### Performance Considerations
- max_num_hands=1: Only tracks one hand for efficiency
- min_detection_confidence=0.7: Balance between accuracy and speed
- Real-time processing at ~30 FPS depending on hardware

### Safety Features
- pyautogui.FAILSAFE disabled to prevent interruption
- ESC key provides reliable exit mechanism
- Proper resource cleanup on exit

## Troubleshooting

### Common Issues
1. **Cursor not moving**: Check webcam is working and hand is visible
2. **Inaccurate movement**: Adjust lighting or camera angle
3. **Delayed response**: Close other applications using CPU
4. **No detection**: Ensure hand is fully visible in frame

### Platform-Specific Notes
- **macOS**: May need to grant camera and accessibility permissions
- **Windows**: Ensure camera drivers are up to date
- **Linux**: May need to install additional camera libraries

## Future Enhancements

Potential improvements:
- Right-click gesture (e.g., peace sign)
- Double-click gesture
- Drag and drop functionality
- Multi-hand support
- Customizable gesture mappings
- Sensitivity adjustments
- Visual feedback for clicks
- Keyboard shortcut emulation

## Project Structure

```
hand gesture mouse/
├── app.py                 # Main gesture control application
├── streamlit_app.py       # Web interface
├── requirements.txt       # Python dependencies
└── PROCESS_DOCUMENTATION.md  # This file
```

## License & Credits

This project uses open-source libraries:
- OpenCV (Apache 2 License)
- MediaPipe (Apache 2 License)
- PyAutoGUI (BSD License)
- Streamlit (Apache 2 License)

## Support

For issues or questions about hand gesture recognition, computer vision, or mouse automation, refer to the respective library documentation:
- OpenCV: https://docs.opencv.org/
- MediaPipe: https://google.github.io/mediapipe/
- PyAutoGUI: https://pyautogui.readthedocs.io/
