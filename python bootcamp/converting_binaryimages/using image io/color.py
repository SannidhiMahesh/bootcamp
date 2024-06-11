import imageio.v2 as imageio  # Import ImageIO with the correct version to avoid deprecation warnings
import numpy as np
import pandas as pd

# Read the image using ImageIO
image = imageio.imread('D:\Downloads\lavender.jpg')

# Convert the image to a NumPy array and reshape it
reshaped_array = image.reshape(-1, image.shape[2])

# Convert the reshaped array to a DataFrame
df = pd.DataFrame(reshaped_array, columns=['R', 'G', 'B'])

# Write the DataFrame to a CSV file
csv_file_path = 'output_image3.csv'
df.to_csv(csv_file_path, index=False)

# Read and display the CSV file
df_from_csv = pd.read_csv(csv_file_path)
print(df_from_csv)
