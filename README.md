# UNDAV-Distribuida2
# Conexiones de servicios a traves de GRPC

Levanta un servidor GRPC de consulta horaria el cual se consumira desde una API REST con una conexion entre los dos servicios a traves del uso de GRPC stubs comunicados con el protocolo proto3.

## Iniciar proyecto

El proyecto se encuentra dockerizado por lo que, mediante docker-compose desde la carpeta raiz se debe ejecutar:

'docker-compose build'
'docker-compose up -d'

Esto levanta en primera instancia el servicio de consulta horaria en el puerto 50000 y luego levanta el servicio de consumo que va a ser usado para leer los datos del servidor por el cliente en el localhost:5000.

## Documentacion de consulta

Tipos de formatos aplicables a las fechas en datetime

'https://strftime.org/'

Listado de Timezones disponibles para consulta

'https://mljar.com/blog/list-pytz-timezones/'

## ¿Cómo resolvió la conexión entre el contenedor REST y el gRPC, cómo se ven entre sí? ¿Utilizó algún modo de restricción?

Para la comunicacion entre los microservicios se utiliza el protocolo de comunicacion protobuf (version 3 en este caso) que estandariza los mensajes que se utilizan en la comunicacion ya que estos servicios se comportan como una arquitectura cliente/servidor.
Se ven a traves del stub, este funciona como un paso intermedio entre el cliente y el servidor realizando la interpretacion de los datos estandarizados que se intercambian en los mensajes.

## Comparar REST sobre HTTP con gRPC. Definir en qué contexto una tecnología es conveniente por sobre la otra o si no existen diferencias de uso.

gRPC realiza una abtraccion del conocimiento HTTP mejorando la performance en la comunicacion entre microservicios, dando la posibilidad de interaccion entre un servidor con diferentes clientes que se hayan generado con diferentes lenguajes. Ya que utiliza un lenguaje de descripcion de interfaces para definir la interfaz del servicio y el formato de los mensajes, permitiendo con esto la creacion de bibliotecas de manera automatica.
La principal diferencia que tiene gPRC con REST es el uso de HTTP, mientras que gPRC se basa en el streaming REST se basa en peticion/respuesta. Esto hace una diferencia en el uso de la version de HTTP, ya que por mas que REST pueda utilizar HTTP 2 no puede sacarle el maximo provecho. Esto hace que gPRC sea ideal para ser utilizado en ambientes en los que el servidor tiene que aceptar una gran cantidad de consultas de varios clientes en simultaneo pudiendo procesar varias al mismo tiempo. Contando tambien que gPRC utiliza protobuf por defecto y al ser datos transmitidos en binario esto hace que sean mas pequeños.

## Generacion automatica de esquema proto 3

Una vez generado el archivo .proto para la comunicacion entre servicios se utiliza el siguiente comando para generar de manera automatizada las librerias que se utilizaran para el stub. El mismo debe utilizarce en caso de que se realice alguna modificacion sobre retrieve_time.proto y se debe realizar la copia de retrieve_time_pb2_gprc.py y retrieve_time_pb2.py en el folder del servicio srv_reader

'python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/retrieve_time.proto'
