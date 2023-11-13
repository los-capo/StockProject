from django.db import models
from django.core.validators import MinValueValidator
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

#ABONOSCELULAR
class AbonoCelular(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"

#ABONOOFFICE
class AbonoOffice(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
     
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"

#ABONOSIMPRSORA
class AbonoImpresora(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
     
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"

# USUARIO - CRUD Funciona
class Usuario(models.Model):

    AREAS_CHOICES = [
        ('-', '-'),
        ('PLAN DE AHORRO', 'PLAN DE AHORRO'),
        ('REPUESTOS', 'REPUESTOS'),
        ('VENTA DIRECTA 0KM SUC', 'VENTA DIRECTA 0KM SUC'),
        ('ADM VENTAS', 'ADM VENTAS'), 
        ('SIN CLASIFICAR', 'SIN CLASIFICAR'),
        ('ADM VENTAS PLANES', 'ADM VENTAS PLANES'),
        ('SERVICIOS PV', 'SERVICIOS PV'),
        ('CONTACT C', 'CONTACT C'),
        ('VENTA DIRECTA 0KM', 'VENTA DIRECTA 0KM'),
        ('ADM POST VENTA', 'ADM POST VENTA'),
        ('ADMINISTRACION', 'ADMINISTRACION'),
        ('ADMINISTRACION CENTRAL', 'ADMINISTRACION CENTRAL'),
        ('PREENT Y ALISTAJE VN', 'PREENT Y ALISTAJE VN'),
        ('POST VENTA SERVICIOS', 'POST VENTA SERVICIOS'),
        ('REPUESTOS SUCURSAL', 'REPUESTOS SUCURSAL'),
        ('TALLER SUCURSAL', 'TALLER SUCURSAL'),
        ('PLAN DE AHORRO SUCURSAL', 'PLAN DE AHORRO SUCURSAL'),
        ('SISTEMAS', 'SISTEMAS'),
        ('LAVADERO','LAVADERO'),
	('TALLER','TALLER'),
	('MKT','MKT'),
	('COMERCIAL','COMERCIAL'),
	('GESTORIA','GESTORIA'),
	('MAESTRANZA','MAESTRANZA'),
	('VENTA DIRECTA VO','VENTA DIRECTA VO'),
	('PREENT Y ALISTAJE VO','PREENT Y ALISTAJE VO'),
	('ADMINISTRACION SUCURSAL','ADMINISTRACION SUCURSAL'),
	('ADM POST VENTA SUCURSAL','ADM POST VENTA SUCURSAL'),
	('GERENTE COMERCIAL','GERENTE COMERCIAL'),
	('ENTREGAS VN','ENTREGAS VN'),
	('REPUESTOS_NEW','REPUESTOS *'),
	('SERVICIOS_NEW','SERVICIOS *'),
    ]
    
    LABPLG_CHOICES = [
	('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('PEUGEOT CORDOBA','PEUGEOT CORDOBA'),
    ]
    
    LUGARTRAB_CHOICES = [
	('-','-'),
        ('CORDOBA','CORDOBA'),
        ('BUENOS AIRES','BUENOS AIRES'),
        ('SANTA FE','SANTA FE'),
        ('CAPITAL FEDERAL','CAPITAL FEDERAL'),
    ]
    
    CCO_CHOICES = [
	('-','-'),
        ('PDA','PDA'),
        ('REPUESTOS','REPUESTOS'),
        ('0KM','0KM'),
        ('ADM. COMERCIAL','ADM. COMERCIAL'),
        ('(****)SIN CLASIFICAR','(****)SIN CLASIFICAR'),
        ('ADM. PLAN DE AHOROR','ADM. PLAN DE AHORRO'),
        ('TALLER','TALLER'),
        ('MKT','MKT'),
        ('CONT. E IMP.','CONT. E IMP.'),
        ('SISTEMAS','SISTEMAS'),
        ('ADMINISTRACION','ADMINISTRACION'),
        ('PREENTREGA','PREENTREGA'),
        ('USADOS','USADOS'),
        ('AUDITORIAS','AUDITORIAS'),
        ('RRHH','RRHH'),
        ('TESORERIA','TESORERIA'),
        ('COMPRAS','COMPRAS'),
        ('CALIDAD','CALIDAD'),
        ('ESPECIAL','ESPECIAL'),
        ('MANTENIMIENTO','MANTENIMIENTO'),
        ('LOGISTICA','LOGISTICA'),

    ]
    
    RAZONSOCIAL_CHOICES = [
	('-','-'),
        ('IQSA S.A.','IQSA S.A.'),
        ('AUTOROUTE S.A.','AUTOROUTE S.A.'),
        ('AVENUE S.A.','AVENUE S.A.'),
        ('AUTO MUNICH S.A.','AUTO MUNICH S.A.'),
        ('AILES S.A.','AILES S.A.'),
        ('CHEVENT S.A.','CHEVENT S.A.'),
        ('VOLANT S.A.','VOLANT S.A.'),
    ]
    
    CATEGORIACTT_CHOICES = [
	('-','-'),
        ('VEND Y/O PROM DE PLANES','VEND Y/O PROM DE PLANES'),
        ('ESPECIALISTA EN SERVICIOS','ESPECIALISTA EN SERVICIOS'),
        ('VENDEDOR Y/O PROM DE VENTAS','VENDEDOR Y/O PROM DE VENTAS'),
        ('EXCLUIDO DE CONVENIO','EXCLUIDO DE CONVENIO'),
        ('ADM MULTIPLE ESPECIALIZADO','ADM MULTIPLE ESPECIALIZADO'),
        ('ADMINISTRATIVO ESPECIALIZADO','ADMINISTRATIVO ESPECIALIZADO'),
        ('ESPECIALISTA MULT SUP EN SERV','ESPECIALISTA MULT SUP EN SERV'),
        ('ESPECIALISTA SUP. EN SER. MOTO','ESPECIALISTA SUP. EN SER. MOTO'),
        ('ADMINISTRATIVO BASICO','ADMINISTRATIVO BASICO'),
        ('ADMINISTRATIVO AUXILIAR','ADMINISTRATIVO AUXILIAR'),
        ('ADMINISTRATIVO CALIFICADO','ADMINISTRATIVO CALIFICADO'),
        ('ESPECIALISTA SUPERIOR EN SERV','ESPECIALISTA SUPERIOR EN SERV'),
        ('LAVADOR','LAVADOR'),
        ('EXPERTO EN SERVICIOS','EXPERTO EN SERVICIOS'),
        ('AYUDANTE EN SERVICIOS','AYUDANTE EN SERVICIOS'),
        ('MAESTRANZA A','MAESTRANZA A'),
        ('LOGISTICA','LOGISTICA'),
    ]
    
    CARGO_CHOICES = [
	('-','-'),
        ('VENDEDOR','VENDEDOR'),
        ('SIN CLASIFICAR','SIN CLASIFICAR'),
        ('ADMINISTRATIVO','ADMINISTRATIVO'),
        ('RESPONSABLE ADM PLANES','RESPONSABLE ADM PLANES'),
        ('MECANICO','MECANICO'),
        ('CONTACT C','CONTACT C'),
        ('AUXILIAR','AUXILIAR'),
        ('TECNICO','TECNICO'),
        ('PREPARADOR','PREPARADOR'),
        ('RESPNSABLE COMERCIAL','RESPNSABLE COMERCIAL'),
        ('SUBCONTADOR','SUBCONTADOR'),
        ('SUPERVISOR','SUPERVISOR'),
        ('PREENTREGA Y ALISTAJE','PREENTREGA Y ALISTAJE'),
        ('DESARROLLO INFORMATICO','DESARROLLO INFORMATICO'),
        ('LAVADOR','LAVADOR'),
        ('RESPONSABLE PV','RESPONSABLE PV'),
        ('SOPORTE INFORMATICO','SOPORTE INFORMATICO'),
        ('GERENTE COMERCIAL','GERENTE COMERCIAL'),
        ('ADMINISTRATIVO PV','ADMINISTRATIVO PV'),
        ('CREDITOS','CREDITOS'),
        ('GERENTE PLAN DE AHORRO','GERENTE PLAN DE AHORRO'),
        ('RRHH','RRHH'),
        ('ATENCION AL CLIENTE','ATENCION AL CLIENTE'),
        ('MANAGER PV','MANAGER PV'),
        ('MAESTRANZA','MAESTRANZA'),
        ('GERENTE POST VENTA','GERENTE POST VENTA'),
        ('RESPONSABLE REPUESTOS','RESPONSABLE REPUESTOS'),
        ('GUARDIA DE SEGURIDAD','GUARDIA DE SEGURIDAD'),
        ('JEFE DE TALLER','JEFE DE TALLER'),
        ('CALIDAD','CALIDAD'),
        ('PERITADOR','PERITADOR'),
        ('RESPONSABLE COMERCIAL','RESPONSABLE COMERCIAL'),
        ('ENTREGAS','ENTREGAS'),
        ('REPUESTOS','REPUESTOS'),
        ('JEFATURA REPUESTOS','JEFATURA REPUESTOS'),
        ('GERENTE MKT','GERENTE MKT'),
        ('GESTORIA','GESTORIA'),
        ('CAJA','CAJA'),
        ('DIRECTOR','DIRECTOR'),
        ('GERENTE DE RRHH','GERENTE DE RRHH'),
        ('INHABILITADO','INHABILITADO'),

        
    ]

    area = models.CharField(max_length=100,blank=False,default="", choices=AREAS_CHOICES)
    nombre_apellido = models.CharField(max_length=100,blank=False, default="")
    legajo = models.CharField(max_length=100,  blank=False, default="")
    razon_social = models.CharField( max_length=100, blank=False, default="", choices=RAZONSOCIAL_CHOICES)
    DNI = models.CharField(max_length=100,  blank=False, default="")
    CATEGORIA_CTT = models.CharField(max_length=100,  blank=False, default="", choices=CATEGORIACTT_CHOICES)
    cargo = models.CharField(max_length=100,  blank=False, default="", choices=CARGO_CHOICES)
    CCO = models.CharField(max_length=100,  blank=False, default="", choices=CCO_CHOICES)
    lugar_trab = models.CharField(max_length=100,  blank=False, default="", choices=LUGARTRAB_CHOICES)
    lab_lpg = models.CharField(max_length=100,  blank=False, default="", choices=LABPLG_CHOICES) 

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.nombre_apellido} ({self.cargo} - {self.area}) Legajo: {self.legajo} - Categoria CTT: {self.CATEGORIA_CTT} - CCO: {self.CCO} - DNI: {self.DNI} - Lugar de Trabajo: {self.lugar_trab} - Lab LPG: {self.lab_lpg}"

class Licencia(models.Model):

    OFFICE_CHOICES = [

        ('Exchange Online (plan 1)','Exchange Online (plan 1)'),
        ('Office 365 E1','Office 365 E1'),
        ('Office 365 E5','Office 365 E5'),
        ('Office 365 E5 sin Audioconferencia','Office 365 E5 sin Audioconferencia'),
        ('Quiosco de Exchange Online','Quiosco de Exchange Online'),

    ]


    PRECIOS = {

        'Office 365 E1': 3836.00,
        'Office 365 E5': 14139.00,
        'Office 365 E5 sin Audioconferencia': 14139.00,
        'Exchange Online (plan 1)': 1453.00,
        'Quiosco de Exchange Online': 770.00,

    }

    licenciaoffice = models.CharField(max_length=100, blank=False, choices=OFFICE_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Licencias"
        
    def __str__(self):
        return f"Microsoft {self.licenciaoffice}"
    
    def get_precio_licenciaoffice(self):
        return self.PRECIOS.get(self.licenciaoffice, 0)

#ALTA LICENCIAOFFICE
class AltaLicenciaoffice(models.Model):
    licencia = models.ForeignKey(Licencia, on_delete=models.CASCADE, default=1)
    nombrelicencia = models.CharField(max_length=100)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)

# TELEFONOS - CRUD Funciona
class Telefono(models.Model):
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Roto', 'Roto'),
    ]
    REPARABILIDAD_CHOICES = [
        ('Reparable', 'Reparable'),
        ('Irreparable', 'Irreparable'),
    ]
    
    RS_CHOICES = [
	('-','-'),
        ('AMSA', 'PERSONAL - AMSA'),
        ('AVENUE', 'PERSONAL - AVENUE'),
        ('VOLANT', 'PERSONAL - VOLANT'),
        ('IQSA', 'PERSONAL - IQSA'),
        ('CHEVENT', 'CLARO - CHEVENT'),
        ('AILES', 'CLARO - AILES'),
        ('AUTOROUTE', 'CLARO - AUTOROUTE'),
        ('CLAROAVENUECBA', 'CLARO - AVENUE CORDOBA'),
    ]

    PLAN_CHOICES = [

	('-','-'),
        ('Plan Control Empresas 1gb', 'Plan Control Empresas 1gb'),
        ('Empresas Conexion Control M - PERSONAL', 'Empresas Conexion Control M - PERSONAL'),
        ('Plan Libre Empresas 3gb', 'Plan Libre Empresas 3gb'),
        ('Plan Libre Empresas 5gb', 'Plan Libre Empresas 5gb'),
        ('Plan Libre Empresas 8gb', 'Plan Libre Empresas 8gb'),
        ('Plan Control Empresas 3gb', 'Plan Control Empresas 3gb'),
        ('Plan Control Empresas 5gb', 'Plan Control Empresas 5gb'),
        ('Conexion Total Premium XX', 'Conexion Total Premium XX'),
        ('Plan Control 3GB PC72R', 'Plan Control 3GB PC72R'),
        ('Plan Control 3GB PC52R', 'Plan Control 3GB PC52R'),
        ('Plan Control 5GB PC73R',' Plan Control 5GB PC73R'),
        ('Plan Control 8GB PC74R', ' Plan Control 8GB PC74R'),
        ('Plan Control 3GB PC52R - AUTOROUTE','Plan Control 3GB PC52R - AUTOROUTE'),
        ('Plan Control 5GB PC73R - AUTOROUTE','Plan Control 5GB PC73R - AUTOROUTE'),
        ('Plan Control 5GB PC53R - AUTOROUTE','Plan Control 5GB PC53R - AUTOROUTE'),
        ('Plan Control 3GB PC72R - AUTOROUTE','Plan Control 3GB PC72R - AUTOROUTE'),
        ('Plan Control 5GB PC73R - AILES','Plan Control 5GB PC73R - AILES'),
        ('Plan Control 3GB PC72R - AILES','Plan Control 3GB PC72R - AILES'),
        ('Plan Libre 8GB PC74C - AILES','Plan Libre 8GB PC74C - AILES'),
        ('Plan Control 8GB PC54R - AILES','Plan Control 8GB PC54R - AILES'),
        ('Plan Control 5GB PC83R - AILES','Plan Control 5GB PC83R - AILES'),
        ('Plan Control 1GB PC70R - AILES','Plan Control 1GB PC70R - AILES'),
        ('Plan Control 3GB PC52R - AILES','Plan Control 3GB PC52R - AILES'),
        ('Plan Control 5GB PC53R - AILES','Plan Control 5GB PC53R - AILES'),
        ('Plan Control 8GB PC74R - AILES','Plan Control 8GB PC74R - AILES'),
        ('Plan Control 2GB PC71R - AILES','Plan Control 2GB PC71R - AILES'),
        ('Plan Control 3GB PC82R - AILES','Plan Control 3GB PC82R - AILES'),
        ('Plan Control 8GB PC93R - AILES','Plan Control 8GB PC93R - AILES'),

    ]

    EMPRESAABONO_CHOICES = [
	('SINEMPRESA','SIN EMPRESA'),
	('PERSONAL','PERSONAL'),
	('CLARO','CLARO'),
    ]

    LABPLG_CHOICES = [
	('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('PEUGEOT CORDOBA','PEUGEOT CORDOBA'),
    ]


    estado = models.CharField(max_length=100, default='Nuevo', choices=ESTADO_CHOICES)
    reparabilidad = models.CharField(
        max_length=100, default='Reparable', choices=REPARABILIDAD_CHOICES, null=True, blank=True
    )
    numero = models.CharField(max_length=100,blank=False, default="")
    modelo = models.CharField(max_length=100,blank=False, default="")
    marca = models.CharField(max_length=100,blank=False, default="")
    fecha_entrada = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    fecha_devolucion = models.DateField(default=datetime.date(1, 1, 1))
    imei_o_sn = models.CharField(max_length=100,blank=False, default="")
    accesorio = models.CharField(max_length=100,blank=False, default="") 
    plan = models.CharField(max_length=100, default='Nuevo', choices=PLAN_CHOICES)
    empresa_abono = models.CharField(max_length=100, default="", choices=EMPRESAABONO_CHOICES)
    rs = models.CharField(max_length=100, default='Nuevo', choices=RS_CHOICES)
    lablpg = models.CharField(max_length=100,  blank=False, default="", choices=LABPLG_CHOICES) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
       
    class Meta:
        verbose_name_plural = "Telefonos"

    def __str__(self):
        return f"Telefono - Numero: {self.numero} - Modelo: {self.modelo} - Empresa: {self.empresa_abono} - Usuario: {self.usuario}"
 
#EMPRESA
class Empresa(models.Model):

    MARCA_CHOICES = [
        ('FIAT','FIAT'),
        ('RENAULT','RENAULT'),
        ('PEUGEOT','PEUGEOT'),
        ('DS','DS'),
        ('CITROEN','CITROEN'),
        ('BMW','BMW'),
        ('CHEVROLET','CHEVROLET'),
          ]

    CONSECIONARIO_CHOICES = [
	('-','-'),
        ('AVEC','AVEC'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('CENTRO AUTOMOTORES','CENTRO AUTOMOTORES'),
        ('DS STORE','DS STORE'),
        ('AUTOMUNICH','AUTOMUNICH'),
        ('CHEVENT','CHEVENT'),
                 ]

    marca = models.CharField( max_length=100, blank=False, default="", choices=MARCA_CHOICES)
    consecionario = models.CharField( max_length=100, blank=False, default="", choices=CONSECIONARIO_CHOICES)

# NOTEBOOK - CRUD Funciona
class Notebook(models.Model):

    MARCAS_CHOICES = [
        ('hp', 'HP'),
        ('asus', 'Asus'),
        ('lenovo', 'Lenovo'),
        ('xpg', 'Xpg'),
        ('dell', 'Dell'),
        ('acer', 'Acer'),
        ('macbook', 'Macbook'),
        ('samsung', 'Samgung'),
        ('vaio', 'Vaio'),
        ('sony', 'Sony'),
        ('bangho', 'Bangho'),
        ('gigabyte', 'Gigabyte'),
    ]

    LABPLG_CHOICES = [
	('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),
    ]

    
    marca = models.CharField(max_length=100, choices=MARCAS_CHOICES, default='marca1')
    PROCESADORES_CHOICES = [
        ("Celeron", "Celeron"),
        ("Pentium", "Pentium"),
        ("Intel Core i3 (1ma generacion)", "Intel Core i3 (1ma generacion)"),
        ("Intel Core i3 (2ma generacion)", "Intel Core i3 (2ma generacion)"),
        ("Intel Core i3 (3ma generacion)", "Intel Core i3 (3ma generacion)"),
        ("Intel Core i3 (4ma generacion)", "Intel Core i3 (4ma generacion)"),
        ("Intel Core i3 (5ma generacion)", "Intel Core i3 (5ma generacion)"),
        ("Intel Core i3 (6ma generacion)", "Intel Core i3 (6ma generacion)"),
        ("Intel Core i3 (7ma generacion)", "Intel Core i3 (7ma generacion)"),
        ("Intel Core i3 (8va generacion)", "Intel Core i3 (8va generacion)"),
        ("Intel Core i3 (9na generacion)", "Intel Core i3 (9na generacion)"),
        ("Intel Core i3 (10ma generacion)", "Intel Core i3 (10ma generacion)"),
        ("Intel Core i3 (11va generacion)", "Intel Core i3 (11ma generacion)"),
        ("Intel Core i3 (12va generacion)", "Intel Core i3 (12ma generacion)"),
        ("Intel Core i5 (1ma generacion)", "Intel Core i5 (1ma generacion)"),
        ("Intel Core i5 (2ma generacion)", "Intel Core i5 (2ma generacion)"),
        ("Intel Core i5 (3ma generacion)", "Intel Core i5 (3ma generacion)"),
        ("Intel Core i5 (4ma generacion)", "Intel Core i5 (4ma generacion)"),
        ("Intel Core i5 (5ma generacion)", "Intel Core i5 (5ma generacion)"),
        ("Intel Core i5 (6ma generacion)", "Intel Core i5 (6ma generacion)"),
        ("Intel Core i5 (7ma generacion)", "Intel Core i5 (7ma generacion)"),
        ("Intel Core i5 (8va generacion)", "Intel Core i5 (8va generacion)"),
        ("Intel Core i5 (9na generacion)", "Intel Core i5 (9na generacion)"),
        ("Intel Core i5 (10ma generacion)", "Intel Core i5 (10ma generacion)"),
        ("Intel Core i5 (11va generacion)", "Intel Core i5 (11va generacion)"),
        ("Intel Core i5 (12va generacion)", "Intel Core i5 (12va generacion)"),
        ("Intel Core i7 (2da generacion)", "Intel Core i7 (2da generacion)"),
        ("Intel Core i7 (8va generacion)", "Intel Core i7 (8va generacion)"),
        ("Intel Core i7 (9na generacion)", "Intel Core i7 (9na generacion)"),
        ("Intel Core i7 (10ma generacion)", "Intel Core i7 (10ma generacion)"),
        ("Intel Core i7 (11va generacion)", "Intel Core i7 (11va generacion)"),
        ("Intel Core i7 (12va generacion)", "Intel Core i7 (12va generacion)"),
        ("Intel Core i9 (9na generacion)", "Intel Core i9 (9na generacion)"),
        ("Intel Core i9 (10ma generacion)", "Intel Core i9 (10ma generacion)"),
        ("AMD Ryzen 3 (1ra generacion)", "AMD Ryzen 3 (1ra generacion)"),
        ("AMD Ryzen 3 (2da generacion)", "AMD Ryzen 3 (2da generacion)"),
        ("AMD Ryzen 5 (1ra generacion)", "AMD Ryzen 5 (1ra generacion)"),
        ("AMD Ryzen 5 (2da generacion)", "AMD Ryzen 5 (2da generacion)"),
        ("AMD Ryzen 7 (1ra generacion)", "AMD Ryzen 7 (1ra generacion)"),
        ("AMD Ryzen 7 (2da generacion)", "AMD Ryzen 7 (2da generacion)"),
        ("AMD Ryzen 9 (1ra generacion)", "AMD Ryzen 9 (1ra generacion)"),
        ("AMD Ryzen 9 (2da generacion)", "AMD Ryzen 9 (2da generacion)"),
        ("AMD A6", "AMD A6"),
        ("AMD A8", "AMD A8"),
        ("AMD A10", "AMD A10"),
        ("AMD A12", "AMD A12"),

        # procesadores 
    ]
    procesador = models.CharField(max_length=100, choices=PROCESADORES_CHOICES, default='procesador1')
    RAM_CHOICES = [
        ('ram4gbddr3', '4GB ddr3'),
        ('ram8gbddr3', '8GB ddr3'),
	('ram12gbddr3', '12GB ddr3'),
        ('ram16gbddr3', '16GB ddr3'),
        ('ram32gbddr3', '32GB ddr3'),
        ('ram4gb', '4GB ddr4'),
        ('8GB ddr4', '8GB ddr4'),
	('ram12gbddr4', '12GB ddr4'),
        ('ram16gb', '16GB ddr4'),
        ('ram32gb', '32GB ddr4'),
        # opciones de RAM
    ]
    ram = models.CharField(max_length=50, choices=RAM_CHOICES, default='ram4gb')
    
    DISCOS_CHOICES = [
        ('SSD120GB', 'SSD 120 GB'),
        ('SSD240GB', 'SSD 240 GB'),
        ('SSD480GB', 'SSD 480 GB'),
        ('SSD1TB', 'SSD 1 TB'),
        ('SSD2TB', 'SSD 2 TB'),
        ('HDD500GB', 'HDD 500 GB'),
        ('HDD1TGB', 'HDD 1TB '),
        ('HDD2T', 'HDD 2TB'),
        ('HDD3TB', 'HDD 3TB'),
        ('HDD4TB', 'HDD 4TB'),
        # discos
    ]
    
    disco = models.CharField(max_length=50, choices=DISCOS_CHOICES, default='disco128gb')
    
    MONITORES_CHOICES = [
        ('monitor13', '13 pulgadas'),
        ('monitor15', '15 pulgadas'),
        ('monitor17', '17 pulgadas'),
        ('monitor17', '22 pulgadas'),
        ('monitor17','24 pulgadas'),
        ('monitor17','27 pulgadas'),
        ('monitor17', '32 pulgadas'),
        #monitores
    ]
    
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Roto', 'Roto'),
    ]
    REPARABILIDAD_CHOICES = [
        ('Reparable', 'Reparable'),
        ('Irreparable', 'Irreparable'),
    ]
    estado = models.CharField(max_length=100, default='Nuevo', choices=ESTADO_CHOICES)
    reparabilidad = models.CharField(
        max_length=100, default='Reparable', choices=REPARABILIDAD_CHOICES, null=True, blank=True
    )
    monitor = models.CharField(max_length=100, choices=MONITORES_CHOICES, default="")
    lablpg = models.CharField(max_length=100, choices=LABPLG_CHOICES, default="")
    modelo = models.CharField(max_length=100, blank=False, default="")
    mouse = models.CharField(max_length=100, blank=False, default="")
    mousesn = models.CharField(max_length=100, blank=False, default="")
    sn = models.CharField(max_length=100, blank=False, default="")
    antiguedad = models.CharField(max_length=100,blank=False, default="")
    fecha_entrada = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    fecha_devolucion = models.DateField(default=datetime.date(1, 1, 1))
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
    
    class Meta:
        verbose_name_plural = "Notebooks"

    def __str__(self):
        return f"Notebook - Usuario: {self.usuario} - Procesador: {self.procesador} - RAM: {self.ram} - Disco: {self.disco} - Monitor: {self.monitor} - Mouse: {self.mouse} - Mousesn: {self.mousesn}"



# PC - CRUD Funciona
class PC(models.Model):
    LABPLG_CHOICES = [
	    ('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),
    ]
    PROCESADOR_CHOICES = (
        
        ("Celeron", "Celeron"),
        ("Pentium", "Pentium"),
        ("Intel Core i3 (1ma generacion)", "Intel Core i3 (1ma generacion)"),
        ("Intel Core i3 (2ma generacion)", "Intel Core i3 (2ma generacion)"),
        ("Intel Core i3 (3ma generacion)", "Intel Core i3 (3ma generacion)"),
        ("Intel Core i3 (4ma generacion)", "Intel Core i3 (4ma generacion)"),
        ("Intel Core i3 (5ma generacion)", "Intel Core i3 (5ma generacion)"),
        ("Intel Core i3 (6ma generacion)", "Intel Core i3 (6ma generacion)"),
        ("Intel Core i3 (7ma generacion)", "Intel Core i3 (7ma generacion)"),
        ("Intel Core i3 (8va generacion)", "Intel Core i3 (8va generacion)"),
        ("Intel Core i3 (9na generacion)", "Intel Core i3 (9na generacion)"),
        ("Intel Core i3 (10ma generacion)", "Intel Core i3 (10ma generacion)"),
        ("Intel Core i3 (11va generacion)", "Intel Core i3 (11ma generacion)"),
        ("Intel Core i3 (12va generacion)", "Intel Core i3 (12ma generacion)"),
        ("Intel Core i5 (1ma generacion)", "Intel Core i5 (1ma generacion)"),
        ("Intel Core i5 (2ma generacion)", "Intel Core i5 (2ma generacion)"),
        ("Intel Core i5 (3ma generacion)", "Intel Core i5 (3ma generacion)"),
        ("Intel Core i5 (4ma generacion)", "Intel Core i5 (4ma generacion)"),
        ("Intel Core i5 (5ma generacion)", "Intel Core i5 (5ma generacion)"),
        ("Intel Core i5 (6ma generacion)", "Intel Core i5 (6ma generacion)"),
        ("Intel Core i5 (7ma generacion)", "Intel Core i5 (7ma generacion)"),
        ("Intel Core i5 (8va generacion)", "Intel Core i5 (8va generacion)"),
        ("Intel Core i5 (9na generacion)", "Intel Core i5 (9na generacion)"),
        ("Intel Core i5 (10ma generacion)", "Intel Core i5 (10ma generacion)"),
        ("Intel Core i5 (11va generacion)", "Intel Core i5 (11va generacion)"),
        ("Intel Core i5 (12va generacion)", "Intel Core i5 (12va generacion)"),
        ("Intel Core i7 (8va generacion)", "Intel Core i7 (8va generacion)"),
        ("Intel Core i7 (9na generacion)", "Intel Core i7 (9na generacion)"),
        ("Intel Core i7 (10ma generacion)", "Intel Core i7 (10ma generacion)"),
        ("Intel Core i9 (9na generacion)", "Intel Core i9 (9na generacion)"),
        ("Intel Core i9 (10ma generacion)", "Intel Core i9 (10ma generacion)"),
        ("AMD Ryzen 3 (1ra generacion)", "AMD Ryzen 3 (1ra generacion)"),
        ("AMD Ryzen 3 (2da generacion)", "AMD Ryzen 3 (2da generacion)"),
        ("AMD Ryzen 5 (1ra generacion)", "AMD Ryzen 5 (1ra generacion)"),
        ("AMD Ryzen 5 (2da generacion)", "AMD Ryzen 5 (2da generacion)"),
        ("AMD Ryzen 7 (1ra generacion)", "AMD Ryzen 7 (1ra generacion)"),
        ("AMD Ryzen 7 (2da generacion)", "AMD Ryzen 7 (2da generacion)"),
        ("AMD Ryzen 9 (1ra generacion)", "AMD Ryzen 9 (1ra generacion)"),
        ("AMD Ryzen 9 (2da generacion)", "AMD Ryzen 9 (2da generacion)"),
        ("AMD A6", "AMD A6"),
        ("AMD A8", "AMD A8"),
        ("AMD FX", "AMD FX"),
        ("AMD A10", "AMD A10"),
        ("AMD A12", "AMD A12"),
        ("AMD Athlon", "AMD Athlon"),

)

    RAM_CHOICES = [
        ('ram2gbddr2', '2GB ddr2'),
        ('ram2gbddr3', '2GB ddr3'),
        ('ram4gbddr3', '4GB ddr3'),
        ('ram8gbddr3', '8GB ddr3'),
	('ram12gbddr3', '12 GB ddr3'),
        ('16GB ddr3', '16GB ddr3'),
        ('32GB ddr3', '32GB ddr3'),
        ('4GB ddr4', '4GB ddr4'),
        ('8GB ddr4', '8GB ddr4'),
	('12GB ddr4', '12GB ddr4'),
        ('16GB ddr4', '16GB ddr4'),
        ('32GB ddr4', '32GB ddr4'),
        # opciones de RAM
    ]


    DISCO_CHOICES = (
        ('SSD120GB', 'SSD 120 GB'),
        ('SSD240GB', 'SSD 240 GB'),
        ('SSD480GB', 'SSD 480 GB'),
        ('SSD1TB', 'SSD 1 TB'),
        ('SSD2TB', 'SSD 2 TB'),
        ('HDD500GB', 'HDD 500 GB'),
        ('HDD1TGB', 'HDD 1TB '),
        ('HDD2T', 'HDD 2TB'),
        ('HDD3TB', 'HDD 3TB'),
        ('HDD4TB', 'HDD 4TB'),
    )

    MONITOR_CHOICES = (
        ("19 pulgadas", "19 pulgadas"),
        ("21 pulgadas", "21 pulgadas"),
        ("24 pulgadas", "24 pulgadas"),
        ("27 pulgadas", "27 pulgadas"),
    )
    
    MODELO_CHOICES = (
        ('clon', 'Clon'),
        ('lenovo', 'Lenovo'),
        ('hp', 'HP'),
        ('asus', 'Asus'), 
        ('xpg', 'Xpg'),
        ('dell', 'Dell'),
        ('acer', 'Acer'),
        ('macbook', 'Macbook'),
        ('samsung', 'Samsung'),
        ('vaio', 'Vaio'),
        ('sony', 'Sony'),
        ('SENTEY','Sentey'),
        ('BANGHO','Bangho'),
        ('OVERTECH','Overtech'),
        ('BRB','Brb'),
        ('MUSTIFF','Mustiff'),
        ('CX','CX'),
        ('Magnum','Magnum'),
        ('Coradir','Coradir'),
        ('SOLARMAX','SOLARMAX'),

    )
    
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Roto', 'Roto'),
    ]

    REPARABILIDAD_CHOICES = [
        ('Reparable', 'Reparable'),
        ('Irreparable', 'Irreparable'),
    ]

    MONITOR_CHOICES = [
    ("-","-"),
    ('LG','LG'),
    ('SAMSUNG','SAMSUNG'),
    ('LENOVO','LENOVO'),
    ('NETSYS','NETSYS'),
    ('CX','CX'),
    ('HP','HP'),
    ('BENQ','BENQ'),
    ('NOBLEX','NOBLEX'),
    ('PHILIPS','PHILIPS'),
    ('VIEWSONIC','VIEWSONIC'),
    ('E-VIEW','E-VIEW'),
    ('CORADIR','CORADIR'),
    ('2151AXA','2151AXA'),
    ('ACER','ACER'),

    ]


    estado = models.CharField(max_length=100, default='Nuevo', choices=ESTADO_CHOICES)
    reparabilidad = models.CharField(
    max_length=100, default='Reparable', choices=REPARABILIDAD_CHOICES, null=True, blank=True)
    ram = models.CharField(max_length=50, default="", choices=RAM_CHOICES)
    procesador = models.CharField(max_length=100, choices=PROCESADOR_CHOICES, default="")
    disco = models.CharField(max_length=50, choices=DISCO_CHOICES, default="")
    mouse = models.CharField(max_length=100,default="")
    mousesn = models.CharField(max_length=100,default="")
    teclado = models.CharField(max_length=100,default="")
    tecladosn = models.CharField(max_length=100,default="")
    monitor = models.CharField(max_length=100, choices=MONITOR_CHOICES, default="")
    modelo = models.CharField(max_length=100, choices=MODELO_CHOICES, default="")
    sn = models.CharField(max_length=100)
    antiguedad = models.CharField(max_length=100,blank=False, default="")
    fecha_entrada = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    fecha_devolucion = models.DateField(default=datetime.date(1, 1, 1))
    lablpg = models.CharField(max_length=100,  blank=False, default="", choices=LABPLG_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name_plural = "PCs"

    def __str__(self):
        return f"Ram {self.ram} - Usuario: {self.usuario} - Procesador: {self.procesador} - Modelo: {self.modelo} - Disco: {self.disco} - Monitor: {self.monitor} - Teclado: {self.teclado} - Mouse: {self.mouse} - Mousesn: {self.mousesn} - Tecladosn: {self.tecladosn}"

#IMPRESORA - CRUD Funciona
class Impresora(models.Model):

    PLAN_CHOICES = [

        ('SIN PLAN', 'SIN PLAN'),
        ('Multifuncion RICOH IM 430f PEUGEOT', 'Multifuncion RICOH IM 430f - PEUGEOT CBA'),
        ('Impresora RICOH SP 4510dn PEUGEOT', 'Impresora RICOH SP 4510dn - PEUGEOT CBA'),
        ('Multifuncion BROTHER DCPL5650dn PEUGEOT', 'Multifuncion BROTHER DCPL5650dn - PEUGEOT CBA'),
        ('Multifuncion BROTHER MFCL2720DW PEUGEOT', 'Multifuncion BROTHER MFCL2720dw - PEUGEOT CBA'),
        ('Impresora BROTHER HL-L5100DN PEUGEOT', 'Impresora BROTHER HL-L5100DN - PEUGEOT CBA'),
        ('Impresora RICOH P311 PEUGEOT', 'Impresora RICOH P311 - PEUGEOT CBA'),
        ('Multifuncion RICOH IM 430f IQSA', 'Multifuncion RICOH IM 430f - CITROEN CBA'),
        ('Impresora RICOH SP 4510dn IQSA', 'Impresora RICOH SP 4510dn - CITROEN CBA'),
        ('Multifuncion LEXMARK XM5170 IQSA', 'Multifuncion LEXMARK XM5170 - CITROEN CBA'),
        ('Multifuncion BROTHER MFCL2720dw IQSA', 'Multifuncion BROTHER MFCL2720dw - CITROEN CBA'),
        ('Multifuncion RICOH IM C2000 IQSA', 'Multifuncion RICOH IM C2000 - CITROEN CBA'),
        ('Multifuncion BROTHER DCPL5650dn IQSA', 'Multifuncion BROTHER DCPL5650dn - CITROEN CBA'),
        ('Multifuncion RICOH IM 430f AILES', 'Multifuncion RICOH IM 430f - RENAULT BSAS'),
        ('Multifuncion RICOH IM 430f CHEVENT', 'Multifuncion RICOH IM 430f - CHEVROLET SALADILLO'),
        ('Impresora BROTHER 5470 CHEVENT', 'Impresora BROTHER 5470 - CHEVROLET SALADILLO'),
        ('Impresora CANON LBP630 CHEVENT', 'Impresora CANON LBP630 - CHEVROLET SALADILLO'),
        ('Multifuncion BROTHER DCPL5650dn AMSA', 'Multifuncion BROTHER DCPL5650dn - BMW CBA'),
        ('Multifuncion RICOH IM 430f AMSA', 'Multifuncion RICOH IM 430f - BMW CBA'),
        ('Multifuncion BROTHER DCPL5650dn AUTOROUTE', 'Multifuncion BROTHER DCPL5650dn - CITROEN BSAS'),
        ('Multifuncion BROTHER MFCL2720dw AUTOROUTE', 'Multifuncion BROTHER MFCL2720dw - CITROEN BSAS'),
        ('Impresora BROTHER HL-L5100DN AUTOROUTE', 'Impresora BROTHER HL-L5100DN - CITROEN BSAS'),
        ('Impresora RICOH SP310DN AVENUE TI', 'Impresora RICOH SP310DN - AVENUE ROSARIO'),
        ('Multifuncion RICOH IM 430f AVENUE TI', 'Multifuncion RICOH IM 430f - AVENUE ROSARIO'),
        ('Multifuncion RICOH MP 301 AVENUE TI', 'Multifuncion RICOH MP 301 - AVENUE ROSARIO'),
        ('Impresora RICOH MP 3510 AVENUE TI', 'Multifuncion RICOH MP 3510 - AVENUE ROSARIO'),
        ('Multifuncion RICOH M320F AVENUE TI', 'Multifuncion RICOH M320F - AVENUE ROSARIO'),
        ('Multifuncion KIOCERA M2640DW CHEVENT', 'Multifuncion KIOCERA M2640DW - CHEVROLET VT'),
        ('Multifuncion RICOH IM 430f VOLANT TI', 'Multifuncion RICOH IM 430f - FIAT ROSARIO'),
        ('Multifuncion RICOH M320F VOLANT TI', 'Multifuncion RICOH M320F - FIAT ROSARIO'),
        ('Impresora RICOH P311 VOLANT TI', 'Impresora RICOH P311 - FIAT ROSARIO'),



    ]

    TIPO_CHOICES = [

        ('Alquilada', 'Alquilada'),
        ('Propia', 'Propia')

    ]

    LABPLG_CHOICES = [

	('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),

    ]

    ESTADO_CHOICES = [

        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Roto', 'Roto'),

    ]

    REPARABILIDAD_CHOICES = [

        ('Reparable', 'Reparable'),
        ('Irreparable', 'Irreparable'),

    ]

    estado = models.CharField(max_length=100, default='Nuevo', choices=ESTADO_CHOICES)
    reparabilidad = models.CharField(
        max_length=100, default='Reparable', choices=REPARABILIDAD_CHOICES, null=True, blank=True
    )
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES,blank=False, default="")
    modelo = models.CharField(max_length=100,blank=False, default="")
    abono = models.FloatField(blank=False, default=0.0, validators=[MinValueValidator(0)])
    sn = models.CharField(max_length=100,blank=False, default="")
    plan = models.CharField(max_length=100, default='Nuevo', choices=PLAN_CHOICES)
    antiguedad = models.CharField(max_length=100,blank=False, default="")
    fecha_entrada = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    fecha_devolucion = models.DateField(default=datetime.date(1, 1, 1))
    lablpg = models.CharField(max_length=100,  blank=False, default="", choices=LABPLG_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"Impresora - Tipo: {self.tipo} - Modelo: {self.modelo} - Abono: {self.abono}- usuario: {self.usuario}"


# ACTIVOS DE INFRAESTRUCTURA 
#Revisar
class ActivoInfraestructura(models.Model):
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Roto', 'Roto'),
    ]
    REPARABILIDAD_CHOICES = [
        ('Reparable', 'Reparable'),
        ('Irreparable', 'Irreparable'),
    ]

    LABPLG_CHOICES = [
	('-','-'),
        ('IQSA CORDOBA','IQSA CORDOBA'),
        ('AUTOROUTE','AUTOROUTE'),
        ('AVENUE ROSARIO','AVENUE ROSARIO'),
        ('ADMINISTRACION CENTRAL','ADMINISTRACION CENTRAL'),
        ('AILES CABA','AILES CABA'),
        ('AVENUE CORDOBA','AVENUE CORDOBA'),
        ('AMSA MOTORRAD','AMSA MOTORRAD'),
        ('AMSA BMW','AMSA BMW'),
        ('AMSA MINI','AMSA MINI'),
        ('CHEVENT VENADO TUERTO','CHEVENT VENADO TUERTO'),
        ('AVENUE DS','AVENUE DS'),
        ('CHEVENT SALADILLO','CHEVENT SALADILLO'),
        ('VOLANT CENTRAL','VOLANT CENTRAL'),
        ('VOLANT URQUIZA','VOLANT URQUIZA'),
    ]

    AREAS_CHOICES = [
        
        ('-', '-'),
        ('PLAN DE AHORRO', 'PLAN DE AHORRO'),
        ('REPUESTOS', 'REPUESTOS'),
        ('VENTA DIRECTA 0KM SUC', 'VENTA DIRECTA 0KM SUC'),
        ('ADM VENTAS', 'ADM VENTAS'), 
        ('SIN CLASIFICAR', 'SIN CLASIFICAR'),
        ('ADM VENTAS PLANES', 'ADM VENTAS PLANES'),
        ('SERVICIOS PV', 'SERVICIOS PV'),
        ('CONTACT C', 'CONTACT C'),
        ('VENTA DIRECTA 0KM', 'VENTA DIRECTA 0KM'),
        ('ADM POST VENTA', 'ADM POST VENTA'),
        ('ADMINISTRACION', 'ADMINISTRACION'),
        ('ADMINISTRACION CENTRAL', 'ADMINISTRACION CENTRAL'),
        ('PREENT Y ALISTAJE VN', 'PREENT Y ALISTAJE VN'),
        ('POST VENTA SERVICIOS', 'POST VENTA SERVICIOS'),
        ('REPUESTOS SUCURSAL', 'REPUESTOS SUCURSAL'),
        ('TALLER SUCURSAL', 'TALLER SUCURSAL'),
        ('PLAN DE AHORRO SUCURSAL', 'PLAN DE AHORRO SUCURSAL'),
        ('SISTEMAS', 'SISTEMAS'),
        ('LAVADERO','LAVADERO'),
	('TALLER','TALLER'),
	('MKT','MKT'),
	('COMERCIAL','COMERCIAL'),
	('GESTORIA','GESTORIA'),
	('MAESTRANZA','MAESTRANZA'),
	('VENTA DIRECTA VO','VENTA DIRECTA VO'),
	('PREENT Y ALISTAJE VO','PREENT Y ALISTAJE VO'),
	('ADMINISTRACION SUCURSAL','ADMINISTRACION SUCURSAL'),
	('ADM POST VENTA SUCURSAL','ADM POST VENTA SUCURSAL'),
	('GERENTE COMERCIAL','GERENTE COMERCIAL'),
	('ENTREGAS VN','ENTREGAS VN'),

    ]

    estado = models.CharField(max_length=100, default='Nuevo', choices=ESTADO_CHOICES)
    reparabilidad = models.CharField(
        max_length=100, default='Reparable', choices=REPARABILIDAD_CHOICES, null=True, blank=True
    )
    tipo = models.CharField(max_length=100,blank=False, default="")
    modelo = models.CharField(max_length=100,blank=False, default="")
    sn = models.CharField(max_length=100,blank=False, default="")
    fecha_entrada = models.DateField(blank=False, default=datetime.date(1, 1, 1))
    area = models.CharField(max_length=100, default="", choices=AREAS_CHOICES)
    fecha_devolucion = models.DateField(default=datetime.date(1, 1, 1))
    labplg = models.CharField(max_length=100,default="", choices=LABPLG_CHOICES )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
    class Meta:
        verbose_name_plural = "Activos de Infraestructura"

    def __str__(self):
        return f"Activo de Infraestructura - Tipo: {self.tipo} - Modelo: {self.modelo} - Usuario: {self.usuario}"


# Historial Activo 
# Revisar
class HistorialActivo(models.Model):
    ACTIVO_CHOICES = [
        ('Telefono', 'Telefono'),
        ('Notebook', 'Notebook'),
        ('Escritorio', 'Escritorio'),
        ('Impresora', 'Impresora'),
        ('ActivoInfraestructura', 'ActivoInfraestructura'),
    ]
    

    TIPO_CHOICES = [
        ('Rotura', 'Rotura'),
        ('Actualizacion', 'Actualizacion'),
        ('Perdida', 'Perdida'),
        ('Baja', 'Baja'),
    ]
    
    activo_tipo = models.CharField(max_length=100, choices=ACTIVO_CHOICES,blank=False, default="defCargo")
    activo_id = models.PositiveIntegerField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    dado_de_baja = models.BooleanField(default=False)
    motivo_baja = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default="")
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default="")
    pc = models.ForeignKey(PC, on_delete=models.CASCADE, default="")
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE, default="")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
    
    class Meta:
        verbose_name_plural = "Historial de Activos"

    def __str__(self):
        if self.dado_de_baja:
            return f"{self.get_tipo_display()} {self.activo_tipo} {self.activo_id} fue dado de baja por {self.motivo_baja}"
        else:
            return f"{self.get_tipo_display()} {self.activo_tipo} {self.activo_id} - {self.descripcion}- {self.telefono}- {self.notebook} - {self.pc}  - {self.impresora} - - {self.usuario}"

#ELIMINAR IMPRESORA
class EliminacionImpresora(models.Model):
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE,default=1)
    motivo_eliminacion = models.CharField(max_length=100)
    usuario_eliminacion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_eliminacion = models.DateTimeField(default=timezone.now)
    usuario_ant = models.CharField(max_length=100)

#ELIMINAR ACTIVO
class EliminacionActivo(models.Model):
    activo = models.ForeignKey(ActivoInfraestructura, on_delete=models.CASCADE,default=1)
    motivo_eliminacion = models.CharField(max_length=100)
    usuario_eliminacion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_eliminacion = models.DateTimeField(default=timezone.now)
    usuario_ant = models.CharField(max_length=100)

# ELIMINAR TELEFONO
class EliminacionTelefono(models.Model):
    telefono = models.ForeignKey(Telefono,on_delete=models.CASCADE,default=1)
    motivo_eliminacion = models.CharField(max_length=100)
    usuario_eliminacion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_eliminacion = models.DateTimeField(default=timezone.now)
    usuario_ant = models.CharField(max_length=100)
    
#ELIMINAR NOTEBOOK
class EliminacionNotebook(models.Model):
    notebook = models.ForeignKey(Notebook,on_delete=models.CASCADE,default=1)
    motivo_eliminacion = models.CharField(max_length=100)
    usuario_eliminacion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_eliminacion = models.DateTimeField(default=timezone.now)
    usuario_ant = models.CharField(max_length=100)
    
#ELIMINAR PC
class EliminacionPc(models.Model):
    pc = models.ForeignKey(PC,on_delete=models.CASCADE,default=1)
    motivo_eliminacion = models.CharField(max_length=100)
    usuario_eliminacion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_eliminacion = models.DateTimeField(default=timezone.now)
    usuario_ant = models.CharField(max_length=100)

#ALTA IMPRESORA
class AltaImpresora(models.Model):
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE, default=1)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)

#ALTA ACTIVO
class AltaActivo(models.Model):
    activo = models.ForeignKey(ActivoInfraestructura, on_delete=models.CASCADE, default=1)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)
    
#ALTA TELEFONO
class AltaTelefono(models.Model):
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)
    
#ALTA PC
class AltaPc(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE, default=1)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)
    
#ALTA NOTEBOOK
class AltaNotebook(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default=1)
    usuario_alta = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_alta = models.DateTimeField(default=timezone.now)