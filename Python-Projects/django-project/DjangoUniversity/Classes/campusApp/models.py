from django.db import models

# Create nodel of University Campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default=None)

    # Create model manager
    object = models.Manager

    # displays the object output values in the form of a string
    def __str__(self):
        # returns input value of the title / instructor name field as a tuple to display in browser instead of default titles
        display_campus = '{0.campus_name} / {0.state}'
        return display_campus.format(self)

   # removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"   