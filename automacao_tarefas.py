import os
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

# Função para organizar arquivos
def organizar_arquivos(diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = arquivo.split('.')[-1]
            pasta_destino = os.path.join(diretorio, extensao)
            
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            shutil.move(os.path.join(diretorio, arquivo), os.path.join(pasta_destino, arquivo))
    messagebox.showinfo("Sucesso", f"Arquivos em {diretorio} organizados com sucesso!")

# Função para enviar e-mails
def enviar_email(remetente, senha, destinatarios, assunto, corpo):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = ", ".join(destinatarios)
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatarios, msg.as_string())
        server.quit()
        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar e-mail: {e}")

# Função para fazer backup
def fazer_backup(origem, destino):
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
        
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        pasta_backup = os.path.join(destino, f"backup_{data_hora}")
        
        shutil.copytree(origem, pasta_backup)
        messagebox.showinfo("Sucesso", f"Backup realizado com sucesso em: {pasta_backup}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao fazer backup: {e}")

# Função para renomear arquivos
def renomear_arquivos(diretorio, prefixo="", sufixo=""):
    for nome_arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
            novo_nome = f"{prefixo}{nome_arquivo}{sufixo}"
            os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome))
    messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

# Função para monitorar diretório
def monitorar_diretorio(diretorio, intervalo=5):
    arquivos_conhecidos = set(os.listdir(diretorio))
    
    while True:
        time.sleep(intervalo)
        arquivos_atual = set(os.listdir(diretorio))
        
        novos_arquivos = arquivos_atual - arquivos_conhecidos
        if novos_arquivos:
            for arquivo in novos_arquivos:
                messagebox.showinfo("Novo Arquivo", f"Novo arquivo detectado: {arquivo}")
                # Aqui você pode adicionar ações para lidar com o novo arquivo
        
        arquivos_conhecidos = arquivos_atual

# Interface gráfica
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Automação de Tarefas")
        self.root.geometry("400x300")

        # Botões para cada funcionalidade
        tk.Button(root, text="Organizar Arquivos", command=self.organizar).pack(pady=10)
        tk.Button(root, text="Enviar E-mail", command=self.enviar_email).pack(pady=10)
        tk.Button(root, text="Fazer Backup", command=self.fazer_backup).pack(pady=10)
        tk.Button(root, text="Renomear Arquivos", command=self.renomear).pack(pady=10)
        tk.Button(root, text="Monitorar Diretório", command=self.monitorar).pack(pady=10)

    def organizar(self):
        diretorio = filedialog.askdirectory(title="Selecione o diretório para organizar")
        if diretorio:
            organizar_arquivos(diretorio)

    def enviar_email(self):
        remetente = simpledialog.askstring("E-mail", "Digite o e-mail do remetente:")
        senha = simpledialog.askstring("Senha", "Digite a senha do remetente:", show='*')
        destinatarios = simpledialog.askstring("Destinatários", "Digite os e-mails dos destinatários (separados por vírgula):")
        assunto = simpledialog.askstring("Assunto", "Digite o assunto do e-mail:")
        corpo = simpledialog.askstring("Corpo", "Digite o corpo do e-mail:")
        if remetente and senha and destinatarios and assunto and corpo:
            enviar_email(remetente, senha, destinatarios.split(','), assunto, corpo)

    def fazer_backup(self):
        origem = filedialog.askdirectory(title="Selecione o diretório de origem")
        destino = filedialog.askdirectory(title="Selecione o diretório de destino")
        if origem and destino:
            fazer_backup(origem, destino)

    def renomear(self):
        diretorio = filedialog.askdirectory(title="Selecione o diretório com os arquivos")
        prefixo = simpledialog.askstring("Prefixo", "Digite o prefixo (opcional):")
        sufixo = simpledialog.askstring("Sufixo", "Digite o sufixo (opcional):")
        if diretorio:
            renomear_arquivos(diretorio, prefixo, sufixo)

    def monitorar(self):
        diretorio = filedialog.askdirectory(title="Selecione o diretório para monitorar")
        intervalo = simpledialog.askinteger("Intervalo", "Digite o intervalo de verificação (segundos):", minvalue=1)
        if diretorio and intervalo:
            monitorar_diretorio(diretorio, intervalo)

# Executar a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()