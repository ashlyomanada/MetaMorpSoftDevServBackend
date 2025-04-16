from rest_framework import serializers
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

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class WeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeDo
        fields = '__all__'

class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = '__all__'

class CustomServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomServices
        fields = '__all__'

class WeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeWork
        fields = '__all__'

class TechWeUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechWeUse
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class WebActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebActivities
        fields = '__all__'

class WhyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyMeta
        fields = '__all__'

class HowWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeDo
        fields = '__all__'
        
class CaseStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudies
        fields = '__all__'

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = '__all__'

class OurUxUiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUxUi
        fields = '__all__'

class UxServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UxServices
        fields = '__all__'

class UiServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UiServices
        fields = '__all__'

class QaAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaAbout
        fields = '__all__'

class QaWhyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaWhyMeta
        fields = '__all__'

class QaHowWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaHowWeDo
        fields = '__all__'

class QaTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaTesting
        fields = '__all__'

class CloudOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudOffer
        fields = '__all__'

class CloudBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudBenefits
        fields = '__all__'

class WhoWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoWeAre
        fields = '__all__'

class MissionVissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVission
        fields = '__all__'

class CompanyCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCulture
        fields = '__all__'

class ManageTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageTeam
        fields = '__all__'

class BusPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusPhilosophy
        fields = '__all__'

class HowWeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWork
        fields = '__all__'

class DevelopmentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class AchieveSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveSuccess
        fields = '__all__'

class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'

class PartnershipDropDownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipDropDowns
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
class TechInsightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechInsights
        fields = '__all__'
class OutsourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outsourcing
        fields = '__all__'
class DedicatedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DedicatedTeam
        fields = '__all__'
class HrProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrProcess
        fields = '__all__'
class SolutionOffshoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionOffshore
        fields = '__all__'
class StaffAugmentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAugmentation
        fields = '__all__'
class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = '__all__'
class AdvantagesStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesStaff
        fields = '__all__'
class DifferenceBetweenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferenceBetween
        fields = '__all__'
class MisconceptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misconceptions
        fields = '__all__'
class AugProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugProcess
        fields = '__all__'
class LookForSerializer(serializers.ModelSerializer):
    class Meta:
        model = LookFor
        fields = '__all__'
class AddSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSoftware
        fields = '__all__'
class OutsourcingServSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourcingServ
        fields = '__all__'
class BenefitsSoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitsSoft
        fields = '__all__'
class PremiumSoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumSoft
        fields = '__all__'
class SoftwareStagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareStages
        fields = '__all__'
class SoftChooseMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftChooseMeta
        fields = '__all__'
class AdvantagesSoftDevSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesSoftDev
        fields = '__all__'
class SoftStagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftStages
        fields = '__all__'
class AskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskedQuestions
        fields = '__all__'
class EnsureSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnsureSuccess
        fields = '__all__'
class PremiumCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumCompany
        fields = '__all__'
class DataScienceServSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataScienceServ
        fields = '__all__'
class DataApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataApproach
        fields = '__all__'
class OurDataApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurDataApproach
        fields = '__all__'
class DataUseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseCase
        fields = '__all__'
class DataPrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPrivacy
        fields = '__all__'
class MachineLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearning
        fields = '__all__'
class OurMachineServSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMachineServ
        fields = '__all__'
class DeliverMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverMachine
        fields = '__all__'
class HireMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireMachine
        fields = '__all__'
class FrequentMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentMachine
        fields = '__all__'
class AiDevServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiDevService
        fields = '__all__'
class AiDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiDomain
        fields = '__all__'
class OutsourceAiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourceAi
        fields = '__all__'
class AiDevQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiDevQuestions
        fields = '__all__'
class ExcelAiDevSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelAiDev
        fields = '__all__'
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        

        