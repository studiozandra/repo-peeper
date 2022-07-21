from django.shortcuts import render
import requests
import pygal


response = requests.get("https://api.github.com/users/studiozandra/repos").json()

# view table of all repos
def allrepos(request):
    
    # for repo in response:
    #     repo['name']
    #     repo['size']
    #     repo['stargazers_count']
    #     repo['language']
    #     repo['html_url']

    context = {
        'response': response,
    }

    return render(request, 'pages/allrepos.html', context)

# repo sizes bar chart
def repos_by_size(request):
    bar_chart = pygal.HorizontalBar()
    bar_chart.title = "All repos by size"
    bar_chart.x_labels = map(str, range(1))
    for repo in response:
        bar_chart.add(repo['name'], [repo['size']])
    
    bar_chart.render('bar_chart.svg')

    context = {
        'response': response,
        'bar_chart': bar_chart.render('bar_chart.svg'),
    }

    return render(request, 'pages/size-chart.html', context)
