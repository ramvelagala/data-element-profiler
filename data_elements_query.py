"""Data-profiling data-generator."""

import pandas as pd
import re

class DataQuery:
    """Class to get required fields in data-profiling."""

    def __init__(self, data_main, data_meta):
        """Init to to generate desired fields."""
        self.total_rows = len(data_main.axes[0])
        self.cardinality = len(pd.unique(data_main))
        self.perc_of_cardinality = (self.cardinality / self.total_rows) * 100
        self.num_null_values = data_main.isnull().sum()
        self.min_value = data_main.min()
        self.max_value = data_main.max()
        self.median_value = data_main.median()
        self.freq_highest_value = data_main.dropna().value_counts().idxmax()
        self.freq_highest_count = data_main.dropna().value_counts().max()
        self.freq_highest_perc = self.freq_highest_count / self.total_rows
        self.freq_lowest_value = data_main.dropna().value_counts().idxmin()
        self.freq_lowest_count = data_main.dropna().value_counts().min()
        self.freq_lowest_perc = self.freq_lowest_count / self.total_rows
        self.lowest_value = data_main.min()
        self.highest_value = data_main.max()
        self.median_value = data_main.median()
        self.num_prec = data_meta["NUMERIC_PRECISION"]
        self.num_scale = data_meta["NUMERIC_SCALE"]
        self.is_nullable = data_meta["IS_NULLABLE"]
        self.count_err = data_meta.where(data_meta == -1).count()
        self.count_err_perc = self.count_err/self.total_rows
        # num = data_main.columns[0]
        # n = int(len(df)/4)
        # self.bot_25_perc_unique = data_main.nsmallest(n, num).iloc[:, 0].tolist()
        # self.top_25_perc_unique = data_main.nlargest(n, num).iloc[:,0].tolist()

    @staticmethod
    def format_generation(data_main):
        """Generate general format of values in column."""
        res_list = []
        data1 = [str(num) for num in data_main]
        for num in data1:
            a = num.split('.')
            y = ''
            dd = re.sub(r'[^\w]', '', a[0])
            x = re.sub(r"\d+", len(dd) * '9', dd)
            if len(a) == 2:
                y = re.sub(r"\d+", len(a[1]) * '9', dd)
                y = '.' + y
            else:
                pass
            if a[0].startswith('-'):
                x = '-' + x
            res = x + y
            res_list.append(res)
        return list(set(res_list))


# if __name__ == '__main__':
#     connect_netezza(data_main)
