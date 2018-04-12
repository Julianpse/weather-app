###############################################################################
### This are lists of the available weather codes in the openweathermap API"###
###############################################################################
ids_with_code_11d = [200,201,202,210,211,212,221,230,231,232]
ids_with_code_9d = [300,301,302,310,311,312,313,314,321,520,521,522,531]
ids_with_code_10d = [500,501,502,503,504]
ids_with_code_13d = [511,600,601,602,611,612,615,616,620,621,622]
ids_with_code_50d = [701,711,721,731,741,751,761,762,771,781]
ids_with_code_01d = 800
ids_with_code_01n = 800
ids_with_code_02d = 801
ids_with_code_02n = 801

ids_with_code_03d = 802
ids_with_code_04d = [803,804]

weather_codes = {}

#######################################################################################################################
## This function updates the weather_codes dictionary above with the proper codes in format {id(711) : code ('50d'}}##
#####################################################################################################################

def add_weather_codes_keys():
    codes_list = ["11d", "9d", "10d", "13d", "50d", "01d", "01n", "02d", "02n","03d","04d"]

    for id in ids_with_code_11d:
        weather_codes.update({id:codes_list[0]})

    for id in ids_with_code_9d:
        weather_codes.update({id:codes_list[1]})

    for id in ids_with_code_10d:
        weather_codes.update({id:codes_list[2]})

    for id in ids_with_code_13d:
        weather_codes.update({id:codes_list[3]})

    for id in ids_with_code_50d:
        weather_codes.update({id:codes_list[4]})

    weather_codes.update({ids_with_code_01d:codes_list[5]})
    weather_codes.update({ids_with_code_01n:codes_list[6]})
    weather_codes.update({ids_with_code_02d:codes_list[7]})
    weather_codes.update({ids_with_code_02n:codes_list[8]})
    weather_codes.update({ids_with_code_03d:codes_list[9]})

    for id in ids_with_code_04d:
        weather_codes.update({id:codes_list[10]})

    return weather_codes

#Formats the image link to be used on the results page
def format_picture_links(id):
    add_weather_codes_keys()
    for code, pic_id in weather_codes.items():
        if id == code:
            weather_icons = "http://openweathermap.org/img/w/{}.png".format(pic_id)
            return weather_icons
