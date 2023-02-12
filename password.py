import sqlite3 #usa banco dados relacional SQL, cria apenas um aquivo.db
MASTER_PASSWORD = "123456"

senha = input("insira a senha MASTER: ")
if senha != MASTER_PASSWORD:
    print("senha inválida, digite a senha correta... ")
    exit()

conn = sqlite3.connect('password.db')#comando para acessar o BD

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXTE NOT NULL
);
''')# Cria a tabela users, caso ela não exista

def menu(): # 'def' cria funções
    print('*' * 29)
    print("*i : inserir nova senha *")
    print("*l : listar serviços salvos *")
    print("*r : recuperar uma senha *")
    print("*s : sair *")
    print('*' * 29)
    
def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print('Serviço não encontrado (use "l" para verificar os serviços).')
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input('O que deseja fazer?')
    if op not in ['l','i','r','s']:
        print('Opção inválida!')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuário? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()
    
    if op == 'r':
        service = input('Quer ver a senha de qual serviço? ')
        get_password(service)

conn.close()
