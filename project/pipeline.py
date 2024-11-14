import pandas as pd
import numpy as np
import requests
import zipfile
import io
from sqlalchemy import create_engine
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def kaggle_extract_Data(username, key):
    
    
    # Set environment variables for Kaggle username and API key present in kaggle.JSON
    os.environ['KAGGLE_USERNAME'] = username
    os.environ['KAGGLE_KEY'] = key

    # Initialize Kaggle API and authenticate using the provided credentials
    api = KaggleApi()
    api.authenticate()

    # Define the dataset to download from Kaggle (in this case, it's a Brazilian Amazon Rainforest degradation dataset)
    dataset = "mbogernetto/brazilian-amazon-rainforest-degradation"
    
    # Download the dataset from Kaggle to the current directory (files will be in a zip format)
    api.dataset_download_files(dataset, path=".", unzip=False)

    # Unzip the downloaded file into a folder named after the dataset
    with zipfile.ZipFile("brazilian-amazon-rainforest-degradation.zip", 'r') as zip_ref:
        zip_ref.extractall("brazilian-amazon-rainforest-degradation")
    
    # Load data from a specific CSV file into a pandas DataFrame
    # The zip folder has three files but we only need one
    df = pd.read_csv("brazilian-amazon-rainforest-degradation/def_area_2004_2019.csv")
    
    # Check if the DataFrame is successfully loaded and print a success message
    if df is not None:
        print("Data Extraction Success!")
        
    # Return the loaded DataFrame
    return df

def download_and_extract_in_memory(url):
    
    """
    Here the Zip files can be downloaded directly from the URL
    
    Parameters:
    url: The web address (URL in str) pointing to the ZIP file to be downloaded.

    Returns:
    dict: A dictionary with filenames (keys) and their corresponding in-memory file objects (values), 
          representing the contents of each file within the ZIP file.
          'filenames (keys)': in-memory file objects (values)
          """

    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        return {name: io.BytesIO(zip_ref.read(name)) for name in zip_ref.namelist()}
    
def load_and_clean_data(file_like, delimiter=','):
    
    """
    Load data from a CSV file-like object into a pandas DataFrame, then clean the data.

    Parameters:
    file_like : An object containing the CSV data to be loaded.
    delimiter : Character used to separate values in the CSV. Defaults to ','.

    Returns:
    A cleaned DataFrame where missing values have been removed.
    """
    

    df = pd.read_csv(file_like, delimiter=delimiter)
    df.dropna(inplace=True)
    return df

def drop_irrelevant_columns(df, columns_to_drop):
    
    
#   Removes specified columns from a pandas DataFrame (df). The irrelevant columns not to be used in final db.
    
    df.drop(columns=columns_to_drop, inplace=True)
    return df

def rename_columns(df, columns_mapping):

    df.rename(columns=columns_mapping, inplace=True)
    return df

def drop_rows_with_zeros(df, columns):
    
    
#   Remove rows from a DataFrame where specified columns (list) contain zero values.

#   This returns A DataFrame excluding rows that had zero values in the specified columns.
    

    df = df.loc[~(df[columns] == 0).all(axis=1)]
    return df

def filter_rows_with_brazil(df, column_name1, column_name2, years):
    
    """
    Filter a DataFrame to keep only rows where the specified column contains "Brazil"
    The dataset has data around the world but we are only focusing on Brazil.
    Also the wildfire and emission data is from 2002 - 2023 but the deforestration data is only
    from 2004 - 2019. Hence we drop the data for missing years from wildfire and emission datasets.

    Args:
        df: The input DataFrame.
        column_name1: The name of the column to check for "Brazil" (country).
        column_year2: The name of the column containing year values (year).
        years (list): List of years to exclude.

    Returns:
        pd.DataFrame: DataFrame with only rows containing "Brazil" in the specified column
                      and where the years are excluded provided in the list.
    """
    # Filter for rows where the specified column is "Brazil" and the year is NOT in the list of years
    filtered_df = df[(df[column_name1] == "Brazil") & (~df[column_name2].isin(years))]
    return filtered_df

def create_database(db_dir, db_name):
    
    """
    Create a SQLite database in the specified directory.

    Parameters:
    db_dir  : Directory path where the database will be created.
    db_name : Name of the SQLite database.

    Returns:
    str: Path of the created SQLite database.
    """
    
    db_path = os.path.join(db_dir, f"{db_name}.db")
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    return db_path

def transform_deforestration_data(df):
    
    """
    Transforms deforestration data in a pandas DataFrame 

    This function performs operations such as:
    1. Drop the uncessary columns.
    2. Drops the zero values from the rows with specified columns.
    3. Renames columns for consistency and clarity
    
    Args:
        df : Path to the CSV file containing deforestration data.

    Returns:
        pd.DataFrame: Transformed deforestration DataFrame.
    """
    deforestration_columns_to_drop = ['AC', 'AM', 'AP', 'MA', 'MT', 'PA', 'RO', 'RR', 'TO']
    df = drop_irrelevant_columns(df, deforestration_columns_to_drop).copy()
    
    columns_with_zeros = ["AMZ LEGAL"]
    df = drop_rows_with_zeros(df, columns_with_zeros).copy()
    
    deforestration_columns_rename = {'Ano/Estados': 'Year',
                               'AMZ LEGAL':'Deforested Area'}
    df = rename_columns(df, deforestration_columns_rename).copy()
    
    return df.reindex(columns=['Year','Deforested Area'])

def transform_wildfire_data(df):
    """
    Transforms Wildfire burned area data in a pandas DataFrame 

    This function performs operations such as:
    1. Drop the uncessary columns.
    2. Drops the zero values from the rows with specified columns.
    3. Drops the data (rows) that are not related to Brazil 
    4. Drops the data (rows) from specfied years.
    5. Renames columns for consistency and clarity
    6. Aggregating (sum) monthly data to make it yearly data. 
    
    Args:
        df : Path to the CSV file containing wildfire data.

    Returns:
        pd.DataFrame: Transformed wildfire DataFrame.
    """
    
    wildfire_columns_to_drop = ['gid_0','gid_1' ,'savannas', 'shrublands_grasslands', 'croplands', 'other']
    df = drop_irrelevant_columns(df, wildfire_columns_to_drop).copy()
    
    columns_with_zeros = ["forest"]
    df = drop_rows_with_zeros(df, columns_with_zeros).copy()
    
    years_to_exclude = [2002, 2003, 2020, 2021, 2022, 2023]
    df = filter_rows_with_brazil(df, 'country','year', years=years_to_exclude).copy()
    
    wildfire_columns_rename = {'year': 'Year',
                               'country':'Country_Name',
                               'month':'Month',
                               'forest':'Forest_BA'}
    
    df = rename_columns(df, wildfire_columns_rename).copy()
    df = df.groupby(['Year', 'Country_Name']).agg({
        'Forest_BA': 'sum',
    }).reset_index()
    
    return df[['Year', 'Country_Name', 'Forest_BA']]

def transform_emissions_data(df):
    """
    Transforms Emissions data in a pandas DataFrame 

    This function performs operations such as:
    1. Drop the uncessary columns.
    2. Drops the zero values from the rows with specified columns.
    3. Drops the data (rows) that are not related to Brazil 
    4. Drops the data (rows) from specfied years.
    5. Renames columns for consistency and clarity
    6. Aggregating (sum) monthly data to make it yearly data. 
    
    Args:
        df : Path to the CSV file containing wildfire data.

    Returns:
        pd.DataFrame: Transformed wildfire DataFrame.
    """
    
    emissions_columns_to_drop = ['gid_1', 'gid_0' , "CO", "TPM", "PM25", 
                                 "TPC", "NMHC", "OC", "CH4", "SO2", "BC", "NOx"]
    df = drop_irrelevant_columns(df, emissions_columns_to_drop).copy()
    
    columns_with_zeros = ["CO2"]
    df = drop_rows_with_zeros(df, columns_with_zeros).copy()
    
    years_to_exclude = [2002, 2003, 2020, 2021, 2022, 2023]
    df = filter_rows_with_brazil(df, 'country','year', years=years_to_exclude).copy()
    
    emissions_columns_rename = {'year':'Year',
                                'month':'Month',
                                'country':'Country_Name'}
    df = rename_columns(df, emissions_columns_rename).copy()
    
    df = df.groupby(['Year', 'Country_Name']).agg({
        'CO2': 'sum',
    }).reset_index()
    
    return df[['Year', 'Country_Name', 'CO2']]

def main():
    
    """
    Main function to execute the data engineering automated pipeline. This function downloads,
    extracts, transforms, and saves wildfire and emissions data.
    
    Steps:
        - Download and extract data.
        - Transform data.
        - Save the transformed data to a SQLite database.
    """
#   Define Kaggle credentials to be found in kaggle.JSON
    username = "username"
    key = "key"
#     kaggle_extract_Data(username, key)
    deforestration_df = kaggle_extract_Data(username, key)
    
#   URLs for wildfire and emissions data files to download
#   The URL for deforestration data is set above in the function already
    wildfire_url = "https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002-2023.zip"
    emissions_url = "https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/emission_gfed_full_2002_2023.zip"
    
#   Download and extract wildfire and emissions data in memory
    wildfire_files = download_and_extract_in_memory(wildfire_url)
    emissions_files = download_and_extract_in_memory(emissions_url)
    
#   Specify file paths for the CSV files within the extracted wildfire and emissions data
#   The path for deforestration data is set above in the function already
    wildfire_file_like = wildfire_files['MCD64A1_burned_area_full_dataset_2002-2023.csv']
    emissions_file_like = emissions_files['emission_gfed_full_2002_2023.csv']
    
    wildfire_df = load_and_clean_data(wildfire_file_like)
    emissions_df = load_and_clean_data(emissions_file_like)
    
#   Transform the deforestration, wildfire and emissions data
    wildfire_df = transform_wildfire_data(wildfire_df).copy()
    emissions_df = transform_emissions_data(emissions_df).copy()
    deforestration_df = transform_deforestration_data(deforestration_df).copy()
    
#   Merge the wildfire and emission datasets
#   Merge the intermediate df with deforestration_df to make the final df  
    merged_df1 = pd.merge(wildfire_df, emissions_df, how='inner')
    merged_df2 = pd.merge(merged_df1, deforestration_df, how='inner')
    print(merged_df2.head())

#   SQLite database path
    db_dir = 'data'
    db_name = 'brazil_amazon_deforestration_and_wildfire_and_emission_data'
    db_path = create_database(db_dir, db_name)
    engine = create_engine(f'sqlite:///{db_path}')
    
#   Save the processed data to the database
    wildfire_df.to_sql('wildfire_burned_area_data', engine, index=False, if_exists='replace')
    emissions_df.to_sql('wildfire_emissions_data', engine, index=False, if_exists='replace')
    deforestration_df.to_sql('deforestration_data', engine, index=False, if_exists='replace')
    merged_df2.to_sql('amazon_merged_data', engine, index=False, if_exists='replace')
    
    print("I am finished")

if __name__ == "__main__":
    main()

