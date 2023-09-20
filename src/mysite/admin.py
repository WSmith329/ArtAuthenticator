from django.contrib import admin
from django.urls import path

import mysite.views


class CustomAdminSite(admin.AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin"
    index_title = 'Welcome to the Custom Admin Site'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('count_document/', self.admin_view(mysite.views.CountDocumentAdminView.as_view()), name='count_document_admin_view'),
        ]

        return my_urls + urls
