"""
TODO: Add Documentation
"""

from pandas import read_sql

from dbcommon.utils.dbconnect import TRAINING, DBConnect


def read(connect_dict=None, table=None, query=None, rows=None):
    """Read """
    if connect_dict is None:
        connect_dict = TRAINING
    if (table is None) and (query is None):
        raise ValueError("Either 'query' or 'table' must be passed.")
    if query is None:
        limit_str = f" LIMIT {rows}" if rows is not None else ""
        query = f"SELECT * FROM {table}{limit_str};"
    with DBConnect(connect_dict) as conn:
        return read_sql(query, conn)


def list_tables(connect_dict=None, full=False):
    if connect_dict is None:
        connect_dict = TRAINING
    full_str = "FULL" if full else ""
    with DBConnect(connect_dict) as conn:
        return read_sql(f"SHOW {full_str} TABLES;", conn)

