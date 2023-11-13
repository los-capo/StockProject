from django import forms
from .models import Usuario, Impresora, PC, Notebook, Telefono, ActivoInfraestructura, AbonoCelular, AbonoImpresora, Licencia, AltaLicenciaoffice, AbonoOffice
from .models import EliminacionImpresora, AltaImpresora, AltaTelefono, AltaPc, AltaNotebook, EliminacionNotebook, EliminacionPc, EliminacionTelefono, EliminacionActivo, AltaActivo

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'area': forms.Select(choices=Usuario.AREAS_CHOICES),
            'cargo': forms.Select(choices=Usuario.CARGO_CHOICES),
            'legajo': forms.TextInput(),
            'razon_social': forms.Select(choices=Usuario.RAZONSOCIAL_CHOICES),
            'CATEGORIA_CTT': forms.Select(choices=Usuario.CATEGORIACTT_CHOICES),
            'CCO': forms.Select(choices=Usuario.CCO_CHOICES),
            'DNI': forms.TextInput(),
            'lugar_trab': forms.Select(choices=Usuario.LUGARTRAB_CHOICES),
            'lab_lpg': forms.Select(choices=Usuario.LABPLG_CHOICES),
        }
      

        
#IMPRESORA      
class ImpresorasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImpresorasForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.nombre_apellido}'

    class Meta:
        model = Impresora
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'abono': forms.TextInput(attrs={'oninput': 'this.value = this.value.charAt(0).toUpperCase() + this.value.slice(1)'}),
	    'antiguedad': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
        }

#ACTIVOS
class ActivosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivosForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.nombre_apellido}'
        
    class Meta:
        model = ActivoInfraestructura
        fields = '__all__'
        widgets = {
            'tipo': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'modelo': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'sn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
        }
            

#PC
class PcsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PcsForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.nombre_apellido}'

    class Meta:
        model = PC
        fields = '__all__'
        widgets = {
            'sn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
	    'antiguedad': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'mouse': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'mousesn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'teclado': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'tecladosn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),

        }
        
class NotebooksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NotebooksForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.nombre_apellido}'

    class Meta:
        model = Notebook
        fields = '__all__'
        widgets = {
            'sn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
	    'modelo': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'antiguedad': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'mouse': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'mousesn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),


        }
        
class TelefonosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TelefonosForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.nombre_apellido}'

    class Meta:
        model = Telefono
        fields = '__all__'
        widgets = {
            'numero': forms.TextInput(attrs={'oninput': 'this.value = this.value.charAt(0).toUpperCase() + this.value.slice(1)'}),
            'modelo': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'marca': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'fecha_entrada': forms.DateInput(format='%d/%m/%Y'),
            'fecha_devolucion': forms.DateInput(format='%d/%m/%Y'),
            'antiguedad': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'imei_o_sn': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'accesorio': forms.TextInput(attrs={'oninput': 'this.value = this.value.toUpperCase()'}),
            'plan': forms.Select(),
            'empresa_abono': forms.Select(),
            'lab_lpg': forms.Select(),
            'costo_plan': forms.TextInput(attrs={'oninput': 'this.value = this.value.replace(",", "").replace(".", "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");'}),
        }
        

#ABONOCELULAR
class AbonoCelForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'text-transform:uppercase'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = AbonoCelular
        fields = '__all__'  

#ABONOIMPRESORA
class AbonoImpForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'text-transform:uppercase'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = AbonoImpresora
        fields = '__all__'          




#ELIMINACION ACTIVO
class EliminacionActivoForm(forms.ModelForm):
    class Meta:
        model = EliminacionActivo
        fields = ('motivo_eliminacion',)
        widgets = {
            'motivo_eliminacion': forms.Textarea(attrs={
                'placeholder': 'Ingrese el motivo de la eliminacion',
                'oninput': 'this.value = this.value.toUpperCase()'
            }),
        }        

# ELIMINACION IMPRESORA
class EliminacionImpresoraForm(forms.ModelForm):
    class Meta:
        model = EliminacionImpresora
        fields = ('motivo_eliminacion',)
        widgets = {
            'motivo_eliminacion': forms.Textarea(attrs={
                'placeholder': 'Ingrese el motivo de la eliminacion',
                'oninput': 'this.value = this.value.toUpperCase()'
            }),
        }    
    
# ELIMINACION PC
class EliminacionPcForm(forms.ModelForm):
    class Meta:
        model = EliminacionPc
        fields = ('motivo_eliminacion',)
        widgets = {
            'motivo_eliminacion': forms.Textarea(attrs={
                'placeholder': 'Ingrese el motivo de la eliminacion',
                'oninput': 'this.value = this.value.toUpperCase()'
            }),
        }        
# ELIMINACION NOTEBOOK
class EliminacionNotebookForm(forms.ModelForm):
    class Meta:
        model = EliminacionNotebook
        fields = ('motivo_eliminacion',)
        widgets = {
            'motivo_eliminacion': forms.Textarea(attrs={
                'placeholder': 'Ingrese el motivo de la eliminacion',
                'oninput': 'this.value = this.value.toUpperCase()'
            }),
        }   
     
# ELIMINACION TELEFONO
class EliminacionTelefonoForm(forms.ModelForm):
    class Meta:
        model = EliminacionTelefono
        fields = ('motivo_eliminacion',)
        widgets = {
            'motivo_eliminacion': forms.Textarea(attrs={
                'placeholder': 'Ingrese el motivo de la eliminacion',
                'oninput': 'this.value = this.value.toUpperCase()'
            }),
        }

#ALTA LICENCIA OFFICE
class AltaLicenciaOfficeForm(forms.ModelForm):
    class Meta:
        model = AltaLicenciaoffice
        fields = ()
        widgets = {
        }

        
#ALTA IMPRESORA
class AltaImpresoraForm(forms.ModelForm):
    class Meta:
        model = AltaImpresora
        fields = ()
        widgets = {
        }
        
#ALTA ACTIVO
class AltaActivoForm(forms.ModelForm):
    class Meta:
        model = AltaActivo
        fields = ()
        widgets = {
            
        }

        
#ALTA TELEFONO
class AltaTelefonoForm(forms.ModelForm):
    class Meta:
        model = AltaTelefono
        fields = ()
        widgets = {
        }
        
#ALTA PC
class AltaPcForm(forms.ModelForm):
    class Meta:
        model = AltaPc
        fields = ()
        widgets = {
        }
        
#ALTA NOTEBOOK
class AltaNotebookForm(forms.ModelForm):
    class Meta:
        model = AltaNotebook
        fields = ()
        widgets = {
        }

#LICENCIA
class LicenciaForm(forms.ModelForm):
    class Meta:
        model = Licencia
        fields = ['licenciaoffice']
        widgets = {
            'licenciaoffice': forms.Select(choices=Licencia.OFFICE_CHOICES)
        }
        labels = {
            'licenciaoffice': 'Licencias Office',
        }

class AbonoOffForm(forms.ModelForm):
    class Meta:
        model = AbonoOffice
        fields = '__all__'
        widgets = {
            
        }
