from crewai import Crew
from agents import demandeur_agent, chercheur_agent, redacteur_agent
from tasks import task_demande, task_recherche, task_redaction
from rich.console import Console

console = Console()

crew = Crew(
    agents=[demandeur_agent, chercheur_agent, redacteur_agent],
    tasks=[task_demande, task_recherche, task_redaction],
    verbose=True
)

if __name__ == "__main__":
    demande_utilisateur = input("Quelle est votre demande ?\n> ")
    result = crew.kickoff(inputs={"demande": demande_utilisateur})

    console.rule("[bold cyan]Résultat final du Crew")
    console.print(result, style="bold white on black")