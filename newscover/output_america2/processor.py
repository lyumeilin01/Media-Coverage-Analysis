import json
from pathlib import Path
import pandas as pd

def get_df(file_name):
  path1 = Path(__file__).parent / file_name
  source_name = []
  title = []
  description = []
  with open(path1, 'r') as file:
      data1 = json.load(file)
      #checked to see there are 100 articles in each file
      #print(len(data1))
      cap = len(data1)
      while i < cap:
          source_name.append(data1[i]["source"]["name"])
          title.append(data1[i]["title"])
          description.append(data1[i]["description"])
          i+=1
  df = pd.DataFrame({
      'src_name': source_name,
      'title': title,
      'description': description
  })
  return df

data = []

for i in range (0,1):
  df = get_df(f"swift_0.json")
  data.append(df)


print(data)
# final_df = pd.concat(data, ignore_index=True)
# print(final_df)

# excel_file_path = 'output_america.xlsx'
# final_df.to_excel(excel_file_path, index=False)