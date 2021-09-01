# CryptoApp
A Flask app to show cryptocurrency trading data.

## Get Start!
1. Clone the repository
2. Create and active a virtualenv:
```console
$ python3.8 -m venv env
$ source env/bin/activate
```
3. Install dependencies:
```console
$ pip install -r requirements.txt
$ pip install prometheus-client
```
4. Run the Flask application:
```console
$ flask run
```
5. Open another new terminal and run Prometheus:
```console
// Get the metrics from '/chart-data' endpoint
$ python metric_exporter.py http://127.0.0.1:5000/chart-data
```
6. Confirmation:
Access to http://127.0.0.1:5000/
and you can find the page which every 10 seconds print the result of Q4 and the absolute delta from the previous value for each symbol.:
![Alt text](docs/answeringpage.png?raw=true "The chart shows answer to Q5 and Q1-Q4 by push the Answer button")

Q1:
![Alt text](docs/q1.png?raw=true "Print the top 5 symbols with quote asset BTC and the highest volume over the last 24 hours in descending order.")

Q2:
![Alt text](docs/q2.png?raw=true "Print the top 5 symbols with quote asset USDT and the highest number of trades over the last 24 hours in descending order.")

Q3:
![Alt text](docs/q3.png?raw=true "Using the symbols from Q1, what is the total notional value of the top 200 bids and asks currently on each order book?")

Q4:
![Alt text](docs/q4.png?raw=true "What is the price spread for each of the symbols from Q2?")

Access to http://127.0.0.1:8080/metrics
and get metrics like:
![Alt text](docs/metrics.png?raw=true "Make the output of Q5 accessible by querying http://localhost:8080/metrics using the Prometheus Metrics format.")
