from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render_to_response, RequestContext
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import messages
from website.models import Project


def index(request):
    return render(request, 'index.html')

def index(request, template="index.html"):
    context = {
        'projects': Project.objects.all()[0:9],
    }
    return render_to_response(template, context, context_instance=RequestContext(request))



def profile(request):
    try:
        return redirect('/profile/' + request.user.username)
    except Exception:
        return redirect('/')


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'That user was not found.')
            return redirect("/")
        return super(UserProfileDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        return user

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        return context



class ProjectDetailView(DetailView):
    model = Project
    slug_field = "slug"
    template_name = "project.html"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'That project was not found.')
            return redirect("/")
        return super(ProjectDetailView, self).get(request, *args, **kwargs)



class ProjectCreate(CreateView):
    model = Project
    fields = ['name','description','image','slug']
    template_name = "add_project.html"

    def form_valid(self, form):
        messages.success(self.request, 'Project added! +'+ str(score))
        return HttpResponseRedirect("/"+obj.slug) 

    # def get_context_data(self, **kwargs):
    #     context = super(IssueCreate, self).get_context_data(**kwargs)
    #     context[''] = Action.objects.all()[0:10]
    #     context['hunts'] = Hunt.objects.exclude(plan="Free")[:4]
    #     context['leaderboard'] = User.objects.annotate(total_score=Sum('points__score')).order_by('-total_score').filter(total_score__gt=0)
    #     return context