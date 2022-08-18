from apps.movies.models import Movie


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"