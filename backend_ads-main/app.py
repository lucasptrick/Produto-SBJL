from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def OK():
    return 'OK'

#total de vendas
#lucro
#distribuição
#clientes atendidos
@app.route('/consulta_decisiva', methods=['GET'])
def consulta_decisiva():
    data = {"total_de_vendas": random.randint(0, 200000),
            "lucro": random.randint(0, 50000),
            "distribuicao": random.randint(0, 20000),
            "clientes_atendidos": random.randint(0, 500),
            }
    return data

@app.route('/future_city', methods=['GET'])
def future_city():
    data = {"co2_mes": random.randint(0, 200000),
            "co2_evitado": random.randint(0, 50000),
            }
    return data

@app.route('/eco_energy', methods=['GET'])
def eco_energy():
    data = {"kw_mes": random.randint(0, 500),
            "kw_atual": random.randint(0, 10),
            }
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
