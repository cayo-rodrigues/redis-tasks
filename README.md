# redis-tasks

## Sobre

O objetivo desse projeto é praticar o uso de [Redis](https://redis.io/) com [Django](https://www.djangoproject.com/) e [Django Rest Framework](https://www.django-rest-framework.org/). Basicamente, existe apenas uma rota para gerenciar tarefas, como uma lista de afazeres. A rota de listagem foi feita intencionalmente para ser lenta, usando `time.sleep`. Mas como ela usa o **Redis** como cache, após a primeira vez que é feita uma requisição, as outras são muito mais rápidas.

Porém, existe um dilema. Se um novo recurso for adicionado, seria melhor esperar o cache expirar (no caso dessa aplicação, o cache expira após **1 minuto**), ou apagar a chave que guarda aquele valor em memória? Nesse caso, decidi apagar a chave, para garantir que na próxima listagem os valores estejam atualizados. Porém tudo depende muito da situação. No seu projeto, muitos recursos são criados/atualizados/deletados em uma rota? São feitas muitas requisições GET em algum endpoint, por muitos usuários? Existe alguma operação custosa na sua aplicação? Com que frequência ela é usada? Sempre há um _tradeoff_, seja de complexidade, memória ou performance. Mas de qualquer forma, trabalhar com cache vale muito a pena e aumenta muito a velocidade das requisições.

Algo que eu imagino que dê para fazer, e que seria legal, é apenas _atualizar_ o cache de listagem, quando um recurso for criado. Se o tipo de dado que está guardando as informações da requisição for uma _linked list_, então o tempo de inserção vai ser de **O(1)**, ou seja, imediato, já que se trata de apenas mais um elemento. (https://redis.io/commands/lpush/)

## Rodando a aplicação localmente

Após clonar o projeto em sua máquina, instale as dependências em um ambiente virtual e rode as migrações com o comando:

```
python -m venv venv --upgrade-deps && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate
```

Feito isso, para rodar a API basta usar o seguinte comando:

```
python manage.py runserver
```

Se assim desejar, pode usar a interface gráfica do _Django Rest Framework_ ou então algum outro método para fazer as requisições. Se estiver usando o [Insomnia](https://insomnia.rest/download), você pode usar [este arquivo json](https://drive.google.com/file/d/1H20JVSmUWPVq6iAz1dxTtYyULnUX16VI/view?usp=sharing), que já vem com duas requisições configuradas (é o necessário).

## Rotas

### `GET /tasks/`

Lista todas as tarefas.

### `POST /tasks/`

Cria uma nova tarefa.

Dados necessários:

- `description`: Uma string descrevendo a tarefa
- `priority`: O nível de prioridade. Varia de `1` a `5`.
  - `1`: Extra
  - `2`: Baixo
  - `3`: Médio
  - `4`: Alto
  - `5`: Urgente
- `doing`: Um booleano. Define se a tarefa está em andamento. Padrão `False`.
- `done`: Um booleano. Define se a tarefa foi concluída. Padrão `False`.
