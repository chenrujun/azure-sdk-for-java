# coding=utf-8
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath, sep, pardir

cwd = dirname(realpath(__file__))
root = realpath(join(cwd , pardir, pardir, pardir, pardir, pardir))
sys.path.append(join(root, "ClientRuntimes" , "Python", "msrest"))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyString"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from auto_rest_swagger_bat_service import (
    AutoRestSwaggerBATService, 
    AutoRestSwaggerBATServiceConfiguration)

from auto_rest_swagger_bat_service.models.enums import *

class StringTests(unittest.TestCase):

    def test_string(self):

        config = AutoRestSwaggerBATServiceConfiguration(base_url="http://localhost:3000")
        config.log_level = 10
        client = AutoRestSwaggerBATService(config)

        self.assertIsNone(client.string.get_null())
        client.string.put_null(None)
        self.assertEqual("", client.string.get_empty())
        client.string.put_empty("")
        
        test_str = ("\xe5\x95\x8a\xe9\xbd\x84\xe4\xb8\x82\xe7\x8b\x9b\xe7\x8b"
                    "\x9c\xef\xa7\xb1\xef\xa4\xac\xef\xa7\xb1\xef\xa8\x8c\xef"
                    "\xa8\xa9\xcb\x8a\xe3\x80\x9e\xe3\x80\xa1\xef\xbf\xa4\xe2"
                    "\x84\xa1\xe3\x88\xb1\xe2\x80\x90\xe3\x83\xbc\xef\xb9\xa1"
                    "\xef\xb9\xa2\xef\xb9\xab\xe3\x80\x81\xe3\x80\x93\xe2\x85"
                    "\xb0\xe2\x85\xb9\xe2\x92\x88\xe2\x82\xac\xe3\x88\xa0\xe3"
                    "\x88\xa9\xe2\x85\xa0\xe2\x85\xab\xef\xbc\x81\xef\xbf\xa3"
                    "\xe3\x81\x81\xe3\x82\x93\xe3\x82\xa1\xe3\x83\xb6\xce\x91"
                    "\xef\xb8\xb4\xd0\x90\xd0\xaf\xd0\xb0\xd1\x8f\xc4\x81\xc9"
                    "\xa1\xe3\x84\x85\xe3\x84\xa9\xe2\x94\x80\xe2\x95\x8b\xef"
                    "\xb8\xb5\xef\xb9\x84\xef\xb8\xbb\xef\xb8\xb1\xef\xb8\xb3"
                    "\xef\xb8\xb4\xe2\x85\xb0\xe2\x85\xb9\xc9\x91\xee\x9f\x87"
                    "\xc9\xa1\xe3\x80\x87\xe3\x80\xbe\xe2\xbf\xbb\xe2\xba\x81"
                    "\xee\xa1\x83\xe4\x9c\xa3\xee\xa1\xa4\xe2\x82\xac".decode('utf-8'))

        self.assertEqual(test_str, client.string.get_mbcs())
        client.string.put_mbcs(test_str)

        test_str = "    Now is the time for all good men to come to the aid of their country    "
        self.assertEqual(test_str, client.string.get_whitespace())
        client.string.put_whitespace(test_str)
        
        self.assertIsNone(client.string.get_not_provided())
        self.assertEqual(Colors.redcolor, client.enum.get_not_expandable())
        client.enum.put_not_expandable(Colors.redcolor)


if __name__ == '__main__':
    unittest.main()