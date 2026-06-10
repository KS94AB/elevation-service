from flask import Blueprint, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return "Elevation service is running"

@main.route("/elevation")
def elevation():
    wkt = request.args.get("wkt")

    if not wkt:
        return "Error: wkt parameter is required", 400
    
    return f"Received WKT: {wkt}"