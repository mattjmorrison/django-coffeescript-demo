from django.conf.urls.defaults import patterns, include, url

from sample import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='home'),
)
from webassets.filter import Filter, register_filter
import coffeescript

@register_filter
class CoffeeFilter(Filter):
    name = 'coffee'

    def input(self, _in, out, **kwargs):
        out.write(coffeescript.compile(_in.read()))
