from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog.views import IndexView, ArticleDetailView, CategoryView, CommentCreateView, ArticleCreateView, ArticleUpdateView

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/")),

    url(r'^comment/create/$', CommentCreateView.as_view(), name="comment-create"),
    url(r'^categorie/(?P<slug>[-\w]+)/$', CategoryView.as_view(), name='category'),
    url(r'^article/create/$', ArticleCreateView.as_view(), name='article-create'),
    url(r'^article/(?P<slug>[-\w]+)/edit/$', ArticleUpdateView.as_view(), name='article-update'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^$', IndexView.as_view(), name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
