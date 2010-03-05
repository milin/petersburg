#!/usr/bin/env python
#
#
#Copyright info here
#
#


import lazyboy
from thrift import Thrift
from cassandra import Cassandra
from cassandra.ttypes import *
import time

client = lazyboy.connection.Client(['localhost:9160'])

def main():
   keyspace = "Twitter"
   column_path = ColumnPath(column_family="Timeline",column="message")
   key = "pinggoat"
   value = "hello world!, my first cassandra input"
   timestamp = time.time()
   consistency = ConsistencyLevel.ONE
   try:
      client.insert(keyspace,key,column_path,value,timestamp,consistency)
   except Thrift.TException, tex:
      print 'Thrift: %s' % tex.message

if __name__ == ' __main__':
   main()
