from django.urls import path
from .views import index, listview_1, signupview, loginview, listview, detailview, CreateClass, logoutview, evaluationview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', listview, name='list'),
    path('list_1/', listview_1, name='list_1'),
    path('detail/<int:pk>', detailview, name='detail'),
    path('create/', CreateClass.as_view(), name='create'),
    path('logout/', logoutview, name='logout'),
    path('evaluation/<int:pk>', evaluationview, name='evaluation')
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
