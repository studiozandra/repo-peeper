from django.shortcuts import render
import requests

# view table of all repos
def allrepos(request):
    response = requests.get("https://api.github.com/users/studiozandra/repos")
    # for repo in response.json():
    #     print(repo['name'])
    #     print(repo['size'])
    #     print(repo['stargazers_count'])
    #     print(repo['language'])
    #     print(repo['html_url'])

    context = {
        'response': response.json(),
    }

    return render(request, 'pages/allrepos.html', context)