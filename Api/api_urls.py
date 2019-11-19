from django.urls import path,include
from Api import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# # router.register('api',views.UserViewSet)
# #
# router.register('api/', views.UserViewSet,base_name='users')

urlpatterns = [
    # path('api/', include(router.urls)),
     path('api/', views.UserView.as_view())

]
