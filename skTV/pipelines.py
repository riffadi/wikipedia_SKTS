# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class SktvPipeline(object):

	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect("sktv.db")
		self.curr = self.conn

	def create_table(self):
		self.cursor.execute("""DROP TABLE IF EXISTS ktv_tb""")
		self.cursor.execute("""create table ktv_tb(
						title text,
						tv_network text,
						mont_release text,
						rating text
					)""")

    def process_item(self, item, spider):
    	self.store_db(item)
    	print("Pipline" + item['title'][0])
        return item

    def store_db(self):
    	self.curr.execute("""insert into ktv_tb values (?,?,?)(
    			item['title'][0],
    			item['tv_network'][0],
    			item['mont_release'][0],
    			item['rating'][0],
    		)""")
    	self.conn.commit()