# Documentation Technique

## Objectif du Projet
Ce projet vise à développer une application interactive permettant de classifier les réponses d'un utilisateur en fonction de deux orientations possibles : **SISR** (Solutions d'Infrastructure, Systèmes et Réseaux) ou **SLAM** (Solutions Logicielles et Applications Métier). Le projet utilise un classifieur basé sur des mots-clés et propose un questionnaire interactif avec des visualisations pour guider l'utilisateur.

---

## Structure du Projet

```
IA/
├── src/
│   ├── classifier.py       # Contient la logique de classification
│   ├── questionnaire.py    # Script principal pour exécuter l'application
│   └── __pycache__/        # Fichiers compilés Python (à ignorer)
├── tests/
│   └── test_classifier.py  # Tests unitaires pour les fonctions du classifieur
├── README.md               # Documentation générale
└── requirements.txt        # Liste des dépendances
```

---

## Installation
### Prérequis
- Python 3.8 ou supérieur
- Pip (Gestionnaire de paquets Python)

### Étapes
1. Cloner le projet :
   ```bash
   git clone <URL-du-répertoire>
   cd IA
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## Description des Fichiers

### `src/classifier.py`
Ce module contient les fonctions principales pour analyser et classifier les textes.

#### Fonctions
- **`get_scores(text)`**
    - Entrée : Une chaîne de caractères (texte saisi par l'utilisateur).
    - Sortie : Deux scores correspondant aux occurrences de mots-clés SISR et SLAM.
    - Exemple :
      ```python
      sisr_score, slam_score = get_scores("J'aime les réseaux et le développement web")
      ```

- **`classify_text(text)`**
    - Entrée : Une chaîne de caractères.
    - Sortie : Une chaîne indiquant l'orientation probable : `"SISR"`, `"SLAM"` ou `"Inconnu"`.

### `src/questionnaire.py`
Ce fichier gère l'interface utilisateur et les visualisations interactives avec **Streamlit**.

#### Fonctionnalités principales
1. Pose des questions interactives à l'utilisateur.
2. Analyse les réponses à l'aide de `classify_text`.
3. Affiche une visualisation des scores avec **matplotlib**.

### `tests/test_classifier.py`
Contient des tests unitaires pour valider les fonctions du fichier `classifier.py`.

---

## Dépendances
Les bibliothèques suivantes sont utilisées :

- **Streamlit** : Pour créer une interface utilisateur interactive.
- **Matplotlib** : Pour générer des graphiques.
- **Pytest** : Pour exécuter des tests unitaires.

### Installation manuelle des dépendances
Si `requirements.txt` n'est pas utilisé, installez les bibliothèques directement :
```bash
pip install streamlit matplotlib pytest
```

---

## Exécution de l'Application
Pour lancer l'application Streamlit :
```bash
streamlit run src/questionnaire.py
```

---

## Tests
Pour exécuter les tests unitaires :
```bash
pytest tests/test_classifier.py
```

---

## Améliorations Futures
1Hébergement de l'application sur une plateforme cloud (par ex. Heroku, Streamlit Cloud).


---

## Auteur
Ce projet a été développé dans le cadre d'un atelier d'introduction à l'IA et à l'automatisation avec CI/CD.
