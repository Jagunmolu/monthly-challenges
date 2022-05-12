from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

months = {
    'january': 'Month 1',
    'february': 'Month 2',
    'march': 'Month 3',
    'april': 'Month 4',
    'may': 'Month 5',
    'june': 'Month 6',
    'july': 'Month 7',
    'august': 'Month 8',
    'september': 'Month 9',
    'october': 'Month 10',
    'november': 'Month 11',
    'december': 'Month 12',
}


def month_list(request):
    months_list = list(months.keys())
    return render(request, 'challenges/index.html', {
        'months': months_list,
    })
    # lists = ''
    # months_list = list(months.keys())
    # for month in months_list:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month_val', args=[month])
    #     lists += f'<li><a href="{month_path}">{capitalized_month}</li>'
    # all_months = f'<ul>{lists}</ul>'
    # return HttpResponse(all_months)


def monthly_challenge_num(request, month):
    months_list = list(months.keys())
    if month < 1 or month > len(months_list):
        raise Http404()
    redirect_month = months_list[month - 1]
    return HttpResponseRedirect(reverse('month_val', args=[redirect_month]))


def monthly_challenge(request, month):
    if month in months:
        # return HttpResponse(f'<h1>{months[month]}</h1>')
        return render(request, 'challenges/challenge.html', {
            'text': months[month],
            'month_name': month,
        })
    raise Http404()
