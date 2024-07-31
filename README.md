# api_final_yatube
### Backend Rest API for YaTube service

## Project description

YaTube is a social network where user can publish posts, subscribe to other users, and leave comments under other user's posts.
This project is a backend API for YaTube - an internal part of the product that is located on the server and hidden from users.

This API allows users to create, view, and interact with posts, comments, groups, and subscriptions.

The API requires authentication and authorization using JWT tokens (Djoser), which guarantees the safety and confidentiality of user data.

## Project tech stack:
- [Python 3.9](https://www.python.org/)
- [Django 3.2.16](https://www.djangoproject.com/)
- [Django REST Framework 3.2.14](https://www.django-rest-framework.org/)
- [Simple JWT 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)


## How to run the project:

Clone repository and switch to project directory using command line:

```
git clone git@github.com:kopf8/api_final_yatube.git
```

```
cd api_final_yatube
```

Create & activate virtual environment:

```
python -m venv .venv
```

* For Linux/macOS:

    ```
    source .venv/bin/activate
    ```

* For Win:

    ```
    source .venv/Scripts/activate
    ```

Upgrade pip:

```
python -m pip install --upgrade pip
```

Install project requirements from file _requirements.txt_:

```
pip install -r requirements.txt
```

Make & run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Launch server from directory _**api_final_yatube/yatube_api**_:

```
python manage.py runserver
```
<br><hr>

## Necessary links available after server is launched:
Project itself: `http://127.0.0.1:8000`

Admin panel: `http://127.0.0.1:8000/admin` 

Project documentation: `http://localhost:port/redoc/`
<br><hr>

## Examples of API requests & responses
* Create post:

Send POST-request to enpoint ```http://127.0.0.1:8000/api/v1/posts/``` with obligatory field _**text**_, and with header ```Authorization:Bearer <токен>```.

Sample request:
```
{
  "text": "Test post."
}
```
Sample response:
```
{
    "id": 1,
    "author": "user",
    "text": "Test post.",
    "pub_date": "2024-08-01T11:12:38.848100Z",
    "image": null,
    "group": null
}
```
* Pagination (LimitOffsetPagination):
```
GET /api/v1/posts/?limit=3&offset=7
```
Such GET-request will return 3 objects, from 7th to 9th (or less, if response contains less than 9 objects).

* Requests available for unauthorized users
Unauthorized users are allowed to work with this API only in readonly mode: they can't create, update or delete any object; not all API endpoints are available for them.
```
1. GET api/v1/posts/ - get list of all posts.
If parameters _limit_ and _offset_ are provided in request, list of posts is shown with pagination.
  limit - number of posts per page.
  offset - number of object to start paginated output from.
2. GET api/v1/posts/{id}/ - get post with given id.
3. GET api/v1/groups/ - get list of available groups.
4. GET api/v1/groups/{id}/ - get info on the group with given id.
5. GET api/v1/{post_id}/comments/ - get all comments for post with given id.
6. GET api/v1/{post_id}/comments/{id}/ - get comment with given id for post with given id.
```
**Full list of available API requests & endpoints is shown on the project documentation.**
<br><hr>

### Author:
**Maria Kirsanova**<br>
Github profile — https://github.com/kopf8