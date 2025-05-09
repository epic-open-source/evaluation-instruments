# Automated Evaluation of Comprehensive EHR Summary of Care

This repository provides a Python script and rubric for evaluating large language model (LLM)-generated summaries of electronic health record (EHR) data for inpatient stays. In addition to clinical notes, these summaries may reference discrete data elements such as labs & imaging results, medication administrations, and vital sign measurements. It enables automated, consistent, and transparent scoring of clinical summarization quality for post-discharge workflows such as coding and denial appeals.

This work supports scalable evaluation of generative AI tools integrated into administrative and revenue-cycle focused workflows and contributes to building trustworthy and rigorous AI for healthcare systems.

---

## Features

- Uses LLM-as-a-Judge prompts to assign structured scores on a 1-5 scale with explanations
- Handles multiple inputs from several sources of clinical data
- JSON-based input and output

---

## How It Works

The script constructs a system prompt and user prompt using the provided clinical data and summary, then evaluates the summary against the full rubric. Outputs are returned in JSON with free-text justifications and scores for each attribute.

### Expected Inputs

- medications: dict[str, str] - a dictionary with medication information (including dosage and administration history) as string values. Keys are used as identifiers in summary citations.
- orders: dict[str, str] - a dictionary with lab & imaging order information (including results) as string values. Keys are used as identifiers in summary citations.
- diagnoses: dict[str, str] - a dictionary with coded diagnoses as string values. Keys are used as identifiers in summary citations.
- problem list: dict[str, str] - a dictionary with hospital problems as string values. Keys are used as identifiers in summary citations.
- notes: dict[str, str] - a dictionary with clinical notes as string values. Keys are used as identifiers in summary citations.
- movements: dict[str, str] - a dictionary with patient movement events (admission, discharge, transfers) as string values. Keys are used as identifiers in summary citations.
- vitals: dict[str, str] - a dictionary with recorded vital sign measurements as string values. Keys are used as identifiers in summary citations.
- authorizations: dict[str, str] - a dictionary with authorization information as string values. Keys are used as identifiers in summary citations.
- summary: str - the summary being evaluated. Citations are expected to be in ```[X0]``` format and correspond to items in the source data

### Evaluation Attributes

- Tone
- Grammar
- Conciseness
- Formatting
- Relevancy
- Extrapolation
- Key Events
- Medical Terminology
- Understanding
- Text Quality
