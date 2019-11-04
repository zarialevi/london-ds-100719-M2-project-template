# You don't have to use these classes, but we recommend them as a good place to start!

import os


class MongoHandler():
    
    def __init__(self, dbname,div):
        self.myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.myclient[dbname]
        self.collection= self.db[div]
   
   
    
    def create_doc(self, team_name, total_goals, total_wins, win_percentage):
        dic={}
        dic['Team_Name']= team_name 
        dic['total_goals']= total_goals
        dic['total wins']= total_wins
        dic['win_percentage']= win_percentage
        return self.collection.insert_one(dic)
            

class WeatherGetter():
    pass