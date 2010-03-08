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

import getpass
import tweepy
import lib.TwitterLibrary as twitlib
import lib.Logger as logger

def main():
   username = raw_input("username: ")
   password = getpass.getpass("password: ")
   
   logger.initialize()

   stream = tweepy.Stream(username, password, twitlib.TwitterStream(),\
            timeout=6.0)

   stream.sample()

if __name__ == '__main__':
   main()

