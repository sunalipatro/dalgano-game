import os
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import mediapipe as mp
folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
# Read image frames for intro, kill, and winner screens
intro = cv2.imread("img1.jpeg")  # Replace "img1.jpg" with the actual file path of your intro image
kill = cv2.imread("img2.png")  # Replace "img2.jpg" with the actual file path of your kill image
winner = cv2.imread("img3.png")  # Replace "img3.jpg" with the actual file path of your winner image

# Read camera
cam = cv2.VideoCapture(0)  # Replace 0 with the appropriate camera index if you have multiple cameras

# Initialize HandTrackingMsodule for hand detection
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)

# Read images for game components
sqr_img = cv2.imread("sqr(2).png")  # Replace "sqr.jpg" with the actual file path of your square image
mlsa = cv2.imread("mlsa.png")  # Replace "mlsa.jpg" with the actual file path of your mlsa image

# Set initial game state
gameOver = False
NotWon = True

# Game logic for Dalgona game
while not gameOver:
    # Game logic for Dalgona game

    # Read a frame from the camera
    ret, frame = cam.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect hands in the frame
    hands = detector.detectHands(gray)
    
    # Check if any hands are detected
    if len(hands) > 0:
        # Get the hand landmarks
        handLandmarks = hands[0]["lmList"]
        
        # Get the coordinates of the index finger tip
        x, y = handLandmarks[8][1], handLandmarks[8][2]
        
        # Check if the index finger is above the square image
        if y < sqr_img.shape[0]:
            # Update game state or perform an action
            # For example, you can change the color of the square image to indicate the game progress
            
            # Check if the index finger is in the center of the square image
            if sqr_img.shape[1] // 2 - 50 < x < sqr_img.shape[1] // 2 + 50:
                # Update game state or perform an action
                # For example, you can play a sound or trigger an event
                
                # Set game over to True to end the game
                gameOver = True
    
    # Display the frame with overlays, e.g., square image, mlsa image, etc.
    # For example, you can use the overlayPNG() function from the cvzone library to overlay images onto the frame
    
    # Update game state or perform other game logic
    
    # Exit the game loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    continue

# Loss screen
if NotWon:
    for i in range(10):
        # Show the loss screen from the kill image
        cv2.imshow("Loss Screen", kill)
        cv2.waitKey(0)
    # End the game after pressing 'q'
    cv2.destroyAllWindows()

# Win screen
else:
    # Show the win screen from the winner image
    cv2.imshow("Win Screen", winner)
    cv2.waitKey(0)
    # End the game after pressing 'q'
    cv2.destroyAllWindows()