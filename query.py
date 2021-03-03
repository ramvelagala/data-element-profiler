tab_name = ""
col_name = ""
schema = ""
db_name = ""
statement_1 ="from "+db_name+"."+schema+"."+tab_name
statement_2 = ""

query_total_rows = "select count(*) as Total_Rows from "+db_name+"."+schema+"."+tab_name
Total_Rows = select_netezza(query_total_rows)
query_cardinality = "select count(distinct") as cardinality from PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY  limit
    50;
    "


Cardinality = select_netezza()
% _of_Cardinality = (Cardinality / Total_Rows) * 100
query_non_null = "select count(UNIQ_ACCT_IND_QTY) as non_null from
PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY;
"
num_non_nul1_values = select_netezza(query_non_null)
num_null_values = Total_Rows - query_non_null
query_min_value = "select min(UNIQ_ACCT_IND_QTY) as Min_Value from
PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY;
"
min_value = select_netezza(query_min_value)
query_max_value = "select max(UNIQ_ACCT_IND_QTY) as Max_Value from
PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY;
"
max_value = select_netezza(query_max_value)
median_value = Total_Rows.mean()
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
