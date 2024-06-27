from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import Usuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from rest_framework.utils import json
from django.shortcuts import render
from django.contrib.auth import authenticate

# Tokens por grupo
GRUPO_TOKENS = {
    "ventas": "token_ventas",
    "adquisiciones": "token_adquisiciones",
    "contabilidad": "token_contabilidad",
    "despacho": "token_despacho",
    "postventa": "token_postventa",
    "proveedor": "token_proveedor",
    "reporteria": "token_reporteria",
    "seguridad": "token_seguridad",
    "stock": "token_stock"
}

class IndexView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return render(request, 'api/index.html')

def LoginUsuario(request):
    return render(request, 'api/login.html')

def RegisterUsuario(request):
    return render(request, 'api/register.html')

@api_view(["POST"])
def UsuarioAdd(request):
    token = request.data.get('token')
    departamento = request.data.get('departamento')

    if GRUPO_TOKENS.get(departamento) == token:
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'api/login.html')
        else:
            return Response(serializer.errors)
    else:
        return Response({"error": "Token inválido"}, status=400)

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def ValidarUsuario(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    token = request.POST.get("token")

    user = authenticate(username=username, password=password)
    if user is not None:
        departamento = user.departamento
        if GRUPO_TOKENS.get(departamento) == token:
            return render(request, 'api/index.html', {'user': user})
        else:
            return Response({"error": "Token inválido"}, status=400)
    else:
        return Response({"error": "Credenciales inválidas"}, status=400)
