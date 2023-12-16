from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from my_app.views import  files_views,roles_views,permission_views

urlpatterns = [


    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('files/all', files_views.FilesIndex),
    path('files/add', files_views.FilesStore),
    path('files/view/<int:pk>', files_views.FilesShow),
    path('files/change/<int:pk>', files_views.FilesUpdate),
    path('files/delete/<int:pk>', files_views.FilesDelete),

    path('roles/all', roles_views.RolesIndex),
    path('roles/add', roles_views.RolesStore),
    path('roles/view/<int:pk>', roles_views.RolesShow),
    path('roles/change/<int:pk>', roles_views.RolesUpdate),
    path('roles/delete/<int:pk>', roles_views.RolesDelete),

    path('permission/all', permission_views.PermissionIndex),
    path('permission/add', permission_views.PermissionStore),
    path('permission/view/<int:pk>', permission_views.PermissionShow),
    path('permission/change/<int:pk>', permission_views.PermissionUpdate),
    path('permission/delete/<int:pk>', permission_views.PermissionDelete),
]