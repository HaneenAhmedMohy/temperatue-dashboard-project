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
