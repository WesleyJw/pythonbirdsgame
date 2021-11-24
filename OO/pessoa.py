class Pessoa:
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return "Olá"

if __name__ == '__main__':
    wesley = Pessoa(nome = "Wesley")
    jose = Pessoa(wesley, nome = "Jose")
    print(jose.cumprimentar())

    for filho in jose.filhos:
        print(filho.nome)
