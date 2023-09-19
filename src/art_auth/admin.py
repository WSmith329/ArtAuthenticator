from django.contrib import admin

from .models import Application, Art, Authentication, CreationDate, Technique, Genre, Commissioner, Applicant, AuthenticationDocument, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class ArtAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    list_display = ["id", "title", "archive_code"]
    list_filter = [
        ("creation_date", admin.RelatedOnlyFieldListFilter),
        ("technique", admin.RelatedOnlyFieldListFilter),
        ("genre", admin.RelatedOnlyFieldListFilter)
    ]
    search_fields = ["title"]


class AuthenticationDocumentInline(admin.TabularInline):
    model = AuthenticationDocument
    extra = 1


class AuthenticationAdmin(admin.ModelAdmin):
    inlines = [AuthenticationDocumentInline]

    fieldsets = [
        ("Date Information", {"fields": [
            "date_requested",
            "date_authenticated",
            "first_meeting_date",
            "second_meeting_date",
            "date_archived"
        ]}),
        ("Judgement Details", {"fields": [
            "commission",
            "opinion",
            "has_artist_authentication",
            "artist_authentication_notes",
            "work_requested_for_viewing",
            "comment",
            "note"
        ]}),
        ("Applicant", {"fields": ["applicant"]})
    ]

    list_display = ["id", "application", "applicant", "opinion", "date_requested"]
    list_filter = [
        ("date_requested", admin.DateFieldListFilter),
        ("commission", admin.RelatedOnlyFieldListFilter),
        ("has_artist_authentication", admin.BooleanFieldListFilter)
    ]


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "art", "authentication"]


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ["id", "forename", "surname"]


class CommissionerAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name"]


class GenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name"]


class TechniqueAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name"]


class CreationDateAdmin(admin.ModelAdmin):
    search_fields = ["date"]
    list_display = ["id", "date"]


admin.site.register(Genre, GenreAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(CreationDate, CreationDateAdmin)
admin.site.register(Art, ArtAdmin)

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Commissioner, CommissionerAdmin)
admin.site.register(Authentication, AuthenticationAdmin)

admin.site.register(Application, ApplicationAdmin)
