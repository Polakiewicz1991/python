from flask import Flask, request
from flask_smorest import abort
from db import items, stores
import uuid
#app = Flask(__name__) => Tworzy aplikację,
#nazwa zmiennej i pliku powinny być takie same
#W terminalu należy wskazać ścieżkę :cd C:/Users/P.Polakiewicz/Desktop/PP/Python/python/Udemy/"Your First REST API"
#pip install flask
#python.exe -m pip install --upgrade pi
#jeżeli w ścieżce znajdują się "spację", nazwę folderu należy wziąć w cudzysłów

#aby uruchomić api należy wpisać "flask run", zamknąć api za pomocą CTRL + C
#następnie podgląd zmiennych będzi możliwy za pomocą przeglądarki po wpisaniu adresu http://127.0.0.1:5000/store

#czym jest  .JSON -> dane zapisane w postaci odpowienio sformatowanego stringa
#wszystko musi być zawarte w w listach lub słownikach

#sciągnąc Download Insomnia.rest do testowania API
#1. utworzyć projekt u nas "Your First REST API"
#2. utworzyć kolekcję HTTP Request
#3. wpisać adres zapytania "GET" http://127.0.0.1:5000/store
#4. zczytać dane za pomocą "SEND"

app = Flask(__name__)

@app.post("/store") #htttp://127.0.0.1:5000/store
def create_store():
    #funkcja request znajduje się w bibliotece Flask
    store_data = request.get_json()
    if (
        "name" not in store_data
    ):
        return abort(
            400,
            message= "Ensure that 'name' is included in JSON payload"
        )

    for store in stores.values():
        if(
            store_data["name"] == store["name"]
        ):
            return abort(
                400,
                message="Store already exist in store"
            )

    store_id = uuid.uuid4().hex
    store = \
        {
            **store_data, "id" : store_id
        }
    stores[store_id] = store
    #return 200 -> OK
    #return 201 -> operacja udana
    return store, 201

#zmienna name zostanie przejęta z ścieżki
# inną opcją jest określnie ścieżki jako: htttp://127.0.0.1:5000/store?name=My store
@app.post("/items")
def create_item():
    #here not only we need to validate data exists,
    #But also what type of dara it is, Price should be float
    item_data = request.get_json()
    if (
        "store_id" not in item_data
        or "price" not in item_data
        or "name" not in item_data
    ):
        return abort(
            404,
            message= "Ensure that 'store_id', 'price' and 'name' are included in JSON payload"
        )
    for item in items.values():
        if(
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            return abort(
                404,
                message="Item already exist in store"
            )

    item_id = uuid.uuid4().hex
    item = {**item_data, "item_id" : item_id}
    items[item_id] = item
    return item, 201
    #return 404 - not found

@app.get("/stores") #htttp://127.0.0.1:5000/stores
def get_stores():
    # return "Hello"
    return {"stores": list(stores.values())}

@app.get("/items") #htttp://127.0.0.1:5000/stores
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store/<string:store_id>") #htttp://127.0.0.1:5000/store
def get_store(store_id):
    #funkcja request znajduje się w bibliotece Flask
    try:
        return stores[store_id]
    except KeyError:
        return abort(404, message= "Store not found")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    #funkcja request znajduje się w bibliotece Flask
    try:
        return items[item_id]
    except KeyError:
        return abort(404, message= "Item not found")

@app.delete("/store/<string:store_id>") #htttp://127.0.0.1:5000/store
def delete_store(store_id):
    #funkcja request znajduje się w bibliotece Flask
    try:
        del(stores[store_id])
        return {"message" : "Store deleted"}
    except KeyError:
        return abort(404, message= "Store not found")

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    #funkcja request znajduje się w bibliotece Flask
    try:
        del items[item_id]
        return {"message" : "Item deleted"}
    except KeyError:
        return abort(404, message= "Item not found")

@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message = "Bad request. Ensute that name and price are in JSON payload")

    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        return abort(404, message= "Item not found")
#zainstalować docker desktop
#utworzyć plick Docker file
# FROM python:3.10
# EXPOSE 5000 -> nr portu
# WORKDIR /app -> nazwa ścieżki
# RUN pip install flask ->instalacja flaska
# COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]
# w terminalu wpisać ścieżkę pliku
# komenda kompilacji -> docker build -t rest-apis-flask-python .
# komenda uruchomienie -> docker run -dp 5000:5000 rest-apis-flask-python
# komenda uruchomienie ->  docker run -dp 5005:5000 -w /app -v C:\Users\P.Polakiewicz\Desktop\PP\Python\python\Udemy\"Your First REST API"\app rest-apis-flask-python


#należy zainstalwoać pip install python-dotenv
#aby zainstalować wszystkie biblioteki pip install -r requirements.txt

