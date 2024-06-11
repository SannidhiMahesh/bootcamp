import numpy as np
import pandas as pd
from PIL import Image

# Read the image using Pillow and keep it in RGB mode
image = Image.open('D:\Downloads\lavender.jpg').convert('RGB')  # 'RGB' mode keeps the image in color

# Convert the image to a NumPy array
image_array = np.array(image)

# Reshape the array to have each pixel's RGB values as a separate row
reshaped_array = image_array.reshape(-1, image_array.shape[2])

# Convert the reshaped array to a DataFrame
df = pd.DataFrame(reshaped_array, columns=['R', 'G', 'B'])

# Write the DataFrame to a CSV file
csv_file_path = 'output_image1.csv'
df.to_csv(csv_file_path, index=False)

# Read and display the CSV file
df_from_csv = pd.read_csv(csv_file_path)
print(df_from_csv)
