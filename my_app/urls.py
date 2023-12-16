from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from my_app.views import  files_views

urlpatterns = [


    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('files/all', files_views.FilesIndex),
    path('files/add', files_views.FilesStore),
    path('files/view/<int:pk>', files_views.FilesShow),
    path('files/change/<int:pk>', files_views.FilesUpdate),
    path('files/delete/<int:pk>', files_views.FilesDelete),

]