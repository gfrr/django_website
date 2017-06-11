from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Item, Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import QuestionForm

def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:5]
    context = {'latest_item_list': latest_item_list}
    return render(request, 'items/index.html', context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'items/detail.html', {'item': item})

def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)

def ask(request, item_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(Item, pk=item_id)
            item.question_set.create(question_text = request.POST.get('question_text'), votes = 0, question_answer= " ")

            return HttpResponseRedirect(reverse('items:detail', args=(item.id,)))
    else:
        form = QuestionForm()
    return render(request, 'items/detail.html'), {
        'form': form,
    }

def vote(request, item_id):
    question = get_object_or_404(Question, pk=request.POST.get('id'))
    print(request.POST.get('vote'))
    question.votes += int(request.POST.get('vote'))
    question.save()
    return HttpResponseRedirect(reverse('items:detail', args=(item_id,)))
