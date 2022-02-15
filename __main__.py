#!/usr/bin/env python3
import sqlite3

def main():
  con = sqlite3.connect("openportals.db")
  cur = con.cursor()
  for row in cur.execute("""
    select odp.portal_title, odp.api, odp.url
    from opendataportals as odp
    where odp.api like '%berlin%'
  """): print(row)
  con.commit()
  con.close()

if __name__ == '__main__':
  main()
