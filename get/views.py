from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.github.com/users/defunkt')
    geodata = response.json()
    return render(request, 'get/home.html', {
        'id': geodata['id'],
        'type': geodata['created_at']
    })