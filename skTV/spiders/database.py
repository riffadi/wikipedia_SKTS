import sqlite3

conn =sqlite3.connect('sktv.db')
curr = conn.cursor()

curr.execute("""create table ktv_tb(
					title text,
					tv_network text,
					month_release text,
					rating text
	     		)""")

curr.execute("""insert into ktv_tb values('Python is awesome!', 'buildwithpython', 'python')""")

conn.commit()
conn.close()