'''
A Library of useful pandas helper functions
SOLUTION FILE!!!!
'''
import pandas as pd

def get_column_names(df: pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df.
    Returns the names as a list of strings.
    '''
    return df.columns.tolist()

def get_columns_of_type(df: pd.DataFrame, numpy_type: type) -> list[str]:
    '''
    Return the column names where values match the given numpy type.
    '''
    return [col for col in df.columns if df[col].dtype == numpy_type]

def get_unique_values(df: pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values from a column.
    Raises KeyError if column_name does not exist.
    '''
    if column_name not in df.columns:
        raise KeyError(f"Column '{column_name}' not found in DataFrame.")
    return df[column_name].unique().tolist()

def get_file_extension(file_path: str) -> str | None:
    '''
    Return the file extension (e.g., 'csv', 'xlsx') or None if no extension.
    '''
    parts = file_path.split('.')
    return parts[-1] if len(parts) > 1 else None

def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas DataFrame based on its extension.
    Supported extensions: csv, xlsx, json.
    Raises ValueError for unsupported extensions or invalid files.
    '''
    try:
        if ext == 'csv':
            return pd.read_csv(file_path, header=0)
        elif ext == 'xlsx':
            return pd.read_excel(file_path)
        elif ext == 'json':
            return pd.read_json(file_path, orient='records')
        else:
            raise ValueError(f"Unsupported file extension: '{ext}'")
    except Exception as e:
        raise ValueError(f"Failed to load file: {str(e)}")

if __name__ == '__main__':
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
    })
    
    print(f"Columns: {get_column_names(df)}")
    print(f"Object Columns: {get_columns_of_type(df, 'object')}")
    print(f"Int64 Columns: {get_columns_of_type(df, 'int64')}")
    print(f"Float64 Columns: {get_columns_of_type(df, 'float64')}")
    print(f"Unique States: {get_unique_values(df, 'state')}")
