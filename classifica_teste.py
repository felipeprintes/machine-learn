from testa import carregar_acessos
X,Y = carregar_acessos()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(teste_dados,teste_marcacoes)

resultato = modelo.predict(teste_dados)
diferencas = resultato - teste_marcacoes

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acertos = 100*total_de_acertos/total_de_elementos
print("\n total de acertos: ", total_de_acertos)
print("\nTaxa de acerto: ",taxa_de_acertos,"%")
print("\n",total_de_elementos)
