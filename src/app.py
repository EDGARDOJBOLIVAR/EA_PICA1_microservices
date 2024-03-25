from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from config import config

app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/user/*": {"origins": "http://localhost"}})

connect = MySQL(app)


@app.route("/user", methods=["GET"])
def getUsers():
    try:
        cursor = connect.connection.cursor()
        sql = "SELECT id, email, nombre, apellido, fecha FROM user"
        cursor.execute(sql)
        data = cursor.fetchall()
        users = []
        for row in data:
            user = {
                "id": row[0],
                "email": row[1],
                "nombre": row[2],
                "apellido": row[3],
                "fecha": row[4],
            }
            users.append(user)

        return jsonify({"users": users, "mensaje": "Usuarios listados"})
    except Exception as ex:
        print(f"Ha ocurrido un error {ex}")
        return jsonify({"mensaje": "Error al listar los usuarios"})


@app.route("/user/create", methods=["POST"])
def create_user():
    try:
        cursor = connect.connection.cursor()
        sql = """INSERT INTO user (email, nombre, apellido, fecha) 
        VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
            request.json["email"],
            request.json["nombre"],
            request.json["apellido"],
            request.json["fecha"],
        )
        cursor.execute(sql)
        connect.connection.commit()  # Se confirma la transaccion en la BD
        connect.connection.close()  # Se confirma la transaccion en la BD
        return jsonify({"mensaje": "Usuarios registrado exitosamente"})
    except Exception as ex:
        print(f"Ha ocurrido un error {ex}")
        return jsonify({"mensaje": "Error al crear el usuario"})


def page_not_found(error):
    return "<h1>La pagina no existe</h1>"


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404, page_not_found)

    SWAGGER_URL = app.config.get("SWAGGER_URL")
    API_URL = app.config.get("API_URL")

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Users application by PICA 2024"},
    )

    app.register_blueprint(swaggerui_blueprint)

    app.run()
