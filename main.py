import cv2
import numpy as np

# Load transparent overlay emoji images
happy_emoji = cv2.imread('happy.png', cv2.IMREAD_UNCHANGED)
sad_emoji = cv2.imread('sad.png', cv2.IMREAD_UNCHANGED)

# Resize overlays
happy_emoji = cv2.resize(happy_emoji, (100, 100))
sad_emoji = cv2.resize(sad_emoji, (100, 100))

def overlay_image(bg, fg, x, y):
    h, w = fg.shape[:2]
    if y + h > bg.shape[0] or x + w > bg.shape[1]:
        return bg
    alpha = fg[:, :, 3] / 255.0
    for c in range(3):
        bg[y:y+h, x:x+w, c] = (1 - alpha) * bg[y:y+h, x:x+w, c] + alpha * fg[:, :, c]
    return bg

# Load face image
frame = cv2.imread('face.jpg')  # Main image

if frame is None:
    print("Image not found! Make sure 'face.jpg' exists.")
    exit()

# Dummy logic: just use mean color for quick example
mean_color = cv2.mean(frame)[:3]  # BGR
blue, green, red = mean_color

x, y = 100, 100  # Position for overlay

if red > blue:
    frame = overlay_image(frame, happy_emoji, x, y)
    cv2.putText(frame, "HAPPY", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
else:
    frame = overlay_image(frame, sad_emoji, x, y)
    cv2.putText(frame, "SAD", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("AR Emotion Detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
