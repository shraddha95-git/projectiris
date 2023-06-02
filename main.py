
from flask import Flask, jsonify, render_template, request

from project_app.utils import Iris

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Flower Prediction System") 
    return render_template("index.html")


@app.route("/predict_type", methods = ["POST", "GET"])
def get_species_type():
    if request.method == "GET":
        print("We are in a GET Method")

        SepalLengthCm = float(request.args.get("SepalLengthCm"))
        SepalWidthCm = float(request.args.get("SepalWidthCm"))
        PetalLengthCm = float(request.args.get("PetalLengthCm"))
        PetalWidthCm = float(request.args.get("PetalWidthCm"))
    
       
        print("*********************** SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm   **********************\n", SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm )

        iris = Iris(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        prediction = iris.get_predicted_type()
        
        return render_template("index.html", prediction = prediction)
        
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters