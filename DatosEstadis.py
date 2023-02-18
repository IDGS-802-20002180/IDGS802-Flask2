from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.fields import FieldList

class DatosEstadisticos(Form):
    numero = IntegerField('Numeros')
    Lnumeros = FieldList(StringField('numero'), min_entries=1)
