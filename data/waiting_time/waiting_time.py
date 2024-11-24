import torch
from torch.utils.data import DataLoader, Dataset
import torch.nn as nn
import torch.nn.functional as F

import torch
import os
import math
import json
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device

def getData(fileName):
    with open(fileName, 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    return data

class RNN(nn.Module):
  #nn.RNN
  def __init__(self, parameter):
    super().__init__()
    self.num_layers = parameter['num_layers']
    self.hidden_size = parameter['hidden_size']
    self.num_stacked_layers = self.num_layers
    self.bidirectional  = 2 if parameter['bidirectional'] else 1
    self.rnn = nn.GRU( parameter['input_size'], self.hidden_size, self.num_layers, batch_first=True, bidirectional = parameter['bidirectional'], dropout = parameter['dropout'])
    self.fc = nn.Linear(self.bidirectional * self.hidden_size, parameter['output_size'])

  def forward(self, x):
    batch_size = x.size(0)
    h0 = torch.zeros(self.bidirectional * self.num_layers, batch_size, self.hidden_size).to(device)

    out, _ = self.rnn(x, h0)
    #print(out.shape)
    out = self.fc(out[:, -1, :])
    return out

class RNN2(nn.Module):
  #nn.RNN
  def __init__(self, parameter):
    super().__init__()
    self.num_layers = parameter['num_layers']
    self.hidden_size = parameter['hidden_size']
    self.num_stacked_layers = self.num_layers
    self.bidirectional  = 2 if parameter['bidirectional'] else 1
    self.rnn = nn.GRU( parameter['input_size'], self.hidden_size, self.num_layers, batch_first=True, bidirectional = parameter['bidirectional'], dropout = parameter['dropout'])
    self.fc1 = nn.Linear(self.bidirectional * self.hidden_size, 1)
    self.fc2 = nn.Linear(2, 4)
    self.fc3 = nn.Linear(4, 1)

  def forward(self, x):
    batch_size = x.size(0)
    h0 = torch.zeros(self.bidirectional * self.num_layers, batch_size, self.hidden_size).to(device)

    outputs1 = model1(x)
    #x = torch.cat((x, outputs1), dim=2)

    #print('output1:', outputs1)
    #print('output1.shape()', outputs1.shape)
    out, _ = self.rnn(x, h0)
    out = out[:, -1, :]
    #print('output.shape', out.shape)
    out = self.fc1(out)
    out = torch.cat((out, outputs1), dim=-1)
    #print('after fc1 shape:', out.shape)
    #print('after fc1:', out)
    out = self.fc2(out)  # This should now work without shape errors
    #print('after fc2 shape:', out.shape)
    #print('after fc2:', out)
    out = self.fc3(out)
    #print('after fc3 shape:', out.shape)
    #print('after fc3:', out)
    return out

site_path = "sites/"
food_path = "food/"
model_path = "prediction_model/"


site_pt = getData(site_path + 'chiayi_site_popular_timeSpent.json')
site_pnt = getData(site_path + 'chiayi_site_popular_notimeSpent.json')
site_npt = getData(site_path + 'chiayi_site_nopopular_timeSpent.json')
site_npnt = getData(site_path + 'chiayi_site_nopopular_notimeSpent.json')

food_pt = getData(food_path + 'chiayi_food_popular_timeSpent.json')
food_pnt = getData(food_path + 'chiayi_food_popular_notimeSpent.json')
food_npt = getData(food_path + 'chiayi_food_nopopular_timeSpent.json')
food_npnt = getData(food_path + 'chiayi_food_nopopular_notimeSpent.json')

food_para1 = torch.load(model_path + food_path + 'model1.pt', map_location=torch.device('cpu'))
food_para2 = torch.load( model_path + food_path + 'newModel2.pt', map_location=torch.device('cpu'))
site_para1 = torch.load(model_path + site_path + 'model1.pt', map_location=torch.device('cpu'))
site_para2 = torch.load(model_path + site_path + 'newModel2.pt', map_location=torch.device('cpu'))

print(site_pt[0].keys())
print(site_pnt[0].keys())
print(site_npt[0].keys())
print(site_npnt[0].keys())

def getUnseenDataList(file_path):
    populartimes :list = []
    dayCount :list = []
    with open(file_path, 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
        for record in data:
            populartimeList = [record['populartimes'][i]['data'] for i in range(7) if sum(record['populartimes'][i]['data']) != 0]
            for i in range(len(populartimeList)):
                populartimes += populartimeList[i]
            dayCount.append(len(populartimeList))
    return populartimes, dayCount

class dataset(Dataset):
  def __init__(self, mode, X, y):
    assert mode in ['train', 'test', 'unseen']
    if mode == "train" and len(X) != len(y):
      print("Size error: len(X) != len(y)")
      return
    self.mode = mode
    self.x = torch.tensor(X, dtype=torch.float).reshape(-1, 24, 1)
    if self.mode == 'train' or self.mode == 'test':
      self.y = torch.tensor(y, dtype=torch.float)
    self.n = len(self.x)

  def __getitem__(self, index):
    if self.mode == 'train' or self.mode == 'test':
      return self.x[index], self.y[index]
    else:
      return self.x[index]

  def __len__(self):
    return self.n

"""# Predict the unseen data"""

def getUnseenPredictions(file_path, para1, para2):
  unseenData, dayCount = getUnseenDataList(file_path)
  unseenDataset = dataset('unseen', unseenData, None)
  model1_unseenLoader = DataLoader(dataset=unseenDataset, batch_size = para1['batch_size'], shuffle=False)
  model2_unseenLoader = DataLoader(dataset=unseenDataset, batch_size = para2['batch_size'], shuffle=False)

  with torch.no_grad():
    unseen_predictions = []
    outputs1 = torch.tensor([]).to(device)  # Initialize an empty tensor on the correct device
    outputs2 = torch.tensor([]).to(device)  # Initialize an empty tensor on the correct device
    for inputs in model1_unseenLoader:
      inputs = inputs.to(device)
      outputs1 = torch.cat((outputs1, model1(inputs)), dim=0)

    for inputs in model2_unseenLoader:
      inputs = inputs.to(device)
      outputs2 = torch.cat((outputs2, model2(inputs)), dim=0)

    unseen_day_predictions = torch.stack((outputs1, outputs2), dim=1).squeeze(-1)  # Combine outputs along a new dimension


    sites = 0
    index = 0



    while True:
      if sites == len(dayCount):
          break
      days = dayCount[sites]
      tmp = torch.tensor([0, 0], dtype=torch.float).to(device)
      for i in range(days):
          tmp += unseen_day_predictions[index]
          index += 1
      unseen_predictions.append((tmp / days).tolist())
      sites += 1
    return unseen_predictions

def postProcess(unseen_predictions):
  for predict_data in unseen_predictions:
    predict_data[0] =int(round(predict_data[0]))
    predict_data[1] = int(round(predict_data[1]))
  for i in range(len(unseen_predictions)):
    if unseen_predictions[i][0] > unseen_predictions[i][1]:
      tmp = unseen_predictions[i][0]
      unseen_predictions[i][0] = unseen_predictions[i][1]
      unseen_predictions[i][1] = tmp
  for predict_data in unseen_predictions:
    less, most = predict_data
    print(f"({less:}, {most:})")
  return unseen_predictions

def addTimeSpent(sites: list, timeSpent: list):
  assert len(sites) == len(timeSpent)
  for i in range(len(sites)):
    sites[i]['time_spent'] = timeSpent[i]

model1 = site_para1['best_q_model1'].to(device)
model2 = site_para2['best_q_newModel2'].to(device)

unseen_predictions = getUnseenPredictions(site_path + 'chiayi_site_popular_notimeSpent.json', site_para1, site_para2)
unseen_predictions = postProcess(unseen_predictions)
addTimeSpent(site_pnt, unseen_predictions)

model1 = food_para1['best_q_model1'].to(device)
model2 = food_para2['best_q_newModel2'].to(device)

unseen_predictions = getUnseenPredictions(food_path + 'chiayi_food_popular_notimeSpent.json', food_para1, food_para2)
unseen_predictions = postProcess(unseen_predictions)
addTimeSpent(food_pnt, unseen_predictions)


table = getData("dictData/table.json")
foodDict = dict()
for record in food_pt:
  if "food" not in record['types']:
      record['types'].append("food")
  foodDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}


for record in food_npt:
  if "food" not in record['types']:
      record['types'].append("food")
  foodDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}

for record in food_pnt:
  if "food" not in record['types']:
      record['types'].append("food")
  foodDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}

siteDict = dict()
for record in site_pt:
  if "site" not in record['types']:
      record['types'].append("site")
  siteDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}

for record in site_npt:
  if "site" not in record['types']:
      record['types'].append("site")
  siteDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}

for record in site_pnt:
  if "site" not in record['types']:
      record['types'].append("site")
  siteDict[table[record['name']]] = {'address': record['address'], 'rating': record['rating'] if 'rating' in record else None, 'time_spent': record['time_spent'], 'types': record['types']}

typeDict = dict()
for site in foodDict.values():
  for type_ in site['types']:
    if type_ not in typeDict:
      typeDict[type_] = {'time_spent': torch.tensor([site['time_spent']])}
    else:
      typeDict[type_] = {'time_spent': torch.cat((typeDict[type_]['time_spent'], torch.tensor([site['time_spent']])), 0)}

for site in siteDict.values():
  for type_ in site['types']:
    if type_ not in typeDict:
      typeDict[type_] = {'time_spent': torch.tensor([site['time_spent']])}
    else:
      typeDict[type_] = {'time_spent': torch.cat((typeDict[type_]['time_spent'], torch.tensor([site['time_spent']])), 0)}

average = [0, 0]
for type_ in typeDict.values():
  average[0] += type_['time_spent'][:,0].median().item()
  average[1] += type_['time_spent'][:,1].median().item()
average[0] /= len(typeDict)
average[1] /= len(typeDict)
average[0] = int(round(average[0]))
average[1] = int(round(average[1]))
average

for record in food_npnt:
  if "food" not in record['types']:
      record['types'].append("food")
  name = table[record['name']]
  foodDict[name] = {}
  foodDict[name] = {'address': record['address'], 'types': record['types']}
  foodDict[name]['rating'] = record['rating'] if  'rating' in record else None
  time_spent = [0, 0]
  type_num = 0
  for type_ in record['types']:
    if type_ not in typeDict:
      continue
    time_spent[0] += typeDict[type_]['time_spent'][:,0].median().item()
    time_spent[1] += typeDict[type_]['time_spent'][:,1].median().item()
    type_num += 1

  time_spent[0] /= type_num
  time_spent[1] /= type_num
  time_spent[0] = round(time_spent[0])
  time_spent[1] = round(time_spent[1])
  if type_num == 0:
    time_spent = average.copy()
  foodDict[name]['time_spent'] = time_spent

for record in site_npnt:
  if "site" not in record['types']:
      record['types'].append("site")
  name = table[record['name']]
  siteDict[name] = {}
  siteDict[name] = {'address': record['address'], 'types': record['types']}
  siteDict[name]['rating'] = record['rating'] if  'rating' in record else None
  time_spent = [0, 0]
  type_num = 0
  for type_ in record['types']:
    if type_ not in typeDict:
      continue
    time_spent[0] += typeDict[type_]['time_spent'][:,0].median().item()
    time_spent[1] += typeDict[type_]['time_spent'][:,1].median().item()
    type_num += 1
  time_spent[0] /= type_num
  time_spent[1] /= type_num
  time_spent[0] = round(time_spent[0])
  time_spent[1] = round(time_spent[1])
  if type_num == 0:
    time_spent = average.copy()
  siteDict[name]['time_spent'] = time_spent


print(len(foodDict))

print(len(siteDict))

# all_food = torch.empty(0,2) # initialize all_food as a 2D tensor with size (0, 2)
# for food in foodDict.keys():
  # all_food = torch.cat((all_food, torch.tensor([foodDict[food]['time_spent']])), 0)

# food_median = [round(all_food[:,0].median().item()), round(all_food[:,1].median().item())]
# print(food_median)
# foodDict['food_median'] = food_median

# all_site = torch.empty(0,2) # initialize all_site as a 2D tensor with size (0, 2)
# for site in siteDict.keys():
  # all_site = torch.cat((all_site, torch.tensor([siteDict[site]['time_spent']])), 0)

# site_median = [round(all_site[:,0].median().item()), round(all_site[:,1].median().item())]
# print(site_median)
# siteDict['site_median'] = site_median

# merged_dict = {**foodDict, **siteDict}
# Merge dictionaries with metadata
merged_dict = {}

for key, value in foodDict.items():
    merged_dict[key] = {**value, "metadata": {"type": "food"}}

for key, value in siteDict.items():
    merged_dict[key] = {**value, "metadata":{"type": "site"}}

# merged_dict['average'] = average

# Convert dictionary to JSON string
json_string = json.dumps(merged_dict, indent=4)  # Use indent for pretty-printing

# Print JSON string
# print(json_string)

# Save to a file
file_name = "sitesData_waiting.json"
with open( file_name , "w") as json_file:
    json.dump(merged_dict, json_file, indent=4)

with open( file_name , "r") as json_file:
    data = json.load(json_file)

# Print the loaded data
# print(data)

#siteDict[record['name']] = {'address': record['address'], 'rating': record['rating'], 'time_spent': record['time_spent'], 'types': record['types']}

