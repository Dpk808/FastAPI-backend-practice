from fastapi import FastAPI


app = FastAPI()


text_posts = {"1": {"title": "New Post","content": "cool test post"}}

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello World!"}

@app.get("/posts")
def get_all_posts():
    return text_posts
 