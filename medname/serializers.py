from rest_framework import serializers
from .models import MedicineName

class MedicineNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineName
        fields = '__all__'
