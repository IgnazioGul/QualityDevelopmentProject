from src import call
from src.weather import WeatherCall
from pytest_mock import MockerFixture
import pytest


def test_check_key_passes(mocker):
    #arrage
    mock_json_return = 200
    mocker.patch.object(call, "check", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        m.check_key()


def test_check_key_fail(mocker):
    #arrage
    mock_json_return = 401
    mocker.patch.object(call, "check", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        m.check_key()



def test_get_coordinates_passes(mocker):
    #arrage
    mock_json_return = [{"name":"Rome","local_names":{"nl":"Rome","eu":"Erroma","am":"ሮማ","pt":"Roma","af":"Rome","fy":"Rome","mr":"रोम","cv":"Рим","sg":"Rome","ja":"ローマ","pl":"Rzym","hy":"Հռոմ","kl":"Roma","sq":"Roma","ks":"روم","ia":"Roma","mg":"Roma","id":"Roma","ca":"Roma","ko":"로마","ga":"An Róimh","es":"Roma","th":"โรม","he":"רומא","se":"Roma","ml":"റോം","cu":"Римъ","uz":"Rim","da":"Rom","lb":"Roum","tg":"Рим","bg":"Рим","sr":"Рим","hi":"रोम","my":"ရောမမြို့","mt":"Ruma","mk":"Рим","fr":"Rome","cr":"ᖌᒪ","nn":"Roma","so":"Roma","ie":"Roma","oc":"Roma","gn":"Róma","bi":"Rome","cy":"Rhufain","be":"Рым","sv":"Rom","ne":"रोम","sh":"Rim","mi":"Rōma","os":"Ром","ar":"روما","sa":"रोमा","lv":"Roma","ee":"Rome","tk":"Rim","en":"Rome","ru":"Рим","ty":"Roma","la":"Roma","ka":"რომი","yo":"Rómù","io":"Roma","uk":"Рим","de":"Rom","fi":"Rooma","gd":"An Ròimh","si":"රෝමය","rn":"Roma","vo":"Roma","no":"Roma","sc":"Roma","et":"Rooma","fa":"رم","ku":"Roma","ht":"Ròm","it":"Roma","gv":"Yn Raue","rw":"Roma","ta":"உரோமை நகரம்","tr":"Roma","kk":"Рим","sk":"Rím","te":"రోమ్","qu":"Roma","sw":"Roma","kn":"ರೋಮ","ay":"Roma","su":"Roma","lt":"Roma","bs":"Rim","kv":"Рим","is":"Róm","yi":"רוים","rm":"Roma","an":"Roma","gl":"Roma","hr":"Rim","el":"Ρώμη","ur":"روم","li":"Roeme","sl":"Rim","tl":"Roma","ug":"رىم","sd":"روم","az":"Roma","zh":"羅馬/罗马","fo":"Róm","co":"Roma","bo":"རོ་མ།","mn":"Ром","vi":"Rô-ma","tt":"Рим","bn":"রোম","ba":"Рим","br":"Roma","ln":"Roma","hu":"Róma","jv":"Roma","cs":"Řím","ro":"Roma","na":"Roma","eo":"Romo"},"lat":41.8933203,"lon":12.4829321,"country":"IT","state":"Lazio"}]
    mocker.patch.object(call, "geo", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        assert m.get_coordinates('roma', 1) == mock_json_return



def test_get_coordinates_fail(mocker):
    #arrage
    mock_json_return = {"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}
    mocker.patch.object(call, "geo", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        m.get_coordinates('roma', 1)


def test_get_weather_passes(mocker):
    #arrage
    mock_json_return = {"coord":{"lon":12.4829,"lat":41.8933},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":285.51,"feels_like":284.76,"temp_min":283.38,"temp_max":287.2,"pressure":1006,"humidity":75},"visibility":10000,"wind":{"speed":1.03,"deg":110},"clouds":{"all":0},"dt":1669221304,"sys":{"type":2,"id":2000926,"country":"IT","sunrise":1669183751,"sunset":1669218241},"timezone":3600,"id":3169070,"name":"Rome","cod":200}
    mocker.patch.object(call, "weather", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        m.get_weather(41.8933203, 12.4829321)



def test_get_weather_fail(mocker):
    #arrage
    mock_json_return = {"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}
    mocker.patch.object(call, "weather", return_value = mock_json_return )
    m = WeatherCall('test')
    #assert
    with pytest.raises(TypeError):
        #act
        m.get_weather(41.8933203, 12.4829321)