import os import environ
from time import sleep
from api_config.py import api

MINUTES_SLEEP = int(environ.get('RESTREAM_INTERVAL_MINUTES', '30'))
SECONDS_SLEEP = MINUTES_SLEEP * 60

if __name__ == '__main__':
    while True:
        try:
            api.start_restream()
        except Exception as e:
            print e

        print "Restream process sleeping for {}m".format(MINUTES_SLEEP)
        sleep(SECONDS_SLEEP)
