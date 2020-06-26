"""
dbcommon
===

Provides `DBConnect` context manager, and `read` and `list_tables`.

Brief descriptions of classes and functions are given below. Further help can
be found for all classes, methods, and functions by typing `help` in an
interactive prompt. For instance, `help(dbcommon.read)` would provide more
detailed help on the `read` function, including some examples.

Class DBConnect
---------------
  A context manager to provide a safe connection to a remote MariaDB database.
  (MariaDB is the more fully open source version of MySQL.)

  As a context manager, you would use the "with paradigm":

  with DBConnect(connection_details_dict) as my_conn:
      df = pd.read_sql("SELECT * FROM my_table", conn)

  The `connection_details_dict` would look something like this:
  {
      'user': 'ds',
      'password': 'dlimi',
      'host': 'dlitraining.westeurope.azurecontainer.io',
      'port': 3306,
      'database': 'classicmodels'
  }

  If no `connection_dict` is provided, then the default is used, which creates a
  connection similar to what is shown above.


Function read
-------------
  Create a pandas dataframe by reading from a database connection. This can be done by
  providing just a table name or full SQL string.

  For example:

  df = read(table='products', rows=12)

  will create a pandas dataframe, using the default database connection.


Function list_tables
--------------------
  Create a pandas dataframe containing all of the tables in the database within the
  connection.

  For example:

  df = list_tables()

  will create a pandas dataframe, using the default database connection.

"""

__all__ = ["list_tables", "read", "DBConnect"]
__author__ = ("Mike Williamson", "mvw@kapacity.dk")
__version__ = "0.1.0"

from dbcommon.utils.dbconnect import DBConnect
from dbcommon.reading import read, list_tables

