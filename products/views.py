from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'blog_entries': [
            {
                'title': 'BLACK FRIDAY DEAL',
                'body': 'Buy 2 get 3',

            },

        ]
    }
    return render(request, 'home.html', context)

def products(request):
    context = {
        'blog_entries': [
            {
                'title': 'Buy T-shirts',
                'body': 'Get a brand new cotton T-shirt',

            }
        ]}
    return render(request, 'products.html', context)
