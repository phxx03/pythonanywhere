from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.voites}'

#-----------------------------------------------------------------------------------------#
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    Type_Name = models.CharField(max_length=100,default="ประเภท")
    def __str__(self):
        return f'{self.Type_Name}'


class Novels(models.Model):
    TypeName = models.ForeignKey(Type, on_delete=models.CASCADE)
    Fimg = models.CharField(max_length=200)
    FictionName = models.CharField(max_length = 200) #ชื่อ
    FWriterName = models.CharField(max_length = 200)
#    Manga_type = models.CharFeild(max_length = 200)
    Material = models.CharField(max_length = 10000)
    def __str__(self):
        return f'{self.TypeName} - {self.Fimg} - {self.FictionName} - {self.FWriterName} - {self.Material}'

