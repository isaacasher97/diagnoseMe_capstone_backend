from .models import Diagnosis
from rest_framework import serializers

class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'name', 'age', 'specialist', 'practiceType', 'description')