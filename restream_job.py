from os import environ
from requests import exceptions
from api_config import api

MAX_RETRIES = os.environ.get('RESTREAM_MAX_RETRIES', 10)

if __name__ == '__main__':
  print "Restreaming alooma queue."
  retries = 0

  while True:
      try:
          api.start_restream()
          print "Successfully restreamed alooma queue."
      except requests.exceptions.Timeout as e:
          print e
          if retries <= MAX_RETRIES
              "Retrying..."
              retries += 1
              continue
      except Exception as e:
          print e
      break
