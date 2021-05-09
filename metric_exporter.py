from prometheus_client import start_http_server, Metric
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import json
import requests
import sys
import time

class JsonCollector(object):
  def __init__(self, endpoint):
    self._endpoint = endpoint
    
  def collect(self):
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8')[5:])
    list_of_metrics = response["value"]

    for key in list_of_metrics:
      g = GaugeMetricFamily("symbol_spread_delta", 'Get the Price Spread and Delta.', labels=['symbol'])
      g.add_metric([str(key['symbol'])], key['spread'], key['delta'])
      yield g


if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(8080)
  REGISTRY.register(JsonCollector(sys.argv[1]))

  while True: time.sleep(1)