import time
import json
import random
import os
import requests

import settings


class Character:
    race_dict = json.load(open("loads/race_dict.json"))
    race_list = list(race_dict)
    profession_dict = json.load(open("loads/profession_dict.json"))
    profession_list = list(profession_dict)
    btn_token = settings.BTN_TOKEN
    name_dict = {"dwarva":["cela","celm","iri"],
            "forged":["cor","eng","enga","jer","medi","wel"],
            "ghena":["bel","est"],
            "human":["gre","grea","grem"],
            "kirku":["geo","kaz","kyr"],
            "oread":["crs","ita","roma","romm","sar","sic"],
            "ravodit":["ava","bsh","che","cir","ing","oss","rus","tat"],
            "semayawi":["anci","astr","bibl","heb","theo"],
            "serin":["aze","kur","per"],
            "vadasj":["amh","eth","oro"],
            "vekiri":["ara","tur"],
            "volyri":["bre","fre","nrm","pcd","tah"],
            "wulfe":["dut","ger","gmca","lim","sax","sor"],
            "yuan":["chi","jap","kor","uyg"]}

    def __init__(self,owner,seed=None,character_dict=None):
        self.owner = owner
        self.seed = str(f"{owner}.{str(time.perf_counter_ns())[0:6]}")
        self.character_dict = {}

    def random(self):
        profession_seed = random.randint(0,len(self.profession_list)-1)
        profession = list(self.profession_dict.keys())[profession_seed]
        race_seed = random.randint(0,len(self.race_list)-1)
        race = list(self.race_dict.keys())[race_seed]
        region_list = self.name_dict[race]
        region_pos = random.randint(1,len(region_list)-1)
        region = region_list[region_pos]
        api_call = requests.get(f"https://www.behindthename.com/api/random.json?usage={region}&randomsurname=yes&key={self.btn_token}")
        stats_dict = {}
        name = api_call.json()["names"]
        firstname = name[0]
        surname = name[1]
        self.writeback("Name",f"{firstname} {surname}")
        attributes = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
        while attributes:
            for attribute in attributes:
                seed = self.seed + attribute
                random.seed(seed)
                die_roll = random.randint(1,6)
                stat_array = [die_roll,die_roll,die_roll,die_roll]
                del stat_array[stat_array.index(min(stat_array))]
                final_stat = sum(stat_array)
                stats_dict[attribute] = final_stat
                attributes.remove(attribute)
        else:
            self.writeback("Stats",stats_dict)
            self.writeback("Class",profession)
        self.writeback("Race",race)
    
    def build(self):
        return("It's not borked, but it will build!")
    
    def writeback(self,character_key,character_value):
        self.character_dict[f"{character_key}"] = character_value
