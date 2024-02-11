import cv2
import pytesseract

# Path to the image file
image_path = 'image.png'

# Read the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(threshold_image)

# Print the extracted text
print(extracted_text)
