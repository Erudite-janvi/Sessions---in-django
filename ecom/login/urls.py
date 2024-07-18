from django.urls import path
from .views  import user_create



urlpatterns = [
   path('login/',user_create,name='login'),
]
