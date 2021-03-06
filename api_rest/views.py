from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from api_rest.serializers import UserSerializer, LinkSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from core.models import Link


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Por favor, informe todos os campos'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         user = User.objects.create(username=username, password=password)
#     login_django(request, user)
#     payload = jwt_payload_handler(user)
#     token = jwt_encode_handler(payload)
#     return Response({'token': token},
#                     status=HTTP_200_OK)

class LoginCreateView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {'username': '',
                    'password': ''
                   }
        return Response(content)

    def post(self,request):
        mensagem = ""
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Por favor, informe todos os campos'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if not user:
            try:
                user = User()
                user.username = username
                user.set_password(password)
                user.save()
                mensagem= 'Usuario Criado Com Sucesso'
            except:
                mensagem='Erro ao cadastrar/logar'
                return Response({'error': mensagem},
                                                        status=HTTP_400_BAD_REQUEST)
        login_django(request, user)
        mensagem = 'Login Realizado Com Sucesso'
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token, 'messagem':mensagem},
                        status=HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


