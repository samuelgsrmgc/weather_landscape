import os


from weather_landscape import WeatherLandscape
from p_weather.configuration import WLBaseSettings

from configs import *
import secrets



cfgs =  [ 
          WLConfig_BW(),
          WLConfig_BWI(),
          WLConfig_EINK(),
          
          WLConfig_RGB_Black(),          
          WLConfig_RGB_White(),
          ]

for cfg in cfgs:
    print("Using configuration %s" % cfg.TITLE)
    cfg = WLBaseSettings.Fill( cfg, secrets )
    w = WeatherLandscape(cfg)
    fn = w.SaveImage()
    print("Saved",fn)

    
