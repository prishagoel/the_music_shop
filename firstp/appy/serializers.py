from rest_framework import serializers
from .models import UserInfo, Guitar, Piano, Drums, Violin

class UserInfoserializer(serializers.Serializer):
    class meta:
        model = UserInfo
        fields = ('Name', 'Phoneno', 'Email', 'Passwd')

class Guitarserializer(serializers.ModelSerializer):
    class meta:
        model = Guitar
        fields = ('Sno', 'Name', 'Phoneno')

class Pianoserializer(serializers.ModelSerializer):
    class meta:
        model = Piano
        fields = ('Sno', 'Name', 'Phoneno')

class Drumsserializer(serializers.ModelSerializer):
    class meta:
        model = Drums
        fields = ('Sno', 'Name', 'Phoneno')

class Violinserializer(serializers.ModelSerializer):
    class meta:
        model = Violin
        fields = ('Sno', 'Name', 'Phoneno')