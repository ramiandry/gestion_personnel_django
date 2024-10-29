from django.shortcuts import redirect, render
from employee.models import Employees
from poste.models import Postes
# Create your views here.

def employee(request):
    dataPostes=Postes.objects.all()
    dataEmployee=Employees.objects.all()
    #Ajout de nouveau personnel
    if request.POST.get("btnAction")=='btnAjouter':
        images=request.FILES['image']
        postes=Postes.objects.get(pk=request.POST.get("poste"))
        Employees.objects.create(poste=postes, nom=request.POST.get("nom"), prenom=request.POST.get("prenom"), date_de_naissance=request.POST.get("ddn"), date_embauche=request.POST.get("de"), avatar=images, sexe=request.POST.get("sexe"))
        return redirect('employee')
    #Modification de Nom et Prenom
    elif request.POST.get("btnAction")=='modNom':
        id=request.POST.get("id")
        employees=Employees.objects.get(pk=id)
        employees.nom=request.POST.get("nom")
        employees.prenom=request.POST.get("prenom")
        employees.save()
        return redirect('employee')
    #Modification de sexe
    elif request.POST.get("btnAction")=='modSexe':
        id=request.POST.get("id")
        employees=Employees.objects.get(pk=id)
        employees.sexe=request.POST.get("sexe")
        employees.save()
        return redirect('employee')
    #M♂dification du date de naissance
    elif request.POST.get("btnAction")=='modDdn':
        id=request.POST.get("id")
        employees=Employees.objects.get(pk=id)
        employees.date_de_naissance=request.POST.get("ddn")
        employees.save()
        return redirect('employee')
    #Modification de date d'embauche
    elif request.POST.get("btnAction")=='modDe':
        id=request.POST.get("id")
        employees=Employees.objects.get(pk=id)
        employees.date_embauche=request.POST.get("de")
        employees.save()
        return redirect('employee')
    elif request.POST.get("btnAction")=='modPoste':
        id=request.POST.get("id")
        postes=Postes.objects.get(pk=request.POST.get("poste"))
        employees=Employees.objects.get(pk=id)
        employees.poste=postes
        employees.save()
        return redirect('employee')
    elif request.POST.get("btnAction")=='modProfile':
        id=request.POST.get("id")
        employees=Employees.objects.get(pk=id)
        employees.  avatar=request.FILES['image']
        employees.save()
        return redirect('employee')
    return render(request,"employee/index.html",{"dataPostes":dataPostes, "dataEmployee":dataEmployee})