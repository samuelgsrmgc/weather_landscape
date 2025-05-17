class WLBaseSettings(object):

    TEMP_UNITS_CELSIUS = 0 
    TEMP_UNITS_FAHRENHEIT = 1
    PRESSURE_RAIN_HPA = 980
    PRESSURE_FAIR_HPA = 1040

    @property
    def IsCelsius(self):
        return self.TEMPUNITS_MODE!=self.TEMP_UNITS_FAHRENHEIT

    TITLE = "Base config"
    OWM_KEY = "000000000000000000" 
    OWM_LAT = 52.196136
    OWM_LON = 21.007963
    TEMPUNITS_MODE = 0
    PRESSURE_MIN = 980
    PRESSURE_MAX = 1030
    WORK_DIR = None
    OUT_FILENAME = "landscape"
    OUT_FILEEXT = ".bmp"
    TEMPLATE_FILENAME = "template.bmp"
    SPRITES_DIR="sprite"
    DRAWOFFSET = 65
    BACKGROUND = (255,255,255)
    FOREGROUND = (0,0,0)
    POSTPROCESS_INVERT = False
    POSTPROCESS_EINKFLIP = False      
    
    @staticmethod
    def Fill(cfg,obj):
        print("Settings:")
        for key in obj.__dict__.keys():
            if not key.startswith('__'):
                if key.upper() == key:
                    val = obj.__dict__[key]
                    setattr(cfg, key, val)
                    if (key=='OWM_KEY'):
                        print('  ','OWM_KEY updated')
                    else:
                        print('  ',key,'=',val)
                else:
                    print('  ',key,'ignored')
        return cfg    
    
    DRAW_XSTART = 32
    DRAW_XSTEP  = 44
    DRAW_XFLAT =  10
    DRAW_YSTEP = 50  #64
    DRAW_DEFAULT_DEGREE_PER_PIXEL = 0.5
    DRAW_FLOWER_RIGHT_PX = 15
    DRAW_FLOWER_LEFT_PX = 10

    
    