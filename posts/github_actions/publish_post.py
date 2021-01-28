import requests


def publish_post():
    # https://github.com/Medium/medium-api-docs#33-posts
    author_id = "schmidt.jake.c"
    with open("post.md", "r") as f:
        content = f.read()
    requests.post(
        f"https://api.medium.com/v1/users/{author_id}/posts",
        json={
            "title": "My Title",
            "contentFormat": "markdown",
            "content": content,
            "publishStatus": "draft",
        },
    )
