from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import QuestionForm
from .models import Item, Question

class IndexView(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        return Item.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'

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
