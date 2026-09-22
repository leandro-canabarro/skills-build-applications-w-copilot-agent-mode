---
mode: 'agent'
model: GPT-4.1
description: 'Atualizar a app Django OctoFit Tracker com MongoDB, API REST e recursos de fitness.'
---

# Atualização da App Django OctoFit Tracker

Atualize a app Django OctoFit Tracker existente. Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`. Preserve as configurações e os dados existentes quando não houver necessidade de alterá-los.

## Requisitos

1. Atualize `settings.py` para:
   - Configurar a conexão com o banco de dados MongoDB `octofit_db` usando Djongo.
   - Manter o ambiente virtual existente em `octofit-tracker/backend/venv`.
   - Configurar CORS para permitir as requisições necessárias do frontend em `localhost:3000`, `127.0.0.1:3000` e no domínio do Codespace quando aplicável.
   - Garantir que `corsheaders` esteja instalado em `INSTALLED_APPS` e que o middleware CORS esteja configurado corretamente.
   - Garantir que os hosts usados localmente e no Codespace estejam em `ALLOWED_HOSTS`.

2. Atualize os componentes da API Django para suportar as coleções e os endpoints de:
   - Usuários e perfis.
   - Equipes.
   - Atividades.
   - Placar de líderes.
   - Treinos e sugestões de treino.

3. Atualize ou crie os seguintes arquivos conforme a estrutura real do projeto:
   - `models.py`
   - `serializers.py`
   - `urls.py`
   - `views.py`
   - `tests.py`
   - `admin.py`

   Se esses arquivos pertencerem ao app Django `api` em vez do pacote do projeto, faça a alteração no local correto, mantendo a organização existente.

4. Use o ORM do Django para criar, consultar, atualizar e remover os dados. Não use scripts diretos do MongoDB para criar a estrutura ou popular os dados da aplicação.

5. Garanta que os modelos e serializers validem os campos obrigatórios e que o campo `email` dos usuários seja único.

6. Configure as rotas REST para todas as entidades e mantenha respostas consistentes e adequadas para operações de listagem, criação, consulta, atualização e remoção.

7. Em `urls.py`:
   - Garanta que `/` aponte para a API.
   - Mantenha `api_root` disponível.
   - Inclua as rotas dos endpoints da API sem remover a rota administrativa existente.

## Verificação

- Execute as migrações necessárias no ambiente virtual existente.
- Execute os testes Django relevantes para usuários, equipes, atividades, placar de líderes e treinos.
- Verifique que a configuração Django não apresenta erros.
- Verifique que `GET /` e `GET /api/` respondem pela API e que `api_root` está presente em `urls.py`.
- Não altere portas encaminhadas: use somente 8000 para o backend, 3000 para o frontend e 27017 para MongoDB.
