"""
LangChain + Mellea Integration Demo
Generates product descriptions with automatic validation and retries.
"""

from mellea import start_session
from mellea_langchain import MelleaChatModel
from mellea.stdlib.requirements import req
from mellea.stdlib.sampling import RejectionSamplingStrategy
from langchain_core.prompts import ChatPromptTemplate
import time


def demo_product_description():
    """Demo: Generate product descriptions with Mellea validation."""

    # Initialize Mellea session
    m = start_session()
    chat_model = MelleaChatModel(mellea_session=m)

    # Define the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that writes compelling product descriptions."),
        ("human", "Write a product description for: {product}")
    ])

    # Validated chain with quality guarantees
    chain = prompt | chat_model.bind(
        model_options={
            "requirements": [
                req("Must be between 50-100 words"),
                req("Must mention at least two product features"),
                req("Must include a clear benefit statement"),
            ],
            "strategy": RejectionSamplingStrategy(loop_budget=3),
        }
    )

    # Run the chain
    products = [
        "Wireless Bluetooth Headphones",
        "Stainless Steel Water Bottle",
        "Portable Solar Power Bank"
    ]

    for product in products:
        print(f"\n{'='*60}")
        print(f"Generating: {product}")
        print(f"{'='*60}")

        start_time = time.time()

        try:
            result = chain.invoke({"product": product})
            elapsed = time.time() - start_time

            print(f"\nResult:")
            print(result.content if hasattr(result, 'content') else result)
            print(f"\n✓ Passed validation in {elapsed:.1f}s")
        except Exception as e:
            elapsed = time.time() - start_time
            print(f"\n✗ Failed: {e}")
            print(f"Time spent: {elapsed:.1f}s")

        print()


def demo_blog_post():
    """Demo: Generate a blog post with stricter validation."""

    m = start_session()
    chat_model = MelleaChatModel(mellea_session=m)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert technical writer. Write clear, actionable blog posts."),
        ("human", "Write a blog post about: {topic}")
    ])

    # Stricter requirements for blog posts
    chain = prompt | chat_model.bind(
        model_options={
            "requirements": [
                req("Must have a compelling title"),
                req("Must be between 500-1000 words"),
                req("Must include practical examples"),
                req("Must have clear section headers"),
                req("Must conclude with actionable takeaways"),
            ],
            "strategy": RejectionSamplingStrategy(loop_budget=3),
        }
    )

    print(f"\n{'='*60}")
    print("Blog Post Generation with Validation")
    print(f"{'='*60}\n")

    start_time = time.time()

    try:
        result = chain.invoke({"topic": "AI reliability in production"})
        elapsed = time.time() - start_time

        print(f"Generated Blog Post:")
        print(result.content if hasattr(result, 'content') else result)
        print(f"\n✓ Passed all validation requirements in {elapsed:.1f}s")
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"✗ Failed: {e}")
        print(f"Time spent: {elapsed:.1f}s")


if __name__ == "__main__":
    print("LangChain + Mellea Integration Demo")
    print("=" * 60)

    # Run product description demo
    demo_product_description()

    # Run blog post demo
    demo_blog_post()
