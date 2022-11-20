from src.weather import WeatherCall
API_KEY = "3f4da8251bb13dc76d98887324ae70bd"


def test_checkKey():
    pass

def test_coordinates():

    m = WeatherCall(API_KEY)
    roma_json = [{"name":"Rome","local_names":{"gd":"An Ròimh","mt":"Ruma","sr":"Рим","kl":"Roma","pl":"Rzym","lb":"Roum","fr":"Rome","tg":"Рим","ks":"روم","es":"Roma","ko":"로마","io":"Roma","nn":"Roma","ga":"An Róimh","de":"Rom","fo":"Róm","id":"Roma","sh":"Rim","mi":"Rōma","no":"Roma","su":"Roma","rm":"Roma","uk":"Рим","ku":"Roma","bn":"রোম","gn":"Róma","yo":"Rómù","bi":"Rome","hu":"Róma","qu":"Roma","en":"Rome","sw":"Roma","tl":"Roma","lt":"Roma","cr":"ᖌᒪ","ca":"Roma","ay":"Roma","he":"רומא","cs":"Řím","el":"Ρώμη","ml":"റോം","ro":"Roma","sg":"Rome","na":"Roma","se":"Roma","et":"Rooma","eo":"Romo","vo":"Roma","sq":"Roma","lv":"Roma","kv":"Рим","hr":"Rim","my":"ရောမမြို့","ne":"रोम","ia":"Roma","fy":"Rome","bg":"Рим","mr":"रोम","rn":"Roma","tk":"Rim","ht":"Ròm","co":"Roma","ee":"Rome","fa":"رم","sa":"रोमा","vi":"Rô-ma","eu":"Erroma","zh":"羅馬/罗马","da":"Rom","af":"Rome","mn":"Ром","cy":"Rhufain","jv":"Roma","az":"Roma","ar":"روما","nl":"Rome","bo":"རོ་མ།","an":"Roma","it":"Roma","hi":"रोम","si":"රෝමය","be":"Рым","cv":"Рим","tt":"Рим","ru":"Рим","ur":"روم","gl":"Roma","so":"Roma","uz":"Rim","gv":"Yn Raue","li":"Roeme","rw":"Roma","la":"Roma","ka":"რომი","mk":"Рим","fi":"Rooma","ie":"Roma","am":"ሮማ","pt":"Roma","sl":"Rim","sc":"Roma","br":"Roma","kk":"Рим","te":"రోమ్","sd":"روم","ty":"Roma","sv":"Rom","kn":"ರೋಮ","th":"โรม","cu":"Римъ","yi":"רוים","tr":"Roma","ja":"ローマ","ta":"உரோமை நகரம்","hy":"Հռոմ","ln":"Roma","mg":"Roma","bs":"Rim","os":"Ром","oc":"Roma","sk":"Rím","ba":"Рим","is":"Róm","ug":"رىم"},"lat":41.8933203,"lon":12.4829321,"country":"IT","state":"Lazio"},{"name":"Roma","lat":26.4070669,"lon":-99.0055462,"country":"US","state":"Texas"},{"name":"Roma","lat":-26.5674,"lon":148.78751,"country":"AU","state":"Queensland"},{"name":"Roma","local_names":{"ro":"Roma","uk":"Рома"},"lat":47.836931,"lon":26.6129285,"country":"RO"},{"name":"Roma","lat":-31.642912,"lon":-60.7255422,"country":"AR","state":"Santa Fe"}]
    res = m.get_coordinates("roma") 
    assert res == roma_json


def test_weather():

    m = WeatherCall(API_KEY)
    weather_roma = {"coord":{"lon":12.4754,"lat":41.8933},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":286.21,"feels_like":285.24,"temp_min":283.97,"temp_max":287.23,"pressure":1006,"humidity":64},"visibility":10000,"wind":{"speed":4.63,"deg":360},"clouds":{"all":0},"dt":1668962842,"sys":{"type":2,"id":2037790,"country":"IT","sunrise":1668924339,"sunset":1668959162},"timezone":3600,"id":3169070,"name":"Rome","cod":200}
    res = m.get_weather(41.8933,12.4754)
    assert res['coord'] == weather_roma['coord']
    