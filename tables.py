from flask_table import Table, Col

class Results1(Table):
    symbol = Col('Symbol')
    volume = Col('Volume')

class Results2(Table):
    symbol = Col('Symbol')
    count = Col('Trade')    

class Results3(Table):
    symbol = Col('Symbol')
    value = Col('Total Notional Value')

class Results4(Table):
    symbol = Col('Symbol')
    spread = Col('Price Spread')