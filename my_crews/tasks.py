from crewai import Task
from agents import demandeur_agent, chercheur_agent, redacteur_agent

# Tâche 1 : Formuler la demande
task_demande = Task(
    description=(
        "Tu es une association ou une collectivité territoriale souhaitant obtenir une subvention. "
        "Formule une demande claire et contextualisée à propos de ton projet, de son territoire, de son public cible et de ses objectifs. "
        "Prépare cette demande à destination d’un expert en financement."
    ),
    expected_output=(
        "Une demande complète et contextualisée présentant clairement les besoins de financement. "
        "Inclure : nom du projet, type d'acteurs impliqués, territoire concerné, objectifs sociaux, publics cibles, état d’avancement."
    ),
    agent=demandeur_agent
)

# Tâche 2 : Chercher des subventions via l'API
task_recherche_api = Task(
    description=(
        "Tu es expert des dispositifs de financement publics, régionaux, européens. "
        "À partir de la demande exprimée par l’association, utilise l’API Aides-Territoires pour identifier deux ou trois subventions pertinentes. "
        "Utilise ton outil AidesTerritoiresTool pour interroger l’API selon les besoins exprimés dans la demande."
    ),
    expected_output=(
        "Une liste commentée de 2 à 3 dispositifs de financement issus de l’API Aides-Territoires, avec leurs critères d’éligibilité, lien officiel, montant moyen, date limite si connue, et justification de leur pertinence pour le projet."
    ),
    agent=chercheur_agent
)

# Tâche 3 : Rédiger une note de synthèse
task_redaction = Task(
    description=(
        "À partir des informations du demandeur et des recherches du chercheur, rédige une note synthétique. "
        "Cette note doit pouvoir être utilisée pour initier un dossier de demande de subvention."
    ),
    expected_output=(
        "Une note structurée comprenant : résumé du projet, besoins exprimés, dispositifs identifiés, et premières recommandations pour le dépôt du dossier."
    ),
    agent=redacteur_agent
)
