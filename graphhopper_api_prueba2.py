import requests

def calcular_ruta():
    API_KEY = "eb869855-6a04-4396-a8df-448535e528fb"
    base_url = "https://graphhopper.com/api/route"

    while True:
        print("\n--- Calculadora de Ruta ---")
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 'q':
            print("Saliendo del programa, hasta pronto!")
            break  
        destino = input("Ciudad de Destino: ")

        params = {
            "point": [f"{origen}, Chile", f"{destino}, Chile"],
            "vehicle": "car",
            "key": API_KEY
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "paths" in data:
            distancia_km = data["paths"][0]["distance"]/1000
            duracion_seg = data["paths"][0]["time"]/1000
            horas = int(duracion_seg // 3600)
            minutos = int(duracion_seg % 3600) // 60
            segundos = int(duracion_seg % 60)

            print(f"\nDistancia: {distancia_km: .2f} km")
            print(f"Duracion: {horas}h {minutos}m {segundos}s")
        else:
            print("Error al calcular la ruta. Porfavor verificar datos")

if __name__ == "__main__":
    print("Ejemplo: Santiago y Ovalle")
    calcular_ruta()