import os
import json
from dataclasses import dataclass
from typing import List,Tuple
import datetime


@dataclass
class WLHEntry:

    OPT_POSNAN = 0
    OPT_POSTOP = 1
    OPT_POSMID = 2
    OPT_POSBOT = 3

    OPT_POSTOP_STR = "pos_top"
    OPT_POSMID_STR = "pos_center"
    OPT_POSBOT_STR = "pos_bottom"
    
    

    date: str
    sprite: str
    index: int
    time: str
    options: str
    text: str


    def __str__(self):
        return "%02i.%02i %02i:%02i %s %s" % (self.day,self.month,self.hour,self.min,self.sprite,self.text)

    @property
    def hour(self):
        (h,m,s) = self.Split(self.time,":",(12,0,0)) 
        return h

    @property
    def min(self):
        (h,m,s) = self.Split(self.time,":",(12,0,0)) 
        return m
        
    @property
    def day(self):
        (d,m,y) = self.Split(self.date,".",(1,1,2000)) 
        return d

    @property
    def month(self):
        (d,m,y) = self.Split(self.date,".",(1,1,2000)) 
        return m
    
    @property    
    def optpos(self):    
        strs = [self.OPT_POSTOP_STR,OPT_POSMID_STR,OPT_POSBOT_STR]
        ints = [self.OPT_POSTOP,OPT_POSMID,OPT_POSBOT]
        assert len(strs) == len(ints)
        for i in range( len(strs)):
            if (self.options.contains(strs[i])):
                return ints[i]
        return self.OPT_POSNAN
        
        
    def Split(self,text:str,sep:str,default:Tuple):
        assert len(default) == 3
        s = text.split(sep)
        r = ()
        for i in range(3):
            if (i>=len(s)):
                v = default[i]
            else:
                try:
                    v = int(s[i])
                except ValueError:        
                    v = default[i]
            r = r + (v,)
        return r
            
            
    def MakeTime(self,t:datetime.datetime):
        return datetime.datetime(t.year,self.month, self.day, self.hour, self.min, 0, 0)
        



class WLHolidays(object):

    FILEPREFIX = "holiday"
    FILEEXT = ".json"
    
    
    data: List[WLHEntry]
    
    @staticmethod
    def from_json(json_str: str) -> "BirthdayData":
        obj = json.loads(json_str)
        entries = [Entry(**item) for item in obj.get("data", [])]
        return BirthdayData(title=obj["title"], data=entries)    
    

    def __init__(self,path:str=None):
        self.Load(path)
        
     
        
        
    def Reset(self):
        self.data = []
        
        
    def Load(self,path:str):
        self.Reset()
        if (path==None):
            path="."
 
        files = [fn for fn in os.listdir(path) if fn.startswith(self.FILEPREFIX) and fn.endswith(self.FILEEXT) ]
        for filename in files:
            filepath = os.path.join(path,filename)
            try:
                with open(filepath) as f:
                    obj = json.load(f)
                entries = [WLHEntry(**item) for item in obj.get("data", [])]
                self.data += entries
                title = obj.get("title", "Unknown")
                print("Loaded %i of '%s' from '%s'" % (len(entries),obj.get("title", "something"),filepath))               
            except:
                print("Holidays file '%s' load error" % filepath)
                continue
          
        
            
            
            
    def GetOne(self, t0 : datetime.datetime, t1: datetime.datetime) -> WLHEntry:   
        for e in self.data:
            t = e.MakeTime(t0) 
            r = (t!=None) and (t>=t0) and (t<t1)
            if r:
                return e
        return None
                
         

