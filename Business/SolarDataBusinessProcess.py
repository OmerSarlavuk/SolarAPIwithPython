from DataAccess import BaseRepository
from Models.SolarData.SolarDataPostDto import SolarDataPostDto
from Models.SolarData.SolarPutDto import SolarPutDto

#sabit queryler ile ilgili ileride enum olarak tutulup direk oradan çekilebilir.
#SolarDatas tablusuna ait temel CRUD işlemler yapılmıştır sadece diğer extra olaylar yoktur.

base = BaseRepository


def read_solar_datas():
    results = base.read_data(query="select * from SolarDatas")
    response = {}

    if results[0] is None:
        response = {
            "data": None,
            "message": results[1],
            "statusCode": 200
        }
    else:
        solar_datas_lists = [{
            "Id": solar[0], 
            "CityName": solar[1],
            "Year": solar[2],
            "Month": solar[3],
            "Radiation": solar[4]
            }for solar in results[0]]
    
        response = {
            "data": solar_datas_lists,
            "message": results[1],
            "statusCode": 200
        }

    return response


def create_solar_data(solarPostDto: SolarDataPostDto):
    result = base.create_data(f"insert into SolarDatas (CityName, Year, Month, Radiation) values('{solarPostDto.cityName}', '{solarPostDto.year}', '{solarPostDto.month}', '{solarPostDto.radiation}')")

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response


def delete_solar_data(query:str): #Burada toplu silme işlemi vs gerçekleşmesi için query olarak almayı daha doğru buldum direk id olarak değilde o şekilde de alınabilir.
    result = base.delete_data(query=query)

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response


def update_solar_data(solarPutDto: SolarPutDto):
    query = f"update SolarDatas set CityName = '{solarPutDto.cityName}', Year = '{solarPutDto.year}', Month = '{solarPutDto.month}', Radiation = '{solarPutDto.radiation}' where Id = {solarPutDto.id}"
    result = base.update_data(query=query)

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response


