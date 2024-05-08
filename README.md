# Hello, World

Ce projet est conçu pour documenter la création d'un paquet Python exécutable et sa diffusion sur PiPY.
Le système de construction de paquets et de gestion de dépendances utilisé est [Poetry](https://python-poetry.org/).

## Création du paquet

Installez Poetry via [pipx](https://pipx.pypa.io/).
D'autres options d'installation sont proposées dans la [documentation officielle](https://python-poetry.org/docs/#installation).

```bash
pipx install poetry
```

La commande `poetry new` permet ensuite d'initialiser l'arborescence du paquet.

```bash
poetry new opteemo-hello-poetry
```

```
opteemo-hello-poetry
├── pyproject.toml
├── README.md
├── opteemo_hello_poetry
│   └── __init__.py
└── tests
    └── __init__.py
```

## Création d'un paquet exécutable

### Fichier `__main__.py`

La création du fichier `__main__.py` dans le dossier `opteemo_hello_poetry` permet le rendre le paquet exécutable via la commande `python -m opteemo_hello_poetry`.

### Commande CLI

Pour rendre le paquet exécutable via une commande CLI arbitrairement nommée `hello`, il suffit d'ajouter la configuration suivante au fichier `pyproject.toml` :

```
[tool.poetry.scripts]
hello = 'opteemo_hello_poetry:__main__.cli'
```

Ainsi, lancer la commande `hello` entrainera l'appel de la fonction `cli()` du module `__main__` du paquet `opteemo_hello_poetry`.

## Déploiement du paquet

### Construction du paquet

Avant de déployer le paquet, il est nécessaire d'en construire l'archive :

```bash
poetry build
```

Ceci entraine la création du dossier `dist` et des fichiers du paquet :

```
opteemo-hello-poetry
└── dist
    ├── opteemo_hello_poetry-0.1.0-py3-none-any.whl
    └── opteemo_hello_poetry-0.1.0.tar.gz
```

### Installation locale

Si vous ne souhaitez pas diffuser le paquet sur PiPY, `pip` autorise l'installation de paquets à partir d'une archive `tar.gz` :

```
pip install opteemo_hello_poetry-0.1.0.tar.gz
```

### Diffusion sur PiPY

Les prérequis pour diffuser un paquet sur l'environnement PuPY sont :

1. La création d'un compte
2. L'activation de l'authentification à deux facteurs (2FA)
3. La création d'un jeton d'API

Il est préférable d'expérimenter la diffusion de paquet sur [Test PiPy](https://test.pypi.org) avant de passer à PiPY.
Poetry est capable de communiquer avec les dépôts PiPY. Voici la configuration du dépôt [Test PiPy](https://test.pypi.org) que nous avons arbitrairement nommé `test` :

```bash
poetry config repositories.test https://test.pypi.org/legacy/
poetry config pypi-token.test <token-api>
```

Le paquet peut maintenant être diffusé sur [Test PiPy](https://test.pypi.org) à l'aide de la commande :

```bash
poetry publish -r test
```