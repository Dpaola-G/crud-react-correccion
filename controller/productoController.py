from flask import render_template, request, redirect, url_for
import base64

# Lista temporal de productos (puedes reemplazar esto con una base de datos real)
productos = []

def tabla():
    return render_template('tabla.html', productos=productos)

def agregar_producto():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        foto = request.files['foto']

        # Convertir la imagen a base64
        foto_base64 = base64.b64encode(foto.read()).decode('utf-8')

        # Agregar el producto a la lista de productos
        productos.append({'codigo': codigo, 'nombre': nombre, 'categoria': categoria, 'precio': precio, 'foto': foto_base64})

        # Redireccionar a la página de la tabla después de agregar el producto
        return redirect(url_for('tabla'))
    return render_template('agregar_producto.html')

def editar_producto(codigo):
    # Encontrar el producto en la lista de productos
    producto = next((p for p in productos if p['codigo'] == codigo), None)
    if not producto:
        return 'Producto no encontrado'

    if request.method == 'POST':
        # Actualizar los datos del producto con los datos del formulario
        producto['nombre'] = request.form['nombre']
        producto['categoria'] = request.form['categoria']
        producto['precio'] = request.form['precio']
        # Redireccionar a la página de la tabla después de editar el producto
        return redirect(url_for('tabla'))
    
    # Renderizar el formulario de edición con los datos del producto
    return render_template('editar_producto.html', producto=producto)
