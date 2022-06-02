#!/usr/bin/env python3

from inspect import currentframe
import re



class Scraping_utilities:

  @staticmethod
  def __parse_name(string):
    try:
      return string.split("(")[0].strip()
    except Exception as ex:
      print("Error on line no: {}".format( ex))

  @staticmethod
  def __extract_digits(string):
    try:
      return int(re.search(r'\d+', string).group(0))
    except Exception as ex:
      print("Error on line no.: {}".format( ex))
