#!/usr/bin/env python
# coding: utf-8

'''This script will create a cookie cutter-ish folder strucutre and create a database to save the project data'''

# this chunk create the needed folders
import os
if not os.path.exists('./data'):
    os.mkdir('./data')
if not os.path.exists('./wrapper'):
    os.mkdir('./wrapper')
if not os.path.exists('./models'):
    os.mkdir('./models')

# this chunk create the database and create the tables we will need
import sqlite3
# Create de database
sqliteConnection = sqlite3.connect('./data/dtm_master_project.db')
cursor = sqliteConnection.cursor()

# Clean tables if exist
drop_table_query = 'DROP TABLE IF EXISTS raw_news;'
cursor.execute(drop_table_query)
drop_table_query = 'DROP TABLE IF EXISTS metrics;'
cursor.execute(drop_table_query)
drop_table_query = 'DROP TABLE IF EXISTS word_probabilities;'
cursor.execute(drop_table_query)

# This is the table that will store raw texts
create_table_query = "CREATE TABLE raw_news ( date DATE, id VARCHAR(1000) PRIMARY KEY, section VARCHAR(1000), title VARCHAR(1000), author VARCHAR(1000), raw_text VARCHAR(1000000));"
cursor.execute(create_table_query)

# This is the table that will store metrics
create_table_query = "CREATE TABLE metrics ( topics VARCHAR(1000), time_slice VARCHAR(1000), umass VARCHAR(1000), cv VARCHAR(1000), PRIMARY KEY(topics, time_slice));"
cursor.execute(create_table_query)

# This is the table that will store word probabilities
create_table_query = "CREATE TABLE word_probabilities ( month VARCHAR(2), probability VARCHAR(1000), word VARCHAR(1000), topic VARCHAR(1000), PRIMARY KEY(topic, month, word));"
cursor.execute(create_table_query)


sqliteConnection.commit()
sqliteConnection.close()

