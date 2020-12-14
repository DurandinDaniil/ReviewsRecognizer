from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Review
from .forms import UserForm

from .apps import ML

 
def index(request):
    userform = UserForm()
    review = Review.objects.all()
    return render(request, "index.html", { "userform": userform, "review": review})
 
def create(request):
    if request.method == "POST":
        comment = Review()
        comment.text = request.POST.get("text")
        alg = ML()
        text = alg.text_preprocessing(comment.text)
        text = alg.vectorizer.transform([text])
        comment.score = round(max(1, min(10, alg.regressor.predict(text)[0])))

        comment.mark = 1 if comment.score > 5 else 0
        comment.save()
    return HttpResponseRedirect("/")
