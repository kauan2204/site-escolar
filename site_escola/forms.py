from django import forms
from django.core.exceptions import ValidationError
from site_escola.models import Quiz, QuizQuestion


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name',)


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('content', 'n_options')

    def clean_n_options(self):
        options = self.cleaned_data.get('n_options')
        
        if options <= 0:
            raise ValidationError(
                'escreve maior q zero',
                code='invalid'
            )
        
        if options > 9:
            raise ValidationError(
                'escreve mmenor q 10',
                code='invalid'
            )