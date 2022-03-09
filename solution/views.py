from django.http import HttpRequest, JsonResponse


available_paths = [
    "/api",
    "/api/hello-world",
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
