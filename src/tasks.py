from crewai import Task

def create_tasks(topic_agent, writer_agent, seo_agent, topic):
    topic_task = Task(
        description=f"Generate 3 trending LinkedIn post topics about the importance of {topic}.",
        expected_output="A list of 3 topics.",
        agent=topic_agent
    )

    writer_task = Task(
        description="Create Linkedin post in the following styles: 1) long-form, and 2) listicle.",
        expected_output="A content option for the given LinkedIn post topic.",
        agent=writer_agent
    )

    seo_task = Task(
        description="Enhance each post with relevant keywords, hashtags, and an authoritative link.",
        expected_output="SEO-optimized versions of each post.",
        agent=seo_agent
    )

    return topic_task, writer_task, seo_task
