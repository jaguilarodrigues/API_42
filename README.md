# Coding Challenge Vaga Full-time 42 São Paulo
API gerenciar alunos com seus respectivos nomes, intra ids, e projetos que estão trabalhando atualmente.

Stack utilisada foi Python, Flask e MongoDB

![Stack](/img/stack.jpeg)

---------------

## Ambientação

-------

Instalação das dependencias

`pip install -r requirements.txt`

---------------

## Requisitos

-------

### 0: Porta 3000


`http://0.0.0.0:3000/students`


### 1: Listar todos os alunos cadastrados

Mostra todos os estudantes cadasstrados

**URL** : `/students`

**Method** : `GET`

#### Success Responses

**Code** : `200 OK`

**Resposta** :

```json
[
    {
        id: 1,
        name: "Gustavo Belfort",
        intra_id: "gus",
        projects: [
            "42cursus_libft",
            "42cursus_get-next-line",
            "42cursus_ft-printf",
        ]
    },
    {
        id: 2,
        name: "Guilhemar Caixeta",
        intra_id: "guiga",
        projects: [
            "cub3d",
        ]
    }
]
```

### 2: Filtrar alunos utilizando uma busca por projeto

**URL** : `/students?projects=42cursus_libft`

**Method** : `GET`

#### Success Responses

**Code** : `200 OK`

Resposta:

```jsx
[
    {
        id: 1,
        name: "Gustavo Belfort",
        intra_id: "gus",
        projects: [
            "42cursus_libft",
            "42cursus_get-next-line",
            "42cursus_ft-printf",
        ]
    }
]
```

### 3: Cadastrar um novo aluno


**URL** : `/students?projects=42cursus_libft`

**Method** : `GET`

#### Success Responses

**Code** : `200 OK`

O corpo da requisição deve conter as informações do aluno a ser cadastrado, sem o ID (gerado automaticamente pelo servidor). A resposta, em caso de sucesso, deve ser o mesmo objeto, com seu novo ID gerado.

`POST /students
Content-Type: application/json`

```jsx
    {
        "name": "Gustavo Belfort",
        "intra_id": "gus",
        "projects": ["42cursus_libft","42cursus_get-next-line","42cursus_ft-printf"]
    }
```

Resposta:

`Status: 201 Created`

`Content-Type: application/json`

```jsx
    {
        "name": "Gustavo Belfort",
        "intra_id": "gus",
        "projects": ["42cursus_libft","42cursus_get-next-line","42cursus_ft-printf"],
        "id": 1
    }
```

### 4: O usuário deve poder remover um aluno por ID

`DELETE /students/:id`

Resposta:

`Status: 200 OK`

```jsx
{}
```
