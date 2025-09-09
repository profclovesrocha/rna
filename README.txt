
# Sistema de Alerta de Incêndio com Flask

Este é um sistema web simples para envio de alertas de incêndio por e-mail usando Flask.

## Funcionalidades

- Cadastro de múltiplos destinatários de e-mail
- Exclusão de destinatários
- Envio de alerta de incêndio (baixo ou alto)
- Interface web com Flask
- Armazenamento dos e-mails em arquivo local (JSON)

## Requisitos

- Python 3.7+
- Flask
- Conta de e-mail (ex: Gmail) com senha de aplicativo habilitada

## Instalação

1. Instale as dependências:
```
pip install flask
```

2. Configure seu e-mail no arquivo `app.py`:
```python
remetente = "seuemail@gmail.com"
senha = "sua_senha_ou_senha_de_app"
```

3. Execute o aplicativo:
```
python app.py
```

4. Acesse no navegador:
```
http://127.0.0.1:5000
```

## Estrutura de Pastas

```
alerta_incendio/
├── app.py
├── destinatarios.json  # (gerado automaticamente)
├── templates/
│   └── index.html
└── README.txt
```

## Observações

- Para contas Gmail, ative a autenticação com senha de aplicativo:
  [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

## Licença

Uso livre para fins educacionais e não comerciais.
