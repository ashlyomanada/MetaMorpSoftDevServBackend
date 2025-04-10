from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .models import Offer
from .models import WeDo
from .models import ChooseUs
from .models import CustomServices
from .models import WeWork
from .models import TechWeUse
from .models import News
from .models import WebActivities
from .models import WhyMeta
from .models import HowWeDo
from .models import CaseStudies
from .models import OurServices
from .models import OurUxUi
from .models import UxServices
from .models import UiServices
from .models import QaAbout
from .models import QaWhyMeta
from .models import QaHowWeDo
from .models import QaTesting
from .models import CloudOffer
from .models import CloudBenefits
from .models import WhoWeAre
from .models import MissionVission
from .models import CompanyCulture
from .models import ManageTeam
from .models import BusPhilosophy
from .models import HowWeWork
from .models import DevelopmentStage
from .models import AchieveSuccess
from .models import WhyChooseUs
from .models import Partnership
from .models import PartnershipDropDowns
from .models import Clients
from .models import TechInsights
from .models import Outsourcing
from .models import DedicatedTeam
from .models import HrProcess
from .models import SolutionOffshore
from .models import StaffAugmentation
from .models import Planning
from .models import AdvantagesStaff
from .models import DifferenceBetween
from .models import Misconceptions
from .models import AugProcess
from .models import LookFor
from .models import AddSoftware
from .models import OutsourcingServ
from .models import BenefitsSoft
from .models import PremiumSoft
from .models import SoftwareStages
from .models import SoftChooseMeta
from .models import AdvantagesSoftDev
from .models import SoftStages
from .models import AskedQuestions
from .models import EnsureSuccess
from .models import PremiumCompany
from .models import DataScienceServ
from .models import DataApproach
from .models import OurDataApproach
from .models import DataUseCase
from .models import DataPrivacy
from .models import MachineLearning
from .models import OurMachineServ
from .models import DeliverMachine
from .models import HireMachine
from .models import FrequentMachine
from .models import AiDevService
from .models import AiDomain
from .models import OutsourceAi
from .models import AiDevQuestions
from .models import ExcelAiDev
from .models import Location

from .serializers import TaskSerializer
from .serializers import OfferSerializer
from .serializers import WeDoSerializer
from .serializers import ChooseUsSerializer
from .serializers import CustomServicesSerializer
from .serializers import WeWorkSerializer
from .serializers import TechWeUseSerializer
from .serializers import NewsSerializer
from .serializers import WebActivitiesSerializer
from .serializers import WhyMetaSerializer
from .serializers import HowWeDoSerializer
from .serializers import CaseStudiesSerializer
from .serializers import OurServicesSerializer
from .serializers import OurUxUiSerializer
from .serializers import UxServicesSerializer
from .serializers import UiServicesSerializer
from .serializers import QaAboutSerializer
from .serializers import QaWhyMetaSerializer
from .serializers import QaHowWeDoSerializer
from .serializers import QaTestingSerializer
from .serializers import CloudOfferSerializer
from .serializers import CloudBenefitsSerializer
from .serializers import WhoWeAreSerializer
from .serializers import MissionVissionSerializer
from .serializers import CompanyCultureSerializer
from .serializers import ManageTeamSerializer
from .serializers import BusPhilosophySerializer
from .serializers import HowWeWorkSerializer
from .serializers import DevelopmentStageSerializer
from .serializers import AchieveSuccessSerializer
from .serializers import WhyChooseUsSerializer
from .serializers import PartnershipSerializer
from .serializers import PartnershipDropDownsSerializer
from .serializers import ClientsSerializer
from .serializers import TechInsightsSerializer
from .serializers import OutsourcingSerializer
from .serializers import DedicatedTeamSerializer
from .serializers import HrProcessSerializer
from .serializers import SolutionOffshoreSerializer
from .serializers import StaffAugmentationSerializer
from .serializers import PlanningSerializer
from .serializers import AdvantagesStaffSerializer
from .serializers import DifferenceBetweenSerializer
from .serializers import MisconceptionsSerializer
from .serializers import AugProcessSerializer
from .serializers import LookForSerializer
from .serializers import AddSoftwareSerializer
from .serializers import OutsourcingServSerializer
from .serializers import BenefitsSoftSerializer
from .serializers import PremiumSoftSerializer
from .serializers import SoftStagesSerializer
from .serializers import SoftChooseMetaSerializer
from .serializers import AdvantagesSoftDevSerializer
from .serializers import SoftStagesSerializer
from .serializers import AskedQuestionsSerializer
from .serializers import EnsureSuccessSerializer
from .serializers import PremiumCompanySerializer
from .serializers import DataScienceServSerializer
from .serializers import DataApproachSerializer
from .serializers import OurDataApproachSerializer
from .serializers import DataUseCaseSerializer
from .serializers import DataPrivacySerializer
from .serializers import MachineLearningSerializer
from .serializers import OurMachineServSerializer
from .serializers import DeliverMachineSerializer
from .serializers import HireMachineSerializer
from .serializers import FrequentMachineSerializer
from .serializers import AiDevServiceSerializer
from .serializers import AiDomainSerializer
from .serializers import OutsourceAiSerializer
from .serializers import AiDevQuestionsSerializer
from .serializers import ExcelAiDevSerializer
from .serializers import LocationSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer

class WeDoViewSet(viewsets.ModelViewSet):
    queryset = WeDo.objects.all().order_by('-id')
    serializer_class = WeDoSerializer

class ChooseUsViewSet(viewsets.ModelViewSet):
    queryset = ChooseUs.objects.all().order_by('-id')
    serializer_class = ChooseUsSerializer

class CustomServicesViewSet(viewsets.ModelViewSet):
    queryset = CustomServices.objects.all().order_by('-id')
    serializer_class = CustomServicesSerializer

class WeWorkViewSet(viewsets.ModelViewSet):
    queryset = WeWork.objects.all().order_by('-id')
    serializer_class = WeWorkSerializer

class TechWeUseViewSet(viewsets.ModelViewSet):
    queryset = TechWeUse.objects.all().order_by('-id')
    serializer_class = TechWeUseSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all() .order_by('-id')
    serializer_class = NewsSerializer

class WebActivitiesViewSet(viewsets.ModelViewSet):
    queryset = WebActivities.objects.all() .order_by('-id')
    serializer_class = WebActivitiesSerializer

class WhyMetaViewSet(viewsets.ModelViewSet):
    queryset = WhyMeta.objects.all() .order_by('-id')
    serializer_class = WhyMetaSerializer

class HowWeDoViewSet(viewsets.ModelViewSet):
    queryset = HowWeDo.objects.all() .order_by('-id')
    serializer_class = HowWeDoSerializer

class CaseStudiesViewSet(viewsets.ModelViewSet):
    queryset = CaseStudies.objects.all().order_by('-id')
    serializer_class = CaseStudiesSerializer

class OurServicesViewSet(viewsets.ModelViewSet):
    queryset = OurServices.objects.all().order_by('-id')
    serializer_class = OurServicesSerializer

class OurUxUiViewSet(viewsets.ModelViewSet):
    queryset = OurUxUi.objects.all().order_by('-id')
    serializer_class = OurUxUiSerializer

class UxServicesViewSet(viewsets.ModelViewSet):
    queryset = UxServices.objects.all().order_by('-id')
    serializer_class = UxServicesSerializer

class UiServicesViewSet(viewsets.ModelViewSet):
    queryset = UiServices.objects.all().order_by('-id')
    serializer_class = UiServicesSerializer

class QaAboutViewSet(viewsets.ModelViewSet):
    queryset = QaAbout.objects.all().order_by('-id')
    serializer_class = QaAboutSerializer

class QaWhyMetaViewSet(viewsets.ModelViewSet):
    queryset = QaWhyMeta.objects.all().order_by('-id')
    serializer_class = QaWhyMetaSerializer

class QaHowWeDoViewSet(viewsets.ModelViewSet):
    queryset = QaHowWeDo.objects.all().order_by('-id')
    serializer_class = QaHowWeDoSerializer

class QaTestingViewSet(viewsets.ModelViewSet):
    queryset = QaTesting.objects.all().order_by('-id')
    serializer_class = QaTestingSerializer

class CloudOfferViewSet(viewsets.ModelViewSet):
    queryset = CloudOffer.objects.all().order_by('-id')
    serializer_class = CloudOfferSerializer

class CloudBenefitsViewSet(viewsets.ModelViewSet):
    queryset = CloudBenefits.objects.all().order_by('-id')
    serializer_class = CloudBenefitsSerializer

class WhoWeAreViewSet(viewsets.ModelViewSet):
    queryset = WhoWeAre.objects.all().order_by('-id')
    serializer_class = WhoWeAreSerializer

class MissionVissionViewSet(viewsets.ModelViewSet):
    queryset = MissionVission.objects.all().order_by('-id')
    serializer_class = MissionVissionSerializer

class CompanyCultureViewSet(viewsets.ModelViewSet):
    queryset = CompanyCulture.objects.all().order_by('-id')
    serializer_class = CompanyCultureSerializer

class ManageTeamViewSet(viewsets.ModelViewSet):
    queryset = ManageTeam.objects.all().order_by('-id')
    serializer_class = ManageTeamSerializer

class BusPhilosophyViewSet(viewsets.ModelViewSet):
    queryset = BusPhilosophy.objects.all().order_by('-id')
    serializer_class = BusPhilosophySerializer

class HowWeWorkViewSet(viewsets.ModelViewSet):
    queryset = HowWeWork.objects.all().order_by('-id')
    serializer_class = HowWeWorkSerializer

class DevelopmentStageViewSet(viewsets.ModelViewSet):
    queryset = DevelopmentStage.objects.all().order_by('-id')
    serializer_class = DevelopmentStageSerializer

class AchieveSuccessViewSet(viewsets.ModelViewSet):
    queryset = AchieveSuccess.objects.all().order_by('-id')
    serializer_class = AchieveSuccessSerializer

class WhyChooseUsViewSet(viewsets.ModelViewSet):
    queryset = WhyChooseUs.objects.all().order_by('-id')
    serializer_class = WhyChooseUsSerializer

class PartnershipViewSet(viewsets.ModelViewSet):
    queryset = Partnership.objects.all().order_by('-id')
    serializer_class = PartnershipSerializer

class PartnershipDropDownsViewSet(viewsets.ModelViewSet):
    queryset = PartnershipDropDowns.objects.all().order_by('-id')
    serializer_class = PartnershipDropDownsSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all().order_by('-id')
    serializer_class = ClientsSerializer
class TechInsightsViewSet(viewsets.ModelViewSet):
    queryset = TechInsights.objects.all().order_by('-id')
    serializer_class = TechInsightsSerializer
class OutsourcingViewSet(viewsets.ModelViewSet):
    queryset = Outsourcing.objects.all().order_by('-id')
    serializer_class = OutsourcingSerializer
class DedicatedTeamViewSet(viewsets.ModelViewSet):
    queryset = DedicatedTeam.objects.all().order_by('-id')
    serializer_class = DedicatedTeamSerializer
class HrProcessViewSet(viewsets.ModelViewSet):
    queryset = HrProcess.objects.all().order_by('-id')
    serializer_class = HrProcessSerializer
class SolutionOffshoreViewSet(viewsets.ModelViewSet):
    queryset = SolutionOffshore.objects.all().order_by('-id')
    serializer_class = SolutionOffshoreSerializer
class StaffAugmentationViewSet(viewsets.ModelViewSet):
    queryset = StaffAugmentation.objects.all().order_by('-id')
    serializer_class = StaffAugmentationSerializer
class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all().order_by('-id')
    serializer_class = PlanningSerializer
class AdvantagesStaffViewSet(viewsets.ModelViewSet):
    queryset = AdvantagesStaff.objects.all().order_by('-id')
    serializer_class = AdvantagesStaffSerializer
class DifferenceBetweenViewSet(viewsets.ModelViewSet):
    queryset = DifferenceBetween.objects.all().order_by('-id')
    serializer_class = DifferenceBetweenSerializer
class MisconceptionsViewSet(viewsets.ModelViewSet):
    queryset = Misconceptions.objects.all().order_by('-id')
    serializer_class = MisconceptionsSerializer
class AugProcessViewSet(viewsets.ModelViewSet):
    queryset = AugProcess.objects.all().order_by('-id')
    serializer_class = AugProcessSerializer
class LookForViewSet(viewsets.ModelViewSet):
    queryset = LookFor.objects.all().order_by('-id')
    serializer_class = LookForSerializer
class AddSoftwareViewSet(viewsets.ModelViewSet):
    queryset = AddSoftware.objects.all().order_by('-id')
    serializer_class = AddSoftwareSerializer
class OutsourcingServViewSet(viewsets.ModelViewSet):
    queryset = OutsourcingServ.objects.all().order_by('-id')
    serializer_class = OutsourcingServSerializer
class BenefitsSoftViewSet(viewsets.ModelViewSet):
    queryset = BenefitsSoft.objects.all().order_by('-id')
    serializer_class = BenefitsSoftSerializer
class PremiumSoftViewSet(viewsets.ModelViewSet):
    queryset = PremiumSoft.objects.all().order_by('-id')
    serializer_class = PremiumSoftSerializer
class SoftwareStagesViewSet(viewsets.ModelViewSet):
    queryset = SoftwareStages.objects.all().order_by('-id')
    serializer_class = SoftStagesSerializer
class SoftChooseMetaViewSet(viewsets.ModelViewSet):
    queryset = SoftChooseMeta.objects.all().order_by('-id')
    serializer_class = SoftChooseMetaSerializer
class AdvantagesSoftDevViewSet(viewsets.ModelViewSet):
    queryset = AdvantagesSoftDev.objects.all().order_by('-id')
    serializer_class = AdvantagesSoftDevSerializer
class SoftStagesViewSet(viewsets.ModelViewSet):
    queryset = SoftStages.objects.all().order_by('-id')
    serializer_class = SoftStagesSerializer
class AskedQuestionsViewSet(viewsets.ModelViewSet):
    queryset = AskedQuestions.objects.all().order_by('-id')
    serializer_class = AskedQuestionsSerializer
class EnsureSuccessViewSet(viewsets.ModelViewSet):
    queryset = EnsureSuccess.objects.all().order_by('-id')
    serializer_class = EnsureSuccessSerializer
class PremiumCompanyViewSet(viewsets.ModelViewSet):
    queryset = PremiumCompany.objects.all().order_by('-id')
    serializer_class = PremiumCompanySerializer
class DataScienceServViewSet(viewsets.ModelViewSet):
    queryset = DataScienceServ.objects.all().order_by('-id')
    serializer_class = DataScienceServSerializer
class DataApproachViewSet(viewsets.ModelViewSet):
    queryset = DataApproach.objects.all().order_by('-id')
    serializer_class = DataApproachSerializer
class OurDataApproachViewSet(viewsets.ModelViewSet):
    queryset = OurDataApproach.objects.all().order_by('-id')
    serializer_class = OurDataApproachSerializer
class DataUseCaseViewSet(viewsets.ModelViewSet):
    queryset = DataUseCase.objects.all().order_by('-id')
    serializer_class = DataUseCaseSerializer
class DataPrivacyViewSet(viewsets.ModelViewSet):
    queryset = DataPrivacy.objects.all().order_by('-id')
    serializer_class = DataPrivacySerializer
class MachineLearningViewSet(viewsets.ModelViewSet):
    queryset = MachineLearning.objects.all().order_by('-id')
    serializer_class = MachineLearningSerializer
class OurMachineServViewSet(viewsets.ModelViewSet):
    queryset = OurMachineServ.objects.all().order_by('-id')
    serializer_class = OurMachineServSerializer
class DeliverMachineViewSet(viewsets.ModelViewSet):
    queryset = DeliverMachine.objects.all().order_by('-id')
    serializer_class = DeliverMachineSerializer
class HireMachineViewSet(viewsets.ModelViewSet):
    queryset = HireMachine.objects.all().order_by('-id')
    serializer_class = HireMachineSerializer
class FrequentMachineViewSet(viewsets.ModelViewSet):
    queryset = FrequentMachine.objects.all().order_by('-id')
    serializer_class = FrequentMachineSerializer
class AiDevServiceViewSet(viewsets.ModelViewSet):
    queryset = AiDevService.objects.all().order_by('-id')
    serializer_class = AiDevServiceSerializer
class AiDomainViewSet(viewsets.ModelViewSet):
    queryset = AiDomain.objects.all().order_by('-id')
    serializer_class = AiDomainSerializer
class OutsourceAiViewSet(viewsets.ModelViewSet):
    queryset = OutsourceAi.objects.all().order_by('-id')
    serializer_class = OutsourceAiSerializer
class AiDevQuestionsViewSet(viewsets.ModelViewSet):
    queryset = AiDevQuestions.objects.all().order_by('-id')
    serializer_class = AiDevQuestionsSerializer
class ExcelAiDevViewSet(viewsets.ModelViewSet):
    queryset = ExcelAiDev.objects.all().order_by('-id')
    serializer_class = ExcelAiDevSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer
