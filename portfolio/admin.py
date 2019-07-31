from django.contrib import admin
from .models import Portfolio

from .models import TravelsA
from .models import TravelsC
from .models import TravelsL

admin.site.register(Portfolio) #admin 사이트에 등록해라

admin.site.register(TravelsA) #admin 사이트에 등록해라
admin.site.register(TravelsC) #admin 사이트에 등록해라
admin.site.register(TravelsL) #admin 사이트에 등록해라

