
from django.contrib import admin
from django.urls import path,include
from Api import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.routers import DefaultRouter

# router= DefaultRouter()

# router.register('statusupdate', views.TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createteam/', views.CreateTeam.as_view()),
    path('createtask/', views.CreateTask.as_view()),
    path('updatetask/<int:pk>/', views.UpdateTask.as_view()),
    path('updatestatus/<int:pk>/', views.Updatestatus.as_view()),
    path('displaytask/', views.ListTask.as_view()),
    #path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),  
      ]
