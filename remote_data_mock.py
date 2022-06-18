# Copyright (c) 2019 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"

# installed libraries
import pandas as pd
# standard libraries
import time


class mock_data():
    def __init__(self):
        # self.df = pd.Series([])
        # self.df.name = "Time"

        self.df = pd.DataFrame([], columns=["Time", "Ory"])
        self.df.index = self.df["Time"]
        self.number = 1

    def get_data(self):
        time.sleep(1)
        now = pd.Timestamp.now()
        # self.df = pd.concat([self.df, pd.Series([self.number])])
        new_df = pd.DataFrame([[now, self.number]], columns=["Time", "Ory"])
        new_df.index = new_df["Time"]
        print('====')
        print(new_df)
        print('====')
        self.df = pd.concat([self.df, new_df])
        self.number += 1
        # print(f"shape: {self.df.shape}, {self.df.shape[1]}")
        # self.df.insert(self.df.shape[1], 0, self.number)
        # print(self.df)


