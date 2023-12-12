from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from employee_management.models import Employee, Team


def getallusers(request):
    teams = Team.objects.values('id', 'name', 'description', 'team_lead_id')
    employees = Employee.objects.values('id', 'name', 'email', "team_id")

    teams_list = list(teams) if teams else []
    emp_list = list(employees) if employees else []

    data = {"team": teams_list, "emp": emp_list}
    context = {'employees': employees, 'teams': teams}
    return render(request, 'index.html', context)
    # return JsonResponse(data)


def create_user(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        name = data["name"]
        email = data["email"]
        team_id = data["teamid"]
        emp = Employee.objects.create(name=name, email=email)
        emp.save()
        try:
            if(team_id != ""):
                team = Team.objects.get(id=team_id)
                emp.team_id = team
                emp.save()
                return  JsonResponse({"message": "Successfully created"})
            else:
                emp.save()
                return JsonResponse({"message": "Successfully created but invalid team id"})
        except Team.DoesNotExist:
            return JsonResponse({"message": "Successfully created but invalid team id"})


def edit_user(request, user_id):
    employee = Employee.objects.get(id=user_id)
    print(employee.name)
    if request.method == "GET":
        return render(request, 'edit.html', {'employee': employee})
    elif request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        team_id = request.POST.get('team')

        employee.name = name
        employee.email = email
        if team_id != "None":
            try:
                team = Team.objects.get(id=team_id)
                employee.team_id = team
                employee.save()
                return JsonResponse({"message": "sucessfully updated", "code": 1})
            except Team.DoesNotExist:
                employee.save()
                return JsonResponse({"message": "no team found"})
            except Team.MultipleObjectsReturned:
                return JsonResponse({"message": "multiple entries found"})
        else:
            employee.save()
            return JsonResponse({"message": "no team found"})


def delete_user(request, user_id):
    user = Employee.objects.get(id=user_id)
    user.delete()
    return JsonResponse({"message": "Successfully deleted", "code": 1})


def create_team(request):
    if request.method == "GET":
        return render(request, 'team.html')
    elif request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        name = data["name"]
        des = data["description"]
        team_lead_id = data["teamid"]
        try:
            team_lead = Employee.objects.get(id=team_lead_id)
            new_team = Team.objects.create(name=name, description=des, team_lead_id=team_lead)
            new_team.save()
            return JsonResponse({"message": "successfully done"})
        except Employee.DoesNotExist:
            new_team = Team.objects.create(name=name, description=des)
            new_team.save()
            return JsonResponse({"message": "Sucessfully Created,But team lead id is invalid"})
        except Employee.MultipleObjectsReturned:
            return JsonResponse({"message": "multiple entries found"})


def update_team(request, team_id):
    team = Team.objects.get(id=team_id)
    if request.method == "GET":
        return render(request, 'edit_team.html', {'team': team})
    elif request.method == "POST":
        # Update team details based on the form data
        team_name = request.POST.get('teamName')
        team_lead_id = request.POST.get('teamLeadId')
        description = request.POST.get('description')

        try:
            team_lead = Employee.objects.get(id=team_lead_id)
            team = Team.objects.get(id=team_id)
            team.name = team_name
            team.description = description
            team.team_lead_id = team_lead
            team.save()
            return JsonResponse({"message": "successfully done", "code": 1})
        except Employee.DoesNotExist:
            new_team = Team.objects.create(name=team_name, description=description)
            new_team.save()
            return JsonResponse({"message": "Sucessfully Created,But team lead id is invalid"})


def delete_team(request, team_id):
    team = Team.objects.get(id=team_id)
    team.delete()
    return JsonResponse({"message": "Successfully deleted", "code": 1})

def get_team_details(request, team_id):
    team = Team.objects.get(id=team_id)
    employees = Employee.objects.filter(team_id=team_id)
    context = {'employees': employees, 'team': team}
    print(team.team_lead_id.name)
    return render(request, 'team_details.html', context)


