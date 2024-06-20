import requests
import pandas as pd
import pulsedive
import sqlalchemy as db

url = "https://pulsedive.com/api/info.php"
params = {
  "iid": "466961",
  "pretty": "1",
  "sanitize": "1",
  "key": "d4e44dd77337a590f4cba0b00e7569cdc251045c54a7f5bc8b0831b631e91c5c"
}


response = requests.get(url, params = params)

info_dict = response.json()

df = pd.DataFrame.from_dict(info_dict)

engine = db.create_engine('sqlite:///pulsedive.db')
df.to_sql('information', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM information;")).fetchall()
   print(pd.DataFrame(query_result))