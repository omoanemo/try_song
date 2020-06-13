
import pandas as pd
import requests
import json
import datetime
from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def main():

    url_1065 = 'https://graph.atimeonline.com/v5.5/playing/5?_=1592028949859'
    try:
        r = requests.get(url_1065, timeout=3)
        data = json.loads(r.text)
        song = [data['data']['audio']['title']]
        artist = [data['data']['audio']['description']]
    except:
        song = 'N/A'
        artist = 'N/A'
        
    columns = ['time','song','artist']
    df_data = {'time': [datetime.datetime.now()],
            'song':song,
            'artist': artist}
    df = pd.DataFrame(df_data, columns = columns)

    return str(df_data)

if __name__ == '__main__':
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=5000, debug=True) 