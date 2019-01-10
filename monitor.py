import alooma
import datadog
import datetime
import os
import time
from api_config.py import api

DATADOG_API_KEY = os.environ.get('DATADOG_API_KEY')
MINUTES_SLEEP = int(os.environ.get('SLEEP_INTERVAL_MINUTES', '10'))
SECONDS_SLEEP = MINUTES_SLEEP * 60


datadog.initialize(api_key=DATADOG_API_KEY)


def posix_timestamp():
    d = datetime.datetime.now()
    return str(int(time.mktime(d.timetuple())))


def send_metric(data):
    for d in data:
        metric_name = "alooma.{}".format(d['target'].lower())
        values = d['datapoints']

        for x in values:
            x.reverse()

        for v in values:
            v[0] = str(v[0])
            if v[1] is None:
                print "Value is None. Not sending."
                continue
            v[1] = float(v[1])

        values = [tuple(x) for x in values]

        print metric_name
        print values

        for v in values:
            if v[1] is None:
                continue
            print v
            result = datadog.api.Metric.send(
                metric=metric_name,
                points=v,
                type='gauge',
            )
            yield result


metrics = alooma.METRICS_LIST


def record_metric(m):
    data = api.get_metrics_by_names(m, MINUTES_SLEEP)
    print "Sending {}".format(m)
    result = send_metric(data)

    for r in result:
        import pprint; pprint.pprint(r)


def record_all_metrics():
    for m in metrics:
        record_metric(m)


def record_num_inputs():
    inputs = api.get_inputs()
    num_inputs = len(inputs)
    result = datadog.api.Metric.send(
        metric='alooma.num_inputs',
        points=[(posix_timestamp(), num_inputs)],
        type='gauge',
    )


def record_restream_stats():
    restream_queue_size = api.get_restream_queue_size()
    datadog.api.Metric.send(
        metric='alooma.restreamable_events',
        points=[(posix_timestamp(), restream_queue_size)],
        type='gauge',
    )


if __name__ == '__main__':
    while True:
        try:
            record_all_metrics()
            record_num_inputs()
            record_restream_stats()
        except Exception as e:
            print e

        print "Monitor process sleeping for {}m".format(MINUTES_SLEEP)
        time.sleep(SECONDS_SLEEP)
