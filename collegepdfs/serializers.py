from rest_framework import serializers
from .models import Pdf

class PdfSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pdf
		fields = '__all__' #returns all fields