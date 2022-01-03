from django.shortcuts import render
from modules.models import Module
from users_extended.models import UserExtended, Module

# Create your views here.
def module_detail(request, slug):
    module = Module.objects.get(slug=slug)

    built = None
    if request.user.is_authenticated:
        user = UserExtended.objects.get(user=request.user)
        built = user.built_modules.all()

    to_build = None
    if request.user.is_authenticated:
        user = UserExtended.objects.get(user=request.user)
        to_build = user.want_to_build_modules.all()

    components = module.component_bom_list.all()
    print(components)

    return render(request, 'modules/index.html', {"module": module, "built": built, "to_build": to_build, "components": components})