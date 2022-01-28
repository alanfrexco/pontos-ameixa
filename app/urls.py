from django.urls import path, re_path

from .views import InsertAPIView, ResultAPIView, ResultTotalAPIView


urlpatterns = [
    path('register/', InsertAPIView.as_view(), name='register'),
    path('register/<int:id>', InsertAPIView.as_view(), name='register'),
    path('extract/<int:id>', ResultAPIView.as_view(), name='extract'),
    path('result/<int:id>', ResultTotalAPIView.as_view(), name='result'),

    # re_path('^purchases/(?P<username>.+)/$', InsertList.as_view()),

]