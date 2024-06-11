import cv2
import numpy as np
import pandas as pd

# Read the image using OpenCV in grayscale mode
image = cv2.imread('D:\OneDrive\Desktop\python\python bootcamp\download.jpg', cv2.IMREAD_GRAYSCALE)

# Convert the image to a DataFrame
df = pd.DataFrame(image)

# Write the DataFrame to a CSV file
csv_file_path = 'output_image2.csv'
df.to_csv(csv_file_path, index=False, header=False)

# Read and display the CSV file
df_from_csv = pd.read_csv(csv_file_path, header=None)
print(df_from_csv)
