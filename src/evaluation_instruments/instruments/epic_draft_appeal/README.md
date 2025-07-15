# Automated Evaluation of Medical Necessity Justifications for Clinical Denial Appeals

This repository provides a Python script and rubric for evaluating large language model (LLM)-generated medical necessity justifications written for clinical denial appeals. These bases for appeal may reference clinical notes as well as discrete data elements such as labs & imaging results, medication administrations, and vital sign measurements. It enables automated, consistent, and transparent scoring of medical necessity justifications.

This work supports scalable evaluation of generative AI tools integrated into payer-provider communication workflows and contributes to building trustworthy and rigorous AI for healthcare systems.

---

## Features

- Uses LLM-as-a-Judge prompts to assign structured scores on a 1-5 scale with explanations
- Handles multiple inputs from several sources of clinical data
- JSON-based input and output

---

## How It Works

The script constructs a system prompt and user prompt using the provided clinical data and basis for appeal, then evaluates the basis for appeal against the full rubric. Outputs are returned in JSON with free-text justifications and scores for each attribute.

### Expected Inputs

- denied procedures: List[str] - a list of procedures, medications, or other charges that were denied on the basis of medical necessity. The basis for appeal is expected to justify the medical necessity for each element in this list.
- medications: dict[str, str] - a dictionary with medication information (including dosage and administration history) as string values. Keys are used as identifiers in summary citations.
- orders: dict[str, str] - a dictionary with lab & imaging order information (including results) as string values. Keys are used as identifiers in summary citations.
- diagnoses: dict[str, str] - a dictionary with coded diagnoses as string values. Keys are used as identifiers in summary citations.
- problem list: dict[str, str] - a dictionary with hospital problems as string values. Keys are used as identifiers in summary citations.
- notes: dict[str, str] - a dictionary with clinical notes as string values. Keys are used as identifiers in summary citations.
- authorizations: dict[str, str] - a dictionary with authorization information as string values. Keys are used as identifiers in summary citations.
- basis: str - the basis of appeal being evaluated. Citations are expected to be in ```[X0]``` format and correspond to items in the source data.

### Evaluation Attributes

- Text Quality
- Medical Terminology
- Grammar
- Text Format
- Tone
- References
- Relevant References
- Medical Necessity
- False Reasoning
- Opposition
- Factual Accuracy
