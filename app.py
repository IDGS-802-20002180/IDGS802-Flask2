from flask import Flask, render_template
from flask import request
from collections import Counter

import forms
import DatosEstadis
app=Flask(__name__)

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():
    #aqui instanciamos la clase
    #atravez de un objeto le pasamos los datos
    alum_form=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method=="POST":
        
        mat=alum_form.matricula.data
        nom=alum_form.nombre.data
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data
        

    return render_template("Alumnos.html",form=alum_form,mat=mat,nom=nom)

@app.route("/DatosEstadisticos",methods=["GET","POST"])
def DatosEstadisticos():
    DE=DatosEstadis.DatosEstadisticos(request.form)
    btn = request.form.get("button")
    if request.method=="POST":
        
        if btn == 'Imprimir':
            return render_template('DatosEstadisticos.html',form=DE)
        if btn == 'Calcular':
             numeros = request.form.getlist("numeros")
             numerosEnteros=0
             valorMaximo = 0
             valorMinimo = 0
             promedio=0
             repite=""
             contador={}
             for x in numeros:
                valorMaximo=max(numeros)
                valorMinimo=min(numeros)

             for i in range(len(numeros)):            
                numerosEnteros = list(map(int, numeros))
                #print(numerosEnteros)
                promedio=sum(numerosEnteros)/len(numerosEnteros)
               
             for y in numeros:
                if y in contador:
                    contador[y] += 1
                else:
                    contador[y] = 1

             for y, cantidad in contador.items():
                 if cantidad > 1:
                     repite+="El número {} se repite {} veces.<br>".format(y, cantidad) 
                     print(repite)
             return render_template("respuesta.html",form=DE,valorMaximo=valorMaximo,valorMinimo=valorMinimo,promedio=promedio,contador=contador,repite=repite)

    return render_template("DatosEstadisticos.html",form=DE)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
