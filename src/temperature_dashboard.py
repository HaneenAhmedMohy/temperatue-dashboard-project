import os
from openai import OpenAI
from dotenv import load_dotenv
import textwrap

# Load environment variables from .env file
load_dotenv()

# Get API key, model URL, and model name from environment variables
api_key = os.getenv("OPENAI_API_KEY")
model_url = os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("OPENAI_MODEL")

# Initialize the OpenAI client with the custom base URL
client = OpenAI(
    api_key=api_key,
    base_url=model_url
)

def test_temperature(prompt, temperatures=[0.0, 0.5, 0.7, 1.0]):
    """
    Test the same prompt with different temperature values.
    Args:
        prompt: The user prompt to test
        temperatures: List of temperature values to test
    Returns:
        Dictionary mapping temperature to response
    """
    results = {}
    for temp in temperatures:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temp,
            max_tokens=150
        )
        content = response.choices[0].message.content.strip()
        results[temp] = content
    return results


def display_results(prompt, category, results):
    """Display results in a formatted dashboard."""
    print("=" * 50)
    print("TEMPERATURE EXPERIMENTATION DASHBOARD")
    print("=" * 50)
    print(f"Prompt: \"{prompt}\"")
    print(f"Category: {category}")
    print("-" * 50)

    # Show each temperature result
    for temp, response in results.items():
        print(f"Temperature {temp}:")
        print(textwrap.fill(response, width=80))
        print(f"(Length: {len(response.split())} words)\n")

    # Basic analysis
    all_responses = list(results.values())
    unique_responses = len(set(all_responses))

    print("-" * 50)
    print("ANALYSIS:")
    if unique_responses == 1:
        print("- Consistency: All temperatures produced identical responses.")
    else:
        print(f"- Consistency: {unique_responses} unique variations observed.")

    print("- Creativity tends to increase with temperature.")
    print("- Recommendation:")
    if category.lower() == "factual":
        print("  → Use temperature 0.0 or 0.5 for factual accuracy.")
    elif category.lower() == "creative":
        print("  → Use temperature 1.0 or 1.5 for creative writing.")
    elif category.lower() == "code":
        print("  → Use temperature 0.0–0.7 for reliable code generation.")
    elif category.lower() == "reasoning":
        print("  → Use temperature 0.5–0.7 for balanced logical reasoning.")
    print("=" * 50)
    print()


def main():
    """Main CLI interface."""
    print("\nWelcome to the Temperature Experimentation Dashboard!")
    print("==================================================")
    print("Choose a category:")
    print("1. Factual")
    print("2. Creative")
    print("3. Code")
    print("4. Reasoning")
    print("5. Use predefined test suite")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "5":
        test_suite()
        return

    category_map = {
        "1": "Factual",
        "2": "Creative",
        "3": "Code",
        "4": "Reasoning"
    }

    category = category_map.get(choice, "Factual")
    prompt = input(f"\nEnter your {category.lower()} prompt: ").strip()

    results = test_temperature(prompt)
    display_results(prompt, category, results)


def test_suite():
    """Run predefined test prompts."""
    test_prompts = {
        "Factual": "What is the capital of France?",
        "Creative": "Write a short story about a robot who learns to dream.",
        "Code": "Write a Python function to reverse a string.",
        "Reasoning": "If all roses are flowers and some flowers fade quickly, what can we conclude?"
    }

    for category, prompt in test_prompts.items():
        results = test_temperature(prompt)
        display_results(prompt, category, results)


if __name__ == "__main__":
    main()
