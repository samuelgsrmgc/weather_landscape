from p_weather.configuration import WLBaseSettings

class WLConfig_BW(WLBaseSettings):
    TITLE = "BW sprites"
    WORK_DIR = "tmp"
    OUT_FILENAME = "landscape_wb"
    OUT_FILEEXT = ".bmp"
    TEMPLATE_FILENAME = "p_weather/template_wb.bmp"
    SPRITES_DIR="p_weather/sprite"
    DRAWOFFSET = 65
    BACKGROUND = (255,255,255)
    FOREGROUND = (0,0,0)
    POSTPROCESS_INVERT = False
    POSTPROCESS_EINKFLIP = False    
    
class WLConfig_EINK(WLConfig_BW):
    TITLE = "BW sprites EINK"
    OUT_FILENAME = "landscape_eink"
    POSTPROCESS_INVERT = False   
    POSTPROCESS_EINKFLIP = True    
    
    
    
class WLConfig_BWI(WLConfig_BW):
    TITLE = "BW sprites inverted"
    OUT_FILENAME = "landscape_wbi"
    POSTPROCESS_INVERT = True
    POSTPROCESS_EINKFLIP = False


    
class WLConfig_RGB(WLBaseSettings):    
    TITLE = "Color sprites"
    OUT_FILENAME = "landscape_rgb"
    SPRITES_DIR="p_weather/sprite_rgb"
    TEMPLATE_FILENAME = "p_weather/template_rgb.bmp"
    BACKGROUND = (0,0,0)
    FOREGROUND = (255,255,255)
    POSTPROCESS_INVERT = False
    POSTPROCESS_EINKFLIP = False