from flask import Flask, request

#app = Flask(__name__) => Tworzy aplikację,
#nazwa zmiennej i pliku powinny być takie same
#W terminalu należy wskazać ścieżkę :cd C:/Users/P.Polakiewicz/Desktop/PP/Python/python/Udemy/"Your First REST API"
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

stores = [
    {
        "name" : "My store",
        "items": [
            {
                "name"  : "Chair",
                "price" :   15.99
            }
        ]
    }
]

@app.get("/stores") #htttp://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

@app.post("/store") #htttp://127.0.0.1:5000/store
def create_store():
    #funkcja request znajduje się w bibliotece Flask
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    #return 200 -> OK
    #return 201 -> operacja udana
    return new_store, 201

#zmienna name zostanie przejęta z ścieżki
# inną opcją jest określnie ścieżki jako: htttp://127.0.0.1:5000/store?name=My store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    #return 404 - not found
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>") #htttp://127.0.0.1:5000/store
def get_store(name):
    #funkcja request znajduje się w bibliotece Flask
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/items")
def get_items_in_store(name):
    #funkcja request znajduje się w bibliotece Flask
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404