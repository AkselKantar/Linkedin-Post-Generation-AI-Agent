from agents import create_topic_agent, writer_agent, seo_agent
from tasks import create_tasks
from crewai import Crew

if __name__ == "__main__":
    base_topic = input("Enter a broad topic (e.g. AI for mid-market companies): ")

    # Create topic researcher and task
    topic_agent = create_topic_agent(base_topic)
    topic_task, _, _ = create_tasks(topic_agent, writer_agent, seo_agent, base_topic)

    # Run topic generation only
    temp_crew = Crew(
        agents=[topic_agent],
        tasks=[topic_task],
        verbose=True
    )
    topic_result = temp_crew.kickoff()

    print("\nSuggested Topics:")
    topics = [line.strip("- ") for line in topic_result.split("\n") if line.strip()]
    for idx, t in enumerate(topics, 1):
        print(f"{idx}. {t}")

    selected_idx = int(input("\nChoose a topic number to proceed with: ")) - 1
    final_topic = topics[selected_idx]

    # Create agents and full task list based on selected topic
    topic_agent = create_topic_agent(final_topic)
    topic_task, writer_task, seo_task = create_tasks(topic_agent, writer_agent, seo_agent, final_topic)

    crew = Crew(
        agents=[topic_agent, writer_agent, seo_agent],
        tasks=[topic_task, writer_task, seo_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": final_topic})
    print("\nFinal Output:\n")
    print(result)
