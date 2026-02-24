from flask import Flask, render_template, redirect, url_for

app = Flask (__name__)

class Foto:

    def __init__(self, id, titulo, descricao, url):

        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.url = url

lista_de_fotos = [
      
      Foto(id=1, titulo="Foto 1", descricao="Descricao da Foto 1", url="images/foto1.jpg"),
      Foto(id=2, titulo="Foto 2", descricao="Descricao da Foto 2", url="images/foto2.jpg"),
      Foto(id=3, titulo="Foto 3", descricao="Descricao da Foto 3", url="images/foto3.jpg"),
      Foto(id=4, titulo="Foto 4", descricao="Descricao da Foto 4", url="images/foto4.jpg"),
      Foto(id=5, titulo="Foto 5", descricao="Descricao da Foto 5", url="images/foto5.jpg"),
      Foto(id=6, titulo="Foto 6", descricao="Descricao da Foto 6", url="images/foto6.jpg"),
      Foto(id=7, titulo="Foto 7", descricao="Descricao da Foto 7", url="images/foto7.jpg"),
      Foto(id=8, titulo="Foto 8", descricao="Descricao da Foto 8", url="images/foto8.jpg"),
      Foto(id=9, titulo="Foto 9", descricao="Descricao da Foto 9", url="images/foto9.jpg"),
      Foto(id=10, titulo="Foto 10", descricao="Descricao da Foto 10", url="images/foto10.jpg"),
      Foto(id=11, titulo="Foto 11", descricao="Descricao da Foto 11", url="images/foto11.jpg"),
      Foto(id=12, titulo="Foto 12", descricao="Descricao da Foto 12", url="images/foto12.jpg"),
      Foto(id=13, titulo="Foto 13", descricao="Descricao da Foto 13", url="images/foto13.jpg"),
      Foto(id=14, titulo="Foto 14", descricao="Descricao da Foto 14", url="images/foto14.jpg"),
      Foto(id=15, titulo="Foto 15", descricao="Descricao da Foto 15", url="images/foto15.jpg"),
        
      ] 

@app.route('/') 
def fotos():
    return render_template('fotos.html', fotos=lista_de_fotos)


@app.route('/foto/<int:id>')
def foto(id):

    foto = next((foto for foto in lista_de_fotos if foto.id == id), None)

    return render_template('foto.html', foto=foto)




if __name__ == '__main__':
    app.run(debug=True)