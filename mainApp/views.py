# Create your views here.
import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from mainApp.models import gallery

@require_POST
def upload( request ):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.

    file = upload_receive( request )

    instance = gallery(image = file)
    instance.save()

    basename = os.path.basename( instance.image.file.name )
    file_dict = {
        'name' : basename,
        'size' : instance.image.file.size,

        # The assumption is that image is a FileField that saves to
        # the 'media' directory.
        'url': settings.MEDIA_URL + basename,
        'thumbnail_url': settings.MEDIA_URL + basename,


        'delete_url': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'delete_type': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, pk ):
    # An example implementation.
    success = True
    try:
        instance = gallery.objects.get( pk = pk )
        os.unlink( instance.image.file.name )
        instance.delete()
    except gallery.DoesNotExist:
        success = False

    return JFUResponse( request, success )