from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField, validators

class UserForm(Form):
    matricula=IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=StringField('Correo', [
        validators.Email(message="Ingrese un correo válido")
    ])

class CinepolisForm(Form):
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido")
    ])
    compradores=IntegerField('Compradores', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingresa al menos un comprador")
    ])
    tarjeta=RadioField(
        '¿Cuenta con tarjeta Cinépolsis?',
        choices=[
            ('true', 'Sí'),
            ('false', 'No')
        ]
    )
    boletos=IntegerField('Boletos', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingresa al menos un boleto")
    ])
