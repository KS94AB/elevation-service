from flask import Blueprint, request
from app.services.wkt import add_elevation_to_wkt

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return "Elevation service is running"

@main.route("/elevation")
def elevation():
    wkt = request.args.get("wkt")

    if not wkt:
        return "Error: wkt parameter is required", 400
    try:
        result = add_elevation_to_wkt(wkt)
    except FileNotFoundError as error:
        return f"Error: {error}", 500
    except ValueError as error:
        return f"Error: {error}", 400
        
    return result