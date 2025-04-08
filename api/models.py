from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class WeDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class ChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class CustomServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class WeWork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/services/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
class TechWeUse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/technologies/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/insights/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class CaseStudies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/insights/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class WebActivities(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/webActivities/', blank=True, null=True)  # Add image field 
    def __str__(self):
        return self.title
    
class WhyMeta(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/whyMeta/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
class HowWeDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/howWeDo/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# ux-ui-design
class AboutUxUi(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/uxUi/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# 2 and 4 page section
class OurUxUi(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/uxUi/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Our UX Services
class UxServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/uxUi/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Our UI Design Services
class UiServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/uxUi/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Independent dedicated QA & testing teams
class QaAbout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/QA/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Why Metamorphosis
class QaWhyMeta(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/QA/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# How We Do It
class QaHowWeDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/QA/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Testing Expertise
class QaTesting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/QA/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# cloud-computing 2nd page section
class CloudOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Cloud/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# cloud-benefits
class CloudBenefits(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Cloud/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# Who We Are
class WhoWeAre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/whoWeAre/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# MISSION AND VISION
class MissionVission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/whoWeAre/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Company Culture and Values
class CompanyCulture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Management Team
class ManageTeam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/whoWeAre/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Business Philosophy
class BusPhilosophy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# How We Work Page
# OUR APPROACH
class HowWeWork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/howWeWork/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# DEVELOPMENT STAGES
class DevelopmentStage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/howWeWork/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# How We Achieve Success
class AchieveSuccess(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/howWeWork/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Why Choose Us
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/chooseUs/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Partnership Program
class Partnership(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/partnership/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Partnership Program DropDowns
class PartnershipDropDowns(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title