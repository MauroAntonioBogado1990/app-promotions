from fastapi import FastAPI, Request
import xmlrpc.client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# @app.post("/api/login")
# async def login(request: Request):
#     try:
#         body = await request.json()
#         email = body.get("email")
#         password = body.get("password")
#         url = body.get("url")
#         db = body.get("db")

#         # Validación básica
#         if not all([email, password, url, db]):
#             print("⚠️ Faltan campos en la solicitud:", body)
#             return {"error": "⚠️ Faltan campos obligatorios"}

#         # Mostrar datos recibidos
#         print("📥 Datos recibidos:")
#         print("🖥️ Servidor:", url)
#         print("📂 Base de datos:", db)
#         print("👤 Usuario:", email)
#         print("🔒 Contraseña:", "*" * len(password))  # oculta la contraseña

#         # Conexión XML-RPC
#         connection_url = f"{url}/xmlrpc/2/common"
#         print(f"🔗 Intentando conexión con: {connection_url}")

#         common = xmlrpc.client.ServerProxy(connection_url)
#         uid = common.authenticate(db, email, password, {})

#         print("🔎 Resultado autenticación:", uid)

#         if uid:
#             return {
#                 "uid": uid,
#                 "message": "✅ Usuario logueado correctamente",
#                 "server": url,
#                 "db": db
#             }
#         else:
#             return {
#                 "error": "❌ Credenciales inválidas o base de datos incorrecta",
#                 "debug": {
#                     "server": url,
#                     "db": db,
#                     "user": email
#                 }
#             }

#     except xmlrpc.client.ProtocolError as e:
#         return {"error": f"⛔ Error de protocolo: {e.errmsg}"}
#     except ConnectionRefusedError:
#         return {"error": "🚫 No se pudo conectar con el servidor Odoo"}
#     except Exception as e:
#         return {"error": f"❌ Error inesperado: {str(e)}"}
    

#apikey de maptiler : Ls7yI4nYgwreJ0NUyN99
# 🔐 Configuración fija
ODOO_URL = "http://host.docker.internal:8069"
ODOO_DB = "admin"
ODOO_USER = "carlos@gmail.com"
ODOO_PASSWORD = "carlos"

@app.post("/api/login")
async def login():
    try:
        # Autenticación
        common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        print("UID:", uid)
        if uid:
            return {
                "uid": uid,
                "message": "✅ Usuario logueado correctamente",
                "server": ODOO_URL,
                "db": ODOO_DB
            }
        else:
            return {
                "error": "❌ Credenciales inválidas o base de datos incorrecta"
            }

    except Exception as e:
        return {
            "error": f"💥 Error al conectar con Odoo: {str(e)}"
        }
