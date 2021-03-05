"""Data Element Profiler main module,Argument -1 still needs to be passed."""


import configparser
import json
from grp_bank_dq_engine_dindu.netezza import NetezzaClient


list_tables = ('PBKGPDMDB.ADMIN.M_BFT_FC_TRN_FIX_TERM_MNTY',
               'PBKDMDB.ADMIN.M_BCC_FC_ACCT_DTL_MLY'
               'PBKDMDB.ADMIN.M_BCH_FC_MEM_DIGITAL_AGG',
               'PBKDMDB.ADMIN.M_BCC_FC_ACCT_AGG_MLY',
               'PBKDMDB.ADMIN.M_CPF_FC_MO_CNSMR_LOAN_ARGT_DTL',
               'PBKGPDMDB.ADMIN.M_BCC_DM_ARG_CREDIT_CARD',
               'PBKDMDB.ADMIN.M_BCH_FC_MASTER_CALL_AGG',
               'PBKGPDMDB.ADMIN.M_BDP_FC_TRN_TEXT_SAVINGS_TRAN',
               'PBKGPDMDB.ADMIN.M_BCC_DM_ORG_CRCD_SCORE',
               'PBKGPDMDB.ADMIN.M_BDP_FC_TRN_SAV_BOOST_TRAN',
               'PBKGPDMDB.ADMIN.M_BDP_DM_ARG_OVDF_FNDG',
               'PBKDMDB.ADMIN.M_BCL_CU_LOAN_FORECAST',
               'PBKGPDMDB.ADMIN.M_BDP_FC_TRN_TEXT_MSG_COMMAND',
               'PBKGPDMDB.ADMIN.M_BHL_DM_ARG_MTG_PII',
               'PBKGPDMDB.ADMIN.M_BCC_DM_ORG_CRCD_APP_FULM',
               'PBKDMDB.ADMIN.M_BCH_FC_VL_TAG_TRANS_DTL',
               'PBKDMDB.ADMIN.M_BDP_DM_TRANS_CHAR',
               'PBKDMDB.ADMIN.M_BCH_FC_MASTER_CALL_DTL',
               'PBKGPDMDB.ADMIN.M_BDP_FC_ARG_DEM_DEP_BAL_DLY',
               'PBKDMDB.ADMIN.M_BRK_CS_CC_LN_ORIG_DLY',
               'PBKDMDB.ADMIN.M_BRK_CS_CR_CARD_SVC_MLY',
               'PBKGPDMDB.ADMIN.M_BFT_DM_ARG_FIXED_TERM_DEP',
               'PBKGPDMDB.ADMIN.M_BDP_FC_TRN_DEM_DEP_MNTY',
               'PBKGPDMDB.ADMIN.M_BCC_FC_ARG_CRCD_BAL_DLY',
               'PBKGPDMDB.ADMIN.M_BDP_DM_ARG_DEMAND_DEP',
               'PBKGPDMDB.ADMIN.M_BHL_FC_ARG_MTG_BAL_DLY',
               'PBKDMDB.ADMIN.M_BCL_CU_APPLICATION_PACKAGE',
               'PBKGPDMDB.ADMIN.M_BDB_DM_ARG_DEBT_PROT_CLAIM_DTL',
               'PBKDMDB.ADMIN.M_BDP_FC_CHK_ACCT_DTL_MLY',
               'PBKGPDMDB.ADMIN.M_BHL_FC_ORG_MTG_LN_APP_EVENT',
               'PBKGPDMDB.ADMIN.M_BHL_DM_ARG_MORTGAGE_LN',
               'PBKGPDMDB.ADMIN.M_BDP_DM_ARG_TEXT_SAVINGS',
               'PBKDMDB.ADMIN.M_BNK_CU_FACTA_ALERT_CLAIMS',
               'PBKGPDMDB.ADMIN.M_BCL_FC_ARG_CSM_LN_BAL_DLY',
               'PBKDMDB.ADMIN.M_BDP_FC_CHK_ACCT_AGG_MLY',
               'PBKDMDB.ADMIN.M_BCP_FC_PROD_ACQ_MLY',
               'PBKDMDB.ADMIN.M_BCH_FC_VOICE_LINE_CALL_AGG',
               'PBKDMDB.ADMIN.M_BDP_FC_ACCT_DTL_MLY',
               'PBKDMDB.ADMIN.M_MDS_FC_AGENT_SCORE_AGG',
               'PBKDMDB.ADMIN.M_BCC_FC_APP_STATUS_AGG',
               'PBKGPDMDB.ADMIN.M_BCL_DM_ARG_CONSUMER_LOAN',
               'PBKGPDMDB.ADMIN.M_BDB_DM_ARG_DEBT_PROTECTION',
               'PBKGPDMDB.ADMIN.M_BCC_FC_ARG_CRCD_BAL_MLY',
               'PBKGPDMDB.ADMIN.M_BHL_FC_ORG_MTG_APP_STAT_EVT',
               'PBKDMDB.ADMIN.M_BDP_FC_PST_TRN_MER_AGG_MLY',
               'PBKGPDMDB.ADMIN.M_BCC_DM_ORG_CRCD_APPL',
               'PBKDMDB.ADMIN.M_BCL_CU_SERVICING_DTL',
               'PBKGPDMDB.ADMIN.M_BFT_FC_ARG_FIX_DEP_BAL_DLY',
               'PBKGPDMDB.ADMIN.M_BDP_DM_ARG_SAVINGS_BOOSTER',
               'PBKDMDB.ADMIN.M_BCH_FC_MEM_ACTIVE_MLY',
               'PBKGPDMDB.ADMIN.M_BCC_DM_ORG_CRCD_APP',
               'PBKGPDMDB.ADMIN.M_BHL_DM_ORG_MTG_LN_APP')


config = configparser.ConfigParser()
config.read('database_logins.ini')


def do_our_task(connection, table: str):
    """Get all "*SK*" elements of `table` that are an int* type.

    yeild {columnname, datatype}
    """
    query_2 = """
            select column_name, DATA_TYPE
            from INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '$table'
            AND COLUMN_NAME  LIKE '%_SK'
            AND DATA_TYPE IN ('INTEGER','SMALLINT','BIGINT');
            """

    for _ in connection.sql(query_2, dict(table=table)).itertuples():
        print(tuple(_)[1:])
        yield tuple(_)[1:]


def main():
    """Run from the cli."""
    # setup task from input
    args = dict(config.items('dbdetails'))
    # connect to database
    client = NetezzaClient(**args)
    with client.connection as connection:
        for table in list_tables:
            table = table.rpartition('.')[-1].strip()
            sk_elements = do_our_task(connection, table)
            print(json.dumps(dict(tablename=table,
                                  elements=[element_name for element_name, _ in
                                            sk_elements])))


main()
