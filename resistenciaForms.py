from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField,TextAreaField
from wtforms import validators
from wtforms.validators import InputRequired


def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('¡El campo no tiene datos. Por favor selecciona una!')

def mi_validacion2(form,field):
    if str(field.data)==' ':
        raise validators.ValidationError('¡El campo no tiene datos. Por favor selecciona una opcion!')

class colores(Form):
    colores = [(' ','Selecciona una opcion'),('black', 'Negro'), ('chocolate', 'Marrón'), ('red', 'Rojo'), ('orange', 'Naranja'), ('yellow', 'Amarillo'), ('green', 'Verde'), ('blue', 'Azul'), ('purple', 'Violeta'), ('grey', 'Gris'), ('white', 'Blanco')]
    colores2 = [(' ','Selecciona una opcion'),('black', 'Negro'), ('chocolate', 'Marrón'), ('red', 'Rojo'), ('orange', 'Naranja'), ('yellow', 'Amarillo'), ('green', 'Verde'), ('blue', 'Azul'), ('purple', 'Violeta'), ('grey', 'Gris'), ('white', 'Blanco'), ('gold', 'Dorado'),('silver', 'Plateado')]

    linea1 = SelectField('Primera banda:', choices=colores,validators=[mi_validacion2])
    linea2 = SelectField('Segunda banda:', choices=colores,validators=[mi_validacion2])
    linea3 = SelectField('Tercera banda:', choices=colores2,validators=[mi_validacion2])
    linea4 = RadioField('Tolerancia:', choices=[('gold', 'Dorada'), ('silver', 'Plateada')],validators=[validators.InputRequired("se requiere este campo")])