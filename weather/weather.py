#!/usr/bin/env python2

import urllib2
import sys
import json
import ovg
try:
    import coords
except:
    import coords_default as coords
    coords.default=True

WEATHER_API="http://forecast.weather.gov/MapClick.php?lat=%(lat)s&lon=%(lon)s&unit=0&lg=english&FcstType=%(type)s"
ICON_URL="http://forecast.weather.gov/images/wtf/medium/%(img)s"
"""
    Known types:
        dwml
        json
        xml
        kml
"""



def main():

    white = ovg.Color(255,255,255,255)
    black = ovg.Color(0,0,0,255)
    ovg.open(0,0,300,300)
    ovg.fill(white)
    bg = ovg.draw_path(ovg.rect(0,0,300,300), ovg.PaintMode.Fill)
    

    ovg.fill(black)
    ovg.text(20,150,"Fetching Data...",15)
    
    ovg.draw()
    
    


    data = urllib2.urlopen( WEATHER_API % {
                        "lat":coords.lat,
                        "lon":coords.lon,
                        "type":"json"
                    })

    data = json.loads(data.read())


    ovg.clear()
    ovg.fill(white)
    ovg.draw_path(bg, ovg.PaintMode.Fill)

    ovg.fill(black)
    ovg.text(10,290,"%s F, %s" % (data['currentobservation']['Temp'], data['currentobservation']['Weather']),12)
    ovg.text(10,275,data['location']['areaDescription'],12)

    if hasattr(coords,'default') and coords.default:
        ovg.text(10,20,"Using default location.",9)
        ovg.text(10,10,"Please update your coordinates",9)

    ovg.draw()

    sys.stdin.read(1)

    ovg.cleanup()



if __name__ == "__main__":
    main()
