from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):

    def getQuestionsPage(self, request, questions, baseurl, html):
        limit = request.Get.get('limit',10)
        page = request.Get.get('page',1)
        paginator = Paginator(questions, limit)
        paginator.baseurl = baseurl
        page = paginator.page(page)
        return render(
            request,
            html,
            {
                'questions':page.object_list,
                'paginator':paginator,
                'page':page
            }
        )

    def new (self, request):
        questions = self.order_by('-added_at')
        return self.getQuestionsPage(self,request, questions,'?page=', 'new.html')

    def popular(self,request):
        questions =  self.order_by('-rating')
        return self.getQuestionsPage(self,request, questions,'/popular/?page=', 'popular.html')

    def question(self,request, pk):
        question = get_object_or_404(Question, pk)
        return render(
            request,
            'question.html',
            {
                'question': question,
            }
        )


class Question (models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    #links
    author = models.ForeignKey(User, related_name="authors_users")
    likes = models.ManyToManyField(User, related_name="likes_users")


class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True,auto_now_add=True)
    #links
    question = models.ForeignKey(Question, related_name="question_id")
    author = models.ForeignKey(User, related_name = "author_id")
