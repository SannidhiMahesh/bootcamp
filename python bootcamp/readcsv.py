import pandas as pd

# Reading a CSV file
def read_csv(file_path):
    df = pd.read_csv("D:\OneDrive\Documents\Book1.csv")
    return df

# Writing to a CSV file
def write_csv(df, file_path):
    df.to_csv(f"D:\OneDrive\Documents\Book1.csv", index=True)

# Example usage
csv_file_path = 'data.csv'
df = read_csv(csv_file_path)
print(df)
write_csv(df, 'output.csv')
