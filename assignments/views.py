from django.shortcuts import redirect, render
from .forms import AssignmentForm
from .models import Assignment


def assignment_list(request):
    assignments = Assignment.objects.order_by("due_date")
    return render(
        request,
        "assignments/assignment_list.html",
        {"assignments": assignments},
    )


def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("assignment_list")
    else:
        form = AssignmentForm()

    return render(
        request,
        "assignments/add_assignment.html",
        {"form": form},
    )