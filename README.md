# Primary Coding Challenge Usecase

## Description

This repository contains a solution for a primary coding challenge use case. The challenge involves working with a SQLite database (`Chinook_Sqlite.sqlite.db`), json (`array-of-nested-objects.py`) and csv (`business-employment-data.csv`) file. Based on this file, data transformation logic is performed using Python.

## Files

- `Chinook_Sqlite.sqlite.db`: This is the SQLite database file provided for the challenge. The database can be found [here](https://github.com/sakthi-reema/Primary-Coding-Challenge-Usecase/blob/main/Chinook_Sqlite.sqlite.db).
- `sqlite.py`: Contains Python code that creates a new table in the SQLite database by applying transformation logic. The code can be found [here](https://github.com/sakthi-reema/Primary-Coding-Challenge-Usecase/blob/main/sqlite.py).
- `array-of-nested-objects.py`: This Python script utilizes the path constructor to extract matching data from each object in an array. The code can be found [here](https://github.com/sakthi-reema/Primary-Coding-Challenge-Usecase/blob/main/array-of-nested-objects.py).
- `employee-data.py`: Using csv file, transformation logic is applied and created a new table based on that. Then, the table is converted to dataframe and write that in sql. The code can be found [here](https://github.com/sakthi-reema/Primary-Coding-Challenge-Usecase/blob/main/employee-data.py).

## Usage

1. Clone the repository:

    ```
    git clone https://github.com/sakthi-reema/Primary-Coding-Challenge-Usecase.git
    ```

2. Navigate to the repository directory:

    ```
    cd Primary-Coding-Challenge-Usecase
    ```

3. View SQLite database (`Chinook_Sqlite.sqlite.db`) using DBeaver.

4. View CSV file (`business-employment-data.csv`) using excel sheet.

5. Run the Python scripts (`sqlite.py`, `array-of-nested-objects.py` and `employee-data.py`) using a Jupiter notebook in Anaconda navigator.
