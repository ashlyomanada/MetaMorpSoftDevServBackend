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
from .models import AboutUxUi
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
from .serializers import AboutUxUiSerializer
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

class AboutUxUiViewSet(viewsets.ModelViewSet):
    queryset = AboutUxUi.objects.all().order_by('-id')
    serializer_class = AboutUxUiSerializer

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
