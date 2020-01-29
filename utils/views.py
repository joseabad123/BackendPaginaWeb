# Django imports
# ...

# Rest_framework imports
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication # Para que valide los tokens

# Local project imports
from core.models import (Category,
                        Item_Category)

# Serializadores
from utils.serializers import (University_Career_Serializer)

from login.permissions import IsSuperadmin, IsCoordinator, IsRespectiveCoordinator



# * Views
class University_Career_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de university_career
    """

    def get_queryset(self):
        category_name = 'Titulación'
        try:
            category_id = Category.objects.get(name='Titulación').category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None

    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer


class Contact_Type_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de contact_type
    """

    def get_queryset(self):
        category_name = 'Contact_type'
        try:
            category_id = Category.objects.get(name=category_name).category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None

    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer


class Menu_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de menu
    """

    def get_queryset(self):
        category_name = 'Menu'
        try:
            category_id = Category.objects.get(name=category_name).category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None



    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer


class Type_Content_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de type_content
    """

    def get_queryset(self):
        category_name = 'Type_Content'
        try:
            category_id = Category.objects.get(name=category_name).category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None

    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer


class Academic_Period_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de academic_period
    """

    def get_queryset(self):
        category_name = 'Academic_Period'
        try:
            category_id = Category.objects.get(name=category_name).category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None

    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer


class Media_Type_Viewset(ModelViewSet):
    """
    Proporciona un CRUD completo del modelo Item_Category, siempre y cuando estos spertenezcan a la categoria de media_type
    """

    def get_queryset(self):
        category_name = 'Media_Type'
        try:
            category_id = Category.objects.get(name=category_name).category_id
            final_queryset =  Item_Category.objects.filter(category_id=category_id)
            return final_queryset
        except:
            error_message = ('Category with name %s not found' %(category_name))
            print(error_message)
            return None

    #authentication_classes = [authentication.JWTAuthentication]
    #permission_classes = [IsRespectiveCoordinator]

    serializer_class = University_Career_Serializer













