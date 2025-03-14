Programa de Automação de Tarefas
Este é um programa de automação de tarefas desenvolvido em Python com uma interface gráfica interativa. Ele permite realizar várias tarefas repetitivas de forma simples e eficiente, como organizar arquivos, enviar e-mails, fazer backups, renomear arquivos em massa e monitorar diretórios.

Funcionalidades
O programa oferece as seguintes funcionalidades:

Organizar Arquivos:

Organiza arquivos em um diretório, movendo-os para pastas correspondentes à sua extensão.

Enviar E-mails:

Envia e-mails automaticamente usando o protocolo SMTP (compatível com Gmail).

Fazer Backup:

Cria um backup de um diretório em outro local, com um nome baseado na data e hora atual.

Renomear Arquivos:

Renomeia arquivos em massa, adicionando um prefixo e/ou sufixo ao nome de cada arquivo.

Monitorar Diretório:

Monitora um diretório em busca de novos arquivos e notifica quando um novo arquivo é detectado.

Como Usar
Pré-requisitos
Python 3.x: O programa foi desenvolvido em Python. Certifique-se de ter o Python instalado.

Bibliotecas Necessárias:

tkinter (já vem com o Python).

smtplib (já vem com o Python).

shutil (já vem com o Python).

os (já vem com o Python).

time (já vem com o Python).

datetime (já vem com o Python).

Instalação
Clone o repositório ou baixe o código-fonte:

bash
Copy
git clone https://github.com/seu-usuario/automacao-tarefas.git
cd automacao-tarefas
Instale o PyInstaller (opcional, para criar um executável):

bash
Copy
pip install pyinstaller
Crie um executável (opcional):

Para criar um executável, execute o seguinte comando:

bash
Copy
pyinstaller --onefile --noconsole automacao_tarefas.py
O executável será gerado na pasta dist.

Executando o Programa
Execute o programa:

Se você criou um executável, navegue até a pasta dist e execute o arquivo automacao_tarefas.

Se preferir executar o código-fonte diretamente, use:

bash
Copy
python automacao_tarefas.py
Interface Gráfica:

A interface gráfica será aberta, com botões para cada funcionalidade.

Clique no botão correspondente à tarefa que deseja realizar e siga as instruções.

Exemplos de Uso
1. Organizar Arquivos
Clique em "Organizar Arquivos".

Selecione o diretório que deseja organizar.

Os arquivos serão automaticamente movidos para pastas com base em suas extensões.

2. Enviar E-mail
Clique em "Enviar E-mail".

Insira o e-mail do remetente, senha, destinatários (separados por vírgula), assunto e corpo do e-mail.

O e-mail será enviado automaticamente.

3. Fazer Backup
Clique em "Fazer Backup".

Selecione o diretório de origem e o diretório de destino.

Um backup do diretório de origem será criado no diretório de destino.

4. Renomear Arquivos
Clique em "Renomear Arquivos".

Selecione o diretório com os arquivos que deseja renomear.

Insira um prefixo e/ou sufixo (opcional).

Os arquivos serão renomeados automaticamente.

5. Monitorar Diretório
Clique em "Monitorar Diretório".

Selecione o diretório que deseja monitorar.

Insira o intervalo de verificação (em segundos).

O programa notificará quando novos arquivos forem detectados.

Configurações Adicionais
Envio de E-mails
O programa usa o protocolo SMTP do Gmail. Se você usar outro provedor de e-mail, pode ser necessário ajustar as configurações do servidor SMTP.

Para usar o Gmail, você precisa permitir o acesso de aplicativos menos seguros nas configurações da sua conta Google.

Backup
O backup é feito em uma pasta com o nome no formato backup_AAAAMMDD_HHMMSS, onde AAAAMMDD é a data e HHMMSS é a hora.

Monitoramento de Diretório
O monitoramento é contínuo. Para interromper, feche o programa.

Contribuição
Se você quiser contribuir para o projeto, siga estas etapas:

Faça um fork do repositório.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adicionando nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: winicyus henrique

E-mail: [winicyus1997@gmail.com]

GitHub: https://github.com/Winicyus97
