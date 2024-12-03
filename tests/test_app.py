import pytest
from fastapi.testclient import TestClient
from main import app  # Cambia "main" por el nombre real de tu archivo principal

client = TestClient(app)

# Datos del usuario único para las pruebas
usuario_prueba = {
    "nombre": "Laura Pérez",
    "edad": 30,
    "sexo": "femenino",
    "nacionalidad": "Española",
    "situacion_sentimental": "Soltera",
    "situacion_laboral": "Empleada",
    "hijos": 2
}

def test_registro_usuario():
    """
    Prueba que el registro del usuario funciona correctamente.
    """
    response = client.post("/registro", json=usuario_prueba)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Información registrada exitosamente."
    assert response.json()["datos"] == usuario_prueba

# def test_registro_usuario_duplicado():
#     """
#     Prueba que no se permite registrar un segundo usuario.
#     """
#     nuevo_usuario = {
#         "nombre": "Pedro García",
#         "edad": 40,
#         "sexo": "masculino",
#         "nacionalidad": "Mexicana",
#         "situacion_sentimental": "Casado",
#         "situacion_laboral": "Autónomo",
#         "hijos": 1
#     }
#     response = client.post("/registro", json=nuevo_usuario)
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Ya hay un usuario registrado."

# def test_consulta_burocratica():
#     """
#     Prueba el endpoint de consulta burocrática general.
#     """
#     # Registrar el usuario antes de la consulta
#     test_registro_usuario()

#     # Consulta de prueba
#     prompt = "¿Cómo puedo renovar mi pasaporte en España?"
#     response = client.get("/consulta_burocratica_general", params={"prompt": prompt})

#     # Verificar que la respuesta sea exitosa
#     assert response.status_code == 200

#     # Validar que el prompt generado incluye los datos del usuario y la consulta
#     data = response.json()
#     assert "prompt" in data
#     assert "respuesta" in data
#     assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
#     assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
#     assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
#     assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
#     assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado


def test_consulta_derechos_laborales():
    """
    Prueba el endpoint de consulta sobre derechos laborales.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los derechos laborales básicos en España?"
    response = client.get("/tramites/laborales/derechos-laborales", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

    from fastapi.testclient import TestClient
from main import app  # Cambia "main" por el nombre de tu archivo principal

client = TestClient(app)

# Datos del usuario único para las pruebas
usuario_prueba = {
    "nombre": "Laura Pérez",
    "edad": 30,
    "sexo": "femenino",
    "nacionalidad": "Española",
    "situacion_sentimental": "Soltera",
    "situacion_laboral": "Empleada",
    "hijos": 2
}

def test_registro_usuario():
    """
    Prueba que el registro del usuario funciona correctamente.
    """
    response = client.post("/registro", json=usuario_prueba)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Información registrada exitosamente."
    assert response.json()["datos"] == usuario_prueba

def test_consulta_prestaciones_desempleo():
    """
    Prueba el endpoint de consulta sobre prestaciones por desempleo.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los requisitos para solicitar prestaciones por desempleo en España?"
    response = client.get("/tramites/laborales/prestaciones-desempleo", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado


def test_consulta_bajas_laborales():
    """
    Prueba el endpoint de consulta sobre bajas laborales.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué tipos de bajas laborales existen y cómo puedo gestionarlas en España?"
    response = client.get("/tramites/laborales/bajas-laborales", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_reclamaciones_prod_serv():
    """
    Prueba el endpoint de consulta sobre reclamaciones de productos y servicios.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cómo puedo presentar una reclamación por un producto defectuoso?"
    response = client.get("/tramites/consumo/reclamaciones-productos-servicios", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_derechos_consumidor():
    """
    Prueba el endpoint de consulta sobre los derechos del consumidor.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son mis derechos como consumidor y cómo puedo ejercerlos?"
    response = client.get("/tramites/consumo/derechos-consumidor", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado


def test_consulta_declaracion_renta():
    """
    Prueba el endpoint de consulta sobre la declaración de la renta.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cómo puedo realizar la declaración de la renta en España?"
    response = client.get("/tramites/fiscales/declaracion-renta", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_impuestos_municipales():
    """
    Prueba el endpoint de consulta sobre impuestos municipales.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cómo puedo pagar el IBI en mi municipio?"
    response = client.get("/tramites/fiscales/impuestos-municipales", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_afiliacion_cotizacion():
    """
    Prueba el endpoint de consulta sobre afiliación y cotización a la Seguridad Social.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cómo puedo afiliarme a la Seguridad Social y empezar a cotizar?"
    response = client.get("/tramites/seguridad-social/afiliacion-cotizacion", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_solicitud_pensiones():
    """
    Prueba el endpoint de consulta sobre la solicitud de pensiones.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué requisitos necesito para solicitar una pensión por jubilación en España?"
    response = client.get("/tramites/seguridad-social/solicitud-pensiones", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_permiso_residencia_trabajo():
    """
    Prueba el endpoint de consulta sobre permisos de residencia y trabajo.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué requisitos necesito para obtener un permiso de residencia y trabajo en España?"
    response = client.get("/tramites/extranjeria/permisos-residencia-trabajo", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_reagrupacion_familiar():
    """
    Prueba el endpoint de consulta sobre reagrupación familiar.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los requisitos para realizar una reagrupación familiar en España?"
    response = client.get("/tramites/extranjeria/reagrupacion-familiar", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_nacimiento_defuncion():
    """
    Prueba el endpoint de consulta sobre inscripción de nacimientos y defunciones.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué documentación necesito para inscribir un nacimiento en el Registro Civil?"
    response = client.get("/tramites/registro-civil/inscripcion-nacimiento-defuncion", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_matrimonio_divorcio():
    """
    Prueba el endpoint de consulta sobre matrimonios y divorcios.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cómo puedo gestionar un matrimonio o un divorcio en España?"
    response = client.get("/tramites/registro-civil/matrimonios-divorcios", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_ayudas_alquiler():
    """
    Prueba el endpoint de consulta sobre ayudas al alquiler.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los requisitos para solicitar ayudas al alquiler en España?"
    response = client.get("/tramites/vivienda/ayudas-alquiler", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_hipotecas():
    """
    Prueba el endpoint de consulta sobre tramitación de hipotecas.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué requisitos necesito para tramitar una hipoteca en España?"
    response = client.get("/tramites/vivienda/tramitacion-hipotecas", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_carnet_conducir():
    """
    Prueba el endpoint de consulta sobre renovación del carnet de conducir.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué pasos debo seguir para renovar mi carnet de conducir en España?"
    response = client.get("/tramites/trafico/renovacion-carnet-conducir", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_transferencia_vehiculos():
    """
    Prueba el endpoint de consulta sobre transferencia de vehículos.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué pasos debo seguir para realizar la transferencia de un vehículo en España?"
    response = client.get("/tramites/trafico/transferencia-vehiculos", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_tarjeta_sanitaria_europea():
    """
    Prueba el endpoint de consulta sobre la tarjeta sanitaria europea.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué pasos debo seguir para solicitar la tarjeta sanitaria europea en España?"
    response = client.get("/tramites/sanitarios/tarjeta-sanitaria-europea", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_cambio_medico_cabecera():
    """
    Prueba el endpoint de consulta sobre cambio de médico de cabecera.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los pasos para cambiar de médico de cabecera en España?"
    response = client.get("/tramites/sanitarios/cambio-medico-cabecera", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_becas_ayudas_estudio():
    """
    Prueba el endpoint de consulta sobre becas y ayudas al estudio.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Qué requisitos debo cumplir para solicitar una beca en España?"
    response = client.get("/tramites/educativos/becas-ayudas-estudio", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado

def test_consulta_homologacion_titulos_extranjeros():
    """
    Prueba el endpoint de consulta sobre homologación de títulos extranjeros.
    """
    # Registrar el usuario antes de la consulta
    test_registro_usuario()

    # Consulta de prueba
    prompt = "¿Cuáles son los pasos para homologar un título extranjero en España?"
    response = client.get("/tramites/educativos/homologacion-titulos-extranjeros", params={"prompt": prompt})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200

    # Validar que el prompt generado incluye los datos del usuario y la consulta
    data = response.json()
    assert "prompt" in data
    assert "respuesta" in data
    assert f"Nombre: {usuario_prueba['nombre']}" in data["prompt"]
    assert f"Edad: {usuario_prueba['edad']}" in data["prompt"]
    assert f"Sexo: {usuario_prueba['sexo']}" in data["prompt"]
    assert f"Nacionalidad: {usuario_prueba['nacionalidad']}" in data["prompt"]
    assert prompt in data["prompt"]  # La consulta debe aparecer en el prompt generado






# pytest test_app.py