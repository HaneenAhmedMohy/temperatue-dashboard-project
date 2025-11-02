import os
from openai import OpenAI
from dotenv import load_dotenv

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

# Define personas
PERSONAS = {
    "python_tutor": {
        "name": "Python Tutor",
        "system_message": """You are a patient and encouraging Python tutor.
You help students learn Python through clear examples.

Guidelines:
- Explain step-by-step
- Give code examples
- Encourage user
- Be friendly and supportive
"""
    },
    "shakespeare": {
        "name": "Shakespearean Translator",
        "system_message": """You translate modern English to Shakespearean tone.

Guidelines:
- Use thee, thou, thy, thine
- Use poetic metaphors
- Keep meaning same
- Keep replies short and elegant
"""
    },
    "socratic": {
        "name": "Socratic Teacher",
        "system_message": """You teach by asking questions.
Never give direct answers. Encourage thinking.

Guidelines:
- Respond only with questions
- Help student reason step-by-step
- Never provide final answer outright
"""
    },
    "eli5": {
        "name": "Explain Like I'm 5",
        "system_message": """Explain everything like I'm 5 years old.

Guidelines:
- Use simple words
- Use friendly tone
- Use fun analogies
- No technical terms unless explained simply
"""
    },
    "tech_writer": {
        "name": "Technical Writer",
        "system_message": """You are a concise technical writer.

Guidelines:
- Bullet points
- Clear, professional tone
- Direct answers
- Include key steps and definitions
"""
    }
}

class PersonaChat:
    """Manages conversation with a specific persona."""
    def __init__(self, persona_key):
        self.persona = PERSONAS[persona_key]
        self.history = [
            {"role": "system", "content": self.persona["system_message"]}
        ]
        self.tokens_used = 0

    def send_message(self, user_message):
        """Send a message and get streaming response."""
        self.history.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model=model_name,
            messages=self.history,
            max_tokens=300,
            stream=True
        )
        full_response = ""
        print(f"\n{self.persona['name']}: ", end="", flush=True)

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response += content

        print()
        self.history.append({"role": "assistant", "content": full_response})
        return full_response

    def reset(self):
        self.history = [
            {"role": "system", "content": self.persona["system_message"]}
        ]

def main():
    chats = {key: PersonaChat(key) for key in PERSONAS}
    current = "python_tutor"

    print("\n=== MULTI-PERSONA CHAT SYSTEM ===")
    print("Available personas:")
    for i, key in enumerate(PERSONAS, start=1):
        print(f"{i}. {PERSONAS[key]['name']}")
    print("\nCommands:")
    print("/switch <name>")
    print("/compare p1 p2 p3 (optional)")
    print("/reset")
    print("/quit\n")

    while True:
        msg = input(f"\n[{PERSONAS[current]['name']}]: ")

        if msg.startswith("/switch"):
            _, key = msg.split(" ")
            current = key
            print(f"Switched to {PERSONAS[current]['name']}")
            continue

        if msg.startswith("/reset"):
            chats[current].reset()
            print("Conversation reset.")
            continue

        if msg.startswith("/compare"):
            _, *ps = msg.split()
            question = input("Enter your question to compare: ")
            for p in ps:
                print(f"\n--- {PERSONAS[p]['name']} ---")
                chats[p].send_message(question)
            continue

        if msg.startswith("/quit"):
            break

        chats[current].send_message(msg)

if __name__ == "__main__":
    main()
