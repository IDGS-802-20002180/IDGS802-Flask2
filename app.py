from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms
import DatosEstadis
import Dicc
app=Flask(__name__)
app.config['SECRET_KEY']="Esta es una clave encriptada"
csrf=CSRFProtect()

@app.route("/cookies",methods=['GET','POST'])
def cookies():
    print('numero2')

    reg_user=forms.LoginForm(request.form)
    datos=''
   
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos=user+'@'+passw
        succes_message='Bienvenido {}'.format(user)
        flash(succes_message)
        
    response=make_response(render_template("cookies.html",form=reg_user))
    response.set_cookie('datos_user',datos)
    return response

@app.after_request
def after_request(response):
    print('numero3')
    return response

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print('numero1')

@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get('datos_user')
    nombre=valor_cookie.split('@')
    return render_template("saludo.html",nom=nombre[0])


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
    if request.method=="POST" and alum_form.validate():
        
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


@app.route("/Diccionario",methods=["GET","POST"])
def Diccionario():
    alum_form=Dicc.UserForm(request.form)
    idiom_form=Dicc.idiomas(request.form)
    btn = request.form.get("Guardar")
    btn2= request.form.get("Buscar")
    if request.method=="POST" and 'Guardar' in request.form :
        if alum_form.validate():
            
            if btn=='Guardar':
                ing = request.form['ingles']
                esp = request.form['espanol']
                g=open('diccionarios.txt', 'a')
                g.write(ing.lower() + ' ' + esp.lower() + '\n')
            
                return render_template("Diccionario.html",form=alum_form,form1=idiom_form)
    if request.method=="POST" and 'Buscar' in request.form:
        if idiom_form.validate():
            
            ingles=None
            espanol=None
            if btn2=='Buscar':
                idi=idiom_form.idioma.data
                lenguage=idiom_form.lenguage.data.lower()
                f=open('diccionarios.txt','r')
                lineas=f.readlines()
                mensaje=''
                for linea in lineas:
                    ingles,espanol = linea.strip().lower().split(' ') 
                
                    if idi=='es':
                        if lenguage==ingles:
                            mensaje = f'la traduccion de "{ingles.upper()}" es "{espanol.upper()}".'
                            break 
                    elif idi=='in':
                        if lenguage==espanol:
                            mensaje = f'la traduccion de "{espanol.upper()}" es "{ingles.upper()}".'
                            break
                if not mensaje:
                    mensaje="No existe la palabra en el Diccionario"
                    f.close()
                return render_template("Diccionario.html",form=alum_form, form1=idiom_form, mensaje=mensaje)
                
    return render_template("Diccionario.html",form=alum_form ,form1=idiom_form)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
