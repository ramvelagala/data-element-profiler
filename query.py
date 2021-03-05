import configparser
from grp_bank_dq_engine_dindu.netezza import NetezzaClient
table = 'DBKDMDB.ADMIN.B_BCL_CU_TOTAL_LOSS'

config = configparser.ConfigParser()
config.read('database_logins.ini')

args = dict(config.items('dbdetails'))
    # connect to database
client = NetezzaClient(**args)

queries = dict(
    query_total_rows='select count(*) as Total_Rows from {0}',
    query_cardinality='select count(distinct {1}) as cardinality from {0} limit 50',
    query_non_null="select count({1}) as non_null from {0} ",
    num_not_null=""
)


# list = [tot_rows,cardinlaity ]
#
# for query_type, query in queries.items():
#     result = pd.to_sql(query.format(db_name, schema, table_name), connection)

query_total_rows = "select count(*) as Total_Rows from {0}".format(table)

for _ in query_total_rows:
    print(_)


client.connection.sql(query_total_rows)
client.connection.close()



query_cardinality = 'select count(distinct {0}) as cardinality from {1}.{2}.{3} limit 50'.format(
    column_name, db_name, schema, table_name)
perc_of_Cardinality = "select count(distinct {0})/count(*) as perc_cardinality from {1}.{2}.{3} \
limit 50;".format(column_name, db_name, schema, table_name)
query_non_null = "select count({0}) as non_null from {1}.{2}.{3}".format(column_name, db_name,
                                                                         schema, table_name)
num_null_values = "select count(*)-count({0}) as non_null from {1}.{2}.{3}".format(column_name,
                                                                                   db_name, schema,
                                                                                   table_name)
query_min_value = "select min({0}) as Min_Value from {1}.{2}.{3}".format(column_name, db_name,
                                                                         schema, table_name)
query_max_value = "select max({0}) as Min_Value from {1}.{2}.{3}".format(column_name, db_name,
                                                                         schema, table_name)
# todo median_value
query_least_frequent_value_and_freq = "select {0}, count(*) from 1}.{2}.{3} group by {0} order by count(*) \
limit 1;".format(column_name, db_name, schema, table_name)
# todo dask least_frequent_value_freq_perc =  (least_frequent_value_and_freq/Total_rows)*100
query_highest_frequent_value_and_freq = "select {0}, count(*) from {1}.{2}.{3} group by {0} by count(*)\
desc limit 1;".format(column_name, db_name, schema, table_name)
# todo dask least_frequent_value_freq_perc =  (least_frequent_value_and_freq/Total_rows)*100
# todo top and bot 25% values count and percent too.

##META DATA###
query_meta_data = "select *  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)

query_data_type = "select DATA_TYPE  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_char_max_len = "select CHARACTER_MAXIMUM_LENGTH  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_num_precision = "select NUMERIC_PRECISION  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_num_scale = "select NUMERIC_SCALE  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_nullability = "select IS_NULLABLE  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
##Defined
query_dec_data_type = "select DECLARED_DATA_TYPE  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_dec_num_precision = "select DECLARED_NUMERIC_PRECISION  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
query_dec_num_scale = "select DECLARED_NUMERIC_SCALE  from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}.{2}.{3}' \
AND COLUMN_NAME = '{0}'".format(column_name, db_name, schema, table_name)
