#!/usr/bin/env python3

from sqlite_connector import SQLiteConnector

sqlite_connector = SQLiteConnector('openportals.db')
sqlite_connector.execute_transform('init.sql')
