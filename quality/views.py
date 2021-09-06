from django.shortcuts import render
from .models import Images,Location
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ImageForm,UpdateForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Images
    template_name = 'welcome.html'

def all_images(request):
    images = Images.objects.all()
    locations = Location.objects.all()

    return render(request,'welcome.html',{"images": images, "locations":locations})

class imageDetailsView(DetailView):
    model = Images
    template_name = 'images.html'

class AddImagesView(CreateView):
    models = Images
    form_class = ImageForm
    template_name = 'post_image.html'

    def get_queryset(self): 
        return Images.objects.all()
class UpdateImagesView(UpdateView):
    models = Images
    form_class = UpdateForm
    template_name = 'update_post.html'
    
    def get_queryset(self): 
        return Images.objects.all()

class DeleteImagesView(DeleteView):
    models = Images
    template_name = 'delete_post.html'
    success_url = reverse_lazy('welcome')

    def get_queryset(self): 
        return Images.objects.all()

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Images.search_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def view_locations(request):
    locations = Location.objects.all()
    return render(request,'welcome.html',{"locations":locations})

def go_to_locations(request, location):
    locations = Images.objects.filter(location_id = location).all()
    print(locations)
    return render(request,'location.html',{"location": locations}) 









