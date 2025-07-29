## Clinical Note Quality with AI-Powered Evaluation at NYU Langone Health
NYU Langone Health has implemented an AI-powered system to evaluate and improve the quality of clinical notes. This initiative addresses the long-standing issue of poor and overly long documentation that can lead to delayed treatments and unclear diagnoses. By leveraging artificial intelligence, NYU Langone has transformed clinical note quality from a subjective, difficult-to-measure domain into a data-driven process.


**How the AI Grading Systems Works**

NYU Langone's approach began with the development of the "5Cs" assessment tool: a practical rubric measuring note Completeness, Concisness, Contingency (Discharge) Planning, Correctness, and Clinical Assessment and Reasoning.

To scale this evaluation process, NYU Langone collaborated with its MCIT Department of Health Informatics. The institution initially built its own models, but later successfully leveraged large language models (LLMs) to make the system more scalable across different specialties.

Here's a closer look at the key components of this process:

- **Data Extraction and Processing:** The system evaluates clinical progress notes extracted directly from NYU Langone's database. These notes are formatted into rich text format (RTF) before being sent to the LLM. It is crucial to understand that this extraction process does not preserve the original formatting from the Electronic Health Record (EHR). As a result, changes to spacing, symbols, and formatting—such as question marks (?) or vertical bars (|)—are common. This process was developed and validated exclusively using progress notes and has not been tested on other types of clinical notes, such as discharge summaries or consultation notes.

- **Prompt Engineering:** NYU Langone's teams used extensive prompt engineering to create five distinct prompts, one for each of the 5Cs. To achieve a high degree of accuracy and generalizability, each prompt utilizes few-shot learning by including two examples: one positive and one negative. These examples, provided with a chain-of-thought explanation, teach the LLM the desired classification pattern and reasoning.

- **Classification and Output:** The system evaluates each note against the full 5Cs rubric. The output for each category is a binary classification: 1 if the quality standard is met ("yes") and 0 if it is not met ("no"). This structured data is then returned in JSON format, allowing for robust quality reporting and analysis.

- **AI-Powered Evaluation:** A significant advantage of this system is its ability to identify low-scoring notes and providers, and then generate specific, classifications per 5C category. This detailed, AI-powered evaluation is something that was previously difficult to provide due to resource limitations.

- **Model and Compliance:** The institution validated and utilized a HIPAA-compliant private instance of GPT-4 Turbo (gpt-4-turbo-2024-04-09) for its production model. It is important to note that as of June 2025, GPT-4 Turbo (gpt-4-turbo-2024-04-09) has been deprecated by OpenAI. Due to this deprecation, the institution is actively validating other large language models to ensure the continued performance and functionality of its note quality evaluation system.

---

**Expected Input and Outputs**

The system takes a pandas DataFrame as input, where each row represents a clinical note with the note text and its corresponding ID. It then constructs system and user prompts to evaluate each note against the 5Cs rubric, returning the classifications in a JSON output.

---

**Important Considerations for Other Institutions**

While this AI-powered approach has proven highly effective for NYU Langone Health, it's important to note that performance may vary for other institutions. The system's prompts were specifically fine-tuned and validated using NYU Langone’s data and its HIPAA-compliant private instance of GPT-4 Turbo (gpt-4-turbo-2024-04-09). The same prompts may be used with other models or different note types, but human validation is warranted, and further fine-tuning of the prompts may be required to achieve effective and accurate classifications. This is crucial to ensure that the system's performance translates reliably to different environments and use cases.

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
