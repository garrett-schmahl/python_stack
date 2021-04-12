# from django.shortcuts import render
# def index(request):
#     return render(request,"index.html")
        
# def create_user(request):
#     print("Got Post Info....................")
#     print(request.POST)
#     return render(request,"index.html")


from django.shortcuts import render, redirect

def index(request):
  return render(request,"index.html")
        
        
def post_result(request):
  name_from_form = request.POST['name']
  dojo_location_from_form = request.POST['dojo_location']
  favorite_language_from_form = request.POST['favorite_language']
  

  # if keyname in request.post
  survey_languages_from_form = request.POST.getlist("lesson_input")

  eve_enjoy_from_form = request.POST["eve_enjoy_check"]
  comment_from_form = request.POST["comment_box_survey"]



  context = {
    "name_on_template": name_from_form,
    "dojo_location_on_template": dojo_location_from_form,
    "favorite_language_on_template": favorite_language_from_form,
    "survey_languages_on_template": survey_languages_from_form,
    "eve_enjoy_on_template": eve_enjoy_from_form,
    "comment_on_template": comment_from_form
  }
  return render(request,"show.html",context)
  