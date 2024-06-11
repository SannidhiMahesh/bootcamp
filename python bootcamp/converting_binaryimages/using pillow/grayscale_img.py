import numpy as np
import pandas as pd
from PIL import Image

# Read the image using Pillow and convert to grayscale
image = Image.open('D:\OneDrive\Desktop\python\python bootcamp\download.jpg').convert('L')  # 'L' mode converts the image to grayscale

# Convert the image to a NumPy array
image_array = np.array(image)

# Convert the NumPy array to a DataFrame
df = pd.DataFrame(image_array)

# Write the DataFrame to a CSV file
csv_file_path = 'output.csv'
df.to_csv(csv_file_path, index=False, header=False)

# Display the image
image.show()

# Read and display the CSV file
df_from_csv = pd.read_csv(csv_file_path, header=None)
print(df_from_csv)
