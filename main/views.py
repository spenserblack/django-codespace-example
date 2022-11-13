from django.shortcuts import redirect, render
from django.views import View

from .forms import NewPostForm
from .models import Post


class Index(View):
    model = Post
    form_class = NewPostForm
    template_name = "main/index.html"

    def get(self, request):
        """
        Renders all posts
        """
        posts = self.model.objects.all()
        return render(
            request, self.template_name, {"posts": posts, "form": self.form_class}
        )

    def post(self, request):
        """
        Creates a new post
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        posts = self.model.objects.all()
        return render(request, self.template_name, {"posts": posts, "form": form})
