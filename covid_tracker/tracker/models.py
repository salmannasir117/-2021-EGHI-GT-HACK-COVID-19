from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone

# Create your models here.

class Test(models.Model):
    date = models.DateTimeField('date test taken')
    is_positive = models.BooleanField(blank=False)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)

class CourseDateTime(models.Model):
    class Day(models.TextChoices):
        MONDAY = "Monday", _("Monday")
        TUESDAY = "Tuesday", _("Tuesday")
        WEDNESDAY = "Wednesday", _("Wednesday")
        THURSDAY = "Thursday", _("Thursday")
        FRIDAY = "Friday", _("Friday")
    course = models.ForeignKey('Course', on_delete=models.CASCADE,)
    day = models.CharField(max_length=200, choices=Day.choices, blank=True)
    time = models.TimeField(blank=True)

class Course(models.Model):
    title = models.CharField(max_length=200, blank=True)
    professor = models.CharField(max_length=200, blank=True)
    Section = models.CharField(max_length=200, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_account', on_delete=models.CASCADE, blank=True) # can now access user account easily, such as request.user.account.date
    course_schedule = models.ManyToManyField(Course, related_name='course_schedule', blank=True)
    class Dorm(models.TextChoices):
        ARMSTRONG = "Armstrong", _("Armstrong")
        BROWN = "Brown", _("Brown")
        CALDWELL = "Caldwell", _("Caldwell")
        CENTER_STREET_NORTH = "Center Street North", _("Center Street North")
        CENTER_STREET_SOUTH = "Center Street South", _("Center Street South")
        CLOUDMAN = "Cloudman", _("Cloudman")
        EIGHTH_STREET_EAST = "Eighth Street East", _("Eighth Street East")
        EIGHTH_STREET_SOUTH = "Eighth Street South", _("Eighth Street South")
        EIGHTH_STREET_WEST = "Eighth Street West", _("Eighth Street West")
        FIELD = "Field", _("Field")
        FITTEN = "Fitten", _("Fitten")
        FOLK = "Folk", _("Folk")
        FREEMAN = "Freeman", _("Freeman")
        FULMER = "Fulmer", _("Fulmer")
        GLENN = "Glenn", _("Glenn")
        GOLDIN_HOUSE = "Goldin House", _("Goldin House")
        GRADUATE_LIVING_CENTER = "Graduate Living Center", _("Graduate Living Center")
        GRAY_HOUSE = "Gray House", _("Gray House")
        HANSON = "Hanson", _("Hanson")
        HARRIS = "Harris", _("Harris")
        HARRISON = "Harrison", _("Harrison")
        HAYES_HOUSE = "Hayes House", _("Hayes House")
        HEFNER = "Hefner", _("Hefner")
        HOWELL = "Howell", _("Howell")
        MATHESON = "Matheson", _("Matheson")
        MAULDING = "Maulding", _("Maulding")
        MONTAG = "Montag", _("Montag")
        NELSON_SHELL = "Nelson Shell", _("Nelson Shell")
        NORTH_AVENUE_EAST = "North Avenue East", _("North Avenue East")
        NORTH_AVENUE_NORTH = "North Avenue North", _("North Avenue North")
        NORTH_AVENUE_SOUTH = "North Avenue South", _("North Avenue South")
        NORTH_AVENUE_WEST = "North Avenue West", _("North Avenue West")
        PERRY = "Perry", _("Perry")
        SMITH = "Smith", _("Smith")
        STEIN_HOUSE = "Stein House", _("Stein House")
        TENTH_AND_HOME_BLDG_A = "Tenth and Home Bldg A", _("Tenth and Home Bldg A")
        TENTH_AND_HOME_BLDG_B = "Tenth and Home Bldg B", _("Tenth and Home Bldg B")
        TENTH_AND_HOME_BLDG_C = "Tenth and Home Bldg C", _("Tenth and Home Bldg C")
        TENTH_AND_HOME_BLDG_D = "Tenth and Home Bldg D", _("Tenth and Home Bldg D")
        TENTH_AND_HOME_BLDG_F = "Tenth and Home Bldg E", _("Tenth and Home Bldg E")
        TENTH_AND_HOME_BLDG_G = "Tenth and Home Bldg F", _("Tenth and Home Bldg F")
        TOWERS = "Towers", _("Towers")
        WOODRUFF_NORTH = "Woodruff North", _("Woodruff North")
        WOODRUFF_SOUTH = "Woodruff South", _("Woodruff South")
        ZBAR = "Zbar", _("Zbar")
    dorm = models.CharField(max_length=200, choices=Dorm.choices, blank=True)

    def is_infected(self):
        test_date = None
        if len(self.test_set.filter(is_positive=True).order_by('-date')[0].date) == 0: #get most recent positive test)
            return False
        test_date = self.test_set.filter(is_positive=True).order_by('-date')[0].date #get most recent positive test
        delta = timedelta(weeks=3)
        now = datetime.now(timezone(timedelta(hours=-5)))
        return now - test_date < delta
        
class Employee(models.Model):
    user = models.OneToOneField(User, related_name='employee_account', on_delete=models.CASCADE) # can now access user account easily, such as request.user.account.date
    class Building(models.TextChoices):
        SPRING_STREET = "760 Spring Street", _("760 Spring Street")
        ALLEN = "Allen Sustainable Eduation Building", _("Allen Sustainable Eduation Building")
        BOGGS = "Boggs Building", _("Boggs Building")
        BUNGER_HENRY = "Bunger Henry Building", _("Bunger Henry Building")
        CHERRY_EMERSON = "Cherry Emerson Building", _("Cherry Emerson Building")
        CULC = "Clough Undergraduate Learning Commons", _("Clough Undergraduate Learning Commons")
        COC = "College of Computing", _("College of Computing")
        GUGGENHEIM = "GUGGENHEIM AEROSPACE BUILDING", _("GUGGENHEIM AEROSPACE BUILDING")
        ENGINEERING = "ENGINEERING SCIENCE & MECHANICS", _("ENGINEERING SCIENCE & MECHANICS")
        HOWEY = "HOWEY PHYSICS BUILDING", _("HOWEY PHYSICS BUILDING")
        IC = "INSTRUCTIONAL CENTER", _("INSTRUCTIONAL CENTER")
        KENDEDA = "KENDEDA BUILDING FOR INNOVATIVE SUSTAINABLE DESIGN", _("KENDEDA BUILDING FOR INNOVATIVE SUSTAINABLE DESIGN")
        LOVE = "LOVE MANUFACTURING BLDG (MRDC II)", _("LOVE MANUFACTURING BLDG (MRDC II)")
        MASON = "MASON", _("MASON") 
        MSE = "MSE", _("MSE")
        PAPER = "PAPER TRI", _("PAPER TRI") 
        SCHELLER = "SCHELLER", _("SCHELLER")
        SKILES = "SKILES", _("SKILES") 
        SMITH = "SMITH", _("SMITH")
        SWANN = "SWANN", _("SWANN") 
        VAN_LEER = "VAN_LEER", _("VAN_LEER")
        WEBER = "WEBER", _("WEBER") 
        WEST_VILLAGE = "WEST vILLAGE DINING COMMONS", _("WEST vILLAGE DINING COMMONS")
        WHITAKER = "WHITAKER", _("WHITAKER")
    workplace = models.CharField(max_length=200, choices=Building.choices, blank=True)

class FriendGroup(models.Model):
    friends = models.ManyToManyField(User, related_name='friend_group', blank=True)