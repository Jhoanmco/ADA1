import csv
import pandas as pd


#algoritmo del merge sort
def merge_sort(productos):
    if len(productos)<=1:
        print(f"[merge sort] Caso base: {productos}")
        return productos

    mid = len(productos)//2
    print(f"[merge sort] Dividiendo: {productos[:mid]} y {productos[mid:]}")
    izquierda = merge_sort(productos[:mid])
    derecha = merge_sort(productos[mid:])
    
    print(f"[merge] Fusionando: {izquierda} y {derecha}")
    return merge(izquierda, derecha)

def merge(left, right):
    resultado=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if (left[i]["calificacion"] > right[j]["calificacion"]) or (left[i]["calificacion"] == right[j]["calificacion"] and left[i]["precio"] < right[j]["precio"]):
            resultado.append(left[i])
            i+=1
        else:
            resultado.append(right[j])
            j+=1
            
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    print(f"[merge] Resultado: {resultado}")
    return resultado


#proceso principal
def mejores_productos(archivo_csv, archivo_salida="productos_ordenados.csv"):
    print(f"[proceso principal] Leyendo el archivo .csv...")
    #leer el archivo
    df= pd.read_csv(archivo_csv)
    productos = df.to_dict(orient="records")
    print(f"[proceso principal] productos leidos: {productos}")
    
    print(f"[proceso principal] aplicando merge soft...")
    #aplica el merge sort
    productos_ordenados=merge_sort(productos)
    print(f"[proceso principal] productos ordenados: {productos_ordenados}")
    
    print(f"[proceso principal] guardando en un nuevo archivo .csv ordenado...")
    #guarda  en un nuevo archivo ordenado
    with open(archivo_salida, mode="w", newline="", encoding="utf-8") as f:
        writer=csv.DictWriter(f, fieldnames=["id", "nombre", "precio", "calificacion", "stock"])
        writer.writeheader()
        writer.writerows(productos_ordenados)
    print(f"[proceso principal] archivo guardado: {archivo_salida}")  
    
    print(f"[proceso principal] encontrando mejores productos...")
    #1. calificacion maxima
    max_calif = productos_ordenados[0]["calificacion"]
    print(f"[proceso principal] calificacion maxima encontrada: {max_calif}")
    
    #2. filtrar productos con esa clasificacion
    candidatos = [p for p in productos_ordenados if p["calificacion"] == max_calif]
    print(f"[proceso principal] candidatos con calificacion maxima: {candidatos}")
    
    #3. obtener el menor precio 
    min_precio = min(p["precio"] for p in candidatos)
    print(f"[proceso principal] menor precio entre los candidatos: {min_precio}")
    
    #4. filtrar los productos con calificacion maxima y menor precio
    mejores = [p for p in candidatos if p["precio"] == min_precio]
    print(f"[proceso principal] productos con calificacion maxima y menor precio: {mejores}")
    
    return mejores


#ejecucion
if __name__ == "__main__":
    archivo = "productos.csv"
    mejores = mejores_productos(archivo)
    
    print("\nMejores productos encontrados (final :> ):")
    print(mejores)