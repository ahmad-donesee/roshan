from rest_framework import serializers

from .models import Dataset,Data,Tags,Information



class DatasetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dataset
        fields='__all__'
        validators = [] 

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'
        validators = [] 

class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'
        validators = [] 

class InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Information
        fields='__all__'
        validators = [] 


