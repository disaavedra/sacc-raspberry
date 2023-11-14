import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDgmKDcWjsupUzP8YgUm6t1BZMmY5FQfuI",
  'authDomain': "sacc-firebase.firebaseapp.com",
  'databaseURL': "https://sacc-firebase-default-rtdb.firebaseio.com",
  'projectId': "sacc-firebase",
  'storageBucket': "sacc-firebase.appspot.com",
  'messagingSenderId': "22330926167",
  'appId': "1:22330926167:web:3979172ddc291127962f12"
}

firebase = pyrebase.initialize_app(firebaseConfig)

#PERSONAL MANAGE

def get_personal_manage():
    try:
        db = firebase.database()
        personal_manage = db.child("personal_manage").get().val()
        return personal_manage
    except Exception as error:
        print("Error:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def get_personal_manage_by_personal_manage_code(personal_manage_code):
    try:
        db = firebase.database()
        personal_manage_ref = db.child("personal_manage")
        personal_manage_data = personal_manage_ref.get().val()
        for personal_id, personal_data in personal_manage_data.items():
            if personal_data.get("personal_manage_code") == personal_manage_code:
                return {personal_id: personal_data}
        return f"No se encontró personal con el código {personal_manage_code}"
    except Exception as error:
        print("Error al obtener datos del personal:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def update_personal_manage_state(personal_manage_id, new_state):
    try:
        db = firebase.database()
        personal_ref = db.child(f"personal_manage/{personal_manage_id}")
        personal_ref.update({"personal_manage_state": new_state})
        print(f"Estado del manejo del personal {personal_manage_id} actualizado a {new_state}.")
    except Exception as error:
        print("Error al actualizar el estado del manejo del personal:", error)

#CLIENT MANAGE
    
def get_client_manage():
    try:
        db = firebase.database()
        client_manage = db.child("client_manage").get().val()
        return client_manage
    except Exception as error:
        print("Error:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def get_client_manage_by_client_manage_code(client_code):
    try:
        db = firebase.database()
        client_manage_ref = db.child("client_manage")
        client_manage_data = client_manage_ref.get().val()
        for client_id, client_data in client_manage_data.items():
            if client_data.get("client_manage_code") == client_code:
                return {client_id: client_data}
        return f"No se encontró cliente con el código {client_code}"
    except Exception as error:
        print("Error al obtener datos del cliente:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def update_client_manage_state(client_manage_id, new_state):
    try:
        db = firebase.database()
        client_ref = db.child(f"client_manage/{client_manage_id}")
        client_ref.update({"client_manage_state": new_state})
        print(f"Estado del manejo del cliente {client_manage_id} actualizado a {new_state}.")
    except Exception as error:
        print("Error al actualizar el estado del manejo del cliente:", error)
    
#LOCKERS

def get_locker_by_id(station_id, locker_id):
    try:
        db = firebase.database()
        locker_ref = db.child(f"station/{station_id}/locker/{locker_id}")
        snapshot = locker_ref.get()
        locker = snapshot.val()

        if locker:
            return locker
        else:
            return f"Locker con ID {locker_id} no encontrado en la estación {station_id}"
    except Exception as error:
        print("Error:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def update_locker_state_by_id(station_id, locker_id, new_state):
    try:
        db = firebase.database()
        locker_ref = db.child(f"station/{station_id}/locker/{locker_id}")
        locker_ref.update({"locker_virtual_state": new_state})

    except Exception as error:
        print("Error al obtener datos del locker:", error)
        return "Error al obtener datos de Firebase Realtime Database"

def get_locker_unique_name_by_id(station_id, locker_id):
    try:
        db = firebase.database()
        station_ref = db.child("station").child(station_id)
        station_data = station_ref.get().val()

        if station_data:
            locker_data = station_data.get("locker", {}).get(locker_id)

            if locker_data:
                return locker_data.get("locker_unique_name", f"Se encontró el nombre único del locker con ID {locker_id} en la estación {station_id}")
            else:
                return f"No se encontró el locker con ID {locker_id} en la estación {station_id}"
        else:
            return f"No se encontró la estación con ID {station_id}"
    except Exception as error:
        print("Error al obtener el nombre único del locker:", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
#MANAGE

def get_manage_id_by_random_code(manage_random_code):
    try:
        db = firebase.database()
        manage_ref = db.child("manage").order_by_child('random_code').equal_to(manage_random_code).get()

        if manage_ref.each():
            for manage_snapshot in manage_ref.each():
                return manage_snapshot.key()
        else:
            return None  # Devolver None si no se encuentra ningún resultado
    except Exception as error:
        print("Error al obtener datos de la tabla 'manage':", error)
        return None  # Devolver None en caso de error

    
def update_manage_state(manage_id, new_state):
    try:
        db = firebase.database()
        manage_ref = db.child("manage").child(manage_id)
        manage_ref.update({"manage_state": new_state})
        print(f"Estado de 'manage' con ID {manage_id} actualizado a {new_state}.")
    except Exception as error:
        print("Error al actualizar el estado de 'manage':", error)
    
#PERSONAL

def get_personal_by_id(personal_id):
    try:
        db = firebase.database()
        personal_ref = db.child("personal").child(personal_id)
        personal_data = personal_ref.get().val()

        if personal_data:
            return {personal_id: personal_data}
        else:
            return f"No se encontró el elemento en la tabla 'personal' con ID {personal_id}"
    except Exception as error:
        print("Error al obtener datos de la tabla 'personal':", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def update_personal_state(personal_id, new_state):
    try:
        db = firebase.database()
        personal_ref = db.child("personal").child(personal_id)
        personal_ref.update({"personal_state": new_state})
        print(f"Estado de 'personal' con ID {personal_id} actualizado a {new_state}.")
    except Exception as error:
        print("Error al actualizar el estado de 'personal':", error)
    
#ORDER

def get_order_by_id(order_id):
    try:
        db = firebase.database()
        order_ref = db.child("order").child(order_id)
        order_data = order_ref.get().val()

        if order_data:
            return {order_id: order_data}
        else:
            return f"No se encontró el elemento en la tabla 'order' con ID {order_id}"
    except Exception as error:
        print("Error al obtener datos de la tabla 'order':", error)
        return "Error al obtener datos de Firebase Realtime Database"
    
def update_order_state(order_id, new_state):
    try:
        db = firebase.database()
        order_ref = db.child("order").child(order_id)
        order_ref.update({"order_state": new_state})
        print(f"Estado de 'order' con ID {order_id} actualizado a {new_state}.")
    except Exception as error:
        print("Error al actualizar el estado de 'order':", error)
    
