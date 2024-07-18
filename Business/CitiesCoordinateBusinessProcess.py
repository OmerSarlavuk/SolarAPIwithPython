from Models.CitiesCoordinate.CitiesCoordinatePostDto import CitiesCoordinatePostDto
from Models.CitiesCoordinate.CitiesCoordinatePutDto import CitiesCoordinatePutDto
from DataAccess import BaseRepository

base_repository = BaseRepository


def read_cities_coordinates():
    query = "select * from CitiesCoordinate"
    response = {}

    result = base_repository.read_data(query= query)

    if result[0] is None:
        response = {
            "data": None,
            "message": result[1],
            "code": 400
        }
    else:

        cities_coordinates = [{
            "id": cities_coordinate[0],
            "name": cities_coordinate[1],
            "latitude": cities_coordinate[2],
            "longitude": cities_coordinate[3]
        }
        for cities_coordinate in result[0]
        ]

        response = {
            "data": cities_coordinates,
            "message": result[1],
            "code": 200
        }
    
    return response


def create_citites_coordinate(postDto: CitiesCoordinatePostDto):
    query = f"insert into CitiesCoordinate (Name, Latitude, Longitude) values ('{postDto.name}', '{postDto.latitude}', '{postDto.longitude}')"
    result = base_repository.create_data(query=query)

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response


def delete_cities_coordinate(query: str):
    result = base_repository.delete_data(query=query)

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response


def update_cities_coordinate(putDto: CitiesCoordinatePutDto):
    query = f"update CitiesCoordinate set Name = '{putDto.name}', Latitude = '{putDto.latitude}', Longitude = '{putDto.longitude}' where Id = {putDto.id}"
    result = base_repository.update_data(query=query)

    data = None
    message = result[1]
    code = 200 if result[0] else 400
    
    response = {
        "data": data,
        "message": message,
        "code": code
    }

    return response

