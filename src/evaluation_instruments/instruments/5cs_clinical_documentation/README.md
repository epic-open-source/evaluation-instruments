## Clinical Note Quality with AI-Powered Evaluation at NYU Langone Health
NYU Langone Health, a prominent academic healthcare system, has tackled the critical issue of poor clinical note quality—a widespread concern since the Health Information Technology for Economic and Clinical Health Act. Recognizing that US notes are four times longer than those in other countries and often lead to unclear diagnoses and delayed treatments, NYU Langone spearheaded an initiative to improve documentation, aligning with its data-driven culture.

**The Challenge: Measuring Quality in Medical Documentation**
Despite a strong emphasis on performance and accountability, NYU Langone faced the challenge of applying metric-driven quality improvement strategies to medical documentation, a domain not easily amenable to quantitative measurement. The COVID-19 pandemic further underscored the need for clear communication in provider notes, especially after internal data placed NYU Langone in the bottom quartile for note length, indicating unnecessarily bloated documentation.

**Creating an Enterprise-Wide Structure for Note Quality Measurement**
To address this, NYU Langone established an Enterprise-Wide Documentation Standards Committee in September 2020. Comprising clinical, operational, quality, and informatics leaders, the committee set out to enhance clinical documentation.

Key initiatives included:

- The 5Cs Assessment Tool: The committee developed a valid, practical, and scalable method to measure note quality, known as the "5Cs" assessment tool: Completeness, Conciseness, Contingency (Discharge) Planning, Correctness, and Clinical Assessment and Reasoning.

- AI Model Development: Recognizing the time-consuming nature of manual note grading (unit directors could grade only about five notes per month), NYU Langone collaborated with its MCIT Department of Health Informatics to develop AI models capable of grading thousands of provider notes. This was crucial for robust quality reporting, identifying providers needing feedback, evaluating interventions, and assessing individual performance.

- Piloting AI Note Quality Measurement: Physician leaders used the 5Cs rubric to label a training set of Internal Medicine progress notes. Multiple AI models were developed and trained for each of the 5Cs components, with a validation set used to select the best-performing models. These models were then piloted across all inpatient Internal Medicine progress notes within the health system. Unit directors were trained on an interactive dashboard visualizing AI-generated note grades over time.

**Leveraging GPT-4 for Scalable Note Quality Evaluation and Feedback**
NYU Langone further explored the potential of large language models (LLMs), specifically GPT-4, to enhance their note quality initiatives.

- GPT-4 for 5Cs Classification: NYU Langone teams tested GPT-4 for classifying the 5Cs, aiming for a generalizable note quality evaluation without retraining for each specialty. Through extensive "prompt engineering," a single GPT-4 prompt was developed that exhibited performance comparable to NYU Langone's in-house, specialty-specific models across numerous specialties.

- Scaling Narrative Feedback with GPT-4: A significant advantage of AI implementation is its ability to identify low-performing notes and providers. Historically, resource limitations hindered detailed feedback. LLMs like GPT-4 offer a promising solution by generating AI-powered, note-specific narrative feedback. Using iterative prompt engineering and "few-shot learning," NYU Langone optimized GPT-4's response generation.

**Current Implementation:**

GPT-4 Turbo is now used in production with validated results. Five separate prompts (one for each of the 5Cs categories) are employed to grade notes across all services within the institution. To enhance accuracy, each prompt utilizes few-shot prompting with two examples: one positive and one negative. These examples are provided in rich text format (RTF), which does not preserve the original formatting of the clinical note as it appears in the EHR. This means the RTF may contain symbols like "?" and "|" which may differ from the original symbols used in the clinical note. Each example includes a chain-of-thought explanation, detailing the reasoning behind the classification to guide the LLM's understanding.

**Impact**
This innovative approach allows NYU Langone Health to apply metric-driven quality improvement strategies to medical documentation at scale, leading to more accurate, accessible, and effective clinical notes. This, in turn, positively influences patient care, staff well-being, and clinical documentation integrity, ultimately enhancing the entire care delivery experience.

---

## How It Works

The script constructs a system prompt and user prompt using the provided clinical notes, then evaluates each note against the full 5Cs rubric. Outputs are returned in JSON with classifications (1 (present) or 0 (absent)) for each of the 5C categories for each note. 

---

## Expected Inputs
notes: pandas.DataFrame - a DataFrame where each row represents a clinical note, with columns for note text and its corresponding note ID.

---

## Recommended Large Language Models
gpt-4-turbo-2024-04-09 was utilized and validated as the production model. You may use other models, but gpt-4-turbo-2024-04-09 was used for our purposes.

---

## Citation
```
@article{feldman2024scaling,
  title={Scaling note quality assessment across an academic medical center with AI and GPT-4},
  author={Feldman, Jonah and Hochman, Katherine A and Guzman, Benedict Vincent and Goodman, Adam and Weisstuch, Joseph and Testa, Paul},
  journal={NEJM Catalyst Innovations in Care Delivery},
  volume={5},
  number={5},
  pages={CAT--23},
  year={2024},
  publisher={Massachusetts Medical Society}
}
```