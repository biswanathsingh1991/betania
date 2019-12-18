from django.views.generic import TemplateView


class LoginTemplateView(TemplateView):
    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)