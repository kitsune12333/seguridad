# serializers.py
from rest_framework import serializers
from .models import Usuario, Grupo

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'departamento', 'rol', 'grupo')
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
