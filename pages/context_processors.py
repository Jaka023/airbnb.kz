from appartments.models import Appartments

def apt_context(request):
    return {'new': Appartments.objects.all().order_by('-id')}