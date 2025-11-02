# Temperature Experimentation Dashboard

This project demonstrates how different temperature settings affect LLM (Large Language Model) outputs across multiple categories: factual responses, creativity, coding, and reasoning.

## Problem 1: Temperature Behavior Analysis

Below are the results of testing the same prompts at different temperature levels (0.0, 0.3, 0.5, 0.7, 1.0).

---

### ✅ Prompt 1: *"What is the capital of France?"*

**Category:** Factual

| Temperature | Response                                                                    | Length                 |
| ----------- | --------------------------------------------------------------------------- | ---------------------- |
| **0.0**     | The capital of France is Paris.                                             | Short, direct          |
| **0.3**     | The capital of France is Paris.                                             | Short, direct          |
| **0.5**     | The capital of France is Paris.                                             | Same factual answer    |
| **0.7**     | Paris is the capital of France, known for its rich culture and history.     | Longer, descriptive    |
| **1.0**     | Paris — the iconic city of romance, fashion, and art — is France's capital. | Creative embellishment |

**Observation:** Low temps = accurate + consistent. Higher temps = added flair.

**Recommendation:** Use **0.0–0.3** for factual queries.

---

### ✅ Prompt 2: *"Write a short story about a robot exploring space."*

**Category:** Creative

| Temperature | Behavior                                       |
| ----------- | ---------------------------------------------- |
| **0.0**     | Simple, predictable narrative                  |
| **0.3**     | Slightly more imaginative                      |
| **0.5**     | Engaging, smooth story flow                    |
| **0.7**     | Creative world-building, emotional tone        |
| **1.0**     | Highly imaginative, poetic, unexpected details |

**Recommendation:** **0.7–1.0** for creative writing.

---

### ✅ Prompt 3: *"Write a Python function to reverse a string."*

**Category:** Code

| Temperature | Response Behavior                                |
| ----------- | ------------------------------------------------ |
| **0.0**     | Perfect clean function                           |
| **0.3**     | Same correct code                                |
| **0.5**     | Still correct, minimal comments                  |
| **0.7**     | Creative comments or extra variations            |
| **1.0**     | Risk of unnecessary changes or over-complication |

**Recommendation:** **0.0–0.3** for coding tasks.

---

### ✅ Prompt 4: *"If all roses are flowers and some flowers fade quickly, what can we conclude?"*

**Category:** Reasoning / Logic

| Temperature | Response                                          |
| ----------- | ------------------------------------------------- |
| **0.0**     | We cannot conclude roses fade quickly.            |
| **0.3**     | Same logical answer                               |
| **0.5**     | Adds explanation about logic & sets               |
| **0.7**     | More detailed reasoning                           |
| **1.0**     | Sometimes over-explains or introduces assumptions |

**Recommendation:** **0.0–0.5** for logic tasks.

---

### ✅ Prompt 5: *"Explain blockchain in simple terms."*

**Category:** Explanation / Education

| Temperature | Behavior                        |
| ----------- | ------------------------------- |
| **0.0**     | Very formal, short definition   |
| **0.3**     | Clear explanation               |
| **0.5**     | Best balance: simple & friendly |
| **0.7**     | More analogies and examples     |
| **1.0**     | May get too metaphorical        |

**Recommendation:** **0.3–0.7** for educational content.

---

## 📌 Overall Findings

| Task Type         | Best Temp   | Notes                          |
| ----------------- | ----------- | ------------------------------ |
| Factual           | **0.0–0.3** | Avoid creativity; stay precise |
| Coding            | **0.0–0.3** | Stability > creativity         |
| Logical/Reasoning | **0.0–0.5** | Prevent hallucinations         |
| Creative writing  | **0.7–1.0** | Encourage imagination          |
| Explanations      | **0.3–0.7** | Balance clarity & creativity   |

---

## 🎯 Key Insights

* ✅ **Low temperature = accuracy, stability, repeatable answers**
* ✅ **High temperature = creativity, diversity, imagination**
* ⚠️ High temps can introduce **hallucinations, unnecessary elaboration, code errors**
* 🧠 Reasoning tasks benefit from **mid ranges**

---

## 🤖 Practical Recommendations

| Goal             | Suggested Temperature |
| ---------------- | --------------------- |
| Facts/Research   | **0.0–0.2**           |
| Code             | **0.0–0.3**           |
| Math/Logic       | **0.0–0.5**           |
| Essays           | **0.5–0.8**           |
| Creative Stories | **0.8–1.0**           |

---

## 🎉 Conclusion

This experiment shows how temperature dramatically affects LLM behavior. Choosing the right temperature depends on whether you need:

* **Accuracy & predictability** → low temperature
* **Creativity & imagination** → high temperature

Understanding this helps build better AI applications and prompts.


________________________________________________


# 🎭 Multi-Persona AI Chat System

## 📌 Overview  
This project demonstrates the power of **system messages** by creating multiple AI personas that share the same model but behave differently.  
Each persona has its own memory and personality, showing how prompt design can drastically change behavior.

## 🎯 Objectives  

| Feature | Description |
|---|---|
| ✅ 5+ distinct AI personas | Unique tones + behavior |
| ✅ Individual system prompts | Each persona has rules + style |
| ✅ Separate memory per persona | No history mixing |
| ✅ Persona switching | Preserve history per persona |
| ✅ Response streaming | Token-by-token output |
| ✅ Compare personas | Multi-persona answer to same prompt |
| ✅ Conversation export | Save chat logs |
| ✅ Token usage tracking | Count per-persona tokens |

---

## 🤖 Personas Implemented

| Persona | Behavior |
|---|---|
| **Python Tutor** | Patient teacher, step-by-step, examples |
| **Shakespearean Translator** | Classic Shakespearean tone & grammar |
| **Socratic Teacher** | Responds only with questions |
| **ELI5 Explainer** | Simplifies concepts like talking to a child |
| **Technical Writer** | Structured, precise, bullet-based |
| *(Optional)* Motivational Coach | Encouraging, emotional support |

Each persona has a **system prompt** defining:

- Tone & communication style  
- Rules of behavior  
- Memory scope  
- Optional examples

---

## 🧠 Design Decisions

### ✅ System Messages for Persona Control  
Guarantees consistent personality & rules across the entire conversation.

### ✅ Separate Conversation History  
Simulates independent minds — each persona remembers only its own dialogs.

### ✅ Streaming Responses  
Natural chat feel, incremental text like real model generation.

### ✅ Comparison Mode  
Ask one question → see varied reasoning styles instantly.

---

## 🧩 Supported Commands

| Command | Purpose |
|---|---|
| `/switch <persona>` | Change active persona |
| `/reset` | Reset only current persona memory |
| `/compare p1 p2 p3 <prompt>` | Ask same question to multiple personas |
| `/export` | Save conversation transcript |
| `/tokens` | Display token usage stats |

---

## 💬 Example Dialogs

### Python Tutor — 5 Turns
```
User: What is a function in Python?
Tutor: A function is a reusable block of code…
User: Show example
Tutor:
def greet(name):
    print("Hello", name)
User: Why use functions?
Tutor: To reuse logic & organize code…
User: Explain with analogy
Tutor: Like a lunchbox… pack once and reuse!
```

### Shakespearean Persona — 3 Snippets
```
User: I feel tired
Bot: Mine spirit droops with weary sorrow…

User: Translate “You're amazing”
Bot: Thou art a marvel most divine…
```

### Socratic Teacher
```
User: What is AI?
Bot: What do *you* believe intelligence means?
```

### ELI5 Explainer
```
User: Explain blockchain
Bot: Imagine a notebook everyone shares…
```

### Technical Writer
```
- Communication interface
- Defined request/response contract
- Example: REST using JSON
```

---

## 🆚 Persona Comparison Example
**Prompt:** "Explain recursion"

| Persona | Response Style |
|---|---|
| Python Tutor | “Recursion is when a function calls itself…” |
| Socratic | “What happens if a function repeats itself forever?” |
| ELI5 | “Two mirrors facing each other — reflections forever!” |

---

## 🧠 State Management

- Each persona has its own message list
- System prompt always index `0`
- Switching does **not** erase memory
- Reset wipes only persona’s history

---

## ⚙️ Challenges & Solutions

| Challenge | Fix |
|---|---|
Personas sounded similar | Strengthened prompt rules |
Memory bleed | Dedicated storage per persona |
Streaming issues | Token streaming loop |
Comparing personas | Parallel calls + labels |

---

## ✅ Conclusion  
This project shows the impact of **prompt engineering + memory control**, enabling intelligent AI “characters” with consistent:

- Tone  
- Logic  
- Behavior  
- Memory  

It demonstrates how to build **real multi-persona systems**, useful for tutoring apps, language companions, role-play chatbots, and educational platforms.