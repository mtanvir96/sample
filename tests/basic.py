
from flask import Flask, Response
import requests
import unittest
import re

# Sample output of the rest API
#
# sample_external_url_up{url="https://httpstat.us/200"} = 1
# sample_external_url_response_ms{url="https://httpstat.us/200"} = 314.279
# sample_external_url_up{url="https://httpstat.us/503"} = 0
# sample_external_url_response_ms{url="https://httpstat.us/503"} = 102.471

class Testing(unittest.TestCase):
    
    URL = 'http://localhost:5001/metric'
    CONTENT_TYPE = str('text/plain; version=0.0.4; charset=utf-8')

    LINE0 = 'sample_external_url_up{url="https://httpstat.us/200"} = 1'
    LINE1 = 'sample_external_url_response_ms{url="https://httpstat.us/200"} = ([0-9]*[.])?[0-9]*'
    LINE2 = 'sample_external_url_up{url="https://httpstat.us/503"} = 0'
    LINE3 = 'sample_external_url_response_ms{url="https://httpstat.us/503"} = ([0-9]*[.])?[0-9]*'

    def test_basic(self):
        response = requests.get(self.URL)
        if response.status_code == 200:
            
            lines = response.text.split('\n')

            # Verify the number of lines in the response
            self.assertEqual(len(lines), 4)

            # Verify the lines with = 1 and = 0
            self.assertEqual(lines[0], self.LINE0) 
            self.assertEqual(lines[2], self.LINE2)
            
            # Verify the lines with response time
            z = re.match(self.LINE1, lines[1])
            assert z is not None
            z = re.match(self.LINE3, lines[3])
            assert z is not None

if __name__ == '__main__':
    unittest.main()