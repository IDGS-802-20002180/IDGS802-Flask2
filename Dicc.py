
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,\
SelectField, RadioField
from wtforms.fields import EmailField,TextAreaField
from wtforms import validators

class UserForm(Form): 
    ingles=StringField('Ingles',[validators.DataRequired(message="Llena el campo por favor")])
    espanol=StringField('Español',[validators.DataRequired(message='Este campo es requerido')])
    
class idiomas(Form):
    idioma = RadioField('idioma', choices=[('es', 'Español'),('in', 'Inglés')],
                        validators = [validators.InputRequired(message = 'Por favor completa este campo')])
    lenguage=StringField('Palabra',[validators.DataRequired(message="El campo es necesario")])