from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = ["done", "-created_at"]

    def __str__(self):
        if self.done:
            return f"{self.task} " \
                   f"(created_at: {self.created_at:%Y-%m-%d %H:%M}) - done"
        return f"{self.task} (created_at: {self.created_at:%Y-%m-%d %H:%M})"
