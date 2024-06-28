from .serializer import UsuariosSerializer
from .models import Usuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth import authenticate
import os
import json
from supabase import create_client, Client

#Direccion SUPABASE
url: str = os.environ.get("SUPABASE_URL","https://hedwmixgqtmxzppsucbn.supabase.co")
key: str = os.environ.get("SUPABASE_KEY","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhlZHdtaXhncXRteHpwcHN1Y2JuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc3NzI1MDMsImV4cCI6MjAzMzM0ODUwM30.f9vEpMtNGIFU7xO11w51Ct9CDVFY78RndNnNg_ntseI")
supabase: Client = create_client(url, key)



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
    
    response = supabase.table("token_departamento").select("*").execute()
    data_tokens = [
            {'id': item['id'], 'departamento': item['departamento'], 'token': item['token']}
            for item in response.data]
    
    token = request.data.get('token')
    departamento = request.data.get('departamento')
    
    for i in data_tokens:
        if i["departamento"] == departamento and i["token"] == token:
            serializer = UsuariosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return render(request, 'api/login.html')
            else:
                return Response(serializer.errors)
        
    return Response({"error": "Token inválido"}, status=400)

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def ValidarUsuario(request):
    try:#SI LA DATA ES DE JSON
        
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        token = data.get("token")
        
    except json.JSONDecodeError:#SI NO LO ES

        username = request.POST.get("username")
        password = request.POST.get("password")
        token = request.POST.get("token")
    
    response = supabase.table("token_departamento").select("*").execute()
    data_tokens = [
            {'id': item['id'], 'departamento': item['departamento'], 'token': item['token']}
            for item in response.data]
    
    user = authenticate(username=username, password=password)
    if user is not None:
        departamento = user.departamento
        for i in data_tokens:
            if i["departamento"] == departamento and i["token"] == token:
                return render(request, 'api/index.html', {'user': user})
            else:
                return Response({"error": "Token inválido"}, status=400)
    else:
        return Response({"error": "Credenciales inválidas"}, status=400)


