from fastapi import FastAPI, Depends
from tablekit.table.dependency import get_table_params
from tablekit.table.schema import TableParams

app = FastAPI()


@app.get("/")
def root():
    return {"message": "working"}


@app.get("/api/users")
def get_users(table: TableParams = Depends(get_table_params)):
    return {
        "message": "Table params parsed successfully",
        "meta": table.model_dump()
    }