from django.shortcuts import render
import requests

# view table of all repos
def allrepos(request):
    response = requests.get("https://api.github.com/users/studiozandra/repos")
    response = response.json()
    for repo in response:
        repo['name']
        repo['size']
        repo['stargazers_count']
        repo['language']
        repo['html_url']

    context = {
        'response': response,
    }

    return render(request, 'pages/allrepos.html', context)