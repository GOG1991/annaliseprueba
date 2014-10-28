from annalise_investors.models import InvestorUser
from django.forms import ModelForm

class InvestorsUserForm(ModelForm):
    class Meta:
        model = InvestorUser

    def __init__(self, *args, **kwargs):
        super(InvestorsUserForm, self).__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs={'placeholder':'Nombres', 'class':'form-control input-lg','maxlength':'48'}
        self.fields['apPaterno'].widget.attrs={'placeholder':'Apellido paterno', 'class':'form-control input-lg'}
        self.fields['apMaterno'].widget.attrs={'placeholder':'Apellido materno', 'class':'form-control input-lg'}
        self.fields['genero'].widget.attrs={'class':'form-control input-lg'}
        self.fields['fechNacimiento'].widget.attrs={'placeholder':'Fecha de nacimiento ejemplo 22/04/1990', 'class':'form-control input-lg'}
        self.fields['pais'].widget.attrs={'class':'form-control input-lg'}
        self.fields['estadoPais'].widget.attrs={'class':'form-control input-lg'}
        self.fields['ciudad'].widget.attrs={'class':'form-control input-lg'}
        self.fields['estadoCivil'].widget.attrs={'class':'form-control input-lg'}
        self.fields['curp'].widget.attrs={'placeholder':'CURP (18 caracteres)', 'class':'form-control input-lg','maxlength':'18'}
        self.fields['imss'].widget.attrs={'placeholder':'IMMS (11 numeros)', 'class':'form-control input-lg','min':'0','maxlength':'11'}
        self.fields['numHijos'].widget.attrs={'placeholder':'Numero de hijos', 'class':'form-control input-lg','min':'0','value':'0'}
        self.fields['colonia'].widget.attrs={'placeholder':'Colonia', 'class':'form-control input-lg'}
        self.fields['calle'].widget.attrs={'placeholder':'Calle', 'class':'form-control input-lg'}
        self.fields['numExterior'].widget.attrs={'placeholder':'Numero exterior', 'class':'form-control input-lg'}
        self.fields['numInterior'].widget.attrs={'placeholder':'NUmero interior', 'class':'form-control input-lg'}
        self.fields['telCasa'].widget.attrs={'placeholder':'Telefono', 'class':'form-control input-lg','maxlength':'15'}
        self.fields['celular'].widget.attrs={'placeholder':'Celular (10 digitos minimo)', 'class':'form-control input-lg','maxlength':'15'}
        self.fields['contPrim'].widget.attrs={'class':'form-control input-lg'}
        self.fields['contSec'].widget.attrs={'class':'form-control input-lg'}


