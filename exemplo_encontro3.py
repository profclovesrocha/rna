# Prof. Mentor Cloves Rocha - Passos para a Análise de Sentimentos:
# Coleta de Dados (Simulada):

import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download de recursos necessários (execute uma vez)
try:
    stopwords.words('portuguese')
except LookupError:
    nltk.download('stopwords')
try:
    word_tokenize("exemplo")
except LookupError:
    nltk.download('punkt')

# Simulação de alguns tweets
tweets = [
    "A devastação da Amazônia é alarmante e precisa parar #SOSAmazonia #MeioAmbiente",
    "Notícias positivas sobre iniciativas de reflorestamento na Amazônia!",
    "O governo precisa fazer mais para proteger a floresta amazônica.",
    "Estou muito preocupado com o aumento do desmatamento.",
    "A beleza natural da Amazônia é inspiradora.",
    "A impunidade para crimes ambientais é inaceitável.",
    "Há esperança para a conservação da Amazônia com projetos inovadores.",
    "O futuro do planeta depende da preservação da Amazônia.",
    "A situação do desmatamento é crítica e urgente.",
    "Ações de fiscalização ambiental são essenciais."
]

# Carregar um léxico de sentimentos (exemplo simplificado - em um caso real, você usaria um léxico mais completo como o Sentilex-PT)
lexico_sentimentos = {
    "devastação": -1, "alarmante": -1, "parar": -1, "preocupado": -1, "crítica": -1, "urgente": -1, "impunidade": -1, "inaceitável": -1,
    "positivas": 1, "reflorestamento": 1, "beleza": 1, "inspiradora": 1, "esperança": 1, "conservação": 1, "inovadores": 1, "essenciais": 1,
    "proteger": 0, "fazer": 0, "mais": 0, "depende": 0, "situação": 0, "ações": 0
}

stop_words_pt = set(stopwords.words('portuguese'))

def preprocessar_texto(texto):
    texto = re.sub(r'http\S+|@\S+|#\S+', '', texto) # Remover URLs, menções e hashtags
    tokens = word_tokenize(texto.lower())
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words_pt]
    return tokens

def analisar_sentimento(texto_processado, lexico):
    pontuacao = 0
    num_palavras = 0
    for palavra in texto_processado:
        if palavra in lexico:
            pontuacao += lexico[palavra]
            num_palavras += 1

    if num_palavras > 0:
        sentimento = pontuacao / num_palavras
        if sentimento > 0.2:
            return "positivo"
        elif sentimento < -0.2:
            return "negativo"
        else:
            return "neutro"
    else:
        return "neutro"

resultados_sentimentos = []
for tweet in tweets:
    texto_processado = preprocessar_texto(tweet)
    sentimento = analisar_sentimento(texto_processado, lexico_sentimentos)
    resultados_sentimentos.append(sentimento)
    print(f"Tweet: {tweet} -> Sentimento: {sentimento}")

# Contagem dos sentimentos
contagem_sentimentos = {
    "positivo": resultados_sentimentos.count("positivo"),
    "negativo": resultados_sentimentos.count("negativo"),
    "neutro": resultados_sentimentos.count("neutro")
}

print("\nContagem geral de sentimentos:")
print(contagem_sentimentos)
