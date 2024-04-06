import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime as dt
import numpy as np
import pandas as pd
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

conn = sqlite3.connect('data.db')