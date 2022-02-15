#!/usr/bin/env python3
from sqlite3 import connect
from os import environ

for item, value in environ.items():
  print('{}: {}'.format(item, value))

def main():
  connection = connect(environ["DATABASE"])
  cursor = connection.cursor()
  for row in cursor.execute("""
    select odp.portal_title, odp.api, odp.url
    from opendataportals as odp
  """): print(row)
  connection.commit()
  connection.close()

if __name__ == "__main__":
  main()
