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
    background_dict = json.load(open("loads/background_dict.json"))
    background_list = list(background_dict)
    btn_token = settings.BTN_TOKEN
    name_dict = {
        "dwarva":["cela","celm","iri"],
        "forged":["cor","eng","enga","jer","wel"],
        "ghena":["bel","est"],
        "human":["gre","grea","grem"],
        "kirku":["geo","kaz","kyr"],
        "oread":["crs","ita","roma","romm","sar","sic"],
        "ravodit":["ava","bsh","che","cir","ing","oss","rus","tat"],
        "semayawi":["anci","astr","heb","theo"],
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
        skill_list = []
        tool_list = []
        language_list = ["Common"]
        # CLASS
        profession_seed = random.randint(0,len(self.profession_list)-1)
        profession = list(self.profession_dict.keys())[profession_seed]
        self.writeback("Class",profession)
        # RACE
        race_seed = random.randint(0,len(self.race_list)-1)
        race = list(self.race_dict.keys())[race_seed]
        self.writeback("Race",race)
        # NAME
        region_list = self.name_dict[race]
        region_pos = random.randint(1,len(region_list)-1)
        region = region_list[region_pos]
        api_call = requests.get(f"https://www.behindthename.com/api/random.json?usage={region}&randomsurname=yes&key={self.btn_token}")
        name = api_call.json()["names"]
        firstname = name[0]
        surname = name[1]
        self.writeback("Name",f"{firstname} {surname}")
        # BACKGROUND
        background_seed = random.randint(0,len(self.background_list)-1)
        background = list(self.background_dict.keys())[background_seed]
        bg_dict = self.background_dict[background]
        proficiencies = bg_dict["proficiencies"]
        skill_proficiencies = proficiencies["skill"]
        if list(skill_proficiencies.keys())[0] == "numberof":
            numberof = skill_proficiencies["numberof"]
            while numberof:
                skill_seed = random.randint(0,len(skill_proficiencies["possibles"])-1)
                skill_list.append(skill_proficiencies["possibles"][skill_seed])
                numberof -=1
            else:
                self.writeback("Skills",", ".join(skill_list))
        tool_proficiencies = proficiencies["tool"]
        if list(tool_proficiencies.keys())[0] == "numberof":
            numberof = tool_proficiencies["numberof"]
            while numberof:
                tool_seed = random.randint(0,len(tool_proficiencies["possibles"])-1)
                tool_list.append(tool_proficiencies["possibles"][tool_seed])
                numberof -=1
            else:
                self.writeback("Skills",", ".join(skill_list))
        self.writeback("Background",background)
        # STATS
        stats_dict = {}
        attributes = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
        while attributes:
            for attribute in attributes:
                die_results = self.die_roll(4,6,attribute,1)
                die_result_1 = die_results[0]
                die_result_2 = die_results[1]
                die_result_3 = die_results[2]
                die_result_4 = die_results[3]
                stat_array = [die_result_1,die_result_2,die_result_3,die_result_4]
                del stat_array[stat_array.index(min(stat_array))]
                final_stat = sum(stat_array)
                stats_dict[attribute] = final_stat
                attributes.remove(attribute)
        else:
            self.writeback("Stats",stats_dict)

    def die_roll(self,num,len,attribute,index):
        seed = self.seed + attribute + str(index)
        random.seed(seed)
        rolls_left = num
        die_results = []
        while rolls_left > 0:
            result = random.randint(1,len)
            die_results.append(result)
            rolls_left -= 1
        else:
            return die_results

    def build(self):
        return("It's not borked, but it will build!")
    
    def writeback(self,character_key,character_value):
        self.character_dict[f"{character_key}"] = character_value
