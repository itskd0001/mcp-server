from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "MCP server is running!"}


@app.get("/.well-known/mcp.json")
def get_manifest():
    return FileResponse(os.path.join(".well-known", "mcp.json"))


@app.post("/v1/queries")
async def handle_query(request: Request):
    body = await request.json()
    query = body.get("query", "")

    return JSONResponse({
        "items": [
            {
                "name": "Example Result",
                "content": f"You searched for '{query}'. Here's some fake data!",
                "metadata": {
                    "source": "MockDB",
                    "relevance": 0.98
                }
            }
        ]
    })
