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

from lazyboy import *
from lazyboy.key import Key
from thrift import Thrift
import Logger as logger

connection.add_pool('Twitter',['localhost:9160'])

class CassandraStorage:
   def __init__(self, keyspace="Twitter",column_family=None):
      if(not column_family):
         logger.subsection("ERROR: no column family specified")
         return 
      self.keyspace = keyspace
      self.column_family = column_family
      return 

   #TODO: Create batch save to recordset
   def store(self,data):
      #Create Message
      message = Message(data)
      message.key = Key(keyspace=self.keyspace, 
                        column_family=self.column_family)

      #Store Message
      try:
         message.save()
      except:
         logger.subsection("ERROR: could not save to cassandra")

class Message(record.Record):
   def __init__(self, *args, **kwargs):
      record.Record.__init__(self, *args, **kwargs)
