from django.shortcuts import render

def index(request):
    return render(request, 'job_application/index.html')

def details(request):
    return render(request, 'job_application/details.html')

def apply(request):
    return render(request, 'job_application/apply.html')

def admin(request):
    return render(request, 'job_application/admin.html')

    # Retrieve and display job listings
    # You can add more logic here

# def job_details(request, job_id):
#     # Display details of a specific job listing
#     # You can add more logic here

# def application_details(request, app_id):
#     # Display details of a specific job application
#     # You can add more logic here
