import pandas as pd
import numpy as np
from datetime import datetime, timedelta

date_columns = ['property_scraped_at', 'host_since', 'reviews_first', 'reviews_last']
train_df = pd.read_csv("Assignment1/train.csv", parse_dates=date_columns)
test_df = pd.read_csv("Assignment1/test.csv", parse_dates=date_columns)

def string_to_int(input_var):
    return_number = 0
    if input_var[0] == 'a':
        return_number = 1
    else:
        return_number = int(input_var.split(" ",1)[0])    
    return return_number

last_updated_text = train_df.property_last_updated.unique()
#last_updated_text = np.array_str(last_updated_text)
my_list = []
for mytext in last_updated_text: 
    if "week" in mytext:
        xyz = string_to_int(mytext)
        datetime_date = timedelta(weeks=-xyz)
    elif "month" in mytext:
        xyz = string_to_int(mytext) * 4 + 2
        datetime_date = timedelta(weeks=-xyz)
    elif "days" in mytext:
        xyz = string_to_int(mytext)
        datetime_date = timedelta(days=-xyz)
    elif mytext == "yesterday":
        datetime_date = timedelta(days = -1)
    else:
        datetime_date = timedelta()
    my_list.append([mytext, datetime_date])

train_df['property_last_updated'] = train_df['property_last_updated'].apply(lambda x: dict(my_list)[x])
#train_df2['property_scraped_at'] = pd.to_datetime(train_df2['property_scraped_at'])
train_df['property_last_updated_dt'] = train_df['property_scraped_at'] + train_df['property_last_updated']

train_df['daypassed_since_lastreview'] = train_df['property_scraped_at'] - train_df['reviews_last']
train_df['daypassed_since_firstreview'] = train_df['property_scraped_at'] - train_df['reviews_first']

### just import the module to access train df
### from assignment1_preprocessing import train_df