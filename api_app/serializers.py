from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.HyperlinkedModelSerializerModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        
        