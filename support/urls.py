from django.urls import path

from .views import NList, AList, EList, detail_view

app_name = 'support'

urlpatterns = [
    path('normal/', NList.as_view(), name="normal"),
    path('account/', AList.as_view(), name="account"),
    path('etc/', EList.as_view(), name="etc"),
    path('<int:object_id>/', detail_view, name="detail"),
]