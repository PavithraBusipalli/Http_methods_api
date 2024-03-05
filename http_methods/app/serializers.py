from rest_framework import serializers
from app.models import *
class DeptModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = '__all__'


class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
        