## Clinical Note Quality with AI-Powered Evaluation at NYU Langone Health
NYU Langone Health has implemented a groundbreaking AI-powered system to evaluate and improve the quality of clinical notes. This initiative addresses the long-standing issue of poor and overly long documentation that can lead to delayed treatments and unclear diagnoses. By leveraging artificial intelligence, NYU Langone has transformed clinical note quality from a subjective, difficult-to-measure domain into a data-driven process.


**How the AI Grading Systems Works**

NYU Langone Health has implemented a groundbreaking AI-powered system to evaluate and improve the quality of clinical notes. This initiative addresses the long-standing issue of poor and overly long documentation that can lead to delayed treatments and unclear diagnoses. By leveraging artificial intelligence, NYU Langone has transformed clinical note quality from a subjective, difficult-to-measure domain into a data-driven process.

How the AI System Works
NYU Langone's approach began with the development of the "5Cs" assessment tool: a practical rubric measuring note Completeness, Concisness, Contingency (Discharge) Planning, Correctness, and Clinical Assessment and Reasoning.

To scale this evaluation process, NYU Langone collaborated with its MCIT Department of Health Informatics. The institution initially built its own models, but later successfully leveraged large language models (LLMs) to make the system more scalable across different specialties. The system uses a specific technique known as few-shot learning, which enables the model to adapt to new tasks with minimal examples, without the need for extensive retraining.

Here's a closer look at the key components of this process:

- Prompt Engineering and Few-Shot Learning: NYU Langone's teams used extensive prompt engineering to create five distinct prompts, one for each of the 5Cs. To achieve a high degree of accuracy and generalizability, each prompt utilizes few-shot learning by including two examples: one positive and one negative. These examples, provided in rich text format (RTF) along with a chain-of-thought explanation, teach the LLM the desired classification pattern and reasoning.

- Classification and Output: The system evaluates each note against the full 5Cs rubric. The output for each category is a binary classification: 1 if the quality standard is met ("yes") and 0 if it is not met ("no"). This structured data is then returned in JSON format, allowing for robust quality reporting and analysis.

- AI-Powered Feedback: A significant advantage of this system is its ability to identify low-scoring notes and providers, and then generate specific, narrative feedback. This detailed, AI-powered feedback is something that was previously difficult to provide due to resource limitations.

- Model and Compliance: The institution validated and utilized GPT-4 Turbo for its production model. It's crucial to note that as of July 2025, GPT-4 Turbo has been deprecated by OpenAI. However, the system's underlying technology relies on a private instance of GPT, which has been configured to be HIPAA compliant. This ensures that patient data is handled securely and in accordance with privacy regulations, a fundamental requirement for any healthcare application.

The system takes a pandas DataFrame as input, where each row represents a clinical note with the note text and its corresponding ID. It then constructs system and user prompts to evaluate each note against the 5Cs rubric, returning the classifications in a JSON output.

---

**Important Considerations for Other Institutions**

While this AI-powered approach has proven highly effective for NYU Langone Health, it's important to note that performance may vary for other institutions. The system's prompts were specifically fine-tuned using NYU Langone’s data and were validated using GPT-4 Turbo. Therefore, any institution looking to implement a similar system should be aware that human validation is warranted and some fine-tuning may be required to achieve similar levels of accuracy and effectiveness.

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
