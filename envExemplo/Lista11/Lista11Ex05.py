import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    def imc(self):
        return self.peso / (self.altura ** 2)

pacientes = {
    'Paciente 1': Paciente('Ana', 25, 'F', 60, 1.70),
    'Paciente 2': Paciente('João', 35, 'M', 80, 1.80),
    'Paciente 3': Paciente('Maria', 45, 'F', 70, 1.65),
    'Paciente 4': Paciente('José', 30, 'M', 90, 1.85),
}

# Criar um dataframe com os dados dos pacientes
df_pacientes = pd.DataFrame.from_records([p.__dict__ for p in pacientes.values()], index=pacientes.keys())

# Calcular o IMC dos pacientes
df_pacientes['IMC'] = df_pacientes.apply(lambda row: row.peso / (row.altura ** 2), axis=1)

# Calcular a média do IMC dos pacientes
media_imc = np.mean(df_pacientes['IMC'])

# Calcular a porcentagem de pacientes com sobrepeso
sobrepeso = df_pacientes[df_pacientes['IMC'] >= 25]
pct_sobrepeso = len(sobrepeso) / len(df_pacientes) * 100

print("Média do IMC dos pacientes:", media_imc)
print("Porcentagem de pacientes com sobrepeso:", pct_sobrepeso)

