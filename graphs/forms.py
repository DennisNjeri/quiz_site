from django import forms
from .models import EResources

# form for model[ User ] : registration

# form - model[ ProfileModel ]
class PdfResources( forms.ModelForm ):
	class Meta:
		model = EResources
		fields = [ 'pdf', 'Class', 'subject' ]