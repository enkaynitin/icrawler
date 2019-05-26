from django import forms
from .models import ScrapyItem


class CrawlForm(forms.Form):

    url = forms.URLField(label="Start Url ", required=True)



