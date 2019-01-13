from os import environ
from requests import exceptions
from api_config import api

MAX_RETRIES = os.environ.get('RESTREAM_MAX_RETRIES', 10)

if __name__ == '__main__':
    print "Restreaming alooma queue."
    for _ in range(MAX_RETRIES)::
        try:
            api.start_restream()
            print "Successfully restreamed alooma queue."
        except requests.exceptions.Timeout as e:
            print e
            print "Retrying..."
            continue
        except Exception as e:
            print e
        else:
            break
