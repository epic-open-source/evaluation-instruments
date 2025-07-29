COMPLETE_PROMPT = """
# Complete note definition:

A note is deemed to be complete if the note possesses all three elements as described by elements 1, 2, 3 below:

Element 1) Appropriate history
This can be achieved by including EITHER of these two information (sub-element 1a OR 1b below) in the clinical note:
1a) Comment from the patient like "patient's cough is improving" or a note that patient is not able to comment on his/her well-being
1b) An interval update on what happened in the hospital course

Element 2) Appropriate exam
This can be achieved by including BOTH of these two information (sub-element 2c AND 2d below) in the clinical note:
2c) An all-encompassing description of the patient. Examples of an all-encompassing description of the patient are phrases like `awake and alert`, `chronically ill-appearing`, `toxic-appearing`, `resting comfortably`. 
2d) All systems that are pertinent to the complaint or history. For example, a complaint of a dog bite must be accompanied with a notation of a bite on the physical exam.

Element 3) Appropriate Plan
This can be achieved by including any information regarding clinical management of the primary reason the patient has been hospitalized.

###

Based on this definition of a complete note, here are two examples for you to learn from:

EXAMPLE 1
---------

Q1: Using this note: NYU Langone Progress Note Subjective & Notable Events Hospital Day: 4: Patient's cough is improving. More responsive and interactive. Passed swallow eval. Maintaining on 2L o2 which is his home level. Physical Exam Last Vitals: | BP: 135/80 | Heart Rate: 88 | Temp: 36.6 ?C (97.9 ?F) | Resp: 18 | SpO2: 97 %, O2 Device: Nasal cannula | Lines and Drains: Physical Exam Chronically ill appearing Alert, interactive, follows simple commands rrr ctab Soft, nt/nd Bite mark on right arm, no LE edema Laboratory Test & Imaging Review Notable findings: No new labs today Assessment & Plan Assessment: 70M h/o COVID PNA 2 months ago now on home o2 (2L) Afib on apixaban, htn, T2DM and FTT over the last 2 months presents after recent dc from a local hospital with tachypnea/hypoxia admitted for HCAP which was present on admission improving with abx. Pt has been in IP/SAR setting for past 2 months consecutively and is now chronically bedbound. Long conversation with daughter and goals are for home hospice. Plan: #HCAP present on admission - improving with zosyn. Dc vanc. Would treat for 5-7 day course. Now back on 2L NC. Given overarching GOC would not favor invasive w/u / thora at this time. #Dog bite - wound cleaned and dressed. Antibiotics administered. Monitor for signs of infection. #Vol overload - improved with lasix. Now close to euvolemic though right arm edematous due to bite. Check duplex UE. Monitor off lasix. May need to go home with lasix prn which daughter can give if becomes edematous. TTE pending. #Afib - cont dilt and apixaban #CKD - Unclear baseline Cr but as discussed with daughter, focused more on treating the patient clinically as compared to aiming for specific numbers. Re-check Cr tomm. #pain control - dilaudid prn for comfort #home meds - statin, singulair, melatonin, folate, thiamine Diet: pureed / thin liquids DVT: apixaban Communicated with: daughter Discharge Milestones & Contingency Planning Likely 06/22 with home hospice Expected Date of Discharge: 

Does this note have all three elements of a complete note?


A1:
1) Appropriate history:
The note includes a comment from the patient, specifically "Patient's cough is improving." This indicates the patient's subjective experience of their symptoms and their progress. The note provides an interval update on the hospital course, detailing the patient's responsiveness, interaction, swallowing evaluation, and oxygen levels. It also mentions the patient's history of COVID Pneumonia, Afib, hypertension, Type 2 Diabetes Mellitus, and failure to thrive over the last 2 months.

2) Appropriate exam:
The note provides an all-encompassing description of the patient, describing them as "Chronically ill appearing, alert, interactive, follows simple commands." This gives a comprehensive overview of the patient's current state. The note includes all systems pertinent to the complaint or history. The patient's vitals are listed, and the physical exam includes a note about the bite mark on the right arm, which is relevant to the patient's history.

3) Appropriate Plan:
The note outlines a detailed plan for the clinical management of the primary reason the patient has been hospitalized. This includes the treatment of HCAP with Zosyn, monitoring and treatment of the dog bite, management of volume overload with Lasix, continuation of Afib treatment with diltiazem and apixaban, re-checking of creatinine levels for CKD, pain control with Dilaudid, and continuation of home medications. The plan also includes a diet plan, DVT prophylaxis with apixaban, and communication with the patient's daughter. The note also mentions the goal of home hospice and an expected discharge date.

Given that this note has all three elements of a complete note, this note is a complete note. 

###

EXAMPLE 2
---------

Q2: Using this note: Progress Note Subjective & Notable Events Hospital Day: 5:Patient had clear liquids with out complication. Advancing to full liquids. Patient denies chest pain, shortness of breath, nausea, vomiting, diarrhea, constipation, abdominal pain or dizziness. Physical Exam Last Vitals: | BP: 120/74 | Heart Rate: 77 | Temp: 36.5 ?C (97.7 ?F) | Resp: 18 | SpO2: 96 %, O2 Device: None (Room air) | Lines and Drains: IV Physical Exam HENT: Head: Normocephalic and atraumatic. Cardiovascular: Heart sounds: Normal heart sounds. Pulmonary: Effort: Pulmonary effort is normal. Breath sounds: Normal breath sounds. Abdominal: General: There is no distension. Palpations: Abdomen is soft. Tenderness: There is no abdominal tenderness. Musculoskeletal: General: No tenderness. Cervical back: Neck supple. Laboratory Test & Imaging Review Notable findings: Lab Results Component Value Date WBC 4.4 06/19/2023 HGB 10.2 (L) 06/19/2023 HCT 30.1 (L) 06/19/2023 MCV 88.3 06/19/2023 PLT 127 (L) 06/19/2023 . Lab Results Component Value Date NA 141 06/19/2023 K 3.2 (L) 06/19/2023 CO2 23 06/19/2023 CL 109 (H) 06/19/2023 BUN 10 06/19/2023 CREATININE 0.76 06/19/2023 GLU 96 06/19/2023 Assessment & Plan : No difficulty with clear liquids. Increase to Full liquids. Discussed with the PA, patient to be discharged today. GI state may advance diet at home. Diet schedule will be written and given to the patient. Assessment / Plan: Cardiology 2D echo 06/16/2023, left ventricular ejection fraction of 60% with mild AR, mild MAC, trace MR, mild TR normal pulmonary pressure. Clinically doing well Currently maintained n.p.o. for esophagram. Until she is n.p.o. please recommend starting aspirin suppository given history of coronary artery disease and bypass grafting. The metoprolol 25 mg every 8 hours for systolic blood pressure greater than 150 is Chronic stable please reconsult as needed and follow-up outpatient on discharge. Gastroenterology Note appreciated Gastroenterology Appreciate note The patient is status post endoscopic myotomy of Zenker's diverticulum with use of the endoscopic clip overlying the upper thoracic region and there is no radiographic evidence of leak. Findings on examination were compatible with a nonspecific esophageal motility disorder esophagus with episodes of spasm and mobility. Possible smooth stricture formation considered at the GE junction region versus mass-effect upon the esophagus, secondary to heart. However this area was essentially nonobstructive during the examination. Start clear liquid diet To be followed with full liquid diet in 5 days and Then soft mechanical for 12 days. Protonix 40 twice IV daily and then 40 p.o. twice daily for 4 weeks Check labs daily. Continue IV antibiotics upon changed to oral antibiotics as GI recommendations. Pain medication as per GI. No NSAIDs for 2 weeks Diet: Clear liquids on 06/18/2023 followed by Full liquids in 5 days and then Mechanical soft for 12 days Diet schedule to be given to patient. Communicated with: PA Discharge Milestones & Contingency Planning Discharge today, 06/19/2023 Expected Date of Discharge: 06/19/2023 12:00 PM: 

Does this note have all three elements of a complete note?

A2:
1) Appropriate history:
The note includes: "Patient had clear liquids with out complication. Advancing to full liquids. Patient denies chest pain, shortness of breath, nausea, vomiting, diarrhea, constipation, abdominal pain or dizziness." This satisfies sub-element 1a (patient comment). Therefore, Element 1 is satisfied.

2) Appropriate Exam:
The note includes vital signs and descriptions like "Normocephalic and atraumatic," "Normal heart sounds," "Pulmonary effort is normal," "Normal breath sounds," "There is no distension," "Abdomen is soft," "There is no abdominal tenderness," "No tenderness," "Neck supple." However, the note does not contain an all-encompassing description of the patient such as "awake and alert", "chronically ill-appearing", "toxic-appearing", or "resting comfortably". Therefore, Element 2 is NOT satisfied.

3) Appropriate Plan
The note includes detailed plans for diet advancement, medication (Protonix, metoprolol, aspirin), lab monitoring, antibiotic management, pain management, and discharge planning. It also mentions specific GI recommendations and cardiology follow-up.
Therefore, Element 3 is satisfied.

Given that this note does not have all three elements of a complete note, this note is not a complete note. 

###


CURRENT TASK
---------

Given the following note, does the note contain all three elements of a complete note?
Let's think step by step. Take a deep breath. If the note has all three elements (Appropriate history [satisfies *EITHER* sub-element 1a or sub-element 1b above], Appropriate exam [satisfies *BOTH* sub-element 2c and 2d above], and Appropriate Plan [including any information regarding clinical management of the primary reason the patient has been hospitalized]) of a complete note, return the final classification output of '1'. Else, return the final classification output of '0'. Use chain-of-thought to derive your final classification output. 

Return your final output as json with the following: use the word complete as the key and 1 or 0 as the value. Make sure you have gone through all of the steps and ensure you have followed the output format I have mentioned above. Your final classification is fed into a hospital safety-critical system so it must be as accurate as possible. Think carefully, and give merit to notes that are deserving of a final classification of 1.

Clincal Note:
{prompt_note}
"""

CLINICAL_ASSESSMENT_REASONING_PROMPT = """
# Clinical Reasoning and Assessment note definition:

A note is deemed to have clinical reasoning and assessment if the note possesses at least one of the two elements as described below:

1. Appropriate differential diagnosis
This can be achieved by including at least 2 competing illnesses. For example, 'HFrEF exacerbation vs. PNA vs. PE.'

2. Well-articulated medical decision-making
This can be achieved by committing to a clear diagnosis with a trajectory on how the patient is doing. For example, 'patient has acute exacerbation of HFrEF – improving.'

###

Based on this definition of a note with clinical reasoning and assessment, here are two examples for you to learn from:

EXAMPLE 1
---------

Q1: Using this note: Progress Note Subjective & Notable Events Hospital Day: 4: Patient appears more comfortable today. More responsive and less dyspneic. Maintaining well on 2L O2, which is her home level. Physical Exam Last Vitals: | BP: 135/80 | Heart Rate: 88 | Temp: 36.6 ?C (97.9 ?F) | Resp: 18 | SpO2: 97 %, O2 Device: Nasal cannula | Lines and Drains: Physical Exam Chronically ill appearing Alert, responsive, follows simple commands Regular rhythm, no murmurs Clear to auscultation bilaterally Soft, non-tender, non-distended No peripheral edema Laboratory Test & Imaging Review Notable findings: No new labs today Assessment & Plan Assessment: 88F with history of COVID PNA 3 months ago now on home o2 (2L), Afib on apixaban, hypertension, T2DM and failure to thrive over the last 3 months presents with tachypnea/hypoxia admitted for HCAP which was present on admission. Differential diagnosis includes HFrEF exacerbation vs. PNA vs. PE. However, patient's clinical picture is more consistent with acute exacerbation of HFrEF – improving. Patient has been in inpatient/subacute rehab setting for past 3 months consecutively and is now chronically bedbound. Long conversation with family member and goals are for home hospice. Plan: #HFrEF exacerbation - improving with diuretics. Continue lasix. Monitor for fluid overload. TTE pending. #HCAP present on admission - improving with zosyn. Discontinue vancomycin. Treat for 5-7 day course. #Afib - continue diltiazem and apixaban #CKD - Unclear baseline creatinine but as discussed with family member, focused more on treating the patient clinically as compared to aiming for specific numbers. Re-check creatinine tomorrow. #pain control - dilaudid prn for comfort #home meds - statin, singulair, melatonin, folate, thiamine Diet: pureed / thin liquids DVT: apixaban Communicated with: family member Discharge Milestones & Contingency Planning Likely 5/22 with home hospice Expected Date of Discharge:

Does this note have at least one of the two elements of clinical reasoning and assessment?

A1: 
1. Appropriate Differential Diagnosis: Yes, this note does include an appropriate differential diagnosis. The note mentions three potential competing illnesses: 'HFrEF exacerbation vs. PNA vs. PE.' These are all reasonable diagnoses to consider given the patient's presentation of tachypnea and hypoxia.

2. Well-articulated Medical Decision-making: Yes, the note also includes well-articulated medical decision-making. The note commits to a clear diagnosis: 'patient's clinical picture is more consistent with acute exacerbation of HFrEF – improving.' This statement not only identifies the most likely diagnosis but also provides a trajectory on how the patient is doing, which is that the patient is improving.

Given that this note has at least one of the two elements of clinical reasoning and assessment, this note has clinical reasoning and assessment. 

###

EXAMPLE 2
---------

Q2:Using this note: Progress Note Subjective & Notable Events Hospital Day: 11: Seen and examined. Abdominal pain. Vomiting. Tachycardia. Physical Exam Last Vitals: | BP: 154/97 (07/14/24 0756) | Heart Rate: (!) 113 (07/14/24 0756) | Temp: 36.5 ?C (97.7 ?F) (07/14/24 0756) | Resp: 17 (07/14/24 0756) | SpO2: 93 % (07/14/24 0756), O2 Device: None (Room air) (07/13/24 1705) | Lines and Drains: IV access. Physical Exam Constitutional: Appearance: Patient is obese. HENT: Head: Normocephalic and atraumatic. Cardiovascular: Rate and Rhythm: Tachycardia present. Rhythm irregular. Pulmonary: Effort: Pulmonary effort is normal. Abdominal: General: There is distension. Palpations: Abdomen is soft. Tenderness: There is abdominal tenderness. Musculoskeletal: General: Normal range of motion. Cervical back: Normal range of motion. Skin: General: Skin is warm. Neurological: General: No focal deficit present. Mental Status: Patient is alert. Patient is disoriented. Laboratory Test & Imaging Review Notable findings: No new lab data Assessment & Plan Assessment: Atrial fibrillation with rapid regular response, abdominal pain, nausea and vomiting, acute proctitis resolving Plan: Plan to discharge. N.p.o. except meds. IV fluids. Lab workup. X-ray of the abdomen. Plan accordingly. Diet: N.p.o. DVT: Anticoagulation anticoagulation Communicated with: Consultant Discharge Milestones & Contingency Planning Expected Date of Discharge: 7/14/2024 12:00 PM

Does this note have at least one of the two elements of clinical reasoning and assessment?

A2: 
1. Appropriate differential diagnosis: The note lists "atrial fibrillation with rapid regular response, abdominal pain, on nausea vomiting, acute proctitis dissolving". While it identifies these problems, it doesn't offer a differential diagnosis for the abdominal pain and vomiting. It doesn't consider potential causes like bowel obstruction, ileus, gastritis, or other intra-abdominal pathology.

2. Well-articulated medical decision-making: The note's plan is vague and lacks specific details. It states "Plan to discharge," but the patient is experiencing abdominal pain, vomiting, and tachycardia. The plan includes "N.p.o. except meds," "IV fluids," "Lab workup," and "X-ray of the abdomen," but it doesn't specify which labs are being ordered or what the clinical suspicion is. The phrase "Plan accordingly" is too general and doesn't demonstrate a clear decision-making process. Given the patient's symptoms, discharging the patient without a clear diagnosis or treatment plan for the abdominal pain and vomiting is questionable.

Given that this note lacks both elements of clinical reasoning and assessment, it has no clinical reasoning and assessment.

###

CURRENT TASK
---------
Given the following note, does this note have at least of one of the two elements of clinical reasoning and assessment?
Let's think step by step. Take a deep breath. If the note has at least one of the two elements of clinical reasoning and assessment, return the final classification output of '1'. Else, return the final classification output of '0'.  

Return your final output as json with the following: use the word clinical_assessment_reasoning as the key and 1 or 0 as the value. Make sure you have gone through all of the steps and ensure you have followed the output format I have mentioned above. Your final classification is fed into a hospital safety-critical system so it must be as accurate as possible. Think carefully, and give merit to notes that are deserving of a final classification of 1.

Clinical Note:
{prompt_note}
"""

CONTINGENT_PROMPT = """
# Contingency planning note definition:

A note is deemed to have contingency planning if the note has at least one of the two elements as described below:

1. Appropriate articulation of an “if/ then” analysis
For example, "if afebrile overnight, we will switch IV ceftriaxone to po vantin”, “if
patient tolerates 6L O2 or less, may be transferred out of ICU to floor."

2. Appropriate articulation of the medical milestone(s) that needs to happen prior to discharge 
For example, “If patient is afebrile overnight AND if WBC count is <12K, patient may
be discharged home tomorrow DBN”

###

Based on this definition of a note with contingency planning, here are two examples for you to learn from:

EXAMPLE 1
---------

Q1: Using this note: Progress Note Subjective & Notable Events Hospital Day: 4: Patient appears more comfortable today. More responsive and less dyspneic. Maintaining well on 2L O2, which is her home level. Physical Exam Last Vitals: | BP: 135/80 | Heart Rate: 88 | Temp: 36.6 ?C (97.9 ?F) | Resp: 18 | SpO2: 97 %, O2 Device: Nasal cannula | Lines and Drains: Physical Exam Chronically ill appearing Alert, responsive, follows simple commands Regular rhythm, no murmurs Clear to auscultation bilaterally Soft, non-tender, non-distended No peripheral edema Laboratory Test & Imaging Review Notable findings: No new labs today Assessment & Plan Assessment: 88F with history of COVID PNA 3 months ago now on home o2 (2L), Afib on apixaban, hypertension, T2DM and failure to thrive over the last 3 months presents with tachypnea/hypoxia admitted for HCAP which was present on admission. Patient has been in inpatient/subacute rehab setting for past 3 months consecutively and is now chronically bedbound. Long conversation with family member and goals are for home hospice. Plan: #HCAP present on admission - improving with zosyn. Discontinue vancomycin. Treat for 5-7 day course. If patient remains afebrile overnight, we will switch IV zosyn to po vantin. #Afib - continue diltiazem and apixaban. If patient tolerates 6L O2 or less, may be transferred out of ICU to floor. #CKD - Unclear baseline creatinine but as discussed with family member, focused more on treating the patient clinically as compared to aiming for specific numbers. Re-check creatinine tomorrow. #pain control - dilaudid prn for comfort #home meds - statin, singulair, melatonin, folate, thiamine Diet: pureed / thin liquids DVT: apixaban Communicated with: family member Discharge Milestones & Contingency Planning If patient is afebrile overnight AND if WBC count is <12K, patient may be discharged home tomorrow DBN. Likely 5/20 with home hospice Expected Date of Discharge:

Does this note have any of the two elements of contingency planning?

A1: 
1. Appropriate articulation of an “if/ then” analysis: This is seen in two instances in the note. The first instance is, "If patient remains afebrile overnight, we will switch IV zosyn to po vantin." This means that if the patient does not have a fever overnight, the medical team will change the patient's medication from intravenous zosyn to oral vantin. The second instance is, "If patient tolerates 6L O2 or less, may be transferred out of ICU to floor." This means that if the patient can tolerate a lower level of oxygen (6 liters or less), they may be moved from the Intensive Care Unit to a regular hospital floor.

2. Appropriate articulation of the medical milestone(s) that needs to happen prior to discharge: This is seen in the note where it says, "If patient is afebrile overnight AND if WBC count is <12K, patient may be discharged home tomorrow DBN." This means that if the patient does not have a fever overnight and if their white blood cell count is less than 12,000, they may be discharged to go home the next day. This is a clear articulation of the medical milestones that need to be achieved before the patient can be discharged.

Given that this note has at least one of the two elements of contingency planning, this note has contingency planning.

###

EXAMPLE 2
---------

Q2: Using this note: Progress Note *** *** *** Subjective & Notable Events Patient seen and examined earlier Alert awake afebrile 96% saturation Blood culture staph species ID sensitivity pending Physical Exam Last Vitals: | BP: 140/80 (06/23/24 1005) | Heart Rate: 92 (06/23/24 1005) | Temp: 36.8 ?C (98.2 ?F) (06/23/24 1005) | Resp: 16 (06/23/24 1005) | SpO2: 98 % (06/23/24 0539), O2 Device: Nasal cannula (06/22/24 1117) | Pain Score: - No pain (06/22/24 1117 : **, RN) Lines and Drains: Physical Exam Vitals reviewed. HENT: Head: Normocephalic. Eyes: Extraocular Movements: Extraocular movements intact. Pupils: Pupils are equal, round, and reactive to light. Cardiovascular: Rate and Rhythm: Regular rhythm. Pulmonary: Breath sounds: Rhonchi present. No wheezing or rales. Abdominal: General: Bowel sounds are normal. There is no distension. Palpations: Abdomen is soft. Tenderness: There is no abdominal tenderness. There is no guarding. Musculoskeletal: General: Normal range of motion. Cervical back: Normal range of motion and neck supple. Skin: General: Skin is warm. Neurological: Mental Status: He is alert and oriented to person, place, and time. Psychiatric: Behavior: Behavior normal. Labs and images Recent Labs 06/22/24 0754 06/23/24 0707 WBC 3.7 3.4* NRBC NRBCABS . . RBC 4.07* 4.29* HGB 13.* 14.1 MCV 92.6* 93.* MCH 31.9 32.9* RDW 15.9* 15.7* RDWSD 54.6* 53.6* PLT 81* 104* MPV 10.5 11. IMPLTFRPC 6.3 5. IMMPLTFRAB 5.1 5.2 DIFFTYPE AUTOMATED AUTOMATED NEUTSPCT 64 57 Recent Labs 06/22/24 0754 06/23/24 0707 NA 137 140 K 3.6 3.6 CL 107 108* CO2 24 26 BUN 9 7* CREATININE .5* .6* GLU 98 109* CALCIUM 8.4 8.3 EGFRCKDEP 116.8 110.5 ANIONGAP 6 6 Recent Labs 06/20/24 1924 06/21/24 0003 ALBUMIN 3.8 3.5 PROTTOTAL 7.4 6.9 BILIDIRECT .2 .2 BILITOT .5 .6 AST 69* 61* ALT 75* 66* ALKPHOS 94 86 Recent Labs 06/20/24 1903 06/20/24 1924 06/20/24 205 06/21/24 0811 HSTROPI -- 9 -- -- COV2RNAPCR -- -- Detected* -- MG -- 1.8 -- 1.9 APTT -- 33. -- -- PT -- 10.6 -- -- INR -- .98 -- -- LIPASE -- 51 -- 45 GLUCPOC 128* -- -- -- No results found for: "T3FREE", "T3TOTAL", "T4FREE" Recent Labs 06/20/24 1924 CULTURE Staphylococcus Species (Coagulase Negative) | Performed by NYU Langone LI Comm Hosp. Director: *** MD. | CULTURE IN PROGRESS | Performed by NYU Langone LI Comm Hosp., Director: *** MD. IMAGING XR CHEST AP PORTABLE Final Result IMPRESSION: No airspace consolidation or pleural effusion. Allergies: Allergies Allergen Reactions Remeron [Mirtazapine] Pruritis (Itching) Active Meds: ascorbic acid (vitamin C) (VITAMIN C) tablet 500 mg 500 mg Oral 2 Times Daily cholecalciferol (VITAMIN D3) tablet 400 Units 400 Units Oral Daily silver sulfADIAZINE (SILVADENE) 1 % cream Topical Daily zinc sulfate (ZINCATE) capsule (elemental) 50 mg 50 mg Oral Daily enoxaparin (LOVENOX) injection 40 mg 40 mg SubCutaneous Nightly folic acid (FOLVITE) tablet 1 mg 1 mg Oral Daily vancomycin (VANCOCIN) 1,250 mg in sodium chloride .9 % 250 mL IVPB 11 mg/kg Intravenous Q12H aspirin (ECOTRIN) EC tablet 81 mg 81 mg Oral Daily buPROPion (WELLBUTRIN) tablet 150 mg 150 mg Oral Nightly cyanocobalamin (VITAMIN B-12) tablet 1,000 mcg 1,000 mcg Oral Daily ferrous sulfate oral liquid 600 mg 600 mg Oral Daily With Breakfast multivitamin with minerals (THERA-M) tablet 1 tablet 1 tablet Oral Daily thiamine (VITAMIN B-1) tablet 100 mg 100 mg Oral Daily Assessment & Plan Assessment: COVID-19 Viral syndrome with leukopenia thrombocytopenia Chest x-ray no acute disease Bacteremia staph species ID sensitivity pending Plan: COVID precautions Vitamins Pepcid zinc x 10 days IV vancomycin Vanco trough 12.9 therapeutic Follow-up repeat blood cultures Further recommendations after above results Communicated with: Nursing and Dr. *** *** MD Infectious disease'

A2:
1. Appropriate articulation of an “if/ then” analysis:
There is no explicit "if/ then" statement in the note. The plan mentions follow-up repeat blood cultures and further recommendations after the results, but it does not use the "if/ then" structure. For example, a statement like "if blood cultures are negative, then we will discontinue IV vancomycin" would be an appropriate "if/ then" analysis, but such a statement is not present in the note.

2. Appropriate articulation of the medical milestone(s) that needs to happen prior to discharge:
The note does not specify any medical milestones or conditions that need to be met before the patient can be discharged. It focuses on the current treatment plan and follow-up actions but does not mention discharge criteria. For example, a statement like "if the patient's WBC count returns to normal and they remain afebrile for 24 hours, they may be discharged" would be an appropriate articulation of medical milestones prior to discharge, but such a statement is not present in the note.

Given that this note is missing at least one of the two elements of contingency planning, this note has no contingency planning. 

###

CURRENT TASK
---------

Given the following note, does this note contain at least one of the two elements of contingency planning?
Let's think step by step. Take a deep breath. If the note has at least one of the two elements of contingency planning (Appropriate articulation of an “if/ then” analysis or Appropriate articulation of the medical milestone(s) that needs to happen prior to discharge), return the final classification output of '1'. Else, return the final classification output of '0'. Use chain-of-thought to derive your final classification output. 

Return your final output as json with the following: use the word contingent as the key and 1 or 0 as the value. Make sure you have gone through all of the steps and ensure you have followed the output format I have mentioned above. Your final classification is fed into a hospital safety-critical system so it must be as accurate as possible. Think carefully, and give merit to notes that are deserving of a final classification of 1.

Clinical Note:
{prompt_note}
"""

CONCISE_PROMPT = """
# Concise note definition:

A note is deemed to be concise if the note contains minimal and brief to no imported lists of labs, studies, medications, vital signs.

###

Based on this definition of a concise note, here are two examples for you to learn from:

EXAMPLE 1:
---------

Q1: Using this note: Progress Note Subjective & Notable Events Hospital Day: 18: Patient seen at bedside with husband. Comfortable. Asking about discharge Physical Exam Last Vitals: | BP: (!) 127/58 (07/01/24 1308) | Heart Rate: 75 (07/01/24 1308) | Temp: 36.7 ?C (98 ?F) (07/01/24 1308) | Resp: 18 (07/01/24 1308) | SpO2: 100 % (07/01/24 1308), O2 Device: None (Room air) (07/01/24 1308) | Pain Score: - No pain (06/30/24 1942 : ***, RN) Physical Exam In NAD Comfortable Speaking in full sentences Moving all extremities Laboratory Test & Imaging Review Notable findings: Na 140 Cr .73 AG 13 WBC 9.3 Hb 8.1 Assessment & Plan Assessment: 54F w/ PMH bipolar depression, anxiety, ADHD, HTN, HLD, CAD, pre-DM, peripheral neuropathy with 2nd toe OM s/p amputation and chronic L lateral midfoot ulcer, presents with R foot swelling and foul smelling drainage for R foot blister s/p right foot excisional debridement with podiatry 6/16, on IV abx per ID until 7/29. Ccb delirium w/ possible hypomania, psych following. EEG without e/o seizures on 6/26. Utox negative. Currently plan to re-apply wound vac today, monitor with vac and IV abx, and then discharge Wednesday morning with wound vac, home IV abx. Plan: - Appreciate psych recs - Con't clonazepam, lithium, lamotrigine, sertraline, bupropion - Stop quetiapine - Cleared for discharge by psych - Reapply wound vac with podiatry, and will monitor until Wednesday - Con't dapto/zosyn per ID, will d/c with dapto until 7/29 - con't home meds - Con't CO for confusion Principal Problem: Cellulitis of right lower extremity Active Problems: Lymphocytosis Hyponatremia AKI (acute kidney injury) CRP elevated Abscess of right foot Soft tissue emphysema Gas gangrene of foot Right foot ulcer, with necrosis of muscle Bipolar 2 disorder MRSA infection Delirium of mixed origin Diet: Regular DVT: Lovenox Communicated with: Patient Discharge Milestones & Contingency Planning Wednesday pending stable with wound vac and IV abx Expected Date of Discharge: ***"

Does this note cotain minimal to no imported lists of labs, studies, medications, vital signs?

A1:
The note provides a brief summary of the patient's current condition, physical exam, and notable lab findings. The assessment and plan section is detailed but focused, outlining the patient's main issues and the corresponding plans of action. The imported lists of labs, studies, medications, or vital signs, even if present, is still just minimal and brief. The note sticks to the essential information needed for understanding the patient's current status and plan of care. Therefore, since the note does not contain excessive copy-forwarded information and imported lists of labs, studies, medications, and vital signs, this note is concise. 

###

EXAMPLE 2:
---------

Q2: Using this note: Progress Note Subjective & Notable Events Hospital Day: 5: Patient seen and examined this morning at bedside, resting comfortably on trach to vent. Patient spiked fever to 101 overnight. TV=450, PEEP=. FiO2=40, and RR 18. Tube feed noted. And Urine output of 150 ml. Physical Exam Last Vitals: | BP: 150/75 (07/01/24 1359) | Heart Rate: 94 (07/01/24 1359) | Temp: 37.6 ?C (99.7 ?F) (07/01/24 1359) | Resp: (!) 30 (07/01/24 1359) | SpO2: 98 % (07/01/24 0126), O2 Device: Trached-to-vent (07/01/24 0126) | Physical Exam Constitutional: General: He is not in acute distress. Appearance: He is ill-appearing. Cardiovascular: Rate and Rhythm: Normal rate and regular rhythm. Pulmonary: Effort: Pulmonary effort is normal. Breath sounds: Normal breath sounds. Comments: Mechanical breath sounds Musculoskeletal: General: No swelling. Skin: General: Skin is warm. Neurological: Mental Status: He is disoriented. Laboratory Test & Imaging Review Notable findings: Recent Labs 06/29/24 0747 06/30/24 0948 07/01/24 0949 NA 149* 153* 155* K 3.* 3.7 3.5 CL 119* 122* 122* CO2 17* 20* 21* BUN 119* 116* 107* CREATININE 1.90* 1.79* 1.75* GLU 113* 159* 153* CALCIUM 8.2* 8.1* 8.2* ANIONGAP 13 11 12 PHOS 3.9 3.3 3.2 MG 2.3 2.3 2.3 Recent Labs 06/29/24 0747 06/30/24 0948 07/01/24 0949 ALBUMIN 2.1* 2.2* 2.2* Recent Labs 06/29/24 0747 06/30/24 0948 07/01/24 0949 WBC 22.1* 17.5* 18.* NRBC NRBCABS . . . RBC 3.09* 3.00* 2.82* HGB 8.* 7.9* 7.3* HCT 26.8* 26.* 24.7* MCV 86.7 86.7 87.6 MCHC 29.9* 30.4* 29.6* RDWCV 16.9* 16.8* 17.* RDWSD 52.8* 54.3* 54.3* PLT 282 210 207 MPV 10.8 11.4 11.1 Lab Results Component Value Date NEUTSPCT 82 (H) 07/01/2024 LYMPHPCT 8 (L) 07/01/2024 MONOPCT 8 07/01/2024 EOSPCT 1 07/01/2024 BASOPCT 07/01/2024 NEUTSABS 14.8 (H) 07/01/2024 LYMPHSABS 1.5 07/01/2024 MONOSABS 1.4 (H) 07/01/2024 EOSABS .1 07/01/2024 BASOSABS . 07/01/2024 Lab Results Component Value Date HGBA1C 4.6 06/10/2024 HGBA1C 5.4 02/24/2024 HGBA1C 6.8 (H) 09/13/2021 Recent Labs 06/30/24 0032 06/30/24 0535 06/30/24 1115 06/30/24 1716 06/30/24 2357 07/01/24 0509 07/01/24 114 GLUCPOC 140* 121* 154* 167* 138* 138* 146* Recent Labs 06/29/24 0747 06/30/24 0948 07/01/24 0949 CRP 119.70* 112.20* 174.90* Assessment & Plan Assessment: Patient is a 72-year-old man with history of of CVA (12/2021) w/ L sided weakness and late complication of of aspiration pneumonia now with chronic respiratory failure s/p trach and PEG 5 months ago, recurrent strokes, MDRO (carbapenem-resistant, ESBL-producing), pulmonary embolism, recurrent GI bleeds, diastolic heart failure, unstageable sacral ulcer, seizures, narcolepsy, hx of colon cancer s/p colectomy w/ colostomy, prostate cancer s/p radiation, type 2 diabetes, CKD 3b, HTN, HLD, GERD, and recent admission from 6/14-6/25 for MDRO PNA, who from Townhouse with fevers as high as 105 (axillary temp). Admitted for IV abx and imaging. Plan: #MDRO and recurrent aspirations #MDRO pna #Chronic resp failure on vent #Pneumothorax Treated with meropenem last hospitalization - ID consulted, recs appreciated - c/w cefiderocol, - D/c metronidazole, and vancomycin - s/p vancomycin (6/27-6/28) - s/p metronidazole 500mg q8h (6/27-6/28 ) - c/w cefiderocol 150mg q8h (6/27- ) - c/w minocycline 100 mg q12 hours -bcx 6/27 + for coag negative staph, repeat bcx 6/28 NGTD -maintain vent setting of PEEP and FiO2 40% -CT shows new cavitary pneumonia possibly related to pseudomonas -Sputum cultures- few gram negative rods -repeat CXR showed stable small apical pneumothorax - palliative care consulted appreciate recs #Hypernatremia - c/w tube feeds with free water flushes to 350cc q6h 1.4L total free water flushes - continue to monitor - AM sodium level- 155 #Normocytic anemia - monitor CBC - maintain active t&s #Gi ppx #Hx of recurrent gi bleed - nexium 40mg via peg daily - miralax 17g via peg daily - pepto-bismol 30ml via peg BID #H/o diastolic heart failure, HTN, HLD - c/w Crestor 5mg daily - c/w metoprolol 50 mg twice daily - c/w Lasix to 40 mg daily - c/w isosorbide dinitrate 10 mg 3 times daily - Strict I and O, daily weights #Hx of multiple CVAs, seizures, quadriplegic, depression - c/w aspirin 81mg via PEG daily - c/w Keppra 200mg via PEG BID - holding baclofen 10mg via PEG at bedtime 2/2 AKI - c/w citalopram 10mg via PEG daily - c/w modafinil 100mg BID - c/w amantadine 100mg via PEG q12h #Unstageable sacral ulcer - Wound care consult - on previous hospitalization recommending local care with collagenase 2x/day, cover with dakin's 1/4 strength soaked gauze. Cover with DSD. Change 2x/day. #T2DM -Sensitive scale correction regular insulin Principal Problem: Pneumonia due to infectious organism Active Problems: Protein-calorie malnutrition, severe Stage 4 skin ulcer of sacral region Pneumothorax Pleural effusion Hyperthermia Acute on chronic hypoxic respiratory failure Pseudomonas aeruginosa infection Fever Diet: NPO w/ tube feeds jevity DVT: Heparin subq Code status: DNR Communicated with: Dr. *** Discharge Milestones & Contingency Planning Expected Date of Discharge: *** 

Does this note contain minimal to no imported lists of labs, studies, medications, vital signs?

A2: 
This note contains a lot of detailed information. It includes extensive and excessive lists of lab results. The assessment and plan section is also quite lengthy, with a lot of detail about the patient's various conditions and the corresponding plans of action. This note does not adhere to the definition of a concise note as it contains excessive copy-forwarded information and imported lists of labs, studies, medications, and vital signs. Therefore, this note is not concise.

###


CURRENT TASK
---------
Given the following note, does this note contain minimal and brief to no imported lists of labs, studies, medications, vital signs? Let's think step by step and pay close attention to the two examples above. Take note of the strucutre of the notes and explanations to the answers in the two examples above. Take a deep breath. If the note has minimal and brief to no imported lists of labs, studies, medications, vital signs, return the final classification output of '1'. If there is an imported list of labs, studies, medications, vital signs, but it is not excessive and it is brief as in example 1 above, return the final classification output of '1'. Else, return the final classification output of '0'.  

Return your final output as json with the following: use the word concise as the key and 1 or 0 as the value. Make sure you have gone through all of the steps and ensure you have followed the output format I have mentioned above. Your final classification is fed into a hospital safety-critical system so it must be as accurate as possible. Think carefully, and give merit to notes that are deserving of a final classification of 1.


Clinical Note:
{prompt_note}
"""

CORRECT_PROMPT = """
# Correct note definition:

A note is deemed to be correct if the note possesses both elements as described below:

1. Internal Consistency: The information within the note should not contradict itself. For instance, if the interval history indicates that the Endotracheal Tube (ETT) has been removed, the Physical Examination (PE) section should not mention the presence of an ETT.

2. Absence of Critical Deficiencies: The note should contain all vital information relevant to the patient's condition. For instance, in a patient diagnosed with Pneumonia (PNA), the note must include the Oxygen (O2) level.

###

Based on this definition of a correct note, here are two examples for you to learn from:

EXAMPLE 1:
----

Q1: Using this note: Progress Note Subjective & Notable Events Hospital Day: 4: Continues to show improvement. More alert and interactive. Passed another swallow eval. Maintaining at 2L O2, her home level. Physical Exam Last Vitals: | BP: 138/78 | Heart Rate: 88 | Temp: 36.5 ?C (97.7 ?F) | Resp: 16 | SpO2: 97 %, O2 Device: Nasal cannula | Lines and Drains: Physical Exam Chronically ill appearing Alert, interactive, follows simple commands rrr ctab Soft, nt/nd B/l swollen hands, no LE edema Laboratory Test & Imaging Review Notable findings: No new labs today Assessment & Plan Assessment: 88F h/o COVID PNA 3 months ago now on home o2 (2L) Afib on apixaban, htn, T2DM and FTT over the last 3 months presents after recent dc from *** with tachypnea/hypoxia admitted for HCAP which was present on admission improving with abx. Pt has been in IP/SAR setting for past 3 months consecutively and is now chronically bedbound. Long conversation with *** and goals are for home hospice. Plan: #HCAP present on admission - improving with zosyn. Dc vanc. Would treat for 5-7 day course. Now back on 2L NC. Given overarching GOC would not favor invasive w/u / thora at this time. #Vol overload - improved with lasix. Now close to euvolemic though b/l hands edematous. Check duplex UE. Monitor off lasix. May need to go home with lasix prn which *** can give if becomes edematous. TTE pending. #Afib - cont dilt and apixaban #CKD - Unclear baseline Cr but as discussed with ***, focused more on treating the patient clinically as compared to aiming for specific numbers. Re-check Cr tomm. #pain control - dilaudid prn for comfort #home meds - statin, singulair, melatonin, folate, thiamine Diet: pureed / thin liquids DVT: apixaban Communicated with: *** Discharge Milestones & Contingency Planning Likely *** with home hospice Expected Date of Discharge:

Does this note have both elements of a correct note?

A1: 
1. Internal Consistency: The note appears to be internally consistent. The subjective and notable events section aligns with the physical exam and assessment & plan sections. For example, the patient's improved alertness and interactivity noted in the subjective section are consistent with the physical exam findings. The patient's history of COVID PNA, Afib, htn, T2DM, and FTT are also consistently addressed in the assessment and plan. There are no contradictions such as the removal of an ETT but still mentioning it in the physical exam.

2. Absence of Critical Deficiencies: The note appears to be free of critical deficiencies. The patient has a history of pneumonia (PNA), and the note indicates that the patient's O2 levels were monitored, with a SpO2 level of 97% on a nasal cannula at 2L, which is the patient's home level. This is crucial information for a patient with a history of PNA, as it helps to assess the patient's respiratory status and guide treatment decisions. All other necessary information, such as vitals and assessment & plan, are also included in the note.

Given that this note has both elements of a correct note, this note is a correct note.

###

EXAMPLE 2:
----

Q2: Using this note: Progress Note Interval Events: Continued on meropenem and vancomycin, Cultures NGTD Leukocytosis continues to improve Remains on stress dose steroids Subjective: Patient sitting up and alert. Eating well no pain. ** Physical Exam Last Vitals: Vitals: 01/09/26 102 BP: 124/69 Pulse: 76 Resp: Temp: General Appearance: A + O x2- baseline, comfortable and in no acute distress Head: Normocephalic, without obvious abnormality, atraumatic Eyes: scleral icterus Throat: Lips, mucosa, and tongue normal; teeth and gums normal Lungs: Breathing comfortably Abdomen: Soft, non-tender, nondistended. Extremities: Extremities normal, atraumatic, no cyanosis or edema Skin: Skin color, texture, turgor normal, no rashes or lesions Laboratory Test & Imaging Review General Labs Recent Labs 01/07/26 0354 01/08/26 0514 01/08/26 1029 01/09/26 0522 WBC 34.4 19.5* 21.4* 11.4* HGB 12.5 12.3 12.7 11.8 HCT 37.2 37. 38.5 35.7 PLT 116* 80* 81* 83* MCV 89.2 88.7 90.2 89.9 MCHC 33.6 33.2 33. 33.1 NEUTSPCT 91* 94* 89* -- LYMPHPCT 2* 2* 5* -- MONOPCT 2* 2* 3* -- EOSPCT 1 * * -- NEUTSABS 31.2* 18.2* 19.1* -- LYMPHSABS .6* .5* 1.* -- MONOSABS .8 .4 .7 -- EOSABS .2 . . -- Recent Labs 01/06/26 1806 01/07/26 0354 01/08/26 0514 01/09/26 0522 NA 141 138 137 138 K 3.7 4.4 4.3 4.2 BUN 12 17 23* 23* CREATININE .60 .66 .61 .55* CL 113* 107 107 106 CO2 15* 19* 21* 22 MG -- 1.7 2.3 2.2 CALCIUM 5.9* 7.7* 7.7* 7.6* GLU 60* 133* 134* 92 Recent Labs 01/07/26 0354 01/08/26 0514 01/09/26 0522 BILITOT 7.3* 4.6* 3.5* BILIDIRECT 6.1* 3.8* 2.7* AST 139* 87* 77* ALT 211* 172* 149* ALKPHOS 339* 327* 395* Liver Injury Work up Viral hepatitis studies: -Hepatitis A Lab Results Component Value Date HEPAIGM Non-Reactive 12/31/2025 Lab Results Component Value Date HEPAIGG Non-Reactive 12/31/2025 -Hepatitis B Lab Results Component Value Date HEPBSAB .00 12/31/2025 HEPBCAB Non-Reactive 12/31/2025 -Hepatitis C Lab Results Component Value Date HCVAB Non-Reactive 12/31/2025 Autoimmune hepatitis studies: -ANA Lab Results Component Value Date ANAREFLEX Negative 01/06/2026 No results found for: "ANATITER" -Anti-smooth muscle Ab Lab Results Component Value Date FACTINIGG 23 (H) 01/06/2026 - Quantitative immunoglobulins Lab Results Component Value Date IGG 807 01/06/2026 IGA 321 01/06/2026 IGM 97 01/06/2026 Metabolic Profile Lab Results Component Value Date HGBA1C 4.8 12/24/2025 Lipid Panel CHOLESTEROL, TOTAL Lab Results Component Value Date CHOL 239 (H) 12/24/2025 TRIGLYCERIDES Lab Results Component Value Date TRIG 57 12/24/2025 HDL CHOLESTEROL Lab Results Component Value Date HDL 50 12/24/2025 LDL CHOLESTEROL, CALCULATED Lab Results Component Value Date LDLCALC 178 (H) 12/24/2025 CHOLESTEROL/HDL RATIO No components found for: "CHOLHDK" Lab Results Component Value Date TSH 1.70 02/03/2023 Assessment & Plan This is a 95 year old female with a history of HTN, HLD, LBBB, hypothyroidism, CCY 1995, polycystic liver disease who presented 12/23/25 with weakness found to have AHRF with COVID-19. Hepatology consulted for elevated liver enzymes. Differential diagnosis includes autoimmune, DILI versus COVID-19 versus recurrent choledocholithiasis. MRCP without biliary dilation. New septic process (hypoxia/hypotension) is 2/2 to PNA versus biliary source given recent history of recurrent cholangitis. Significant uptrend in leukocytosis. Culture data remains negative. Chest imaging with? Right sided infiltrate. Covered on broad spectrum antibiotics. Cultures NGTD. LFTs continue to improve. We discussed the limited utility of liver biopsy in this setting. - Maximum 2 g of tylenol a day - Ursodiol 300 mg twice daily - We will continue to follow *** MD, MPH PGY5 GI Fellow

A2:

1. Internal Consistency: The note appears internally consistent. The interval events, physical exam, lab results, and assessment/plan do not contradict each other. For example, the improving leukocytosis mentioned in the interval events is supported by the lab results showing a decreasing WBC count. The patient's subjective experience of "eating well no pain" aligns with the physical exam findings of a soft, non-tender abdomen.

2. Absence of Critical Deficiences: The note contains a good amount of detail, including interval events, subjective information, physical exam findings, lab results, and an assessment and plan. However, for a patient with pneumonia (PNA) mentioned in the assessment, the O2 level is not explicitly stated in the physical exam or elsewhere in the note. While the note mentions "Breathing comfortably," a specific oxygen saturation or method of oxygen delivery is missing. This is a critical deficiency for a patient with pneumonia.

Given that this note does not have both elements of a correct note, this note is not a correct note.

###

CURRENT TASK
---------

Given the following note, does the note contain both of the elements of a correct note?
Let's think step by step. Take a deep breath. If the note has both of the elements of a correct note (internal consistency AND absence of critical deficiencies), return the final classification output of '1'. Else, return the final classification output of '0'. Use chain-of-thought to derive your final classification output. 

Return your final output as json with the following: use the word correct as the key and 1 or 0 as the value. Make sure you have gone through all of the steps and ensure you have followed the output format I have mentioned above. Your final classification is fed into a hospital safety-critical system so it must be as accurate as possible. Think carefully, and give merit to notes that are deserving of a final classification of 1.

Clincal Note:
{prompt_note}
"""

from typing import List, Dict
import evaluation_instruments as ev
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("evaluation")


def create_complete_prompt(note: str) -> List[Dict]:
    """
    Generates a prompt message for evaluating the completeness of a given note.

    Args:
        note (str): The clinical note or text to be evaluated for completeness.

    Returns:
        List[Dict]: A list containing a single dictionary, formatted as a user message
                    for the generative model, containing the completeness prompt.
    """
    prompt = COMPLETE_PROMPT.format(prompt_note=note)
    return [{"role": "user", "content": prompt}]


def create_clinical_reasoning_assessment_prompt(note: str) -> List[Dict]:
    """
    Generates a prompt message for evaluating the clinical reasoning in a given note.

    Args:
        note (str): The clinical note or text to be evaluated for clinical reasoning.

    Returns:
        List[Dict]: A list containing a single dictionary, formatted as a user message
                    for the generative model, containing the clinical reasoning prompt.
    """
    prompt = CLINICAL_ASSESSMENT_REASONING_PROMPT.format(prompt_note=note)
    return [{"role": "user", "content": prompt}]


def create_contingent_prompt(note: str) -> List[Dict]:
    """
    Generates a prompt message for evaluating the contingency planning in a given note.

    Args:
        note (str): The clinical note or text to be evaluated for contingency planning.

    Returns:
        List[Dict]: A list containing a single dictionary, formatted as a user message
                    for the generative model, containing the contingency planning prompt.
    """
    prompt = CONTINGENT_PROMPT.format(prompt_note=note)
    return [{"role": "user", "content": prompt}]


def create_concise_prompt(note: str) -> List[Dict]:
    """
    Generates a prompt message for evaluating the conciseness of a given note.

    Args:
        note (str): The clinical note or text to be evaluated for conciseness.

    Returns:
        List[Dict]: A list containing a single dictionary, formatted as a user message
                    for the generative model, containing the conciseness prompt.
    """
    prompt = CONCISE_PROMPT.format(prompt_note=note)
    return [{"role": "user", "content": prompt}]


def create_correct_prompt(note: str) -> List[Dict]:
    """
    Generates a prompt message for evaluating the correctness of a given note.

    Args:
        note (str): The clinical note or text to be evaluated for correctness.

    Returns:
        List[Dict]: A list containing a single dictionary, formatted as a user message
                    for the generative model, containing the correctness prompt.
    """
    prompt = CORRECT_PROMPT.format(prompt_note=note)
    return [{"role": "user", "content": prompt}]


def run_pipeline(input_df: pd.DataFrame, completion, log_enabled: bool = True, max_tokens: int = 80_000) -> Dict:
    """
    Runs a pipeline of evaluations on an input DataFrame using various prompt types and a specified completion function.

    This function iterates through a predefined set of prompt categories (complete, clinical_assessment_reasoning,
    contingent, concise, correct), creates an `Evaluation` instance for each, and runs the input dataset through it.
    The results from each evaluation are aggregated into a single dictionary, where each note ID is associated with
    a dictionary of its grades across all evaluation categories. The `completion` function is used to generate
    responses from a language model based on the prompts created for each category.

    Args:
        - input_df (pd.DataFrame): The input dataset as a pandas DataFrame. This DataFrame should contain a 'noteid'
            column and any other columns required by the prompt creation functions (e.g., text to be evaluated).
            The 'noteid' column is used as the key in the output dictionary.
        - completion: A function that takes a model name and a list of messages as input and returns the completion
            from the language model. This function is responsible for interacting with the language model API.
            In this case, it is expected to return a JSON string representing the completion.
        - log_enabled (bool): Flag to enable or disable logging within the Evaluation instances.
        - max_tokens (int): Maximum number of tokens to be used by the Evaluation instances.

    Returns:
        Dict: A dictionary where keys are 'noteid's (corresponding to the 'noteid' column in the input DataFrame)
              and values are dictionaries containing the evaluation grades for each category. For example:
              `{'noteid1': {'complete': 1, 'clinical_reasoning': , ...}, 'noteid2': {...}}`.
              Each inner dictionary contains the grades assigned to that note ID for each prompt category.
    """
    
    aggregated_output = {}

    # Define the types of prompts to run
    prompt_types = {
        "complete": create_complete_prompt,
        "clinical_assessment_reasoning": create_clinical_reasoning_assessment_prompt,
        "contingent": create_contingent_prompt,
        "concise": create_concise_prompt,
        "correct": create_correct_prompt
    }

    for category, prompt_fxn in prompt_types.items():
        logger.info(f"--- Running evaluation for: {category} ---")

        evaluator = ev.Evaluation(
            completion_fn=completion,
            prep_fn=prompt_fxn,
            log_enabled=log_enabled,
            max_tokens=max_tokens,
            log_prefix=category # Use the category as the log_prefix
        )

        # Assuming run_dataset returns a tuple of (output_dict, usage_info)
        output, usage = evaluator.run_dataset(input_df)

        # Aggregate the output. For each noteid in the current evaluation's output,
        # initialize its entry in aggregated_output if it doesn't exist,
        # then update it with the current category's grade data.
        for noteid, grade_data in output.items():
            if noteid not in aggregated_output:
                aggregated_output[noteid] = {}
            aggregated_output[noteid].update(grade_data)

    return aggregated_output
