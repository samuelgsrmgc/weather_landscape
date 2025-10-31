import os


from weather_landscape import WeatherLandscape
from configs import *




cfgs =  [ 
          WLConfig_BW(),
          WLConfig_BWI(),
          WLConfig_EINK(),
         
          WLConfig_RGB_Black(),          
          WLConfig_RGB_White(),
          ]
          

for cfg in cfgs:
    print("Using configuration %s" % cfg.TITLE)
    w = WeatherLandscape(cfg)
    fn = w.SaveImage()
    print("Saved",fn)

    
