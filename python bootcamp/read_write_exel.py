# Reading an Excel file
import pandas as pd

def read_excel(file_path):
    df = pd.read_excel("D:\OneDrive\Documents\Book2.xlsx")
    return df

# Writing to an Excel file
def write_excel(df, file_path):
    df.to_excel("D:\OneDrive\Documents\Book2.xlsx", index=False)

# Example usage
excel_file_path = 'data.xlsx'
df = read_excel(excel_file_path)
print(df)
write_excel(df, 'output.xlsx')
