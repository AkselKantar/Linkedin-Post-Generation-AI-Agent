from src.agents import topic_agent, writer_agent, seo_agent
from src.tasks import topic_task, writer_task, seo_task
from crewai import Crew

# Assemble Crew
task_list = [topic_task, writer_task, seo_task]
agents = [topic_agent, writer_agent, seo_agent]

crew = Crew(
    agents=agents,
    tasks=task_list,
    verbose=True
)

# Run it!
result = crew.kickoff()
print("\nFinal Output:\n")
print(result)