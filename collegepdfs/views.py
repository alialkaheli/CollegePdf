# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Pdf
from .serializers import PdfSerializer


class PdfList(APIView):
	
    def get(self, request, format=None):
        pdfs = Pdf.objects.all()
        serializer = PdfSerializer(pdfs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PdfDetail(APIView):
    ##retrieve, update, and delete a single pdf

    def get_object(self,id):
        pdf = get_object_or_404(Pdf,id=id)
        return pdf

    def get(self, request, id, format=None):
        pdf = self.get_object(id)
        serializer = PdfSerializer(pdf)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        pdf = self.get_object(id)
        serializer = PdfSerializer(pdf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        pdf = self.get_object(id)
        pdf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)