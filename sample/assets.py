from webassets.filter import Filter, register_filter
import coffeescript

@register_filter
class CoffeeFilter(Filter):
    name = 'coffee'

    def input(self, _in, out, **kwargs):
        out.write(coffeescript.compile(_in.read()))
