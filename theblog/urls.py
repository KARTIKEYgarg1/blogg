from django.urls import path
from .views import DeletePostView, HomeView,ArticleDetailView,UpdatePostView,AddPostView
urlpatterns = [
 path('', HomeView.as_view(), name='home'),
 path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
 path('article/edit/<int:pk>', UpdatePostView.as_view(), name='article_update'),
 path('article/<int:pk>/remove', DeletePostView.as_view(), name='article_delete'),
 path('addPost', AddPostView.as_view(), name='add'),
   ]
# BASE_DIR / "static",
