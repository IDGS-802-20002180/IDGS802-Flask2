from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash,redirect, url_for


import forms
import DatosEstadis
import Dicc
import resistenciaForms
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

@app.route("/Resistencias",methods=["GET","POST"])
def Resistencias():
    res=resistenciaForms.colores(request.form)
    l1=''
    l2=''
    l3=''
    l4=''
    omhsMx=''
    omhsMn=''
    omhs=''
    linea1E=''
    linea2E=''
    linea3E=''
    linea4E=''
    linea1=''
    linea2=''
    linea3=''
    linea4=''
    td_style=''
    td_style2=''
    td_style3=''
    td_style4=''
    if request.method=='POST' and res.validate():
        linea1=res.linea1.data
        linea2=res.linea2.data
        linea3=res.linea3.data
        linea4=res.linea4.data
        td_style = f'background-color: {linea1};'
        td_style2 = f'background-color: {linea2};'
        td_style3 = f'background-color: {linea3};'
        td_style4 = f'background-color: {linea4};'
        if request.form.get('limpiar'):
            response=make_response(render_template("Actividad3_resistencias.html",form=res,linea1=linea1E,linea2=linea2E,linea3=linea3E,linea4=linea4E,omhs=omhs,omhsMn=omhsMn,omhsMx=omhsMx,td_style=td_style,td_style2=td_style2,td_style3=td_style3,td_style4=td_style4))
            response.delete_cookie('linea1',str(l1).encode())
            response.delete_cookie('linea2',str(l2).encode())
            response.delete_cookie('linea3',str(l3).encode())
            response.delete_cookie('linea4',str(l4).encode())
            response.delete_cookie('Valor',str(omhs).encode())
            response.delete_cookie('Maximo',str(omhsMx).encode())
            response.delete_cookie('Minimo',str(omhsMn).encode())
            td_style=''
            td_style2=''
            td_style3=''
            td_style4=''
            return response
            return redirect(url_for('Resistencias'))
        else:
        
        
            if linea1=='black':
                linea1=int(0)
                linea1E='Negro'
            elif linea1=='chocolate':
                linea1=int(1)
                linea1E='Marron'
            elif linea1=='red':
                linea1=int(2)
                linea1E='Rojo'
            elif linea1=='orange':
                linea1=int(3)
                linea1E='Naranja'
            elif linea1=='yellow':
                linea1=int(4)
                linea1E='Amarillo'
            elif linea1=='green':
                linea1=int(5)
                linea1E='Verde'
            elif linea1=='blue':
                linea1=int(6)
                linea1E='Azul'
            elif linea1=='purple':
                linea1=int(7)
                linea1E='Violeta'
            elif linea1=='grey':
                linea1=int(8)
                linea1E='Gris'
            elif linea1=='white':
                linea1=int(9)
                linea1E='Blanco'
            
            if linea2=='black':
                linea2=int(0)
                linea2E='Negro'
            elif linea2=='chocolate':
                linea2=int(1)
                linea2E='Marron'
            elif linea2=='red':
                linea2=int(2)
                linea2E='Rojo'
            elif linea2=='orange':
                linea2=int(3)
                linea2E='Naranja'
            elif linea2=='yellow':
                linea2=int(4)
                linea2E='Amarrillo'
            elif linea2=='green':
                linea2=int(5)
                linea2E='Verde'
            elif linea2=='blue':
                linea2=int(6)
                linea2E='Azul'
            elif linea2=='purple':
                linea2=int(7)
                linea2E='Violeta'
            elif linea2=='grey':
                linea2=int(8)
                linea2E='Gris'
            elif linea2=='white':
                linea2=int(9)
                linea2E='Blanco'
            
            if linea3=='black':
                linea3=int(1)
                linea3E='Negro'
            elif linea3=='chocolate':
                linea3=int(10)
                linea3E='Marron'
            elif linea3=='red':
                linea3=int(100)
                linea3E='Rojo'
            elif linea3=='orange':
                linea3=int(1000)
                linea3E='Naranja'
            elif linea3=='yellow':
                linea3=int(10000)
                linea3E='Amarillo'
            elif linea3=='green':
                linea3=int(100000)
                linea3E='Verde'
            elif linea3=='blue':
                linea3=int(1000000)
                linea3E='Azul'
            elif linea3=='purple':
                linea3=int(10000000)
                linea3E='Violeta'
            elif linea3=='grey':
                linea3=int(100000000)
                linea3E='Gris'
            elif linea3=='white':
                linea3=int(1000000000)
                linea3E='Blanco'
            elif linea3=='gold':
                linea3=float(0.1)
                linea3E='Dorado'
            elif linea3=='silver':
                linea3=float(0.01)
                linea3E='Plateado'
            
            if linea4=='gold':
                linea4=float(5)
                linea4E='Dorada'
            elif linea4=='silver':
                linea4=float(10)
                linea4E='Plateada'
            l1=(linea1)
            l2=(linea2)
            l3=(linea3)
            l4=(linea4)
        
            unidos=(str(linea1) + str(linea2))
        
            operacion1 = int(unidos)*float(linea3)*(1+int(linea4)/100)
            operacion2=int(unidos)*float(linea3)*(1-int(linea4)/100)
            operacion=int(unidos)*float(linea3)
            
            omhsMx=(operacion1)
            omhsMn=(operacion2)
            omhs=(operacion)
            succes_message='El calculo es de: {}'.format(omhs)+"Ω"+' y tiene una tolerancia de {}%'.format(linea4)
            flash(succes_message)
        
    response=make_response(render_template("Actividad3_resistencias.html",form=res,linea1=linea1E,linea2=linea2E,linea3=linea3E,linea4=linea4E,omhs=omhs,omhsMn=omhsMn,omhsMx=omhsMx,td_style=td_style,td_style2=td_style2,td_style3=td_style3,td_style4=td_style4))
    response.set_cookie('linea1',str(l1).encode())
    response.set_cookie('linea2',str(l2).encode())
    response.set_cookie('linea3',str(l3).encode())
    response.set_cookie('linea4',str(l4).encode())
    response.set_cookie('Valor',str(omhs).encode())
    response.set_cookie('Maximo',str(omhsMx).encode())
    response.set_cookie('Minimo',str(omhsMn).encode())
    
    
    return response


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
