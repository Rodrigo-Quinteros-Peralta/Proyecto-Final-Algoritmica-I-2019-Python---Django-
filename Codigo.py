de tkinter import ttk
de tkinter import  *

importar sqlite3

 Producto de clase :
    # propiedad del directorio de conexión
    db_name =  ' database.db '

    def  __init__ ( self , ventana ):
        # Inicializaciones
        self .wind = ventana
        self .wind.title ( ' Aplicación de productos ' )

        # Crear un contenedor de cuadros
        frame = LabelFrame ( self .wind, text  =  ' Registrar nuevo producto ' )
        frame.grid ( fila  =  0 , columna  =  0 , columnpan  =  3 , pady  =  20 )

        # Nombre de entrada
        Etiqueta (marco, texto  =  ' Nombre: ' ). Cuadrícula ( fila  =  1 , columna  =  0 )
        self .name = Entry (marco)
        self .name.focus ()
        self .name.grid ( fila  =  1 , columna  =  1 )

        # Entrada de precio
        Etiqueta (marco, texto  =  ' Precio: ' ). Cuadrícula ( fila  =  2 , columna  =  0 )
        self .price = Entry (marco)
        self .price.grid ( fila  =  2 , columna  =  1 )

        # Botón Agregar producto
        ttk.Button (frame, text  =  ' Save Product ' , command  =  self .add_product) .grid ( row  =  3 , columnpan  =  2 , sticky  = W + E)

        # Mensajes de salida
        self .message = Label ( text  =  ' ' , fg  =  ' red ' )
        self .message.grid ( fila  =  3 , columna  =  0 , columnas  =  2 , adhesivo  = W + E)

        # Tabla
        self .tree = ttk.Treeview ( altura  =  10 , columnas  =  2 )
        self .tree.grid ( fila  =  4 , columna  =  0 , columnas  =  2 )
        self .tree.heading ( ' # 0 ' , text  =  ' Name ' , anchor  =  CENTER )
        self .tree.heading ( ' # 1 ' , text  =  ' Price ' , anchor  =  CENTER )

        # Botones
        ttk.Button ( text  =  ' DELETE ' , command  =  self .delete_product) .grid ( row  =  5 , column  =  0 , sticky  = W + E)
        ttk.Button ( text  =  ' EDIT ' , command  =  self .edit_product) .grid ( fila  =  5 , columna  =  1 , adhesivo  = W + E)

        # Llenando las filas
        self .get_products ()

    # Función para ejecutar consultas de base de datos
    def  run_query ( self , consulta , parámetros  = ()):
        con sqlite3.connect ( self .db_name) como conn:
            cursor = conn.cursor ()
            resultado = cursor.execute (consulta, parámetros)
            conn.commit ()
        resultado devuelto

    # Obtener productos de la base de datos
    def  get_products ( self ):
        # mesa de limpieza
        records =  self .tree.get_children ()
        para elemento en registros:
            self .tree.delete (elemento)
        # obteniendo datos
        query =  ' SELECT * FROM product ORDER BY name DESC '
        db_rows =  self .run_query (consulta)
        # datos de relleno
        para fila en db_rows:
            self .tree.insert ( ' ' , 0 , texto  = fila [ 1 ], valores  = fila [ 2 ])

    # Validación de entrada de usuario
     validación de definición ( auto ):
        return  len ( self .name.get ()) ! =  0  y  len ( self .price.get ()) ! =  0

    def  add_product ( self ):
        Si  auto .validation ():
            query =  ' INSERTAR EN LOS VALORES del producto (NULL,?,?) '
            parámetros =   ( self .name.get (), self .price.get ())
            self .run_query (consulta, parámetros)
            self .message [ ' text ' ] =  ' Producto {} agregado correctamente ' .format ( self .name.get ())
            self .name.delete ( 0 , END )
            self .price.delete ( 0 , END )
        más :
            self .message [ ' text ' ] =  ' Se requiere nombre y precio '
        self .get_products ()

    def  delete_product ( self ):
        self .message [ ' text ' ] =  ' '
        prueba :
           self .tree.item ( self .tree.selection ()) [ ' texto ' ] [ 0 ]
        excepto  IndexError  como e:
            self .message [ ' text ' ] =  ' Seleccione un registro '
            regreso
        self .message [ ' text ' ] =  ' '
        nombre =  self .tree.item ( self .tree.selection ()) [ ' texto ' ]
        query =  ' DELETE FROM product WHERE name =? '
        self .run_query (query, (nombre,))
        self .message [ ' text ' ] =  ' Registro {} eliminado exitosamente ' .format (nombre)
        self .get_products ()

    def  edit_product ( self ):
        self .message [ ' text ' ] =  ' '
        prueba :
            self .tree.item ( self .tree.selection ()) [ ' valores ' ] [ 0 ]
        excepto  IndexError  como e:
            self .message [ ' text ' ] =  ' Por favor, seleccione Grabar '
            regreso
        nombre =  self .tree.item ( self .tree.selection ()) [ ' texto ' ]
        old_price =  self .tree.item ( self .tree.selection ()) [ ' valores ' ] [ 0 ]
        self .edit_wind = Toplevel ()
        self .edit_wind.title =  ' Editar producto '
        # Nombre antiguo
        Etiqueta ( self .edit_wind, text  =  ' Nombre antiguo: ' ) .grid ( fila  =  0 , columna  =  1 )
        Entrada ( self .edit_wind, textvariable  = StringVar ( self .edit_wind, value  = name), state  =  ' readonly ' ) .grid ( fila  =  0 , columna  =  2 )
        # Nombre nuevo
        Etiqueta ( self .edit_wind, text  =  ' Nuevo precio: ' ) .grid ( fila  =  1 , columna  =  1 )
        new_name = Entry ( self .edit_wind)
        new_name.grid ( fila  =  1 , columna  =  2 )

        # Precio anterior
        Etiqueta ( self .edit_wind, text  =  ' Precio anterior: ' ) .grid ( fila  =  2 , columna  =  1 )
        Entrada ( self .edit_wind, textvariable  = StringVar ( self .edit_wind, value  = old_price), state  =  ' readonly ' ) .grid ( fila  =  2 , columna  =  2 )
        # Nuevo precio
        Etiqueta ( self .edit_wind, text  =  ' Nuevo nombre: ' ) .grid ( fila  =  3 , columna  =  1 )
        new_price = Entry ( self .edit_wind)
        new_price.grid ( fila  =  3 , columna  =  2 )

        Botón ( self .edit_wind, text  =  ' Update ' , command  =  lambda : self .edit_records (new_name.get (), name, new_price.get (), old_price)). Grid ( row  =  4 , column  =  2 , sticky  = W)
        self .edit_wind.mainloop ()

    def  edit_records ( self , new_name , name , new_price , old_price ):
        query =  ' ACTUALIZAR producto SET name =?, price =? DONDE nombre =? Y precio =? '
        parámetros = (new_name, new_price, name, old_price)
        self .run_query (consulta, parámetros)
        self .edit_wind.destroy ()
        self .message [ ' text ' ] =  ' Record {} actualizado con éxitoflyly ' .format (nombre)
        self .get_products ()

if  __name__  ==  ' __main__ ' :
    ventana = Tk ()
    aplicación = Producto (ventana)
    window.mainloop ()
