from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
llm_gpt4 = ChatOpenAI(model="gpt-4", temperature=0.7)

load_dotenv()

# Créons un agent test
redacteur = Agent(
    role="Rédacteur de subventions",
    goal="Élaborer des argumentaires convaincants et structurés pour répondre aux appels à projets",
    backstory="Tu travailles main dans la main avec un chercheur de subventions. Ton rôle est de rédiger des réponses percutantes en fonction des éléments fournis par le chercheur et du cahier des charges des financeurs.",
    llm=llm_gpt4,
    verbose=True
)

chercheur = Agent(
    role="Chercheur de subventions",
    goal="Identifier des opportunités de financement pertinentes",
    backstory="Tu travailles en binôme avec un rédacteur pour construire un dossier FEDER pour un projet d’inclusion numérique. Ton rôle est de rechercher sur internet et dans les bases officielles les subventions adaptées.",
    verbose=True
)

decouvreur = Agent(
    role="Demandeur de subvention",
    goal="Exprimer clairement les besoins du porteur de projet et fournir les informations essentielles aux autres agents",
    backstory="Tu es une association ou une collectivité qui cherche des financements. Tu exprimes un besoin concret, une situation locale, un objectif. Ton rôle est d'exposer une demande structurée aux autres agents pour qu’ils puissent chercher et rédiger en retour.",
    llm=llm_gpt4,
    verbose=True
)

user_input = input("Décris ton besoin : ")

# Créons une tâche
task_question = Task(
    description=f"Voici la demande exprimée : {user_input}. Résume-la clairement pour l’équipe.",
    expected_output="Un résumé clair du besoin et du profil du porteur de projet, incluant localisation, public cible, objectifs et contraintes.",
    agent=decouvreur,
    context=[],
    allow_delegation=True
)

task_recherche = Task(
    description="Recherche sur internet les subventions FEDER disponibles pour un projet d’inclusion numérique pour des jeunes en difficulté.",
    expected_output="Un résumé de subventions FEDER pertinentes avec URL, critères d’éligibilité et échéances",
    agent=chercheur,
    context=[],
    allow_delegation=True
)

task_redaction = Task(
    description="À partir des éléments fournis par le découvreur et des subventions trouvées par le chercheur, rédige une synthèse structurée à destination d’un décideur.",
    expected_output="Un document synthétique structuré : contexte, besoin, subventions proposées, lien et résumé des critères.",
    agent=redacteur,
    context=[],
    allow_delegation=False
)

# Créons le crew
crew = Crew(
    agents=[decouvreur, chercheur, redacteur],
    tasks=[task_question, task_recherche, task_redaction],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== Résultat final ===\n")
    print(result)