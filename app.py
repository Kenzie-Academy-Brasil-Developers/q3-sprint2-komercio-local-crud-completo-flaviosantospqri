from flask import Flask, request, jsonify;
from lista_produtos.lista_produtos import produtos
print(produtos)

app = Flask(__name__)

@app.get('/products')
def list_products():
    return jsonify(produtos), 200 

@app.get('/products/<int:product_id>')
def get(product_id: int):
    for produto in produtos:
        if produto['id'] == product_id:
            return jsonify(produto), 200        
    return jsonify({'Message': 'Não encontrado'})

@app.post('/products')
def create():
     data = request.get_json()
     produtos.append(data)
     return jsonify(data), 201
 
@app.route('/products/<int:product_id>', methods=['PATCH', 'PUT'])
def update(product_id: int):
     data = request.get_json()
     for produto in produtos:
        if produto['id'] == product_id:
            produto['name'] = data['name']
            return jsonify(produto), 204

@app.delete('/products/<int:product_id>')

def delete(product_id: int):
    for produto in produtos:
        if produto['id'] == product_id:
            produtos.remove(produto)
            return jsonify({'Menssage': 'Produto removido'}),204
   
        