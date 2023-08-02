import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'My User Agent 1.0',
})

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    #Sacar la cantidad de empleados
    total_employees = len(data['data'])  # Corrección aquí

    #Sacar el promedio de salario de los empleados
    total_salary = sum(float(employee['employee_salary']) for employee in data['data'])
    average_salary = total_salary / total_employees

    #Sacar el promedio de edad de los empleados
    total_age = sum(int(employee['employee_age']) for employee in data['data'])
    average_age = total_age / total_employees

    #Sacar el salario mínimo y máximo
    salaries = [float(employee['employee_salary']) for employee in data['data']]
    min_salary = min(salaries)
    max_salary = max(salaries)

    # edad mínima y máxima
    ages = [int(employee['employee_age']) for employee in data['data']]
    min_age = min(ages)
    max_age = max(ages)

    # Imprimir los resultados
    print(f"Número Total de Empleados: {total_employees}")
    print(f"Promedio del salario de los empleados: {average_salary}")
    print(f"Promedio de las edades de los empleados: {average_age}")
    print(f"El Salario Mínimo es: {min_salary}")
    print(f"EL Salario Máximo es: {max_salary}")
    print(f"La Edad menor es: {min_age}")
    print(f"La Edad mayor es: {max_age}")

else:
    print("Error al obtener los datos de empleados. Código de estado:", response.status_code)