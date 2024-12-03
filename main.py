# from langchain.prompts import PromptTemplate # ojo 
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from modelo_ai import generar_respuesta
from pydantic import BaseModel
import uvicorn
from typing import Optional
from dotenv import load_dotenv  #database
import os    #database
import database
load_dotenv(override=True)
# override=True

from fastapi.middleware.cors import CORSMiddleware




# Leer la clave de la API
gemini_api_key = os.getenv("GEMINI_API_KEY")   #database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# _______________________________________________________________
# Montar la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir el archivo HTML principal
@app.get("/", response_class=HTMLResponse)
def serve_homepage():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())
    

@app.get("/consulta.html", response_class=HTMLResponse)
def serve_consulta():
    with open("templates/consulta.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())
# _______________________________________________________________

# Variable global para guardar el usuario activo
usuario_activo = None
# registrar usuario
# Modelo para los datos del usuario
class DatosUsuario(BaseModel):
    nombre: str
    edad: int
    sexo: str
    nacionalidad: str
    situacion_sentimental: Optional[str]
    situacion_laboral: Optional[str]
    hijos: int

@app.post("/registro")
def registro_usuario(datos: DatosUsuario):
    """
    Registra la información del usuario.
    """
    global usuario_activo  # Hacemos la variable global editable
    usuario_activo = datos  # Guardamos el modelo completo como usuario activo
    return {"mensaje": "Información registrada exitosamente.", "datos": usuario_activo}

@app.get("/acciones", response_class=HTMLResponse)
def serve_acciones():
    with open("templates/acciones.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())
    


@app.get("/consulta_burocratica_general")
def consulta_burocratica(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario: "
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

# --------------------------------------------------------------------------------------------------------

@app.get("/tramites/laborales/derechos-laborales")
def consulta_derechos_laborales(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre derechos laborales en España. Incluye ejemplos prácticos y lenguaje claro para garantizar la comprensión."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}


@app.get("/tramites/laborales/prestaciones-desempleo")
def consulta_prestaciones_desempleo(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar prestaciones por desempleo en España. Detalla los requisitos, pasos y enlaces relevantes."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/laborales/bajas-laborales")
def consulta_bajas_laborales(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo gestionar bajas laborales en España. Asegúrate de incluir los tipos de bajas y los procedimientos paso a paso."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/consumo/reclamaciones-productos-servicios")
def consulta_reclamaciones_prod_serv(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo presentar reclamaciones relacionadas con productos y servicios en España. Proporciona consejos útiles y ejemplos prácticos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/consumo/derechos-consumidor")
def consulta_derechos_consumidor(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre los derechos del consumidor en España. Explica cómo ejercerlos, qué pasos seguir y a dónde acudir si se vulneran."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/fiscales/declaracion-renta")
def consulta_declaracion_renta(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo realizar la declaración de la renta en España. Incluye los plazos, documentos necesarios y herramientas disponibles."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}


@app.get("/tramites/fiscales/impuestos-municipales")
def consulta_impuestos_municipales(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre los impuestos municipales en España, como el IBI. Explica cómo calcularlos, pagarlos y gestionarlos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/seguridad-social/afiliacion-cotizacion")
def consulta_afiliacion_cotizacion(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre el proceso de afiliación y cotización en la Seguridad Social en España. Detalla los pasos y beneficios asociados."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/seguridad-social/solicitud-pensiones")
def consulta_solicitud_pensiones(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar pensiones en España. Explica los tipos de pensiones, requisitos y procedimientos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/extranjeria/permisos-residencia-trabajo")
def consulta_permiso_residencia_trabajo(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar permisos de residencia y trabajo en España. Incluye requisitos, documentos y enlaces oficiales."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/extranjeria/reagrupacion-familiar")
def consulta_reagrupacion_familiar(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo realizar una reagrupación familiar en España. Explica los pasos, requisitos y beneficios asociados."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}


@app.get("/tramites/registro-civil/inscripcion-nacimiento-defuncion")
def consulta_nacimiento_defuncion(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo realizar la inscripción de nacimientos y defunciones en el Registro Civil. Proporciona los pasos, plazos y documentación requerida."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/registro-civil/matrimonios-divorcios")
def consulta_matrimonio_divorcio(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo gestionar matrimonios y divorcios en España. Detalla los procesos legales y los recursos disponibles."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/vivienda/ayudas-alquiler")
def consulta_ayudas_alquiler(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar ayudas al alquiler en España. Incluye los requisitos, plazos y enlaces útiles."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/vivienda/tramitacion-hipotecas")
def consulta_hipotecas(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo gestionar la tramitación de hipotecas en España. Explica los tipos, requisitos y beneficios."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/trafico/renovacion-carnet-conducir")
def consulta_carnet_conducir(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo renovar el carnet de conducir en España. Detalla los pasos, documentación y costos asociados."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/trafico/transferencia-vehiculos")
def consulta_transferencia_vehiculos(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo realizar la transferencia de un vehículo en España. Explica los procedimientos, costos y plazos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/sanitarios/tarjeta-sanitaria-europea")
def consulta_tarjeta_sanitaria_europea(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar la tarjeta sanitaria europea en España. Explica su uso, beneficios y requisitos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/sanitarios/cambio-medico-cabecera")
def consulta_cambio_medico_cabecera(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo cambiar de médico de cabecera en España. Proporciona los pasos y plazos necesarios."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/educativos/becas-ayudas-estudio")
def consulta_becas_ayudas_estudio(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo solicitar becas y ayudas al estudio en España. Incluye los plazos, requisitos y cómo presentar la solicitud."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

@app.get("/tramites/educativos/homologacion-titulos-extranjeros")
def consulta_homologacion_titulos_extranjeros(prompt: str):
    global usuario_activo
    if not usuario_activo:
        raise HTTPException(status_code=400, detail="No hay un usuario registrado actualmente.")
    
    prompt_completo = (
        f"Responde con una explicación detallada y extensa considerando los datos del usuario sobre cómo homologar títulos extranjeros en España. Explica los pasos, documentos necesarios y plazos."
        f"Nombre: {usuario_activo.nombre}, Edad: {usuario_activo.edad}, Sexo: {usuario_activo.sexo}, "
        f"Nacionalidad: {usuario_activo.nacionalidad}, "
        f"Situación sentimental: {usuario_activo.situacion_sentimental or 'No especificada'}, "
        f"Situación laboral: {usuario_activo.situacion_laboral or 'No especificada'}, "
        f"Hijos: {usuario_activo.hijos}.\n\n"
        f"{prompt} Proporciona enlaces útiles, ejemplos y consejos prácticos relacionados con la consulta. Hazlo de una manera muy amable y sin lenguaje dificil, que sea muy comprensible para el publico general."
    )

    # Guardar la consulta del usuario
    database.insertar(
        usuario=usuario_activo.nombre,
        edad=usuario_activo.edad,
        sexo=usuario_activo.sexo,
        nacionalidad=usuario_activo.nacionalidad,
        sentimental=usuario_activo.situacion_sentimental or "No especificada",
        laboral=usuario_activo.situacion_laboral or "No especificada",
        descendencia=usuario_activo.hijos,
        consulta=prompt
    )

    # Generar la respuesta
    respuesta = generar_respuesta(prompt_completo)

    # Guardar la respuesta generada por el sistema
    database.insertar(
        usuario="sistema",
        edad=0,
        sexo="N/A",
        nacionalidad="N/A",
        sentimental="N/A",
        laboral="N/A",
        descendencia=0,
        consulta=respuesta
    )

    return {"prompt": prompt_completo, "respuesta": respuesta}

## GET /tramites/laborales/derechos-laborales
## GET /tramites/laborales/prestaciones-desempleo
## GET /tramites/laborales/bajas-laborales
## GET /tramites/consumo/reclamaciones-productos-servicios
## GET /tramites/consumo/derechos-consumidor
## GET /tramites/fiscales/declaracion-renta
## GET /tramites/fiscales/impuestos-municipales
## GET /tramites/seguridad-social/afiliacion-cotizacion
## GET /tramites/seguridad-social/solicitud-pensiones
## GET /tramites/extranjeria/permisos-residencia-trabajo
## GET /tramites/extranjeria/reagrupacion-familiar
## GET /tramites/registro-civil/inscripcion-nacimiento-defuncion
## GET /tramites/registro-civil/matrimonios-divorcios
## GET /tramites/vivienda/ayudas-alquiler
## GET /tramites/vivienda/tramitacion-hipotecas
## GET /tramites/trafico/renovacion-carnet-conducir
## GET /tramites/trafico/transferencia-vehiculos
## GET /tramites/sanitarios/tarjeta-sanitaria-europea
## GET /tramites/sanitarios/cambio-medico-cabecera
## GET /tramites/educativos/becas-ayudas-estudio
## GET /tramites/educativos/homologacion-titulos-extranjeros


# http://127.0.0.1:8000/tramites/trafico/renovacion-carnet-conducir?prompt=MiConsulta

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



# docker pull pgf3712/burocraticguru:v1
# docker run --env-file .env -p 8000:8000 -t pgf3712/burocraticguru:v1