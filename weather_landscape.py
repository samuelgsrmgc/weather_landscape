import os
from PIL import Image

from p_weather.openweathermap import OpenWeatherMap
from p_weather.draw_weather import DrawWeather
from p_weather.configuration import WLBaseSettings

import secrets


class WeatherLandscape:


    def __init__(self,configuration:WLBaseSettings):
        self.cfg = configuration
        assert self.cfg.OWM_KEY != "000000000000000000",  "Set OWM_KEY variable to your OpenWeather API key in secrets.py"


    def MakeImage(self)->Image:

        owm = OpenWeatherMap(self.cfg)
        owm.FromAuto()

        img = Image.open(self.cfg.TEMPLATE_FILENAME)
        art = DrawWeather(img,self.cfg)
        img = art.Draw(owm)

        return img


    def SaveImage(self)->str:
        img = self.MakeImage() 
        placekey = OpenWeatherMap.MakePlaceKey(self.cfg.OWM_LAT,self.cfg.OWM_LON)
        outfilepath = self.MakeFilePath(self.cfg.OUT_FILENAME+placekey+self.cfg.OUT_FILEEXT)
        img.save(outfilepath) 
        return outfilepath
        
        

    def MakeFilePath(self,filename):
        return os.path.join(self.cfg.WORK_DIR,filename)