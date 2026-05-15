"""
CrewAI + Mellea Integration Demo
Multi-agent system with independent validation per agent.
"""

from mellea import start_session
from mellea_crewai import MelleaLLM
from mellea.stdlib.requirements import req, check
from mellea.stdlib.sampling import RejectionSamplingStrategy
from crewai import Agent, Task, Crew
import time


def demo_multi_agent_validation():
    """Demo: Multi-agent system with independent validation per agent."""

    print("="*60)
    print("CrewAI + Mellea Multi-Agent Demo")
    print("="*60)

    m = start_session()

    # Agent A: Summary Writer
    # Requirements: under 200 words, explain the topic (easier to pass on first try)
    summary_agent = Agent(
        role="Summary Writer",
        goal="Write concise and clear summaries of technical topics",
        backstory="You are an expert at distilling complex information into clear, brief summaries.",
        llm=MelleaLLM(
            mellea_session=m,
            requirements=[
                req("Must be under 200 words"),
                req("Must explain the topic clearly"),
            ],
            strategy=RejectionSamplingStrategy(loop_budget=3),
        )
    )

    # Agent B: JSON Formatter
    # Requirements: valid JSON, specific fields, arrays with minimum items, short point descriptions
    formatter_agent = Agent(
        role="JSON Formatter",
        goal="Format information as structured JSON",
        backstory="You are an expert at organizing data into clean, valid JSON structures.",
        llm=MelleaLLM(
            mellea_session=m,
            requirements=[
                req("Output must be valid JSON"),
                req("Must include 'topic' field with value 'Machine Learning'"),
                req("Must include 'keyPoints' as an array with exactly 3 items"),
                req("Each keyPoint description must be under 3 words"),
            ],
            strategy=RejectionSamplingStrategy(loop_budget=3),
        )
    )

    # Task 1: Summary generation
    summary_task = Task(
        description="Summarize the following topic: Machine Learning in Production. "
                    "Explain what it is, why it matters, and mention a key challenge.",
        expected_output="A brief summary (under 100 words) of machine learning in production",
        agent=summary_agent
    )

    # Task 2: JSON formatting
    json_task = Task(
        description="Format the following as valid JSON: "
                    "Topic: Machine Learning, Key Points: Model training, deployment, monitoring, performance tracking.",
        expected_output="Valid JSON with topic and keyPoints array",
        agent=formatter_agent
    )

    # Create crew
    crew = Crew(
        agents=[summary_agent, formatter_agent],
        tasks=[summary_task, json_task],
        verbose=True,
    )

    print("\nStarting multi-agent crew with independent validation...\n")
    start_time = time.time()

    try:
        result = crew.kickoff()
        elapsed = time.time() - start_time

        print(f"\n{'='*60}")
        print("Crew Execution Complete")
        print(f"{'='*60}")
        print(f"\nResults:\n{result}")
        print(f"\n✓ All agents passed validation in {elapsed:.1f}s")

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n✗ Crew execution failed: {e}")
        print(f"Time spent: {elapsed:.1f}s")


def demo_independent_agent_validation():
    """Demo: Run agents independently to show separate validation cycles."""

    print("\n" + "="*60)
    print("Independent Agent Validation Demo")
    print("="*60)

    m = start_session()

    # Agent A: Researcher
    # Requirements: provide examples and explanation
    researcher = Agent(
        role="Senior Researcher",
        goal="Conduct thorough research on technical topics",
        backstory="You are an expert researcher with decades of experience in AI and software systems.",
        llm=MelleaLLM(
            mellea_session=m,
            requirements=[
                req("Must explain the topic clearly"),
                req("Must include at least two relevant points"),
            ],
            strategy=RejectionSamplingStrategy(loop_budget=3),
        )
    )

    # Agent B: Content Writer
    # Requirements: informative and organized
    writer = Agent(
        role="Content Writer",
        goal="Write engaging technical content",
        backstory="You are an accomplished writer with a talent for making technical topics accessible.",
        llm=MelleaLLM(
            mellea_session=m,
            requirements=[
                req("Must provide clear and useful information"),
                req("Must be organized and coherent"),
            ],
            strategy=RejectionSamplingStrategy(loop_budget=3),
        )
    )

    # Task 1: Research
    research_task = Task(
        description="Research and explain AI reliability in production systems. "
                    "Include specific examples and data about validation techniques.",
        expected_output="A detailed explanation with specific examples and data points",
        agent=researcher
    )

    # Task 2: Writing
    writing_task = Task(
        description="Write an engaging blog post based on AI reliability research.",
        expected_output="An engaging, well-structured blog post with compelling introduction",
        agent=writer
    )

    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
    )

    print("\nStarting independent agent validation...\n")
    start_time = time.time()

    try:
        result = crew.kickoff()
        elapsed = time.time() - start_time

        print(f"\n{'='*60}")
        print("Independent Validation Complete")
        print(f"{'='*60}")
        print(f"\nResults:\n{result}")
        print(f"\n✓ All agents passed independent validation in {elapsed:.1f}s")

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n✗ Validation failed: {e}")
        print(f"Time spent: {elapsed:.1f}s")


if __name__ == "__main__":
    # Run multi-agent demo with different validation per agent
    demo_multi_agent_validation()

    # Run independent validation demo with stricter requirements
    demo_independent_agent_validation()
