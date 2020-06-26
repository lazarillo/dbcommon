"""
TODO: Add Documentation
"""

from importlib import resources
from mariadb import connect
from toml import load

from dbcommon import config  # The *package* containing the config files

CONNECT_FILE = "connect.toml"  # Config file with database connection information
CONNECT = None
TRAINING = None
with resources.path(config, CONNECT_FILE) as connect_fh:
    CONNECT = load(connect_fh)
    TRAINING = CONNECT["training"]


class DBConnect:
    """Context manager to gracefully connect to a database.
    
    As a context manager, it allows for any connection with errors to rollback
    automatically and close, instead of leaving connections open."""

    def __init__(self, connection_dict=None):
        if connection_dict is None:
            connection_dict = TRAINING
        self.connection_dict = connection_dict
        self.connection = None

    def __enter__(self):
        self.connection = connect(**self.connection_dict)
        return self.connection

    def __exit__(self, mytype, val, traceback):
        if traceback is None:
            self.connection.commit()
        else:
            self.connection.rollback()
        self.connection.close()

