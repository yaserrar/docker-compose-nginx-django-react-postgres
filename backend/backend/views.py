from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import HttpResponseForbidden
import jwt
from django.conf import settings


@api_view(["GET"])
def send_some_data(request):
    return Response({"data": "Hello from django backend"})


class MediaAccess(APIView):
    def get(self, request, path):
        token = request.query_params.get("token")

        try:
            decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            response = HttpResponse()
            del response["Content-Type"]
            redirect_path = "/protected_media/" + path if not settings.DEBUG else path
            response["X-Accel-Redirect"] = redirect_path
            return response
        except Exception as e:
            return HttpResponseForbidden("Not authorized to access this media.")
