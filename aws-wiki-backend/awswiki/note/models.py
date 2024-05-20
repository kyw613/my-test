from django.db import models

class Note(models.Model):
    index = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=10)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    image = models.FileField(null=False)

    def __str__(self):
        return str(self.index)    
class NoteReview(models.Model):
    noteReviewId = models.AutoField(primary_key=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=50)

    def __str__(self):
        return self.review 