from data import *
import tkinter as tk
from tkinter import ttk

def click(numero):
    entrada_actual = entrada_var.get()
    if len(entrada_actual) < 8:
        entrada_var.set(entrada_actual + str(numero))

def borrar():
    entrada_var.set("")

def abrir():
    numero_ingresado = entrada_var.get()
    if len(numero_ingresado) == 7:
        personal_manage_data = get_personal_manage()
        for key, value in personal_manage_data.items():
            if value['personal_manage_code'] == numero_ingresado:
                personal_manage = get_personal_manage_by_personal_manage_code(numero_ingresado)
                personal_manage_id = next(iter(personal_manage))
                update_personal_manage_state(personal_manage_id, True)
                manage = get_manage_id_by_random_code(personal_manage[personal_manage_id]['random_code'])
                update_manage_state(manage, 'cargado')
                update_order_state(personal_manage[personal_manage_id]['order_id'], 'cargado')
                update_personal_state(personal_manage[personal_manage_id]['personal_id'], 'libre')
                update_locker_state_by_id(personal_manage[personal_manage_id]['station_id'], personal_manage[personal_manage_id]['locker_id'], 'cargado')
            else:
                print("Codigo Incorrecto")
    elif len(numero_ingresado) == 8:
        client_manage_data = get_client_manage()
        for key, value in client_manage_data.items():
            if value['client_manage_code'] == numero_ingresado:
                client_manage = get_client_manage_by_client_manage_code(numero_ingresado)
                client_manage_id = next(iter(client_manage))
                update_client_manage_state(client_manage_id, True)
                manage = get_manage_id_by_random_code(client_manage[client_manage_id]['random_code'])
                update_manage_state(manage, 'confirmado')
                update_order_state(client_manage[client_manage_id]['order_id'], 'confirmado')
                update_locker_state_by_id(client_manage[client_manage_id]['station_id'], client_manage[client_manage_id]['locker_id'], 'confirmado')
            else:
                print("Codigo Incorrecto")
    else:
        print("Codigo Incorrecto")

ventana = tk.Tk()
ventana.title("Lockers")

entrada_var = tk.StringVar()

style = ttk.Style()
style.configure('TButton', relief="solid", borderwidth=0, bordercolor="gray")
style.map('TButton', background=[('active', 'gray80')])

for i in range(1, 10):
    fila = (i - 1) // 3 + 2
    columna = (i - 1) % 3 
    texto_boton = str(i)
    boton = ttk.Button(ventana, text=texto_boton, command=lambda num=i: click(num), width=5, style='TButton', padding=(10, 10))
    boton.grid(row=fila, column=columna, padx=10, pady=10)

boton_0 = ttk.Button(ventana, text="0", command=lambda num=0: click(num), width=5, style='TButton', padding=(10, 10))
boton_0.grid(row=5, column=1, padx=10, pady=10)

entrada = tk.Entry(ventana, textvariable=entrada_var, justify="center", font=("Arial", 18))
entrada.grid(row=1, columnspan=3, padx=10, pady=10)

boton_borrar = ttk.Button(ventana, text="Borrar", command=borrar, width=20, style='TButton', padding=(10, 10))
boton_borrar.grid(row=6, columnspan=3, padx=10, pady=10)

boton_abrir = ttk.Button(ventana, text="Abrir", command=abrir, width=20, style='TButton', padding=(10, 10))
boton_abrir.grid(row=7, columnspan=3, padx=10, pady=10)

ventana.mainloop()