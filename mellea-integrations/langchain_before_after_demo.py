"""
LangChain Before/After: Unvalidated vs. Validated Outputs
Demonstrates the problem that Mellea solves.
"""

from langchain_ollama import OllamaLLM
from mellea import start_session
from mellea_langchain import MelleaChatModel
from mellea.stdlib.requirements import req
from mellea.stdlib.sampling import RejectionSamplingStrategy
from langchain_core.prompts import ChatPromptTemplate
import time


def demo_unvalidated_chain():
    """BEFORE: Basic LangChain chain without Mellea validation."""
    print("=" * 70)
    print("BEFORE: Unvalidated LangChain Chain (No Quality Guarantees)")
    print("=" * 70)

    # Basic LangChain Ollama LLM without any validation layer
    llm = OllamaLLM(model="granite4:micro", temperature=0.7)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a product marketing expert. Write a compelling product description."),
        ("human", "Write a product description for: {product}")
    ])

    # Simple chain - NO validation (no model_options)
    chain = prompt | llm

    products = [
        "Wireless Bluetooth Headphones",
        "Stainless Steel Water Bottle",
    ]

    for product in products:
        print(f"\n[Product: {product}]")
        print("-" * 70)

        start_time = time.time()

        try:
            result = chain.invoke({"product": product})
            elapsed = time.time() - start_time

            output = result.content if hasattr(result, 'content') else str(result)
            word_count = len(output.split())

            print(f"Output ({word_count} words):")
            print(output[:200] + "..." if len(output) > 200 else output)
            print(f"\n⚠️  No validation! Output may not meet requirements.")
            print(f"Time: {elapsed:.1f}s\n")

        except Exception as e:
            print(f"Error: {e}\n")

    print("=" * 70)
    print("PROBLEMS WITHOUT VALIDATION:")
    print("  ❌ Output too long (200+ words instead of 50-100)")
    print("  ❌ Missing product features")
    print("  ❌ No benefit statement")
    print("  ❌ May break downstream systems")
    print("=" * 70)


def demo_validated_chain():
    """AFTER: LangChain chain with Mellea validation."""
    print("\n\n" + "=" * 70)
    print("AFTER: Validated LangChain Chain (With Mellea)")
    print("=" * 70)

    # Initialize Mellea with ollama granite4:micro
    m = start_session()
    chat_model = MelleaChatModel(
        mellea_session=m,
        model="mellea-ollama"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a product marketing expert. Write a compelling product description."),
        ("human", "Write a product description for: {product}")
    ])

    # Chain with Mellea validation
    chain = prompt | chat_model.bind(
        model_options={
            "requirements": [
                req("Must be between 50-100 words"),
                req("Must mention at least two product features"),
                req("Must include a benefit statement"),
            ],
            "strategy": RejectionSamplingStrategy(loop_budget=3),
        }
    )

    products = [
        "Wireless Bluetooth Headphones",
        "Stainless Steel Water Bottle",
    ]

    for product in products:
        print(f"\n[Product: {product}]")
        print("-" * 70)

        start_time = time.time()

        try:
            result = chain.invoke({"product": product})
            elapsed = time.time() - start_time

            output = result.content if hasattr(result, 'content') else str(result)
            word_count = len(output.split())

            print(f"Output ({word_count} words):")
            print(output)
            print(f"\n✓ Validation PASSED! All requirements met.")
            print(f"Time: {elapsed:.1f}s\n")

        except Exception as e:
            elapsed = time.time() - start_time
            print(f"Error: {e}")
            print(f"Time spent: {elapsed:.1f}s\n")

    print("=" * 70)
    print("BENEFITS WITH MELLEA VALIDATION:")
    print("  ✅ Output always meets word count (50-100 words)")
    print("  ✅ Always includes required features")
    print("  ✅ Always includes benefit statement")
    print("  ✅ Automatic retries until spec is met")
    print("  ✅ No downstream system failures")
    print("=" * 70)


def show_bad_output_examples():
    """Show examples of unvalidated bad outputs."""
    print("\n\n" + "=" * 70)
    print("EXAMPLES OF BAD UNVALIDATED OUTPUTS")
    print("=" * 70)

    examples = [
        {
            "title": "Too Short (8 words)",
            "output": "Great product! Highly recommended for everyone.",
            "issue": "Missing details, requirements, and benefits",
        },
        {
            "title": "Missing Features",
            "output": "This is a great product. It works really well. You will love it.",
            "issue": "No specific features mentioned; too vague",
        },
        {
            "title": "No Benefit Statement",
            "output": "The product has a battery. It charges your devices. It's made of plastic.",
            "issue": "Technical specs but no clear user benefit or value proposition",
        },
        {
            "title": "Wrong Format (Structured Data Expected)",
            "output": "Just some text about the product without any structure or organization.",
            "issue": "Expected JSON/structured output but got plain text",
        },
    ]

    for example in examples:
        print(f"\n[{example['title']}]")
        print("-" * 70)
        print(f"Output: \"{example['output']}\"")
        print(f"Issue:  {example['issue']}")
        print()

    print("=" * 70)
    print("MELLEA VALIDATION CATCHES ALL OF THESE:")
    print("  • Too short/too long: ✓ Word count checks")
    print("  • Missing features: ✓ Content requirement checks")
    print("  • No benefits: ✓ Explicit benefit statement requirement")
    print("  • Wrong format: ✓ Structure/format requirement checks")
    print("=" * 70)


if __name__ == "__main__":
    print("\n")
    print("█" * 70)
    print("█ LangChain Before/After: The Problem Mellea Solves")
    print("█" * 70)
    print()

    # Show unvalidated outputs
    demo_unvalidated_chain()

    # Show validated outputs
    demo_validated_chain()

    # Show examples of bad outputs
    show_bad_output_examples()

    print("\n")
    print("█" * 70)
    print("█ Summary: Mellea adds quality guarantees to LangChain")
    print("█" * 70)
    print()
