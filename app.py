from flask import Flask, Response, render_template, request, redirect
from tables import Results1, Results2, Results3, Results4
from forms import SearchForm
from solvers import Solve1, Solve2, Solve3, Solve4, Solve5
from datetime import datetime
from decimal import Decimal
from ddtrace import tracer

import json
import random
import time
import logging
import json_log_formatter
import threading

# Have flask use stdout as the logger
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)
logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

app = Flask(__name__)

@tracer.wrap(name='my_resource1', service='my_service1')
@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    my_thread= threading.currentThread().getName()
    logger.info('my_resource1 has executed',
        extra={
            'job_category': 'test_my_resource1',
            'logger.name': 'my_json',
            'logger.thread_name' : my_thread
        }
    )    

    return render_template('index.html', form=search)

@tracer.wrap(name='my_resource2', service='my_service2')
@app.route('/results')
def search_results(search):
    search_string = search.data['select']

    my_thread= threading.currentThread().getName()
    logger.info('my_resource2 has executed',
        extra={
            'job_category': 'test_my_resource2',
            'logger.name': 'my_json',
            'logger.thread_name' : my_thread
        }
    )
    
    ############### Q1 ###############
    if search_string == "1": 
        table = Results1(Solve1())
        table.border = True
        return render_template('hw1.html', table=table)

    ############### Q2 ###############
    elif search_string == "2":
        table = Results2(Solve2())
        table.border = True
        return render_template('hw2.html', table=table)    

    ############### Q3 ###############
    elif search_string == "3":
        table = Results3(Solve3())
        table.border = True
        return render_template('hw3.html', table=table) 

    ############### Q4 ###############
    elif search_string == "4":
        table = Results4(Solve4())
        table.border = True
        return render_template('hw4.html', table=table) 
    else:
        return redirect('/')


def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

@tracer.wrap(name='my_resource3', service='my_service3')
@app.route('/chart-data')
def chart_data():
    def time_delta_data():
        json_data = json.dumps(
            {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': Solve5()}, default=decimal_default_proc)
        yield f"data:{json_data}\n\n"
        time.sleep(10)
        
    my_thread= threading.currentThread().getName()
    logger.info('my_resource2 has executed',
        extra={
            'job_category': 'test_my_resource2',
            'logger.name': 'my_json',
            'logger.thread_name' : my_thread
        }
    )
    return Response(time_delta_data(), mimetype='text/event-stream')  
      
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)