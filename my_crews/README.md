# README.md
# FEDER CrewAI — Le Dossier Parfait

Ce projet utilise [CrewAI](https://github.com/crewAIInc/crewAI) pour orchestrer des agents capables d'accompagner la rédaction de dossiers de subvention, avec un premier cas d'usage ciblant les aides FEDER.

## Structure du projet

- `main.py` : Point d’entrée principal. Utilise `crew.kickoff()` pour injecter dynamiquement une demande utilisateur.
- `agents.py` : Contient les trois agents principaux :
  - `demandeur_agent`
  - `chercheur_agent`
  - `redacteur_agent`
- `tasks.py` : Définition des tâches confiées aux agents, avec transmission de l’input `"demande"`.
- `requirements.txt` : Dépendances du projet (attention aux versions compatibles).

## Bonnes pratiques CrewAI

- ✅ Utiliser `crew.kickoff(inputs={"demande": ...})` pour passer des données dynamiques aux tâches.
- ✅ Vérifier que tous les outils héritent bien de `BaseTool`.
- ⚠️ Respecter la compatibilité entre `crewai`, `crewai-tools`, et `pydantic` (souvent en V2).
- ⚠️ En cas d'erreur `pydantic.errors.PydanticUserError`, vérifier que tous les champs de vos classes sont bien annotés.
- ✅ L’import correct de `WebsiteSearchTool` :  
```python
from crewai_tools import WebsiteSearchTool
```

## Prochaine étape

- Intégration du `WebsiteSearchTool` pointant vers https://europe.maregionsud.fr
- Ajout d’APIs externes comme `Aides-Territoires`
- Interface utilisateur (terminal puis interface web)

## Auteur

Projet piloté par **Finamars** - Contact : pierre.granchamp@finamars.com

