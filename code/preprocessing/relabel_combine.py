import pandas as pd

# Reads the default sheet of the excel file (.csv)
file_path = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train.csv'

df = pd.read_csv(file_path)

# print(df.head()) # Test if the dataset is loaded

row, col = df.shape
# print("original shape (%d, %d)" % (row, col))


if not (row % 3 == 0):
    print("ERROR: number of rows should be divisible by 3")

# Group the DataFrame by the 'id' column and aggregate the values in each group
grouped = df.groupby('id', as_index=False).agg({'class': list, 'segmentation': list})

print(grouped.head())

# print("new shape (%d, %d)" % (grouped.shape))

# Export to csv
output_file_path = "/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/cisc867_deep_learning_project/data/"
file_name = 'combined_class.csv'
grouped.to_csv(output_file_path + file_name, index=False)