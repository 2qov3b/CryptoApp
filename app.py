from flask import Flask, Response, render_template, request, redirect
from tables import Results1, Results2, Results3, Results4
from forms import SearchForm
from solvers import Solve1, Solve2, Solve3, Solve4, Solve5
from datetime import datetime
from decimal import Decimal

import json
import random
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    search_string = search.data['select']
    
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

@app.route('/chart-data')
def chart_data():
    def time_delta_data():
        json_data = json.dumps(
            {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': Solve5()}, default=decimal_default_proc)
        yield f"data:{json_data}\n\n"
        time.sleep(10)
        
    return Response(time_delta_data(), mimetype='text/event-stream')  
      
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)