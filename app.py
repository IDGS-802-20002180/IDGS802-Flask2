
from flask import Flask, render_template
from flask import request

import forms
app=Flask(__name__)

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():
    #aqui instanciamos la clase
    #atravez de un objeto le pasamos los datos
    alum_form=forms.UserForm(request.form)
    alum_form=forms.matricula.data 
    alum_form=forms.nombre.data
    alum_form=forms.apaterno.data
    alum_form=forms.amaterno.data
    alum_form=forms.email.data

    return render_template("Alumnos.html",alum_form)





if __name__ == "__main__":
    app.run(debug=True, port=3000)
