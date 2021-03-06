#!/usr/bin/env python
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import json
import ovg
from .. import moduleBase
try:
    from . import coords
except ImportError:
    from . import coords_default as coords
    coords.default=True

class Weather(moduleBase.Module):
    """Weather App object"""


    WEATHER_API="http://forecast.weather.gov/MapClick.php?lat=%(lat)s&lon=%(lon)s&unit=0&lg=english&FcstType=%(type)s"
    ICON_URL="http://forecast.weather.gov/images/wtf/medium/%(img)s"
    """
        Known types:
            dwml
            json
            xml
            kml
            text (with TextType 1 or 2)
            graphical
            digital
    """

    def open(self,x,y,w,h):
        super(Weather, self).open(x,y,w,h)
        ovg.clear_color(255,255,255,255)
        ovg.clear()
        self.f = ovg.create_font()
        ovg.text(20,int(h/2),self.f,"Fetching Data...",15)
        ovg.draw()

    def fetch(self):
        data = urllib2.urlopen( self.WEATHER_API % {
                            "lat":coords.lat,
                            "lon":coords.lon,
                            "type":"json"
                        })

        self.data = json.loads(data.read().decode())



    def update(self):
        ovg.clear()
        ovg.text(10,290,self.f,"%s F, %s" % (self.data['currentobservation']['Temp'], self.data['currentobservation']['Weather']),12)
        ovg.text(10,275,self.f,self.data['location']['areaDescription'],12)

        if hasattr(coords,'default') and coords.default:
            ovg.text(10,20,self.f,"Using default location.",9)
            ovg.text(10,10,self.f,"Please update your coordinates",9)

        ovg.draw()

