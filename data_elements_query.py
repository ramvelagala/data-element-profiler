import pandas as pd
import re
import os

print(os.getcwd())
df = pd.read_csv("test_values.csv")
data_main = df["loan_amount"]
# print(df.head())
#one column -data-main
col_names = list(df.columns)




# from .utils import sql_connector

'''
def connect_netezza(query):
    """
    Tests netezza connections
    """
    netezza = sql_connector('NETEZZA')
    df = pd.read_sql(query, netezza)
    return df


query1 = "select * from example database "
query_main_test = "select UNIQ_ACCT_IND_QTY FROM PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY LIMIT 100;"
query_main = "select UNIQ_ACCT_IND_QTY FROM PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY ;"
query_metadata_defined = """SELECT NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS 
WHERE(TABLE_NAME = 'DBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY') AND(COLUMN_NAME = 'CC_VTG_AGG_MLY_SK');"""
data_main = connect_netezza(query_main)
data_meta = connect_netezza(query_metadata_defined)
'''


class DataQuery:

    def __init__(self):
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
        # self.num_prec = data_meta["NUMERIC_PRECISION"]
        # self.num_scale = data_meta["NUMERIC_SCALE"]
        # self.is_nullable = data_meta["IS_NULLABLE"]
        name = list(data_main.columns)[0]
        n = int(len(df)/4)
        self.bot_25_perc_unique = data_main.nsmallest(n, list(data_main.columns)[0]).iloc[:, 0].tolist()
        self.top_25_perc_unique = data_main.nlargest(n, list(data_main.columns)[0]).iloc[:, 0].tolist()

    @staticmethod
    def format_generation():
        res_list = []
        data1 = [str(num) for num in data_main]
        for num in data1:
            a = num.split('.')
            y = ''
            dd = re.sub(r'[^\w]', '', a[0])
            x = re.sub(r"\d+", len(dd) * '9', dd)
            # print(x)
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


'''
    def json_generation(self):
        data_set = data = {'metatadata':
                               {'length': '', 'precision': '',
                                }
                          }
    

if __name__ == '__main__':
    dataquery = DataQuery
    dataquery.connect_netezza(query1)
'''
