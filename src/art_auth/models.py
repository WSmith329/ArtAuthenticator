from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import RegexValidator


class CreationDate(models.Model):
    date = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.date)


class Dimensions(models.Model):
    class Meta:
        constraints = [
            UniqueConstraint(fields=['height', 'width'],
                             name='unique_dimensions')
        ]

    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return str(self.width) + "x" + str(self.height)


class Technique(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Art(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.ForeignKey(CreationDate, on_delete=models.PROTECT)
    dimensions = models.CharField(
        validators=[
            RegexValidator(
                regex=r"^[\d,]+x[\d,]+$",
                message="Entry should follow format: 100x100",
                code="invalid_dimensions"
            )], max_length=100)
    technique = models.ForeignKey(Technique, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    archive_code = models.CharField(max_length=100, unique=True)
    photo_notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)


class Owner(models.Model):
    name = models.CharField(max_length=100)
    art = models.ManyToManyField(Art, through="Ownership")

    def __str__(self):
        return self.name


class Ownership(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.art.title + " by " + self.owner.name


class Signature(models.Model):
    FRONT = "F"
    BACK = "B"
    LOCATION_CHOICES = [(FRONT, "Front"), (BACK, "Back")]

    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    location = models.CharField(max_length=5, choices=LOCATION_CHOICES, default=FRONT)
    signature_notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.art.title)


# class Position(models.Model):
#     position = models.CharField(max_length=20)
#     code = models.CharField(max_length=20)
#
#     def __str__(self):
#         return str(self.position)


class Photo(models.Model):
    IN_FRONT = "IF"
    FROM_BEHIND = "FBD"
    LEFT_SIDE = "LS"
    RIGHT_SIDE = "RS"
    FROM_ABOVE = "FA"
    FROM_BELOW = "FBW"
    POSITION_CHOICES = [
        (IN_FRONT, "In Front"),
        (FROM_BEHIND, "From Behind"),
        (LEFT_SIDE, "Left Side"),
        (RIGHT_SIDE, "Right Side"),
        (FROM_ABOVE, "From Above"),
        (FROM_BELOW, "From Below"),
    ]

    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default=IN_FRONT)
    file = models.FileField(upload_to="art_photos")

    def __str__(self):
        return str(self.title)


class Applicant(models.Model):
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return str(self.forename) + str(self.surname)


class Commissioner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class AuthenticationDocument(models.Model):
    file = models.FileField(upload_to="authentication_documents")
    authentication = models.ForeignKey("Authentication", on_delete=models.CASCADE)


class Authentication(models.Model):
    TRUE = "T"
    FALSE = "F"
    VIEWING_REQUESTED = "VR"
    TO_EXAMINE = "TE"
    OPINION_CHOICES = [
        (TRUE, "True"),
        (FALSE, "False"),
        (VIEWING_REQUESTED, "Viewing Requested"),
        (TO_EXAMINE, "To Examine")
    ]

    date_requested = models.DateField()
    date_authenticated = models.DateField(blank=True, null=True)
    first_meeting_date = models.DateField(blank=True, null=True)
    second_meeting_date = models.DateField(blank=True, null=True)
    date_archived = models.DateField(blank=True, null=True)
    commission = models.ManyToManyField(Commissioner)
    opinion = models.CharField(max_length=20, choices=OPINION_CHOICES, default=TO_EXAMINE)
    has_artist_authentication = models.BooleanField(default=False)
    artist_authentication_notes = models.TextField(blank=True)
    work_requested_for_viewing = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    note = models.TextField(blank=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Application(models.Model):
    art = models.OneToOneField(Art, on_delete=models.CASCADE)
    authentication = models.OneToOneField(Authentication, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.art.title) + " - (" + str(self.pk) + ")"


# class Employee(models.Model):
#     manager = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='staff')
#     team_leader = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='team')
