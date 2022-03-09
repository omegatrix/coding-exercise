# Coding exercise

* [Requirements](#requirements)
* [Installation](#installation)
* [Running the app](#running-the-app)
* [API Reference](#api-reference)
  * [Index](#index)
  * [Hello World](#hello-world)
  * [Add two numbers](#add-two-numbers)
  * [Join two words by a `-`](#join-two-words-by)
  * [Path not found](#path-not-found)
* [Running tests](#running-tests)

## Requirements

This project uses [Django](https://github.com/django/django) web framework `4.0.3` which requires Python `3.8` or above.

Download and install Python if you have not got it installed already. Guides can be found [here](https://www.python.org/downloads/). From this point forward it is assumed that you have got Python `3.8` or above installed.

## Installation

Clone the repository if you have not already done it. Next, navigate to the folder by using command:

```
cd {path-to-the-folder}/coding-exercise
```

Create a virtual environment
> **_More about virtual environments:_**  [Virtual environment](https://docs.python.org/3/tutorial/venv.html).
```
python -m venv .venv
```

Activate the virtual environment
```
source .venv/bin/activate
```

(Optional) Upgrade `pip` if needed
```
python -m pip install --upgrade pip
```

Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Now you are ready to run the application locally.


## Running the app

Run the following command on your terminal

```
python manage.py runserver
```

> **_NOTE:_**  Django might not be happy about runnig the app without the initial migration. You can ignore the warning message as this is okay since we will not be using a database nor utilise admin functionalitites.

The application runs on `localhost` and port `8000` which is `127.0.0.1:8000`

You can use an API development tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to access the API endpoints. Alternatively, you can use [Curl](https://curl.se/) commands.


## API Reference

#### Index

```http
GET /api/
```

Curl command
```
curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:8000/api/'
```

Response
```json
{
    "message": "Coding exercise solution",
    "available_paths": [
        "/api",
        "/api/hello-world",
        "/api/add-numbers/<num_one>/<num_two>",
        "/api/join-words/<word_one>/<word_two>"
    ]
}
```

#### Hello World

```http
GET /api/hello-world/
```

Curl command
```
curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:8000/api/hello-world/'
```

Response
```json
{
    "message": "Hello World"
}
```

#### Add two numbers

> **_Limitations:_**  Values such as 10 / 2 will be considered as invalid and an error response will be returned.

```http
GET /api/add-numbers/<num_one>/<num_two>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `num_one` | `string` | **Required**. The first number to add. |
| `num_two` | `string` | **Required**. The second number to add. |

Curl command
```
curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:8000/api/add-numbers/101/73/'
```

Success Response
```json
{
    "sum": 174.0,
    "errors": null
}
```

Error Response
```json
{
    "sum": null,
    "errors": [
        {
            "message": "Provided value £101 is not a valid number"
        },
        {
            "message": "Provided value 73% is not a valid number"
        }
    ]
}
```

#### Join two words by a `-`.

> **_Limitations:_**  Values such as `1st`, `It's`, `high-level` will be considered as invalid and an error response will be returned.

```http
GET /api/join-words/<word_one>/<word_two>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `word_one` | `string` | **Required**. The first word to join. |
| `word_two` | `string` | **Required**. The second word to join. |

Curl command
```
curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:8000/api/join-words/Bruce/Wayne/'
```

Success Response
```json
{
    "joined_words": "Bruce-Wayne",
    "errors": null
}
```

Error Response
```json
{
  "joined_words": null,
  "errors": [
        {
            "message": "Provided value Br@ce contains non alphabetic characters"
        },
        {
            "message": "Provided value Wayne101 contains non alphabetic characters"
        }
    ]
}
```

#### Path not found

```http
GET /api/<undefined path>/
```

Curl command
```
curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:8000/api/something/'
```

Response
```json
{
    "message": "Path not found",
    "available_paths": [
        "/api",
        "/api/hello-world",
        "/api/add-numbers/<num_one>/<num_two>",
        "/api/join-words/<word_one>/<word_two>"
    ]
}
```

## Running tests

To run tests, run the following command

```
python manage.py test
```