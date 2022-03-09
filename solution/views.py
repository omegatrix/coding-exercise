from django.http import HttpRequest, JsonResponse

from .utils import string_to_float

available_paths = [
    "/api",
    "/api/hello-world",
    "/api/add-numbers/<num_one>/<num_two>",
    "/api/join-words/<word_one>/<word_two>",
]


def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "message": "Coding exercise solution",
            "available_paths": available_paths,
        }
    )


def hello_world(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "message": "Hello World",
        }
    )


def add_numbers(request: HttpRequest, num_one: str, num_two: str) -> JsonResponse:
    converted_num_one = string_to_float(num_one)
    converted_num_two = string_to_float(num_two)
    num_list = [
        {"original": num_one, "converted": string_to_float(num_one)},
        {"original": num_two, "converted": string_to_float(num_two)},
    ]
    err_list = []

    for num in num_list:
        if num["converted"] is None:
            err_list.append(
                {"message": f"Provided value {num['original']} is not a valid number"},
            )

    if err_list:
        return JsonResponse(
            {
                "sum": None,
                "errors": err_list,
            },
            status=400,
        )

    return JsonResponse(
        {
            "sum": converted_num_one + converted_num_two,
            "errors": None,
        }
    )


def join_words(request: HttpRequest, word_one: str, word_two: str) -> JsonResponse:
    word_list = [
        {"original": word_one, "is_alpha": word_one.isalpha()},
        {"original": word_two, "is_alpha": word_two.isalpha()},
    ]
    err_list = []

    for word in word_list:
        if word["is_alpha"] is False:
            err_list.append({"message": f"Provided value {word['original']} contains non alphabetic characters"})

    if err_list:
        return JsonResponse(
            {
                "joined_words": None,
                "errors": err_list,
            },
            status=400,
        )

    return JsonResponse(
        {
            "joined_words": f"{word_one}-{word_two}",
            "errors": None,
        }
    )
