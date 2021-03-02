from .utils import sql_connector
import pandas as pd


def connect_netezza(query):
    """Test netezza connections."""
    netezza = sql_connector('NETEZZA')
    df = pd.read_sql(query, netezza)
    return df

