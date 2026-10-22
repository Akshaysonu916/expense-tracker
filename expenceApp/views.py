from django.shortcuts import render
from expenceApp.serializers import ExpenceModelSerializer,Userserializer
from django.contrib.auth.models import User
from expenceApp.models import ExpenseModel
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListAPIView
from rest_framework import authentication,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.



class UserCreationView(CreateAPIView):
    serializer_class=Userserializer

    def perform_create(self,serializer):
        print(serializer)
        return User.objects.create_user(**serializer.validated_data)

class ExpenceCreateListView(CreateAPIView,ListAPIView):
    serializer_class=ExpenceModelSerializer
    queryset=ExpenseModel.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['category', 'payment']
    search_fields = ['title', 'category', 'payment']
    ordering_fields = ['title', 'amount', 'created_at']

    def perform_create(self, serializer):
        print('=============')
        user=self.request.user
        return serializer.save(owner=user)

    def get_queryset(self):
        return ExpenseModel.objects.filter(owner=self.request.user)


class ExpenceRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ExpenceModelSerializer

    def get_queryset(self):
        return ExpenseModel.objects.filter(owner=self.request.user)