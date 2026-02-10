from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from.models import shippingAddress
from .models import *
from .models import aboutus
from django.forms.models import ModelForm
from django.forms.widgets import FileInput,PasswordInput
class ProfileForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
        widgets={
            'profile_img':FileInput(),
        }
class CheckoutEditForm(ModelForm):
    class Meta:
        model=shippingAddress
        fields=('address','city','state','zipcode')
class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'profile_img':FileInput(),
        }
        
class AboutForm(ModelForm):
    class Meta:
        model=aboutus
        fields='__all__'
        widgets={
            'image':FileInput(),
            'blog_img':FileInput(),
            'author_img':FileInput(),
        }
class CateForm1(ModelForm):
    class Meta:
        model=category
        fields='__all__'
        widgets={
            'image':FileInput(),
         }
class CateForm2(ModelForm):
    class Meta:
        model=category_1
        fields='__all__'
        widgets={
            'image':FileInput(),
         }
class CateForm3(ModelForm):
    class Meta:
        model=category_2
        fields='__all__'
        widgets={
            'image':FileInput(),
         }
class contactForm(ModelForm):
    class Meta:
        model=contact_us_view
        fields='__all__'
class IndexForm(ModelForm):
    class Meta:
        model=index_collection
        fields='__all__'
        widgets={
            'image_1':FileInput(),
            'image_2':FileInput(),
         }
class InstaForm(ModelForm):
    class Meta:
        model=instagram
        fields='__all__'
        widgets={
            'image_1':FileInput(),
            'image_2':FileInput(),
            'image_3':FileInput(),
            'image_4':FileInput(),
            'image_5':FileInput(),
            'image_6':FileInput(),
         }
class LatestForm(ModelForm):
    class Meta:
        model=latest_news
        fields='__all__'
        widgets={
            'image_1':FileInput(),
            'image_2':FileInput(),
            'image_3':FileInput(),
         }
class LeaveComForm(ModelForm):
    class Meta:
        model=leave_comment
        fields='__all__'
        widgets={
            'image_title':FileInput(),
            'image_writer':FileInput(),
        }
class saleofForm(ModelForm):
    class Meta:
        model=sale_of
        fields='__all__'
        widgets={
            'image':FileInput(),
            
        }
class TeamForm(ModelForm):
    class Meta:
        model=team_members
        fields='__all__'
        widgets={
            'img':FileInput(),
        }

class FormProduct(ModelForm):
    class Meta:
        model=Product
        fields=('unique_id','image','name','price','description','stock')
        widgets={
            'image':FileInput(),
        }
class pendingForm(ModelForm):
    class Meta:
        model=Order
        fields=['complete']

