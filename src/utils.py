import json
import ast
import pandas as pd
import numpy as np

from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")


from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def ym_format(input_str, fmt):
    try: 
        output_dt = dt.strptime(str(input_str), fmt)
    except:
        output_dt = np.nan
    return output_dt


def create_ym_format(df, ym_col, fmt='%Y%m'):
    return df[ym_col].apply(lambda row: ym_format(row, fmt))


from math import ceil

def month_diff(start, end):
  try:
      return ceil((end - start).days / 30.5)
  except:
      return np.nan      


