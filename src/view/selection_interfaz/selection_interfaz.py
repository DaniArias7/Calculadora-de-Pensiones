import sys
sys.path.append("C:/Users/ACER/Desktop/Calculadora_Pension")
from interfaz.app_calculadora import CalculadoraPensionalApp
from src.model.main import main

def seleccionar_interfaz(opcion):
    if opcion == "1":
        main()
    elif opcion == "2":
        # Ejecutar la interfaz gráfica
        app = CalculadoraPensionalApp()
        app.run()
    else:
        print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    opcion = input("Seleccione una opción: (1 para interfaz por consola, 2 para interfaz gráfica): ")
    seleccionar_interfaz(opcion)
