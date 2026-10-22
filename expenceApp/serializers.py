from expenceApp.models import ExpenseModel
from rest_framework import serializers
from django.contrib.auth.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class ExpenceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseModel
        fields="__all__"
        read_only_fields=["id","created_at","owner"]