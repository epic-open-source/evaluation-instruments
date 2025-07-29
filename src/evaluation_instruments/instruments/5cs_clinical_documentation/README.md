## Clinical Note Quality with AI-Powered Evaluation at NYU Langone Health
NYU Langone Health has implemented a groundbreaking AI-powered system to evaluate and improve the quality of clinical notes. This initiative addresses the long-standing issue of poor and overly long documentation that can lead to delayed treatments and unclear diagnoses. By leveraging artificial intelligence, NYU Langone has transformed clinical note quality from a subjective, difficult-to-measure domain into a data-driven process.


**How the AI Grading Systems Works**

NYU Langone’s approach began with the development of the "5Cs" assessment tool: a practical rubric measuring note Completeness, Concisness, Contingency (Discharge) Planning, Correctness, and Clinical Assessment and Reasoning.

To scale this evaluation process, NYU Langone collaborated with its MCIT Department of Health Informatics to develop and train AI models capable of grading thousands of notes. The institution initially built its own models, but later successfully leveraged large language models (LLMs) like GPT-4 Turbo to make the system more scalable across different specialties.

Here's a closer look at the key components of this process:

- Prompt Engineering: NYU Langone's teams used extensive prompt engineering to create five distinct prompts, one for each of the 5Cs. These prompts, which include two examples (i.e. few-shot learning by providing one positive and one negative examples) and a chain-of-thought explanation, guide the LLM to classify each note.

- AI-Powered Feedback: A significant advantage of this system is its ability to generate specific, narrative feedback for low-scoring notes. This detailed, AI-powered feedback is something that was previously difficult to provide due to resource limitations.

- Validated Model: The institution used gpt-4-turbo-2024-04-09 as its production model. This model, which was fine-tuned using data from NYU Langone Health, is now used in production to grade notes across all services.

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
