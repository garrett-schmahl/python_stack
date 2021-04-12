from django.shortcuts import render

def index(request):
  return render(request,"index.html")
        
        
def post_result(request):
  context = {
    "name_on_template": request.POST['name'],
    "dojo_location_on_template": request.POST['dojo_location'],
    "favorite_language_on_template": request.POST['favorite_language'],
    "survey_languages_on_template": request.POST.getlist("lesson_input"),
    "eve_enjoy_on_template": request.POST.get(["eve_enjoy_check"]),
    "comment_on_template": request.POST["comment_box_survey"],
  }
  return render(request,"show.html",context)
  

#   alt if request.POST.get('var):