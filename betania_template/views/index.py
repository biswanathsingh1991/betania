from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']
    template_name = 'tw/index-1.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
