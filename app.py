import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.utils import read_sql_data
import pandas as pd
import logging

# if __name__ == "__main__":
#     logging.info("The Execution has Started")

# try:
#     100/0

# except Exception as e:
#     logging.info("The Execution is starter")


df =read_sql_data()
df.to_csv("sqltables")


