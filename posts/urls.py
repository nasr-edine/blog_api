from django.urls import path

from .views import PostList, PostDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),

#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail().as_view()),
# ]

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = router.urls
