import pandas as pd
import os

path = "C:\\Users\\Lenovo\\Downloads\\PROJECT\\Mobile Project\\Python WebScraping"
csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]


data_frames = []

for file in csv_files:
    full_path = os.path.join(path, file)
    df = pd.read_csv(full_path)
    data_frames.append(df)

concatenated_df = pd.concat(data_frames, ignore_index=True)


concatenated_df.to_csv(f'{path}/Mobile_Data13.csv', index=False)


# 