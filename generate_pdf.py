from .connector import connect_netezza
from .data_elements_query import DataQuery
from .avro_schema import schema

def result():

    query_main_test = "select UNIQ_ACCT_IND_QTY FROM PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY LIMIT 10;"
    query_main = "select UNIQ_ACCT_IND_QTY FROM PBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY ;"
    # query_metadata_defined = "SELECT NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS WHERE(" \
    #                          "TABLE_NAME = 'DBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY') AND(COLUMN_NAME = " \
    #                          "'CC_VTG_AGG_MLY_SK'); "
    #for table
    data_main = connect_netezza(query_main)

    final_result = {}

    for i, j in data_main.iterrows():

        query_metadata_defined = ''' SELECT NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS WHERE(" \
        "TABLE_NAME =  'DBKDMDB.ADMIN.M_BRK_FC_CC_VTG_AGG_MLY') AND(COLUMN_NAME = " '''+ "'" + i + "'" + ");" ''' '''

        # print(query_metadata_defined)

        data_meta = connect_netezza(query_metadata_defined)
        query_data = DataQuery(data_main, data_meta)
        gen_format_items = query_data.format_generation(data_main)
        schema_gen = schema(query_data, gen_format_items)
        final_result[i] = schema_gen

    return final_result



