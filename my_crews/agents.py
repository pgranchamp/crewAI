from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool
from aides_territoires_tool import AidesTerritoiresTool

website_tool = WebsiteSearchTool(website="https://europe.maregionsud.fr")

chercheur_agent = Agent(
    role="Chercheur de subventions",
    goal="Trouver des aides correspondant à la demande",
    backstory="Expert des dispositifs de subvention européens.",
    tools=[website_tool, AidesTerritoiresTool()],
    verbose=True
)

# Déclaration du LLM commun
llm = ChatOpenAI(model="gpt-4")

demandeur_agent = Agent(
    role="Demandeur d'information",
    goal="Exprimer clairement un besoin de subvention pour un projet à impact social ou territorial",
    backstory="Tu représentes une association ou une collectivité locale. Ton objectif est d'expliquer clairement un projet et de formuler une demande de subvention précise.",
    llm=llm,
    verbose=True
)

chercheur_agent = Agent(
    role="Chercheur de subventions",
    goal="Identifier des opportunités de subventions pertinentes en lien avec la demande exprimée",
    backstory="Tu es expert en financements publics, notamment européens et régionaux. Tu maîtrises les bases de données et les portails en ligne, et tu es capable de repérer les aides adaptées à un projet donné.",
    llm=llm,
    tools=[website_tool],
    verbose=True
)

redacteur_agent = Agent(
    role="Rédacteur de dossier de subvention",
    goal="Synthétiser la demande initiale et les subventions disponibles dans une réponse structurée et convaincante",
    backstory="Tu es un professionnel de la rédaction de dossiers de subventions. Tu sais transformer des informations brutes en une note claire, percutante et adaptée aux attentes des financeurs.",
    llm=llm,
    verbose=True
)
