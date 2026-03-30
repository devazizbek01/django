from django.urls import path
from .views import home, post_detail, create_post, edit


urlpatterns = [
    path('', home, name="home"),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('createpost/', create_post, name='create_post'),
    path('post/<int:post_id>/edit_post', edit, name='post_edit')
]