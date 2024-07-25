from flask import Flask, Response, json, request
from Business import SolarDataBusinessProcess as solar_data_business_process 
from Business import CitiesCoordinateBusinessProcess as cities_coordinate_business_process
from Models.SolarData.SolarDataPostDto import SolarDataPostDto
from Models.SolarData.SolarPutDto import SolarPutDto
from Models.CitiesCoordinate.CitiesCoordinatePostDto import CitiesCoordinatePostDto
from Models.CitiesCoordinate.CitiesCoordinatePutDto import CitiesCoordinatePutDto

#Burası main.py tek bir controller gibi düşünülecek yani her modelin HTTP operasyonları bu main.py de olacak istekler buradan yönetilecek.
#Ancak her bir modelin kendi businessı oluşturuldu maplame vs orada yapılıyor.

app = Flask(__name__)

#---------------SolarDatas------------------


@app.route('/SolarData', methods=['GET'])
def read_solarDatas():
    response = solar_data_business_process.read_solar_datas()
    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json')


@app.route('/SolarData', methods= ['POST'])
def create_solarData():
    data = request.json
    city_name = data.get('cityName')
    year = data.get('year')
    month = data.get('month')
    radiation = data.get('radiation')

    solar_post_dto = SolarDataPostDto(city_name, year, month, radiation)

    response = solar_data_business_process.create_solar_data(solarPostDto=solar_post_dto)
    return Response(json.dumps(response))


@app.route('/SolarData', methods=['DELETE']) #Bu uç silinmek istenen  kayıdı id değeri üzerinden silme işlemi gerçekleştirecek.
def delete_solarData():

    solar_id = request.args.get("solarId") #Query den doğrudan alınmalıdır. -> /SolarData?solarId='ilgili id değeri'
    query = f"delete SolarDatas where Id = {solar_id}"

    response = solar_data_business_process.delete_solar_data(query=query)
    return Response(json.dumps(response))


@app.route('/SolarData', methods= ['PUT'])
def update_solarData():
    data = request.json

    id = data.get('id')
    city_name = data.get('cityName')
    year = data.get('year')
    month = data.get('month')
    radiation = data.get('radiation')

    solar_put_dto = SolarPutDto(id, city_name, year, month, radiation)
    
    response = solar_data_business_process.update_solar_data(solarPutDto=solar_put_dto)
    return Response(json.dumps(response))


#-----------SolarDatas--------------------

#-----------CitiesCoordinates-------------


@app.route('/CitiesCoordinates', methods=['GET'])
def read_cities_coordinates():
    response = cities_coordinate_business_process.read_cities_coordinates()
    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json')


@app.route('/CitiesCoordinate', methods = ['POST'])
def create_cities_coordinate():
    data = request.json

    name = data.get('name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    cities_coordinate_post_dto = CitiesCoordinatePostDto(name, latitude, longitude)
    response = cities_coordinate_business_process.create_citites_coordinate(cities_coordinate_post_dto)

    return Response(json.dumps(response))


@app.route('/CitiesCoordinate', methods = ['PUT'])
def update_citites_coordinate():
    data = request.json

    id = data.get('id')
    name = data.get('name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    cities_coordinate_put_dto = CitiesCoordinatePutDto(id, name, latitude, longitude)
    response = cities_coordinate_business_process.update_cities_coordinate(cities_coordinate_put_dto)

    return Response(json.dumps(response))


@app.route('/CitiesCoordinate', methods = ['DELETE'])
def delete_cities_coordinate():
    id = request.args.get("id")
    query = f"delete CitiesCoordinate where Id = {id}"

    response = cities_coordinate_business_process.delete_cities_coordinate(query)
    return Response(json.dumps(response))


#------------------CitiesCoordinates-------------------



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8001)

