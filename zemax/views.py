from django.shortcuts import render, redirect
from .models import House
from .forms import UserRegisterForm, SendEmailForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail


# def index(request):
#     houses = House.objects.all()
#     return render(request, 'zemax/base.html', {'houses': houses})


class HouseListView(ListView):
    model = House
    template_name = 'zemax/base.html'
    context_object_name = 'houses'
    ordering = ['-id']
    paginate_by = 8


# def detail(request, id):
#     house = House.objects.get(id=id)
#     return render(request, 'zemax/House_detail.html', {'house': house})


class HouseDetailView(DetailView):
    model = House


class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    success_url = '/'

# def new_listing(request):
#     if request.method == "POST":
#         house_form = NewHouse(request.POST, request.FILES)
#         if house_form.is_valid():
#             house_form.save()
#             return redirect("home")
#     else:
#         house_form = NewHouse()
#     return render(request, 'zemax/House_form.html', {'form': house_form})


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    fields = ['house_image', 'address', 'price',
              'bedrooms', 'bathrooms', 'square_feet', 'description', 'year', 'agent', 'contact', 'sold']
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HouseUpdateView(LoginRequiredMixin, UpdateView):
    model = House
    fields = ['house_image', 'address', 'price',
              'bedrooms', 'bathrooms', 'square_feet', 'description', 'year', 'agent', 'contact', 'sold']
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     house = self.get_object()
    #     if self.request.user == house.author:
    #         return True
    #     return False
#     couldnt do this since i didnt define an author in model to start out with


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'zemax/register.html', {'form': form})


def profile(request):
    return render(request, 'zemax/profile.html')


def article(request):
    response = requests.get('https://sparkrental.com/how-to-buy-your-first-rental-property-no-money-down/')
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find_all('h1', class_='entry-title')
    header = title[0].text
    person = soup.find('span', class_='author')
    author = person.text
    div = soup.find('div', class_='et_pb_text_inner')
    methods = div.find_all('h2')
    paragraphs = div.find_all('p')
    house_hacking = methods[0].text
    house_hacking_p = [item.text for item in paragraphs[9:17]]
    BRRRR = methods[1].text
    BRRRR_p = [item.text for item in paragraphs[18:22]]
    seller_financing = methods[2].text
    seller_financing_p = [item.text for item in paragraphs[23:29]]
    div2 = soup.find_all('div', class_='et_pb_text_inner')
    real_div2 = div2[3]
    other_methods = real_div2.find_all('h2')
    other_paragraphs = real_div2.find_all('p')
    seller_mortgage = other_methods[0].text
    seller_mortgage_p = [item.text for item in other_paragraphs[:6]]
    second_mortgage = other_methods[1].text
    second_mortgage_p = [item.text for item in other_paragraphs[7:11]]
    collateral = other_methods[2].text
    collateral_p = [item.text for item in other_paragraphs[11:20]]
    method_headings = div2[7]
    more_methods = method_headings.find_all('h2')
    more_paragraphs = method_headings.find_all('p')
    partners = more_methods[0].text
    partners_p = [item.text for item in more_paragraphs[:5]]
    credit_cards = more_methods[1].text
    credit_cards_p = [item.text for item in more_paragraphs[6:13]]
    heloc = more_methods[2].text
    heloc_p = [item.text for item in more_paragraphs[14:22]]
    context = {'header': header, 'person': author, 'house_hacking': house_hacking, 'house_hacking_p': house_hacking_p,
               'BRRRR': BRRRR, 'BRRRR_p': BRRRR_p, 'seller_financing': seller_financing,
               'seller_financing_p': seller_financing_p, 'seller_mortgage': seller_mortgage,
               'seller_mortgage_p': seller_mortgage_p, 'second_mortgage': second_mortgage,
               'second_mortgage_p': second_mortgage_p, 'collateral': collateral, 'collateral_p': collateral_p,
               'partners': partners, 'partners_p': partners_p, 'credit_cards': credit_cards,
               'credit_cards_p': credit_cards_p, 'heloc': heloc, 'heloc_p': heloc_p}
    return render(request, 'zemax/article.html', context)


def send_email(request):
    if request.method == "POST":
        email_form = SendEmailForm(request.POST)
        if email_form.is_valid():
            clean = email_form.cleaned_data
            subject = clean['subject']
            message = clean['email_body']
            from_email = clean['sender']
            recipient_list = [clean['recipient']]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('home')
    else:
        email_form = SendEmailForm()
    return render(request, 'zemax/email_form.html', {'form': email_form})
