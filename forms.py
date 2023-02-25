from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,\
SelectField, RadioField,PasswordField
from wtforms.fields import EmailField,TextAreaField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    

    matricula=StringField('Matricula',[validators.DataRequired(message='La Matricula es Requerida')])
    nombre=StringField('Nombre',[validators.DataRequired(message='Este campo no puede quedarse Vacio'),
                                 validators.length(min=5,max=15,message='Ingresa un valor maximo')])
    apaterno=StringField('Apaterno',[mi_validacion])
    amaterno=StringField('Amaterno')
    email=EmailField('Correo')
    
class LoginForm(Form):
    username=StringField('Usuario',[validators.DataRequired(message='El campo es Requerida')])
    password=PasswordField('Contraseña',[validators.DataRequired(message='Este campo no puede quedarse Vacio'),
                                 validators.length(min=5,max=15,message='Ingresa un valor maximo')])