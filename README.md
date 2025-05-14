# Emotion Detection with AR Emoji Overlay

This project is based on the concepts of Augmented Reality (AR) and Marker Detection. It overlays virtual emojis (happy or sad) onto a static image based on detected emotion using color analysis. The original logic is reused from a traffic signal AR simulation, but applied to a new theme — emotion detection.

## Project Concept

- Detect dominant colors from a face image to infer emotion (red for happy, blue for sad).
- Overlay a transparent emoji image (happy or sad) onto the face in the input image.
- This simulates an Augmented Reality effect using basic image processing techniques.

## Tools and Libraries

- Python
- OpenCV (`cv2`)
- Transparent PNG images with alpha channel (for emoji overlays)


## How It Works

1. Load a face image using OpenCV.
2. Use color averaging to detect dominant tone (red or blue).
3. Based on result, overlay the appropriate emoji using alpha blending.
4. Display the output with AR-style overlay.

## How to Run

1. Install OpenCV:

2. Place `face.jpg`, `happy.png`, and `sad.png` in the same directory.

3. Run the script:

## Notes

- This is a simple demonstration of AR overlay using basic color analysis.
- PNG emoji images must have an alpha (transparency) channel.
- No actual facial expression recognition is used — this is a visual AR simulation.

## Related Project Inspiration

Originally based on an AR Traffic Signal Simulation project:
- Detect real traffic light colors (red/green) from an image.
- Overlay AR signs (e.g., STOP, GO) virtually above the lights.
- Swapped that concept to emotion-based overlay using the same code logic.
