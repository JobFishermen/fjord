from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class ItemIn(BaseModel):
    """This is a class that represents data coming into the server.
    """
    name: str

    # floating point numbers can lead to precision errors
    # it's best to use integers instead
    price: int = Field(..., gt=0, description="The price of an item in cents.")


@app.get("/")
def get_goot():
    """This is a function that returns a JSON object with a message.

    HTTP:
        curl 'http://localhost:8000/'
    """

    # TODO: something

    return {
        "msg": "Hello World"
    }


@app.get("/search")
def get_search(q: str = Query(..., min_length=3, max_length=50)):
    """This is a function that returns a JSON object with a query.

    OK HTTP:
        curl 'http://localhost:8000/search?q=foo'

    BAD HTTP:
        curl 'http://localhost:8000/search?q=fo'
    """

    # TODO: search database

    return {
        "query": q
    }


@app.post("/item")
def post_item(item: ItemIn):
    """This is a function that returns a JSON object with an item.

    OK HTTP:
        curl --request POST 'http://localhost:8000/item' \
             --header 'Content-Type: application/json' \
             --data-raw '{
                 "name": "foo",
                 "price": 100
             }'

    BAD HTTP:
        curl --request POST 'http://localhost:8000/item' \
             --header 'Content-Type: application/json' \
             --data-raw '{
                 "name": "foo",
                 "price": "bar"
             }'
    """

    # TODO: save item to database

    return {
        "item": item
    }
