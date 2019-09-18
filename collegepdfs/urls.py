from django.conf.urls import url

from .views import PdfList, PdfDetail

app_name = "pdf"

urlpatterns = [
    url(r'allpdfs/', PdfList.as_view(), name="getallpdf"),

    url(r'pdf/(?P<id>[0-9]+)/', PdfDetail.as_view(), name="getpdf"),
]