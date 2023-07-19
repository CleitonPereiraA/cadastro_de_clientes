import os
from tkinter import messagebox
import tkinter as tk
import sqlite3

bancoDeDados = 'clientes.db'

def check_database():
    if not os.path.exists(bancoDeDados):
        conexao = sqlite3.connect(bancoDeDados)
        conexao.execute('''
            CREATE TABLE clientes (
                id INTEGER,
                nome TEXT NOT NULL,
                sobrenome TEXT,
                idade INTEGER NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                PRIMARY KEY("id" AUTOINCREMENT)        
            )
        ''')
        conexao.commit()
        conexao.close()

def dados_cliente():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    cpf = entry_cpf.get()
    email = entry_email.get()

    try:
        conecta = sqlite3.connect(bancoDeDados)
        cursor = conecta.cursor()
        cursor.execute("INSERT INTO clientes (nome, sobrenome, idade, cpf, email) VALUES (?, ?, ?, ?, ?)",
                       (nome, sobrenome, idade, cpf, email))
        conecta.commit()
        conecta.close()
        clear_entry(entry_nome, entry_sobrenome, entry_idade, entry_cpf, entry_email)
    except sqlite3.Error as error:
        messagebox.showerror("Erro", f"Erro ao cadastrar o cliente: {str(error)}")

def visualiza_cliente(): 
    largura1 = 430
    altura1 = 250  
    janelaClientes = tk.Tk()
    janelaClientes.geometry(f"{largura1}x{altura1}")
    janelaClientes.title('Pessoas cadastradas')

    
    try:
        informa = tk.Label(janelaClientes, text='Informe o CPF')
        informa.grid(row=0, column=0, padx=20, pady=20)
        # informa o CPF do cliente
        cpf_cliente = tk.Entry(janelaClientes, width=30)
        cpf_cliente.grid(row=0, column=1, padx=20, pady=20)

        def delete_janela():
            janelaClientes.destroy()

        # visualizar os clientes
        def pesquisar_cliente():
            conecta = sqlite3.connect(bancoDeDados)
            cursor = conecta.cursor()
            cursor.execute("SELECT nome, sobrenome, idade, email FROM clientes WHERE cpf = ?", (cpf_cliente.get(),))
            resultado = cursor.fetchone()
            conecta.close()

            if resultado:
               texto_1 = tk.Label(janelaClientes, text=f"Nome: {resultado[0]}")
               texto_1.grid(row=1, column=1, padx=5, pady=5)
               texto_1 = tk.Label(janelaClientes, text=f"Sobrenome: {resultado[1]}")
               texto_1.grid(row=2, column=1, padx=5, pady=5)
               texto_2 = tk.Label(janelaClientes, text=f"Idade: {resultado[2]}")
               texto_2.grid(row=3, column=1, padx=5, pady=5)
               texto_3 = tk.Label(janelaClientes, text=f"Email: {resultado[3]}")
               texto_3.grid(row=4, column=1, padx=5, pady=5)
               
            else:
                messagebox.showerror("Erro", "Cliente não encontrado")
        # Botão para pesquisar
        button_pesquisa = tk.Button(janelaClientes, text='Pesquisar', command=pesquisar_cliente, bg='gray')
        button_pesquisa.grid(row=0, column=2, padx=10, pady=10)

        # Botão para voltar
        button_pesquisa = tk.Button(janelaClientes, text='Voltar', command=delete_janela, bg='gray')
        button_pesquisa.grid(row=6, column=1, padx=10, pady=10)

    except Exception as e:
        print("Ocorreu um erro:", e)

    except cpf_cliente == None as error:
        messagebox.showerror("Erro", f"Erro ao cadastrar o cliente: {str(error)}")

    janelaClientes.mainloop()

def alterar_dados():
    largura1 = 430
    altura1 = 300  
    janelaAltera = tk.Tk()
    janelaAltera.geometry(f"{largura1}x{altura1}")
    janelaAltera.title('Alterar dados do usuario')


    try:
        def delete_janela():
            janelaAltera.destroy()
            
        informa = tk.Label(janelaAltera, text='Informe o CPF')
        informa.grid(row=0, column=0, padx=20, pady=20)
        # informa o CPF do cliente
        cpf_cliente = tk.Entry(janelaAltera, width=30)
        cpf_cliente.grid(row=0, column=1, padx=20, pady=20)

        # Botão para pesquisar
        button_pesquisa = tk.Button(janelaAltera, text='Pesquisar', bg='gray')
        button_pesquisa.grid(row=0, column=2, padx=10, pady=10)

        # Botão para voltar
        button_voltar = tk.Button(janelaAltera, text='Voltar',command=delete_janela, bg='gray')
        button_voltar.grid(row=1, column=1, padx=10, pady=10)


    except Exception as e:
        print("Ocorreu um erro:", e)

    except cpf_cliente == None as error:
        messagebox.showerror("Erro", f"Erro ao cadastrar o cliente: {str(error)}")


    janelaClientes.mainloop()

def delete_dados():
    largura1 = 430
    altura1 = 300  
    janelaDelete = tk.Tk()
    janelaDelete.geometry(f"{largura1}x{altura1}")
    janelaDelete.title('deletar dados do usuario')


    try:
        def delete_janela():
            janelaDelete.destroy()

        informa = tk.Label(janelaDelete, text='Informe o CPF')
        informa.grid(row=0, column=0, padx=20, pady=20)
        # informa o CPF do cliente
        cpf_cliente = tk.Entry(janelaDelete, width=30)
        cpf_cliente.grid(row=0, column=1, padx=20, pady=20)

        # Botão para pesquisar
        button_pesquisa = tk.Button(janelaDelete, text='Pesquisar', bg='gray')
        button_pesquisa.grid(row=0, column=2, padx=10, pady=10)

        # Botão para voltar
        button_voltar = tk.Button(janelaDelete, text='Voltar',command=delete_janela, bg='gray')
        button_voltar.grid(row=1, column=1, padx=10, pady=10)


    except Exception as e:
        print("Ocorreu um erro:", e)

    except cpf_cliente == None as error:
        messagebox.showerror("Erro", f"Erro ao cadastrar o cliente: {str(error)}")


    janelaDelete.mainloop()

def clear_entry(nome_entry, sobrenome_entry, idade_entry, cpf_entry, email_entry):
    nome_entry.delete(0, tk.END)
    sobrenome_entry.delete(0, tk.END)
    idade_entry.delete(0, tk.END)
    cpf_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

largura = 430
altura = 500

janela = tk.Tk()
janela.geometry(f"{largura}x{altura}")
janela.title('Cadastro de Clientes')

check_database()

# Labels informam ao usuário onde digitar cada informação
labels = ['Nome:', 'Sobrenome:', 'Idade:', 'CPF:', 'Email:']  # Os campos marcados com asterisco (*) não podem ficar em branco
for i, label_text in enumerate(labels):
    label = tk.Label(janela, text=label_text)
    label.grid(row=i, column=0, padx=20, pady=20)

# Entradas para digitar os valores
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=20, pady=20)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, padx=20, pady=20)

entry_idade = tk.Entry(janela, width=30)
entry_idade.grid(row=2, column=1, padx=20, pady=20)

entry_cpf = tk.Entry(janela, width=30)
entry_cpf.grid(row=3, column=1, padx=20, pady=20)

entry_email = tk.Entry(janela, width=43)
entry_email.grid(row=4, column=1, padx=20, pady=20)

# Botão para cadastrar o cliente
button_cadastro = tk.Button(janela, text='Cadastrar Cliente', command=dados_cliente, bg='green')
button_cadastro.grid(row=5, column=1, padx=2, pady=7, columnspan=2, ipadx=49)

# visualizar os clientes
button_visualiza = tk.Button(janela, text='visualizar clientes cadastrados', command=visualiza_cliente, bg='gray')
button_visualiza.grid(row=6, column=1, padx=7, pady=7, columnspan=2, ipadx=15)

# alterar dados de um clientes
button_altera = tk.Button(janela, text='alterar cliente cadastrado', command=alterar_dados, bg='gray')
button_altera.grid(row=7, column=1, padx=7, pady=7, columnspan=2, ipadx=28)

# deletar dados de um clientes
button_delete = tk.Button(janela, text='delete cliente cadastrado', command=delete_dados, bg='gray')
button_delete.grid(row=8, column=1, padx=7, pady=7, columnspan=2, ipadx=28)

janela.mainloop()
