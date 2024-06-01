from django.shortcuts import render
from .models import OrgStruct, Departments
# Create your views here.
def orgStruct(request):
    try:
        file = OrgStruct.objects.order_by('-id').first()
        departments = Departments.objects.order_by('-id')
        deps_list = []
        for dep in departments:
            info_parts = dep.info.split('\n')
            dep_data = {
                'name': dep.name,
                'info': info_parts
            }
            deps_list.append(dep_data)
    except:
        file = None
        departments = None
    return render(request, 'orgStructure/orgStruct.html', {'file':file, 'deps': deps_list})