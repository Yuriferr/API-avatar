from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

elementos = [
        {
            "id": 1,
            "nome": "Agua",
            "nações": [
                {
                    "id": 1,
                    "nome": "Tribo da água",
                    "personagens": [
                        {
                            "id": 1,
                            "nome": "Katara",
                            "idade": 14,
                            "dobra": ["Água", "Sangue", "Gelo"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-katara.jpg"
                        },
                        {
                            "id": 2,
                            "nome": "Sokka",
                            "idade": 15,
                            "dobra": ["Nenhuma"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-sokka.jpg"
                        },
                        {
                            "id": 3,
                            "nome": "Hakoda",
                            "idade": 40,
                            "dobra": ["Nenhuma"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-hakoda.jpg"
                        },
                        {
                            "id": 4,
                            "nome": "Hama",
                            "idade": 60,
                            "dobra": ["Água", "Sangue"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-hama.jpg"
                        },
                        {
                            "id": 5,
                            "nome": "Yue",
                            "idade": 16,
                            "dobra": ["Nenhuma"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-yue.jpg"
                        },
                        {
                            "id": 6,
                            "nome": "Pakku",
                            "idade": 60,
                            "dobra": ["Água", "Gelo"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-pakku.jpg"
                        },
                        {
                            "id": 7,
                            "nome": "Kanna",
                            "idade": 80,
                            "dobra": ["Nenhuma"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-kanna.jpg"
                        },
                        {
                            "id": 8,
                            "nome": "Arnook",
                            "idade": 60,
                            "dobra": ["Nenhuma"],
                            "nação": "Tribo da água",
                            "imagem": "https://exemplo.com/imagem-arnook.jpg"
                        }
                    ]
                },
                {
                    "id": 2,
                    "nome": "Reino da terra",
                    "personagens": [
                        {
                            "id": 1,
                            "nome": "Toph",
                            "idade": 12,
                            "dobra": ["Terra", "Metal"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-toph.jpg"
                        },
                        {
                            "id": 2,
                            "nome": "Bumi",
                            "idade": 112,
                            "dobra": ["Terra"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-bumi.jpg"
                        },
                        {
                            "id": 3,
                            "nome": "Suki",
                            "idade": 15,
                            "dobra": ["Nenhuma"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-suki.jpg"
                        },
                        {
                            "id": 4,
                            "nome": "Haru",
                            "idade": 16,
                            "dobra": ["Terra"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-haru.jpg"
                        },
                        {
                            "id": 5,
                            "nome": "The Boulder",
                            "idade": 30,
                            "dobra": ["Terra"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-the-boulder.jpg"
                        },
                        {
                            "id": 6,
                            "nome": "Long Feng",
                            "idade": 50,
                            "dobra": ["Nenhuma"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-long-feng.jpg"
                        },
                        {
                            "id": 8,
                            "nome": "Kyoshi",
                            "idade": 200,
                            "dobra": ["Terra", "Ar", "Fogo", "Água"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-kyoshi.jpg"
                        },
                        {
                            "id": 9,
                            "nome": "Kuei",
                            "idade": 30,
                            "dobra": ["Nenhuma"],
                            "nação": "Reino da terra",
                            "imagem": "https://exemplo.com/imagem-kuei.jpg"
                        }
                    ]
                },
                {
                    "id": 3,
                    "nome": "Nação do fogo",
                    "personagens": [
                        {
                            "id": 1,
                            "nome": "Zuko",
                            "idade": 16,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-zuko.jpg"
                        },
                        {
                            "id": 2,
                            "nome": "Azula",
                            "idade": 14,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-azula.jpg"
                        },
                        {
                            "id": 3,
                            "nome": "Iroh",
                            "idade": 60,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-iroh.jpg"
                        },
                        {
                            "id": 4,
                            "nome": "Ozai",
                            "idade": 40,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-ozai.jpg"
                        },
                        {
                            "id": 5,
                            "nome": "Mai",
                            "idade": 15,
                            "dobra": ["Nenhuma"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-mai.jpg"
                        },
                        {
                            "id": 6,
                            "nome": "Ty Lee",
                            "idade": 15,
                            "dobra": ["Nenhuma"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-ty-lee.jpg"
                        },
                        {
                            "id": 7,
                            "nome": "Zhao",
                            "idade": 40,
                            "dobra": ["Fogo"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-zhao.jpg"
                        },
                        {
                            "id": 8,
                            "nome": "Azulon",
                            "idade": 70,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-azulon.jpg"
                        },
                        {
                            "id": 9,
                            "nome": "Sozin",
                            "idade": 102,
                            "dobra": ["Fogo", "Relâmpago"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-sozin.jpg"
                        },
                        {
                            "id": 10,
                            "nome": "Roku",
                            "idade": 70,
                            "dobra": ["Fogo", "Ar", "Água", "Terra"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-roku.jpg"
                        },
                        {
                            "id": 11,
                            "nome": "Jeong Jeong",
                            "idade": 60,
                            "dobra": ["Fogo"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-jeong-jeong.jpg"
                        },
                        {
                            "id": 12,
                            "nome": "Piandao",
                            "idade": 60,
                            "dobra": ["Nenhuma"],
                            "nação": "Nação do fogo",
                            "imagem": "https://exemplo.com/imagem-piandao.jpg"
                        }
                    ]
                },
                {
                    "id": 4,
                    "nome": "Nômades do ar",
                    "personagens": [
                        {
                            "id": 1,
                            "nome": "Aang",
                            "idade": 112,
                            "dobra": ["Ar", "Água", "Terra", "Fogo"],
                            "nação": "Nômades do ar",
                            "imagem": "https://exemplo.com/imagem-aang.jpg"
                        },
                        {
                            "id": 2,
                            "nome": "Gyatso",
                            "idade": 70,
                            "dobra": ["Ar"],
                            "nação": "Nômades do ar",
                            "imagem": "https://exemplo.com/imagem-gyatso.jpg"
                        }
                    ]
                }
            ]
        }
    ]

@app.route('/')
def get_dados():
    return jsonify(elementos)

if __name__ == "__main__":
    app.run()
