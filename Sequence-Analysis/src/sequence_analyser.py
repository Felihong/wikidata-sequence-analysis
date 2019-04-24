import os
import pandas as pd
from src import data
from src import activity


os.chdir('../data')
data_analyser = data.DataAnalyser('article_sample.csv')
data = data_analyser.data

activity_analyser = activity.ActivityAnalyser()
print(activity_analyser.key_activity(df=data, pred_level='B', succ_level='A'))







