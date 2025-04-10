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
class OurServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/ourServices/', blank=True, null=True)  # Add image field
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





# Clients
class Clients(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# Blog
class TechInsights(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blog/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Outsourcing
class Outsourcing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blog/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Dedicated Software Teams
class DedicatedTeam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dedicatedTeams/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Our HR Process
class HrProcess(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dedicatedTeams/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Your solution to Offshore Software Development
class SolutionOffshore(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dedicatedTeams/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# IT Staff Augmentation Services
# What is IT Staff Augmentation?
class StaffAugmentation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/staffAugmentation/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Planning for IT Staff Augmentation
class Planning(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/staffAugmentation/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# The Advantages of Staff Augmentation Model
class AdvantagesStaff(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# The Difference Between IT Staff Augmentation and Dedicated Teams
class DifferenceBetween(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/staffAugmentation/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# Common Misconceptions Regarding IT Staff Augmentation
class Misconceptions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# IT Staff Augmentation Process
class AugProcess(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/staffAugmentation/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# What to look for in a Software Development Company
class LookFor(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# Additional Software Services
class AddSoftware(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/staffAugmentation/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# Software Outsourcing Services
# Our Software Development Outsourcing Services
class OutsourcingServ(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/softwareOutsourcing/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Benefits of Software Development Outsourcing
class BenefitsSoft(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# OUR PREMIUM SOFTWARE DEVELOPMENT SERVICES
class PremiumSoft(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Our Software Outsourcing Stages
class SoftwareStages(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/softwareOutsourcing/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# WHY CHOOSE METAMORPHOSIS
class SoftChooseMeta(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Advantages of Our Software Development Outsourcing Services
class AdvantagesSoftDev(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    

# How Do We Ensure That Outsourcing Is Safe?
class SoftStages(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/softwareOutsourcing/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# FREQUENTLY ASKED QUESTIONS
class AskedQuestions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# HOW DO YOU ENSURE SUCCESSFULL SOFTWARE OUTSOURCING 
class EnsureSuccess(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/softwareOutsourcing/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Premium Company
class PremiumCompany(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/softwareOutsourcing/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# OUR DATA SCIENCE SERVICES
class DataScienceServ(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dataScienceServ/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# Our Approach to Data Science
class DataApproach(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dataScienceServ/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

class OurDataApproach(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# DATA SCIENCE USE CASES
class DataUseCase(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dataScienceServ/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# DATA PRIVACY AND SECURITY
class DataPrivacy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/dataScienceServ/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# What is Machine Learning?
class MachineLearning(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/machineLearning/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# Our Data Science Services
class OurMachineServ(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/machineLearning/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# How We Deliver Machine Learning Solutions
class DeliverMachine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/machineLearning/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title

# Hire Machine Learning Experts on Your Team
class HireMachine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/machineLearning/', blank=True, null=True)  # Add image field
    def __str__(self):
        return self.title
    
# FREQUENTLY ASKED QUESTIONS Machine
class FrequentMachine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# AI Development Services We Offer
class AiDevService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# AI Domains We Excel in
class AiDomain(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Why Outsource AI Projects to Orient Software?
class OutsourceAi(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Frequently Asked Questions (FAQs)
class AiDevQuestions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# Excel in AI Development with Metamorphosis
class ExcelAiDev(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Location(models.Model):
    address = models.CharField(max_length=255)
    office = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.office} - {self.address}"