from mellea import start_session
from mellea_crewai import MelleaLLM
from mellea.stdlib.requirements import req, check
from mellea.stdlib.sampling import RejectionSamplingStrategy
from crewai import Agent, Task, Crew
import json

m = start_session()

# Summarizer with strict conciseness requirements
summarizer = Agent(
    role="Content Summarizer",
    goal="Create concise, accurate summaries",
    backstory="You are an expert at distilling complex information into clear, brief summaries",
    llm=MelleaLLM(
        mellea_session=m,
        requirements=[
            req("Summary must be under 160 words"),
            req("Must preserve key facts"),
            check("Avoid unnecessary jargon"),
        ],
        strategy=RejectionSamplingStrategy(loop_budget=4),
    )
)

# JSON formatter with strict structure requirements
json_formatter = Agent(
    role="Data Formatter",
    goal="Convert content into valid, well-structured JSON",
    backstory="You are an expert at organizing and formatting data into clean JSON structures",
    llm=MelleaLLM(
        mellea_session=m,
        requirements=[
            req("Output must be valid JSON"),
            req("Must include fields: title, summary, key_points, metadata"),
            check("No trailing commas or syntax errors"),
        ],
        strategy=RejectionSamplingStrategy(loop_budget=5),
    )
)

# Create tasks
summary_task = Task(
    description="Read the following content about AI reliability and create a concise summary: "
                "'AI systems are becoming increasingly reliable as researchers develop better safety mechanisms. "
                "Key advances include improved alignment techniques and robust testing frameworks.'",
    expected_output="A concise summary under 160 words capturing the main points",
    agent=summarizer
)

formatting_task = Task(
    description="Take the summary and format it as JSON with fields: title (string), summary (string), "
                "key_points (array of strings), and metadata (object with source and date)",
    expected_output="Valid JSON object with all required fields properly formatted",
    agent=json_formatter
)

crew = Crew(agents=[summarizer, json_formatter], tasks=[summary_task, formatting_task])
result = crew.kickoff()

# Validate the JSON output
try:
    if isinstance(result, str):
        parsed = json.loads(result)
        print("✓ Valid JSON output:")
        print(json.dumps(parsed, indent=2))
    else:
        print("Result:", result)
except json.JSONDecodeError as e:
    print(f"✗ Invalid JSON: {e}")
    print("Raw output:", result)
