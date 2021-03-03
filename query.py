tab_name = ""
col_name = ""
schema = ""
db_name = ""
statement_1 ="from "+db_name+"."+schema+"."+tab_name
statement_2 = ""

query_total_rows = "select count(*) as Total_Rows from {0}.{1}.{2}".format(db_name, schema, tab_name)
query_cardinality = "select count(distinct {0}) as cardinality from {1}.{2}.{3} \
limit 50;".format(col_name, db_name,schema, tab_name)
perc_of_Cardinality = "select count(distinct {0})/count(*) as perc_cardinality from {1}.{2}.{3} \
limit 50;".format(col_name, db_name,schema, tab_name) 
query_non_null = "select count({0}) as non_null from {1}.{2}.{3}".format(col_name,db_name, schema, tab_name)
num_null_values = "select count(*)-count({0}) as non_null from {1}.{2}.{3}".format(col_name,db_name, schema, tab_name)
query_min_value = "select min({0}) as Min_Value from {1}.{2}.{3}".format(col_name,db_name, schema, tab_name)
query_max_value = "select max({0}) as Min_Value from {1}.{2}.{3}".format(col_name,db_name, schema, tab_name)
#median_value = Total_Rows.mean()
query_least_frequent_value_freq_perc = "select UNIQ_ACCT_IND_QTY, count(*)
from PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY group

by
UNIQ_ACCT_IND_QTY
order
by
count(*)
limit
1;
"
least_frequent_value = select_netezza(query_least_frequent_value_freq_perc)
query_highest_frequent_value_freq_perc = "select UNIQ_ACCT_IND_QTY, count(*)
from PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY group

by
UNIQ_ACCT_IND_QTY
order
by
count(*)
desc
limit
1;
"
highest_frequent_value = select_netezza(query_highest_frequent_value_freq_pe
rc)
