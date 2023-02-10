from django.db import models

# Create model of University Classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # Create model manager
    object = models.Manager

    # displays the object output values in the form of a string
    def __str__(self):
        # returns input value of the title / instructor name field as a tuple to display in browser instead of default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)
    
    # removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"