from flask import Flask, request
import datetime


app = Flask(__name__)

toques = []

@app.route('/')
def index():
    return '''
        <h1>Registro de Pontos</h1>
        <form action="/ponto" method="post">
            <button type="submit">Registrar Ponto</button>
        </form>
    '''

@app.route('/ponto', methods=['POST'])
def registrar_ponto():
    global toques
    now = datetime.datetime.now()
    dia_semana = now.strftime('%a')
    data = now.strftime('%Y/%m/%d')
    hora = now.strftime('%H:%M')

    toques.append(now)

    if len(toques) == 1:
        with open('pontos.txt', 'a') as file:
            file.write(f"{dia_semana};{data};{hora};")
    elif len(toques) == 2:
        intervalo = (toques[1] - toques[0]).total_seconds() / 3600.0
        if intervalo > 7:
            # Inserir saídas e entradas aleatórias
            # [Implementar lógica para adicionar registros aleatórios]
            pass
        else:
            with open('pontos.txt', 'a') as file:
                file.write(f"{hora};\n")
    # Adicionar mais condições para os próximos toques...

    return f"Ponto registrado: {dia_semana};{data};{hora}"

if __name__ == '__main__':
    app.run(debug=True)
