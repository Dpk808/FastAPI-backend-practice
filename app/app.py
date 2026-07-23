from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()


text_posts = {
    1: {"title": "New Post", "content": "Cool test post."},
    2: {"title": "Python Tip", "content": "Use list comprehensions to write cleaner, more readable code."},
    3: {"title": "Daily Motivation", "content": "Small steps every day lead to big achievements."},
    4: {"title": "Fun Fact", "content": "Python was named after Monty Python, not the snake."},
    5: {"title": "Update", "content": "Just finished building a new FastAPI project!"},
    6: {"title": "Tech Insight", "content": "Caching can dramatically improve application performance."},
    7: {"title": "Quote", "content": "Code is like humor. When you have to explain it, it's bad."},
    8: {"title": "Weekend Plans", "content": "Planning to contribute to an open-source project this weekend."},
    9: {"title": "Question", "content": "What's your favorite Python library for backend development?"},
    10: {"title": "Mini Announcement", "content": "A new FastAPI tutorial is coming later this week!"}
}

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello World!"}

@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post 
    return new_post
 
 