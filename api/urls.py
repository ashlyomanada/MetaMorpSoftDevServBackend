from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# Core Sections
router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'offers', views.OfferViewSet, basename='offer')
router.register(r'wedos', views.WeDoViewSet, basename='wedo')
router.register(r'chooseus', views.ChooseUsViewSet, basename='chooseus')
router.register(r'ourServices', views.OurServicesViewSet, basename='ourServices')
router.register(r'customservices', views.CustomServicesViewSet, basename='customservices')
router.register(r'wework', views.WeWorkViewSet, basename='wework')
router.register(r'techweuse', views.TechWeUseViewSet, basename='techweuse')
router.register(r'news', views.NewsViewSet, basename='news')
router.register(r'webactivities', views.WebActivitiesViewSet, basename='webactivities')
router.register(r'whymeta', views.WhyMetaViewSet, basename='whymeta')
router.register(r'howwedo', views.HowWeDoViewSet, basename='howwedo')
router.register(r'casestudies', views.CaseStudiesViewSet, basename='casestudies')

# UI/UX
router.register(r'ouruxui', views.OurUxUiViewSet, basename='ouruxui')
router.register(r'uxservice', views.UxServicesViewSet, basename='uxservice')
router.register(r'uiservice', views.UiServicesViewSet, basename='uiservice')

# QA
router.register(r'qaAbout', views.QaAboutViewSet, basename='qaAbout')
router.register(r'qaWhyMeta', views.QaWhyMetaViewSet, basename='qaWhyMeta')
router.register(r'qaHowWeDo', views.QaHowWeDoViewSet, basename='qaHowWeDo')
router.register(r'qaTesting', views.QaTestingViewSet, basename='qaTesting')

# Cloud
router.register(r'cloudOffer', views.CloudOfferViewSet, basename='cloudOffer')
router.register(r'cloudBenefits', views.CloudBenefitsViewSet, basename='cloudBenefits')

# Company
router.register(r'whoWeAre', views.WhoWeAreViewSet, basename='whoWeAre')
router.register(r'missionVission', views.MissionVissionViewSet, basename='missionVission')
router.register(r'companyCulture', views.CompanyCultureViewSet, basename='companyCulture')
router.register(r'manageTeam', views.ManageTeamViewSet, basename='manageTeam')
router.register(r'busPhilosophy', views.BusPhilosophyViewSet, basename='busPhilosophy')
router.register(r'howWeWork', views.HowWeWorkViewSet, basename='howWeWork')
router.register(r'developmentStage', views.DevelopmentStageViewSet, basename='developmentStage')
router.register(r'achieveSuccess', views.AchieveSuccessViewSet, basename='achieveSuccess')
router.register(r'whyChooseUs', views.WhyChooseUsViewSet, basename='whyChooseUs')

# Partnership
router.register(r'partnership', views.PartnershipViewSet, basename='partnership')
router.register(r'partnershipDropDowns', views.PartnershipDropDownsViewSet, basename='partnershipDropDowns')

# Clients & Insights
router.register(r'clients', views.ClientsViewSet, basename='clients')
router.register(r'techInsights', views.TechInsightsViewSet, basename='techInsights')

# Outsourcing
router.register(r'outsourcing', views.OutsourcingViewSet, basename='outsourcing')
router.register(r'dedicatedTeam', views.DedicatedTeamViewSet, basename='dedicatedTeam')
router.register(r'hrProcess', views.HrProcessViewSet, basename='hrProcess')
router.register(r'solutionOffshore', views.SolutionOffshoreViewSet, basename='solutionOffshore')

# Staff Augmentation
router.register(r'staffAugmentation', views.StaffAugmentationViewSet, basename='staffAugmentation')
router.register(r'planning', views.PlanningViewSet, basename='planning')
router.register(r'advantagesStaff', views.AdvantagesStaffViewSet, basename='advantagesStaff')
router.register(r'differenceBetween', views.DifferenceBetweenViewSet, basename='differenceBetween')
router.register(r'misconceptions', views.MisconceptionsViewSet, basename='misconceptions')
router.register(r'augProcess', views.AugProcessViewSet, basename='augProcess')
router.register(r'lookFor', views.LookForViewSet, basename='lookFor')
router.register(r'addSoftware', views.AddSoftwareViewSet, basename='addSoftware')

# Software Outsourcing
router.register(r'outsourcingServ', views.OutsourcingServViewSet, basename='outsourcingServ')
router.register(r'benefitsSoft', views.BenefitsSoftViewSet, basename='benefitsSoft')
router.register(r'premiumSoft', views.PremiumSoftViewSet, basename='premiumSoft')
router.register(r'softwareStages', views.SoftwareStagesViewSet, basename='softwareStages')
router.register(r'softChooseMeta', views.SoftChooseMetaViewSet, basename='softChooseMeta')
router.register(r'advantagesSoftDev', views.AdvantagesSoftDevViewSet, basename='advantagesSoftDev')
router.register(r'softStages', views.SoftStagesViewSet, basename='softStages')
router.register(r'askedQuestions', views.AskedQuestionsViewSet, basename='askedQuestions')
router.register(r'ensureSuccess', views.EnsureSuccessViewSet, basename='ensureSuccess')
router.register(r'premiumCompany', views.PremiumCompanyViewSet, basename='premiumCompany')

# Data Science
router.register(r'dataScienceServ', views.DataScienceServViewSet, basename='dataScienceServ')
router.register(r'dataApproach', views.DataApproachViewSet, basename='dataApproach')
router.register(r'ourDataApproach', views.OurDataApproachViewSet, basename='ourDataApproach')
router.register(r'dataUseCase', views.DataUseCaseViewSet, basename='dataUseCase')
router.register(r'dataPrivacy', views.DataPrivacyViewSet, basename='dataPrivacy')

# Machine Learning
router.register(r'machineLearning', views.MachineLearningViewSet, basename='machineLearning')
router.register(r'ourMachineServ', views.OurMachineServViewSet, basename='ourMachineServ')
router.register(r'deliverMachine', views.DeliverMachineViewSet, basename='deliverMachine')
router.register(r'hireMachine', views.HireMachineViewSet, basename='hireMachine')
router.register(r'frequentMachine', views.FrequentMachineViewSet, basename='frequentMachine')

# AI Development
router.register(r'aiDevService', views.AiDevServiceViewSet, basename='aiDevService')
router.register(r'aiDomain', views.AiDomainViewSet, basename='aiDomain')
router.register(r'outsourceAi', views.OutsourceAiViewSet, basename='outsourceAi')
router.register(r'aiDevQuestions', views.AiDevQuestionsViewSet, basename='aiDevQuestions')
router.register(r'excelAiDev', views.ExcelAiDevViewSet, basename='excelAiDev')

# Careers
router.register(r'location', views.LocationViewSet, basename='location')
router.register(r'jobs', views.JobsViewSet, basename='jobs')
router.register(r'careerBenefits', views.CareerBenefitsViewSet, basename='careerBenefits')
router.register(r'applicants', views.ApplicantsPositionDetailsViewSet, basename='applicants')
router.register(r'getintouch', views.GetInTouchViewSet, basename='getintouch')

router.register(r'banners', views.BannersViewSet, basename='banners')


# Final URLs list
urlpatterns = [
    path('', include(router.urls)),
]

