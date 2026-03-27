from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from app.form import ContactForm
from app.models import Portfolio, Product


class IndexView(TemplateView):
    template_name = 'index.html'


class MahsulotListView(ListView):
    template_name = 'mahsulotlar.html'

    model = Product
    paginate_by = 3
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_range"] = range(1, 6)
        return context


class MahsulotDetailView(TemplateView):
    template_name = 'mahsulot-detail.html'





class BizHaqimizdaView(TemplateView):
    template_name = 'biz-haqimizda.html'



class BlogListView(ListView):
    model = Portfolio
    paginate_by = 3
    template_name = 'blog.html'
    context_object_name = 'portfolio'

class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ConfirmPasswordView(TemplateView):
    template_name = 'confirm-password.html'


class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'


class SavatchaView(TemplateView):
    template_name = 'savatcha.html'

class AloqaView(FormView):
    template_name = 'aloqa.html'
    form_class = ContactForm
    success_url = reverse_lazy("index")