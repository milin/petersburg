#! /usr/bin/env python
#
# Copyright (c) 2010 Okoye Chuka D.<okoye9@gmail.com>      
#                    All rights reserved.
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
 
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from thrift import Thrift
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from cassandra import Cassandra
from cassandra.ttypes import *
import time
import tweepy
import Logger as logger

class CassandraStorage:
   def __init__(self, keyspace="Twitter"):
      self.socket = TSocket.TSocket("localhost",9160)
      self.transport = TTransport.TBufferedTransport(self.socket)
      self.protocol = \
      TBinaryProtocol.TBinaryProtocolAccelerated(self.transport)
      self.client = Cassandra.Client(self.protocol)
      self.keyspace = keyspace

   def store(self,column_family=None,key=None, column=None, value=""):
      if not column_family or key or column:
         logger.subsection("WARN: no column_family, key or column specified")
         return
      column_path = ColumnPath(column_family=column_family,column=column)
      try:
         self.transport.open()
         self.client.insert(self.keyspace, key, column_path, value,\
                           time.time(),ConsistencyLevel.ONE)
      except Thrift.TException, tex:
         logger.subsection("WARN: thrift error "+tex.message)
      finally:
         transport.close()
