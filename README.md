# REST API Usuários
## Sobre a API :clipboard:
Este documento explicita com exemplos, como utilizar os recursos disponíveis no REST API de usuários. Assim como, as formas de se realizar uma requisição e suas possíveis respostas.

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **API**

-   **[Flask](https://flask.palletsprojects.com/en/2.1.x/)**
-   **[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)**
-   **[Werkzeug](https://pypi.org/project/Werkzeug/)**
-   **[SQLite](https://www.sqlite.org/index.html)**
-   **[SQLAlchemy](https://www.sqlalchemy.org/)**


#### **Utilitários**

-   Editor:  **[Visual Studio Code](https://code.visualstudio.com/)**
-   Teste de API:  **[Insomnia](https://insomnia.rest/)**, **[Postman](https://www.postman.com/)**

---


## Deploy :fax:
- **[Link deploy](https://restapiusuario.herokuapp.com)**
---
## Funcionalidades :wrench:

|Método|Rota|Descrição|
| -----| -----| -----------|
|**GET** | */users* | Mostra todos os usuarios|
|**GET** | */user&filtro=filtro* | Mostra o usuário de acordo com o filtro|
|**GET** | /users/{id} | Mostra o usuário de acordo com o id escolhido|
|**POST** | */add_user* | Cria um novo usuário|
|**POST** | */login* | Loga com o usuário que foi criado|
|**POST** | */logout* | Desloga do usuário que foi logado|
|**PUT** | */edit_user/{id}*| Atualiza as informações do id escolhido|
|**DELETE** | */delete_user/{id}* | Deleta o usuário|
|**GET** | */confirmacao/{id}* | Confirma o cadastro|

---

<h3>:small_blue_diamond: Consultar todos os usuários => /users </h3>
* Não é necessário estar logado
<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Requisição para listar todos os usuários do sistema.

<img src="https://media.discordapp.net/attachments/988397455919943683/988397488279027764/Method.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se uma lista de todos os usuários:

<img src="https://media.discordapp.net/attachments/988397455919943683/988401759997296751/Sem_titulo.png" style="width:400px">

---

<h3>:small_blue_diamond: Consultar todos os usuários com filtro => /users&filtro=filtro </h3>
* Não é necessário estar logado
<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Requisição para listar todos os usuários do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão.
<img src="https://media.discordapp.net/attachments/988397455919943683/988398384987639818/Method_1.png" style="width:400px">

#### :small_orange_diamond: Possiveis filtros:
- [x] nome :bow: Filtrar usuários pelo nome escolhido. Padrão: Nulo
- [x] email :computer: Filtrar usuários pelo email escolhido. Padrão: Nulo
- [x] telefone :iphone: Filtrar usuários pelo telefone escolhido. Padrão: Nulo

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se uma lista de usuários que se enquadram nos filtros de uma das requisições acima:

<img src="https://media.discordapp.net/attachments/988397455919943683/988402737307865099/Status_1.png" style="width:400px">

---

<h3>:small_blue_diamond: Consultar usuário específico => /users/{id} </h3>
* Não é necessário estar logado
<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Requisição para visualizar os dados de um usuário específico. Faz-se um GET de /users/{id}

<img src="https://media.discordapp.net/attachments/988397455919943683/988404378518032425/Method_2.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se um JSON com os dados do usuário requisitado.

<img src="https://media.discordapp.net/attachments/988397455919943683/988402737307865099/Status_1.png" style="width:400px">

<h4>:x: Requisição :x:</h4>
Requisição exemplo de quando pesquisar por um usuário que não existe.

<img src="https://media.discordapp.net/attachments/988397455919943683/988406209193340958/Method_3.png" style="width:400px">

<h4>:x: Resposta :x:</h4>
Como resposta, obtém-se uma mensagem de erro, dizendo que o usuário não foi encontrado.

<img src="https://media.discordapp.net/attachments/988397455919943683/988406897185001472/Status_2.png" style="width:400px">

---

<h3>:small_blue_diamond: Cadastro de Usuário => /add_user </h3>
* Não é necessário estar logado
<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição cadastrar um novo usuário.

<img src="https://media.discordapp.net/attachments/988397455919943683/988409137442471946/Method_4.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988409802042531850/Header.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988410446178570270/Request_Body.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se uma mensagem de sucesso informado que usuário foi criado, e status code 201 Created (Criado).

<img src="https://media.discordapp.net/attachments/988397455919943683/988411301204226108/Status_3.png" style="width:400px">

<h4>:x: Requisição :x:</h4>
Exemplo de Requisição para tentar cadastrar outro email com "marisa@gmail.com". 

<img src="https://media.discordapp.net/attachments/988397455919943683/988409137442471946/Method_4.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988409802042531850/Header.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988410446178570270/Request_Body.png" style="width:400px">

<h4>:x: Resposta :x:</h4>
Como resposta, obtém-se uma mensagem de erro, informando que o email "marisa@gmail.com" já existe

<img src="https://media.discordapp.net/attachments/988397455919943683/988412866262618122/Status_4.png" style="width:400px">

---

<h3>:small_blue_diamond: Confirmar Cadastro => /confirmacao/{id} </h3>

<h4>:heavy_exclamation_mark: Atenção: Após a criação de um usuário, é enviado pelo email cadastrdo uma confirmação de cadastro, esse endpoint foi feito para caso o email não ter sido entregue. OBS: Só é possível fazer o login depois que o cadastro é confirmado, enquando isso o "ativado" será false.</h4>
<img src="https://media.discordapp.net/attachments/988397455919943683/988418898703568916/unknown.png" style="width:200px">

<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição confirmar cadastro.

<img src="https://media.discordapp.net/attachments/988397455919943683/988415964414607380/Method_5.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se uma mensagem de confirmação de cadastro.

<img src="https://media.discordapp.net/attachments/988397455919943683/988416330384424980/unknown.png" style="width:400px">

<h4>:x: Requisição :x:</h4>
Exemplo de Requisição de id que não existe. 

<img src="https://media.discordapp.net/attachments/988397455919943683/988416670777344041/Method_6.png" style="width:400px">

<h4>:x: Resposta :x:</h4>
Como resposta, obtém-se uma mensagem de erro 404 não encontrado, informando que o id do usuário não existe.

<img src="https://media.discordapp.net/attachments/988397455919943683/988417026047492196/Status_5.png" style="width:400px">

---

<h3>:small_blue_diamond: Login de Usuário => /login </h3>

<h4>:heavy_exclamation_mark: Atenção: Para que seja possível fazer o login, é necessário confirmar o cadastro. A confirmação é enviada para o email que foi preenchido durante o cadastro, porém, se o email não chegar tem o endpoint de "confirmacao/id" que será apresentado anteriormente.</h4>

<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição logar com um usuário.

<img src="https://media.discordapp.net/attachments/988397455919943683/988419763724251136/Method_7.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988419832083005460/Header_1.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988420234870403082/Request_Body_1.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Como resposta, obtém-se uma mensagem o token de acesso que será necessário para fazer as requisições que só podem ser feitas com login.

<img src="https://media.discordapp.net/attachments/988397455919943683/988421153922093076/Status_6.png" style="width:400px">

<h4>:x: Requisição :x:</h4>
Exemplo de Requisição para tentar fazer login com um usuário que não existe. 

<img src="https://media.discordapp.net/attachments/988397455919943683/988419763724251136/Method_7.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988419832083005460/Header_1.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988421961669541958/Request_Body_2.png" style="width:400px">

<h4>:x: Resposta :x:</h4>
Como resposta, obtém-se uma mensagem de erro 401 não autorizado, informando que usuário ou senha estão incorretos.

<img src="https://media.discordapp.net/attachments/988397455919943683/988422517804904458/Status_7.png" style="width:400px">

---

<h3>:small_blue_diamond: Atualizar usuário => /edit_user/{id} </h3>

<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição para atualizar um usuário: /edit_user/{id}

<img src="https://media.discordapp.net/attachments/988397455919943683/988424920117698610/Method_9.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988425373781995530/Header_2.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988425893720522772/Request_Body_3.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :x:</h4>
Exemplo de Resposta mensagem de sucesso ao atualizar dados do usuário, e status code 200 OK e mensagem de erro 401 unauthorized quando o token está expirado ou foi realizado o logout. 

<img src="https://media.discordapp.net/attachments/988397455919943683/988427260501573632/Status_8.png" style="width:400px">

---

<h3>:small_blue_diamond: Deletar Usuário => /delete_user/{id} </h3>

<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição para deletar um usuário: /delete_user/{id}

<img src="https://media.discordapp.net/attachments/988397455919943683/988428906979819550/Method_10.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988429162874273802/Header_3.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :x:</h4>
Exemplos de Respostas, primeiro, a mensagem de sucesso ao deletar um usuário existente. Depois, ao tentar deletar o mesmo usuário, obtém-se o erro 404 not found, informando que o usuário não existe ou não foi encontrado. No terceiro exemplo, o cliente enviou um token de autorização expirado.

<img src="https://media.discordapp.net/attachments/988397455919943683/988430128717631488/Status_9.png" style="width:400px">

---

<h3>:small_blue_diamond: Deletar Usuário => /delete_user/{id} </h3>

<h4>:heavy_check_mark: Requisição :heavy_check_mark:</h4>
Exemplo de Requisição para fazer logout de usuário. Envia-se o token de acesso, e esse token é invalidado.

<img src="https://media.discordapp.net/attachments/988397455919943683/988431067943944252/Method_12.png" style="width:400px">
<img src="https://media.discordapp.net/attachments/988397455919943683/988431163616014416/Header_4.png" style="width:400px">

<h4>:heavy_check_mark: Resposta :heavy_check_mark:</h4>
Exemplo de Resposta: mensagem de sucesso informando que o usuário foi deslogado. Ao tentar usar esse token de acesso em qualquer requisição, ele não funcionará mais, a não ser que o usuário faça o login.

<img src="https://media.discordapp.net/attachments/988397455919943683/988431645453463592/Status_10.png" style="width:400px">

