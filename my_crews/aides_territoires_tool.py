import requests
from crewai_tools import BaseTool

class AidesTerritoiresTool(BaseTool):
    name = "AidesTerritoiresTool"
    description = "Interroge l'API Aides-Territoires pour récupérer des subventions correspondant à un mot-clé."

    def _run(self, query: str) -> str:
        url = "https://aides-territoires.beta.gouv.fr/api/aids/"
        params = {
            "search": query,
            "targeted_audiences": "association",
            "limit": 5
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if not data["results"]:
                return f"Aucune aide trouvée pour : {query}"

            result = ""
            for aide in data["results"]:
                result += f"\nTitre : {aide['name']}\n"
                result += f"Description : {aide['description'][:300]}...\n"
                result += f"URL : {aide['url']}\n"

            return result
        except requests.RequestException as e:
            return f"Erreur lors de l'appel à l'API Aides-Territoires : {e}"