from django import forms

from bookstore_app.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from bookstore_app.web.models import Book, Comment, Author


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter book title',
                }
            ),
            'image_URL': forms.TextInput(
                attrs={
                    'placeholder': 'Enter image URL',
                }
            ),
        }


class EditBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['author'].disabled = True

    class Meta:
        model = Book
        fields = '__all__'


class DeleteBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False  # Disables fields

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'


class EditAuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True

    class Meta:
        model = Author
        fields = '__all__'


class DeleteAuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False  # Disables fields

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Author
        fields = '__all__'


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class EditCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].disabled = True

    class Meta:
        model = Comment
        fields = ('book', 'comment',)
