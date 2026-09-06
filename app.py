from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, world! Teste"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8080)

# uvicorn app:app --reload