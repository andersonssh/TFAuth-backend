# MFAuth - Backend (Multi Factor Authentication)

O projeto visa adicionar um passo de segurança a mais para aplicações com login de usuários.

### O que o MFAuth - Backend Faz?

O `MFAuth - Backend` gerencia o fluxo de autenticação por 2 fatores para completar 
o login do usuário. Através de passos simples, é possível integrar esse sistema ao seu projeto.
(Detalhes de como fazer a integração serão adicionados futuramente)

### Como funciona?
O usuário que habilitar esse passo de autenticação dentro do projeto que possui nosso sistema
integrado,  deverá inserir os dígitos secretos fornecidos por esta API para concluir o login.
Os digitos secretos, serão modificados a cada 30 segundos e poderão ser visualmente 
consultados na aplicação do projeto 
`MFAuth - Frontend`. 

### Quais os próximos passos?
 - [ ] Adicionar Fluxos de criação, atualização e verificação do código secreto.
 - [ ] Adicionar Fluxos de registro de novo usuário e ativação do MFA no aplicativo.
 - [ ] Criar uma especificação técnica baseada nos fluxos.