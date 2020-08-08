from flask import Flask, jsonify, request
from controllers import ControllerRegistar

#object server
app = Flask(__name__)

# ping to test the server
@app.route('/registrar', methods=['GET'])
def registrar():

    mi_obj_controller = ControllerRegistar()
    mi_obj_controller.Control_DataHandlerRegisterJSON()
    mi_obj_controller.Control_Extractor()
    mi_obj_controller.Control_ExtractInfo_Register()
    mi_obj_controller.Control_Validator()

    return jsonify(
        {"data_registrar": Control_Player
        })
