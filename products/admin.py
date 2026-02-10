from django.contrib import admin
from.models import category
from.models import category_1
from.models import category_2
from .models import sale_of
from .models import instagram
from .models import latest_news
from .models import newletter
from .models import index_collection
from .models import logo
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(sale_of)
admin.site.register(instagram)
admin.site.register(latest_news)
admin.site.register(newletter)
admin.site.register(index_collection)
admin.site.register(logo)
admin.site.register(contact_us_view)
admin.site.register(Product)
admin.site.register(category_1)
admin.site.register(category_2)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(shippingAddress)
admin.site.register(contact_us_message)
admin.site.register(leave_comment)
admin.site.register(send_comment)
admin.site.register(aboutus)
admin.site.register(team_members)
