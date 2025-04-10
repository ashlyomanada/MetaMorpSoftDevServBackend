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
from .views import OurServicesViewSet
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

from .views import ClientsViewSet
from .views import TechInsightsViewSet
from .views import OutsourcingViewSet
from .views import DedicatedTeamViewSet
from .views import HrProcessViewSet
from .views import SolutionOffshoreViewSet
from .views import StaffAugmentationViewSet
from .views import PlanningViewSet
from .views import AdvantagesStaffViewSet
from .views import DifferenceBetweenViewSet
from .views import MisconceptionsViewSet
from .views import AugProcessViewSet
from .views import LookForViewSet
from .views import AddSoftwareViewSet
from .views import OutsourcingServViewSet
from .views import BenefitsSoftViewSet
from .views import PremiumSoftViewSet
from .views import SoftwareStagesViewSet
from .views import SoftChooseMetaViewSet
from .views import AdvantagesSoftDevViewSet
from .views import SoftStagesViewSet
from .views import AskedQuestionsViewSet
from .views import EnsureSuccessViewSet
from .views import PremiumCompanyViewSet
from .views import DataScienceServViewSet
from .views import DataApproachViewSet
from .views import OurDataApproachViewSet
from .views import DataUseCaseViewSet
from .views import DataPrivacyViewSet
from .views import MachineLearningViewSet
from .views import OurMachineServViewSet
from .views import DeliverMachineViewSet
from .views import HireMachineViewSet
from .views import FrequentMachineViewSet
from .views import AiDevServiceViewSet
from .views import AiDomainViewSet
from .views import OutsourceAiViewSet
from .views import AiDevQuestionsViewSet
from .views import ExcelAiDevViewSet
from .views import LocationViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'wedos', WeDoViewSet, basename='wedo')
router.register(r'chooseus', ChooseUsViewSet, basename='chooseus')
router.register(r'ourServices', OurServicesViewSet, basename='ourServices')
router.register(r'customservices', CustomServicesViewSet, basename='customservices')
router.register(r'wework', WeWorkViewSet, basename='wework')
router.register(r'techweuse', TechWeUseViewSet, basename='techweuse')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'webactivities', WebActivitiesViewSet, basename='webactivities')
router.register(r'whymeta', WhyMetaViewSet, basename='whymeta')
router.register(r'howwedo', HowWeDoViewSet, basename='howwedo')
router.register(r'casestudies', CaseStudiesViewSet, basename='casestudies') 
router.register(r'ouruxui', OurUxUiViewSet, basename='ouruxui')
router.register(r'uxservice', UxServicesViewSet, basename='uxservice') 
router.register(r'uiservice', UiServicesViewSet, basename='uiservice')
router.register(r'qaAbout', QaAboutViewSet, basename='qaAbout') 
router.register(r'qaWhyMeta', QaWhyMetaViewSet, basename='qaWhyMeta') 
router.register(r'qaHowWeDo', QaHowWeDoViewSet, basename='qaHowWeDo') 
router.register(r'qaTesting', QaTestingViewSet, basename='qaTesting')
router.register(r'cloudOffer', CloudOfferViewSet, basename='cloudOffer') 
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

router.register(r'clients', ClientsViewSet, basename='clients')
router.register(r'techInsights', TechInsightsViewSet, basename='techInsights')
router.register(r'outsourcing', OutsourcingViewSet, basename='outsourcing')
router.register(r'dedicatedTeam', DedicatedTeamViewSet, basename='dedicatedTeam')
router.register(r'hrProcess', HrProcessViewSet, basename='hrProcess')
router.register(r'solutionOffshore', SolutionOffshoreViewSet, basename='solutionOffshore')
router.register(r'staffAugmentation', StaffAugmentationViewSet, basename='staffAugmentation')
router.register(r'planning', PlanningViewSet, basename='planning')
router.register(r'advantagesStaff', AdvantagesStaffViewSet, basename='advantagesStaff')
router.register(r'differenceBetween', DifferenceBetweenViewSet, basename='differenceBetween')
router.register(r'misconceptions', MisconceptionsViewSet, basename='misconceptions')
router.register(r'augProcess', AugProcessViewSet, basename='augProcess')
router.register(r'lookFor', LookForViewSet, basename='lookFor')
router.register(r'addSoftware', AddSoftwareViewSet, basename='addSoftware')
router.register(r'outsourcingServ', OutsourcingServViewSet, basename='outsourcingServ')
router.register(r'benefitsSoft', BenefitsSoftViewSet, basename='benefitsSoft')
router.register(r'premiumSoft', PremiumSoftViewSet, basename='premiumSoft')
router.register(r'softwareStages', SoftwareStagesViewSet, basename='softwareStages')
router.register(r'softChooseMeta', SoftChooseMetaViewSet, basename='softChooseMeta')
router.register(r'advantagesSoftDev', AdvantagesSoftDevViewSet, basename='advantagesSoftDev')
router.register(r'softStages', SoftStagesViewSet, basename='softStages')
router.register(r'askedQuestions', AskedQuestionsViewSet, basename='askedQuestions')
router.register(r'ensureSuccess', EnsureSuccessViewSet, basename='ensureSuccess')
router.register(r'premiumCompany', PremiumCompanyViewSet, basename='premiumCompany')
router.register(r'dataScienceServ', DataScienceServViewSet, basename='dataScienceServ')
router.register(r'dataApproach', DataApproachViewSet, basename='dataApproach')
router.register(r'ourDataApproach', OurDataApproachViewSet, basename='ourDataApproach')
router.register(r'dataUseCase', DataUseCaseViewSet, basename='dataUseCase')
router.register(r'dataPrivacy', DataPrivacyViewSet, basename='dataPrivacy')
router.register(r'machineLearning', MachineLearningViewSet, basename='machineLearning')
router.register(r'ourMachineServ', OurMachineServViewSet, basename='ourMachineServ')
router.register(r'deliverMachine', DeliverMachineViewSet, basename='deliverMachine')
router.register(r'hireMachine', HireMachineViewSet, basename='hireMachine')
router.register(r'frequentMachine', FrequentMachineViewSet, basename='frequentMachine')
router.register(r'aiDevService', AiDevServiceViewSet, basename='aiDevService')
router.register(r'aiDomain', AiDomainViewSet, basename='aiDomain')
router.register(r'outsourceAi', OutsourceAiViewSet, basename='outsourceAi')
router.register(r'aiDevQuestions', AiDevQuestionsViewSet, basename='aiDevQuestions')
router.register(r'excelAiDev', ExcelAiDevViewSet, basename='excelAiDev')
router.register(r'ourLocation', LocationViewSet, basename='ourLocation')


# Include router.urls in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # This is necessary for DRF to work
]
