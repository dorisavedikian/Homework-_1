# cd /Volumes
# cd "USDA HD"
# cd "Final Semester Fall 2022"
# cd "CYBI 6378"
# cd "archive"
# python3 -m venv env
# source env/bin/activate

import os
import csv 
import re
import glob
import pandas as pd

# The following function will go line by line and create a data frame with columns 'MovieID', 'CustomerID', 'Rating' and 'Date'
def create4columns(filename): 
    df = {'MovieID':[], 'CustomerID':[],  'Rating':[],  'Date':[]}                      # Create data dictionary   
    with open(filename, 'r', encoding='latin-1') as f:   
        for line in f:
            line = line.strip()                                                         # Skip empty lines
            if line:                                                                    
                if line.endswith(':'):                                                  
                    movie_id = line[:-1]                                                # MovieID = all contents of the string except last character or element   
                else:
                    customer_id, rating, date = line.split(',')                         # Splits string into list seperated by ','
                    df['MovieID'].append(movie_id)
                    df['CustomerID'].append(customer_id)
                    df['Rating'].append(rating)
                    df['Date'].append(date)
    df = pd.DataFrame(df)
    outfile = df.to_csv(filename.split('.')[0] + '.Adjusted.csv')                       # Saves data frame as a csv with a new name 

# Grab all files ending in 'data.txt' in the 'archive' directory than use function above
for filename in glob.glob('*data.txt', recursive = True):
    create4columns(filename)   
    print('Completed')

# View head of the combined data 1 file after its been turned into a data frame and saved as a CSV to check work
#df1 = pd.read_csv("/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/combined_1_data.Adjusted.csv")
#print(df1.head())

# Create new dataframes
df1 = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/combined_1_data.Adjusted.csv')
df2 = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/combined_2_data.Adjusted.csv')
df3 = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/combined_3_data.Adjusted.csv')
df4 = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/combined_4_data.Adjusted.csv')

# Combine all data frames into 1
df_combined = pd.concat([df1,df2,df3,df4])
df_combined.to_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Combined_Data_4.csv')
#print(df_combined.count())

# Add headers to movie_titles.csv
col_names = ["movie_id", "year", "Title", "other"]      
file = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/movie_titles.csv', names = col_names, encoding='latin-1')
file.to_csv("/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Titles.csv", index=False)
file2 = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Titles.csv', encoding='latin-1')
#print(file2.head())
df__combined = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Combined_Data_4.csv', encoding='latin-1')
#print(df__combined.head())

# Merge data frames and drop unwanted columns
df__combined = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Combined_Data_4.csv', encoding='latin-1')
df__title = pd.read_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Titles.csv', encoding='latin-1')
Merged_csv = df__combined.merge(df__title[['movie_id','Title']], left_on='MovieID',right_on='movie_id')
Merged_CSV = Merged_csv.drop(Merged_csv.columns[[0,1,6]], axis=1)
outfile = Merged_CSV.to_csv('/Volumes/USDA HD/Final Semester Fall 2022/CYBI 6378/archive/Final Dataset/Final.csv')
print(Merged_CSV.head(100))
print(Merged_CSV.tail(100))


