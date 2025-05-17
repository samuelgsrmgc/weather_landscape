import os


from weather_landscape import WeatherLandscape
from p_weather.configuration import WLBaseSettings

from configs import WLConfig_BW, WLConfig_BWI, WLConfig_RGB, WLConfig_EINK
import secrets



cfgs =  [ 
#          WLConfig_BW(),
#          WLConfig_BWI(),
          WLConfig_EINK(),
          
#          WLConfig_RGB(),          
          ]

for cfg in cfgs:
    print("Using configuration %s" % cfg.TITLE)
    cfg = WLBaseSettings.Fill( cfg, secrets )
    w = WeatherLandscape(cfg)
    fn = w.SaveImage()
    print("Saved",fn)

    
