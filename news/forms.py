from django.forms import ModelForm
from .models import ModelNews

class ModelNewsForm(ModelForm):
    class Meta:
        model = ModelNews
        fields = ('title', 'content', 'rubric')