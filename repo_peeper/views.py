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
    bar_chart = pygal.HorizontalBar(show_y_labels=False)
    bar_chart.title = "All repos by size"
    bar_chart.x_labels = map(str, range(1))
    for repo in response:
        bar_chart.add(repo['name'], [repo['size']])
    
    # bar_chart.render('bar_chart.svg')
    chart_svg_as_datauri = bar_chart.render_data_uri()

    context = {
        "rendered_chart_svg_as_datauri": chart_svg_as_datauri,
    }

    return render(request, 'pages/size-chart.html', context)
