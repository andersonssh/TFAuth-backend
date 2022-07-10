# TFAuth - Backend

## Introdução

Quando o usuário de um sistema que possui o `TFAuth` integrado ativar a
autenticação por 2 fatores, este será solicitado a inserir os `dígitos secretos` 
que o aplicativo `TFAuth` mostra em sua tela. Os `dígitos secretos`, serão 
atualizados a cada 30 segundos. Quando o usuário inserir os `dígitos secretos`,
a aplicação que ele está a usar deve enviar uma requisição de verificação do código para a API.
Este sistema é destinado a desenvolvedores de aplicativos que desejam adicionar um
passo extra de segurança para a sua aplicação, oferecendo uma opção de autenticação por 
2 fatores a seus usuários.

## Funcionamento da aplicação
Para a integração do sistema com o `TFAuth`, o desenvolvedor deverá registrar o seu aplicativo.
(Esses passos serão definidos em breve)
Após a integração, cabe ao desenvolvedor adicionar esta etapa de verificação a sua rota de login.
(Detalhes mais detalhados em breve)

### `TFAuth - Frontend`
Quando um usuário ativar o `TFA` na sua aplicação, este deverá entrar no `TFAuth - Frontend`, que
realizará os seguintes passos.
1. Enviar uma requisição de criação de `dígitos secretos` para o `TFAuth - Backend`.
2. Mostrar o código recebido para o cliente.
3. Atualizar a cada 30 segundos, enviando uma nova requisição ao fim desse período.

### Aplicação do desenvolvedor
Quando o usuário precisar inserir o código, as seguintes etapas devem ser realizadas pela aplicação
que usa o `TFAuth`:
1. Enviar o código que o cliente inseriu com o token de sessão do usuário para a rota 
de verificação de código da API. (MELHORAR IDEIA)
2. Baseado no `status code`, autorizar ou não, a entrada do usuário.


### Regras de negócio
1. Não deve ser possível atualizar o código antes dos 30 segundos.
   * O código poderá ser criado junto a um timestamp de current_time + 30 segundos, que poderá ser
   utilizado para verificar se o código já expirou para ser possível criar outro.
   * A requisição 

### Passos para integração com outras aplicações.
*****

