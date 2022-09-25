
import talib
import inspect
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

app = FastAPI()

functions = talib.get_functions()

@app.get('/method')
def return_function_groups():
    grp =  talib.get_function_groups()
    del grp['Math Operators']
    del grp['Math Transform']
    return grp

@app.get('/method/{method}')
def return_help(method:str):
    try:
        doc =  eval(f'talib.{method.upper()}.__doc__')
        return HTMLResponse(doc)
    except:
        raise HTTPException(status_code=404)


    
    
    
    