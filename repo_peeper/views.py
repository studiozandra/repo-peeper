from django.shortcuts import render

# view table of all repos
def allrepos(request):

    context = {
        'example_context_variable': 'Hey, change me.',
    }

    return render(request, 'pages/allrepos.html', context)