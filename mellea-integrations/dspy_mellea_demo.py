"""
DSPy + Mellea Integration Demo
Typed signatures with automatic validation and retries.
"""

import dspy
from mellea import start_session
from mellea_dspy import MelleaLM
from mellea.stdlib.requirements import req
from mellea.stdlib.sampling import RejectionSamplingStrategy
import time


# Configure Mellea LM with requirements
def setup_dspy_with_mellea():
    """Setup DSPy with Mellea validation."""
    m = start_session()
    lm = MelleaLM(
        mellea_session=m,
        model="mellea-ollama",
        requirements=[
            req("Must include a working code example"),
            req("Must clearly explain the input parameters"),
            req("Must explain what the function returns"),
        ],
        strategy=RejectionSamplingStrategy(loop_budget=3)
    )
    dspy.configure(lm=lm)
    return m, lm


# DSPy signature - validation happens automatically
class DocGenerator(dspy.Signature):
    """Generate technical documentation for code."""
    code = dspy.InputField(desc="Code snippet to document")
    documentation = dspy.OutputField(desc="Clear, professional documentation with examples and parameter explanations")


def demo_documentation_generation():
    """Demo: Generate documentation with validation."""
    print("=" * 60)
    print("DSPy + Mellea Integration Demo")
    print("=" * 60)

    m, lm = setup_dspy_with_mellea()

    # DSPy Predict - validation happens automatically
    doc_gen = dspy.Predict(DocGenerator)

    code_examples = [
        "def calculate_total(items): return sum(i['price'] * i['quantity'] for i in items)",
    ]

    for idx, code in enumerate(code_examples, 1):
        print(f"\n{'='*60}")
        print(f"Example {idx}: Generating documentation")
        print(f"{'='*60}")
        print(f"Code: {code}\n")

        start_time = time.time()

        try:
            # Invoke DSPy prediction with validation
            result = doc_gen(code=code)
            elapsed = time.time() - start_time

            print("Generated Documentation:")
            print(result.documentation)
            print(f"\n✓ Validation passed in {elapsed:.1f}s")

        except Exception as e:
            elapsed = time.time() - start_time
            print(f"✗ Failed: {e}")
            print(f"Time spent: {elapsed:.1f}s")

    print(f"\n{'='*60}\n")


def demo_typed_signature_validation():
    """Demo: Show typed signature with Mellea validation."""
    print("=" * 60)
    print("Typed Signature with Mellea Validation")
    print("=" * 60)

    m, lm = setup_dspy_with_mellea()

    # More complex typed signature
    class APIEndpointDocumenter(dspy.Signature):
        """Document an API endpoint with comprehensive details."""
        endpoint_name = dspy.InputField(desc="API endpoint name (e.g., /api/users)")
        method = dspy.InputField(desc="HTTP method (GET, POST, PUT, DELETE)")
        documentation = dspy.OutputField(
            desc="API documentation including request example, response structure, and parameters explanation"
        )

    api_documenter = dspy.Predict(APIEndpointDocumenter)

    api_examples = [
        {
            "endpoint": "/api/users",
            "method": "GET"
        }
    ]

    for api in api_examples:
        print(f"\nEndpoint: {api['endpoint']} [{api['method']}]")
        print("-" * 40)

        start_time = time.time()

        try:
            result = api_documenter(
                endpoint_name=api['endpoint'],
                method=api['method']
            )
            elapsed = time.time() - start_time

            print("API Documentation:")
            print(result.documentation)
            print(f"✓ Generated in {elapsed:.1f}s\n")

        except Exception as e:
            elapsed = time.time() - start_time
            print(f"✗ Failed: {e}")
            print(f"Time spent: {elapsed:.1f}s\n")

    print(f"{'='*60}\n")


if __name__ == "__main__":
    print("DSPy + Mellea Integration Demo\n")

    # Run documentation generation demo
    demo_documentation_generation()

    # Run typed signature validation demo
    demo_typed_signature_validation()

    print("All demos completed!")
