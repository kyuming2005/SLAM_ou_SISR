# Orientation SISR ou SLAM

Ce projet est une application interactive permettant aux utilisateurs de déterminer leur orientation entre les deux filières SISR (Systèmes et Réseaux) et SLAM (Solutions Logicielles et Applications Métiers) en fonction de leurs réponses ou de leurs intérêts techniques.

---

## Fonctionnalités principales

- **Analyse des réponses utilisateurs :** Classe les réponses en fonction de mots-clés associés aux deux filières.
- **Graphique interactif :** Affiche un graphique en camembert pour représenter la répartition des scores entre SISR et SLAM.
- **Prise en compte des réponses négatives :** Gère les réponses contenant des phrases telles que "je n'aime pas" pour ajuster les scores.

---

## Structure du projet

Le projet est divisé en deux fichiers principaux:

### `questionnaire.py`
Ce fichier contient l'interface utilisateur développée avec **Streamlit**. Il permet :
- De recueillir la saisie utilisateur.
- De classifier les réponses avec la fonction `classify_text` provenant de `classifier.py`.
- D'afficher les scores et le graphique en camembert.

### `classifier.py`
Ce fichier contient la logique métier du projet :
- **`get_scores` :** Calcule les scores pour chaque filière en fonction des mots-clés trouvés dans le texte.
- **`classify_text` :** Classe l'utilisateur en SISR, SLAM ou indécis (si les scores sont égaux).
- Prend en compte des réponses négatives pour ajuster les scores.

---

## Technologies utilisées

- **Python 3.10+**
- **Bibliothèques :**
    - `streamlit` : Création de l'interface utilisateur interactive.
    - `matplotlib` : Génération de graphiques en camembert.

---

## Installation

### Pré-requis
Assurez-vous que Python 3.10 ou supérieur est installé sur votre machine.

### Étapes d'installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/orientation-sisr-slam.git
   cd orientation-sisr-slam
   ```
   ou télécharger la version ZIP du fichier
2. installer les dépendances:
    ```bash
    pip install -r requirements.txt
    ```
   ou

    ```bash
   pip install streamlit
   pip install matplotlib
   ```

3. lancer l'application :

    ```bash
   cd src
   streamlit run questionnaire.py
   ```

