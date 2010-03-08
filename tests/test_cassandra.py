#!/usr/bin/env python
#
#@author: Chuka Okoye
#Copyright info here
#
#

from thrift import Thrift
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from cassandra import Cassandra
from cassandra.ttypes import *
import time

def main():
   socket = TSocket.TSocket("localhost",9160)
   transport = TTransport.TBufferedTransport(socket)
   protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
   client = Cassandra.Client(protocol)
   keyspace = "Twitter"
   column_path = ColumnPath(column_family="Timeline",column="message")
   key = "pinggoat"
   value = " hello world!, my first cassandra input "
   timestamp = time.time()
   consistency = ConsistencyLevel.ONE
   column_parent = ColumnParent(column_family="Timeline")
   slice_range = SliceRange(start='',finish='')
   slice_predicate =SlicePredicate(column_names=["username","message", "time"])
   
   #Insert data into cassandra database with already defined schema

  # try:
  #    transport.open()
  #    client.insert(keyspace,key,column_path,value,timestamp,\
  #    ConsistencyLevel.ZERO)
  # except Thrift.TException, tex:
  #    print 'Thrift: %s' % tex.message
  # finally:
  #    transport.close()

   #Now retrieve data from cassandra database
   try:
      transport.open()
      start_key=finish_key=""
      row_count = 10000
      data = client.get_range_slice(keyspace,
                                       column_parent,
                                       slice_predicate,
                                       start_key,
                                       finish_key,
                                       row_count,
                                       ConsistencyLevel.ONE)
   except Thrift.TException, tex:
      print 'Thrift %s' % tex.message
   finally:
      transport.close()

if __name__ == '__main__':
   print "Running cassandra program\n"
   main()
