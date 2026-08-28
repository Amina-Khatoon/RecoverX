from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from .views import predict_view, dashboard_view


def home(request):
    return JsonResponse({
        "message": "RecoverX Backend is running!",
        "status": "success"
    })


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/predict/", predict_view),
    path("api/dashboard/", dashboard_view),
]