class Professor:
    def __init__(self, nome, id, materia):
        self.nome = nome
        self.id = id
        self.materia = materia

p1 = Professor('Joao', 123, 'Matemática')
print(p1.materia)

p2 = Professor('Pedro', 456, 'Filosofia')
print(p2.materia)