from django.shortcuts import render
import requests
import pygal


response = requests.get("https://api.github.com/users/studiozandra/repos")

# view table of all repos
def allrepos(request):
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

# repo sizes bar chart
def repos_by_size(request):
    bar_chart = pygal.HorizontalStackedBar()
    bar_chart.title = "All repos by size"
    bar_chart.x_labels = map(str, range(11))
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
    bar_chart.render('bar_chart.svg')

    context = {
        'bar_chart': bar_chart.render('bar_chart.svg'),
    }

    return render(request, 'pages/size-chart.html', context)
