from pygal_maps_world.i18n import COUNTRIES

def get_country_coed(country_name):
    #得到国家的二位识别码
    for code,name in COUNTRIES.items():
        if country_name==name:
            return code
    return None