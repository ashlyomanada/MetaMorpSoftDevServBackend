from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import OfferViewSet
from .views import WeDoViewSet
from .views import ChooseUsViewSet
from .views import CustomServicesViewSet
from .views import WeWorkViewSet
from .views import TechWeUseViewSet
from .views import NewsViewSet
from .views import CaseStudiesViewSet
from .views import WebActivitiesViewSet
from .views import WhyMetaViewSet
from .views import HowWeDoViewSet
from .views import AboutUxUiViewSet
from .views import OurUxUiViewSet
from .views import UxServicesViewSet
from .views import UiServicesViewSet
from .views import QaAboutViewSet
from .views import QaWhyMetaViewSet
from .views import QaHowWeDoViewSet
from .views import QaTestingViewSet
from .views import CloudOfferViewSet
from .views import CloudBenefitsViewSet
from .views import WhoWeAreViewSet
from .views import MissionVissionViewSet
from .views import CompanyCultureViewSet
from .views import ManageTeamViewSet
from .views import BusPhilosophyViewSet
from .views import HowWeWorkViewSet
from .views import DevelopmentStageViewSet
from .views import AchieveSuccessViewSet
from .views import WhyChooseUsViewSet
from .views import PartnershipViewSet
from .views import PartnershipDropDownsViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'wedos', WeDoViewSet, basename='wedo')
router.register(r'chooseus', ChooseUsViewSet, basename='chooseus')
router.register(r'customservices', CustomServicesViewSet, basename='customservices')
router.register(r'wework', WeWorkViewSet, basename='wework')
router.register(r'techweuse', TechWeUseViewSet, basename='techweuse')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'webactivities', WebActivitiesViewSet, basename='webactivities')
router.register(r'whymeta', WhyMetaViewSet, basename='whymeta')
router.register(r'howwedo', HowWeDoViewSet, basename='howwedo')
router.register(r'casestudies', CaseStudiesViewSet, basename='casestudies') 

# ux-ui-design
router.register(r'aboutuxui', AboutUxUiViewSet, basename='aboutuxui') 
# 2 and 4 page section
router.register(r'ouruxui', OurUxUiViewSet, basename='ouruxui')
# Our UX Services
router.register(r'uxservice', UxServicesViewSet, basename='uxservice') 
# Our UI Design Services
router.register(r'uiservice', UiServicesViewSet, basename='uiservice')

# Independent dedicated QA & testing teams
router.register(r'qaAbout', QaAboutViewSet, basename='qaAbout') 
# Why Metamorphosis
router.register(r'qaWhyMeta', QaWhyMetaViewSet, basename='qaWhyMeta') 
# How We Do It
router.register(r'qaHowWeDo', QaHowWeDoViewSet, basename='qaHowWeDo') 
# Testing Expertise
router.register(r'qaTesting', QaTestingViewSet, basename='qaTesting')

# cloud-computing 2nd page section
router.register(r'cloudOffer', CloudOfferViewSet, basename='cloudOffer') 
# cloud-benefits
router.register(r'cloudBenefits', CloudBenefitsViewSet, basename='cloudBenefits')

# Who We Are
router.register(r'whoWeAre', WhoWeAreViewSet, basename='whoWeAre')
# MISSION AND VISION
router.register(r'missionVission', MissionVissionViewSet, basename='missionVission')
# Company Culture and Values
router.register(r'companyCulture', CompanyCultureViewSet, basename='companyCulture')
# Management Team
router.register(r'manageTeam', ManageTeamViewSet, basename='manageTeam')
# Business Philosophy
router.register(r'busPhilosophy', BusPhilosophyViewSet, basename='busPhilosophy')
# How We Work
router.register(r'howWeWork', HowWeWorkViewSet, basename='howWeWork')
# DEVELOPMENT STAGES
router.register(r'developmentStage', DevelopmentStageViewSet, basename='developmentStage')
# How We Achieve Success
router.register(r'achieveSuccess', AchieveSuccessViewSet, basename='achieveSuccess')
# Why Choose Us
router.register(r'whyChooseUs', WhyChooseUsViewSet, basename='whyChooseUs')
# Partnership
router.register(r'partnership', PartnershipViewSet, basename='partnership')
router.register(r'partnershipDropDowns', PartnershipDropDownsViewSet, basename='partnershipDropDowns')


# Include router.urls in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # This is necessary for DRF to work
]
