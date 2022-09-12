"""
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. MS. Fábio H. Cabrini
Atividade: Checkpoint 03 - Cálculo de glicose
Alunos:
Laura Giancoli Aschenbrenner - RM 87194
Matheus Lambert Moreira - RM 87079
Nickolas Pereira do Santos - RM 88103
"""

from sklearn import tree
features = [[99, 139, 199], [75, 115, 130], [50, 100, 150], [84, 126, 133], [30, 70, 180], [15, 40, 100], [40, 111, 177], [99, 139, 199], [81, 93, 70], [97, 86, 173], [69, 84, 127], [100, 140, 199], [120, 150, 200], [105, 150, 180], [122, 187, 140], [115, 160, 185], [125, 199, 199], [110, 148, 167], [125, 141, 100], [107, 159, 137], [109, 183, 143], [113, 178, 187], [127, 201, 201], [126, 200, 350], [110, 215, 240], [130, 250, 500], [200, 211, 244], [300, 300, 300], [160, 260, 273], [154, 279, 201], [147, 357, 341], [199, 285, 363], [235, 371, 267]]
labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
jejum = float(input('Digite o valor durante jejum, em mg/dL: '))
apos_comer = float(input('Digite o valor após comer, em mg/dL: '))
glicemia_casual = float(input('Digite o valor casual, em mg/dL: '))
x = classif.predict([[jejum, apos_comer, glicemia_casual]])
if x == 0:
    print('Sua glicemia está normal.\nA resposta precisa ser analisada por um médico e não deve ser usada como diagnóstico.')
if x == 1:
    print('Sua tolerância a glicose foi diminuída.\nA resposta precisa ser analisada por um médico e não deve ser usada como diagnóstico.')
if x == 2:
    print('Seu diagnóstico é de Diabetes mellitus.\nA resposta precisa ser analisada por um médico e não deve ser usada como diagnóstico.')
'''
Nota 10
'''