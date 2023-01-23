from django.db import models


class Question(models.Model):
    question = models.CharField(
        max_length=500, null=True, blank=True
    )
    describe_question = models.TextField(
        null=True, blank=True
    )
    tags = models.CharField(
        max_length=500,
        null=True, blank=True
    )
    solved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT,
        null=True, blank=True
    )
    answer = models.TextField(
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.answer
