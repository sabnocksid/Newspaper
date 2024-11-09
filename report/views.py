import csv
# import tempfile

from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model
from weasyprint import HTML
from django.template.loader import render_to_string
from django.views.generic import View
from newspaper.models import Post


User = get_user_model()

COLUMNS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "is_staff",
    "is_active",
    "is_superuser",
    "last_login",
    "date_joined",
]


class UserReportView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=users.csv"

        users = User.objects.all().only(*COLUMNS).values(*COLUMNS)

        writer = csv.DictWriter(response, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)

        return response

    


class PostPdfFileView(View):
    def get(self, request):
        # Fetch all posts from the database
        posts = Post.objects.all()

        # Render the HTML content from your template
        html_string = render_to_string('report/posts.html', {'posts': posts})

        # Create an HttpResponse object with PDF headers
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="posts.pdf"'

        # Use WeasyPrint to convert HTML to PDF
        HTML(string=html_string).write_pdf(response)

        return response