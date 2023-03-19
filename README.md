# AppGastosProject
Aplicación de Control de Gastos
La Aplicación de Control de Gastos es una aplicación web desarrollada utilizando Angular en el frontend y Flask en el backend. La aplicación permite a los usuarios llevar un registro de sus gastos diarios, proporcionando una forma fácil y accesible de controlar y analizar sus finanzas personales.

Características
Registro e inicio de sesión de usuarios
Administración de gastos personales
Agregar gastos
Modificar gastos
Eliminar gastos
Categorización de gastos
Visualización de gastos por usuario
Tecnologías utilizadas
Frontend
Angular
HTML5
CSS3
TypeScript
Backend
Flask
SQLAlchemy
MySQL
Instalación y configuración
Requisitos previos
Node.js y npm
Angular CLI
Python 3.x
MySQL
Pasos de instalación
Clonar el repositorio.

Instalar las dependencias del frontend y del backend.

bash
Copy code
cd frontend
npm install

cd ../backend
pip install -r requirements.txt
Configurar la base de datos MySQL.

Crear una base de datos llamada AppGastos.
Importar la estructura de la base de datos desde el archivo database_structure.sql incluido en el repositorio.
Configurar las variables de entorno y las credenciales de la base de datos en el archivo backend/app.py.

python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/AppGastos'
Reemplace username y password con las credenciales de su base de datos MySQL.

Iniciar el servidor de desarrollo de Angular.

bash
Copy code
cd frontend
ng serve
Iniciar el servidor de desarrollo de Flask.

bash
Copy code
cd backend
python app.py
Acceder a la aplicación en http://localhost:4200.

Uso
Regístrese como un nuevo usuario proporcionando su nombre, correo electrónico y contraseña.
Inicie sesión con sus credenciales registradas.
Agregue, modifique o elimine gastos utilizando los campos y botones proporcionados en la interfaz de usuario.
Revise y analice sus gastos a lo largo del tiempo.
Contribución
Si deseas contribuir al proyecto, por favor crea una bifurcación (fork) del repositorio y envía una solicitud de extracción (pull request) con tus cambios.

Licencia
Esta aplicación de Control de Gastos está licenciada bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más información.

Puedes ayudarme con mi labor aportando aqui lo que consideres ;) https://paypal.me/jcalerofm?country.x=ES&locale.x=es_ES
