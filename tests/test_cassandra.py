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
import datetime

def main():
   socket = TSocket.TSocket("localhost",9160)
   transport = TTransport.TBufferedTransport(socket)
   protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
   client = Cassandra.Client(protocol)
   keyspace = "Twitter"
   column_path = ColumnPath(column_family="Timeline")
   key = "pinggoat"
   value = " hello world!, my first cassandra input "
   timestamp = time.time()
   consistency = ConsistencyLevel.ONE
   column_parent = ColumnParent(column_family="Timeline")
   slice_range = SliceRange(start='',finish='')
   slice_predicate =SlicePredicate(slice_range)
   
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
      now = datetime.datetime.now()
      past = now - datetime.timedelta(minutes=5)
      start_key = str(time.mktime(past.timetuple()))
      finish_key = str(time.mktime(now.timetuple()))
      row_count = 100
 #     for x in range(int(time.mktime(past.timetuple())),
 #              int(time.mktime(now.timetuple()))):
 #        keys.append(str(x))   
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
