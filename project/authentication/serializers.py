
from .models import SchoolModel,StudentModel
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=SchoolModel
        fields=["id","stu_name",'Stu_email',"stu_roll"]
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= StudentModel
        fields=["id","stu_name",'Stu_email',"stu_roll"]