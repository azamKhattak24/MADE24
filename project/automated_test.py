import unittest
import os
import sqlite3
import pandas as pd
from pipeline import (
    kaggle_extract_Data,
    download_and_extract_in_memory,
    load_and_clean_data,
    transform_deforestation_data,
    transform_wildfire_data,
    transform_emissions_data,
    main
)

def check_column_names(df, expected_column_names):
    """
    This Function checks if the column names in a DataFrame matches the expected column names.
    Args:
        df (pandas.DataFrame): To validate the DataFrame.
        expected_column_names (list of str): A list of column names that the DataFrame is expected to have.
    Raises:
        AssertionError: Raised if the DataFrame's column names differ from the expected ones.
    """
    for x, y in zip(expected_column_names, df.columns):
        assert x == y, f"Column name incorrect: {y} instead of {x}"

def check_null_values(df, cols):
    """
    This Function checks if any of the specified columns in a DataFrame contains any null values.

    Args:
        df (pandas.DataFrame): To validate the DataFrame.
        cols (list of str): A list column names that are to be checked for null values.
    Raises:
        AssertionError: Raised if any of the specified columns contain null values.
    """
    for col in cols:
        assert not df[col].isna().any(), f"Column {col} contains null values"

def read_sql_table(db_path, table_name):
    """
    Reads a table from an SQLite database into a pandas DataFrame.
    Args:
        db_path (str): The file path to the SQLite database.
        table_name (str): The name of the table to be loaded.
    Returns:
        pandas.DataFrame: A DataFrame containing the data from the specified table.
    """
    query = f"SELECT * FROM {table_name}"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def check_wildfire_data_table(wildfire_df):
    """
    Validates the structure and integrity of a DataFrame containing wildfire data.
    Args:
        wildfire_df (pandas.DataFrame): The DataFrame containing wildfire data.
    Raises:
        AssertionError: Raised if the DataFrame does not pass the integrity checks.
    """
    wildfire_expected_columns = ['Year', 'Country_Name', 'Forest_BA']
    check_column_names(wildfire_df, wildfire_expected_columns)
    check_null_values(wildfire_df, wildfire_df.columns)


def check_emissions_data_table(emissions_df):
    """
    Validates the structure and integrity of a DataFrame containing emissions data.
    Args:
        emissions_df (pandas.DataFrame): The DataFrame containing emissions data.
    Raises:
        AssertionError: Raised if the DataFrame does not pass the integrity checks.
    """
    emissions_expected_columns = ['Year', 'Country_Name', 'CO2']
    check_column_names(emissions_df, emissions_expected_columns)
    check_null_values(emissions_df, emissions_df.columns)


def check_deforestation_data_table(deforestation_df):
    """
    Validates the structure and integrity of a DataFrame containing deforestation data.
    Args:
        deforestation_df (pandas.DataFrame): The DataFrame containing emissions data.
    Raises:
        AssertionError: Raised if the DataFrame does not pass the integrity checks.
    """
    deforestation_expected_columns = ['Year', 'Deforested_Area']
    check_column_names(deforestation_df, deforestation_expected_columns)
    check_null_values(deforestation_df, deforestation_df.columns)

class TestDataPipeline(unittest.TestCase):
    """
    A test case class designed for validating the data pipeline.
    This class includes methods to verify the pipeline's execution 
    and ensure the integrity of the resulting data files and database tables.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment by executing the data pipeline.
        """
        main()

    def test_output_files_exist(self):
        """
        Checks the existence of expected output files and tables.
        This test verifies that the database file and 
        required tables are present following the execution of the data pipeline.
        """
        # Check if the database file exists
        db_file = 'data/brazil_amazon_deforestation_and_wildfire_and_emission_data.db'
        self.assertTrue(os.path.isfile(db_file), f"Database file '{db_file}' does not exist")

        # Check if the tables exist within the database
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            tables = [table[0] for table in tables]

        expected_tables = ['amazon_merged_data', 
                           'deforestation_data', 
                           'wildfire_burned_area_data', 
                           'wildfire_emissions_data']
        for table in expected_tables:
            self.assertIn(table, tables, f"The table '{table}' does not exist in the database")
        print("Test output_files_exist passed successfully.")

    def test_pipeline_execution(self):
        """
        Validates the execution of the data pipeline.
        This test runs the entire pipeline, encompassing data loading, 
        transformation, and validation, and ensures that the resulting 
        data tables adhere to the expected structure and integrity standards.
        """
        username = "azamkhattak"
        key = "3932ac8e3dca141cad0d6841bd395cc8"
    #   kaggle_extract_Data(username, key)
        deforestation_df = kaggle_extract_Data(username, key)
        
    #   URLs for wildfire and emissions data files to download
    #   The URL for deforestation data is set above in the function already
        wildfire_url = "https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/MCD64A1_burned_area_full_dataset_2002-2023.zip"
        emissions_url = "https://effis-gwis-cms.s3.eu-west-1.amazonaws.com/apps/country.profile/emission_gfed_full_2002_2023.zip"
        
    #   Download and extract wildfire and emissions data in memory
        wildfire_files = download_and_extract_in_memory(wildfire_url)
        emissions_files = download_and_extract_in_memory(emissions_url)
        
    #   Specify file paths for the CSV files within the extracted wildfire and emissions data
    #   The path for deforestation data is set above in the function already
        wildfire_file_like = wildfire_files['MCD64A1_burned_area_full_dataset_2002-2023.csv']
        emissions_file_like = emissions_files['emission_gfed_full_2002_2023.csv']
        
        wildfire_df = load_and_clean_data(wildfire_file_like)
        emissions_df = load_and_clean_data(emissions_file_like)
        
    #   Transform the deforestation, wildfire and emissions data
        wildfire_df = transform_wildfire_data(wildfire_df).copy()
        emissions_df = transform_emissions_data(emissions_df).copy()
        deforestation_df = transform_deforestation_data(deforestation_df).copy()
            
        # Check wildfire data table
        check_wildfire_data_table(wildfire_df)

        # Check emissions data table
        check_emissions_data_table(emissions_df)

        # Check deforestation data table
        check_deforestation_data_table(deforestation_df)
        
        print("Test of executing the pipeline passed successfully.")

if __name__ == '__main__':
    unittest.main()