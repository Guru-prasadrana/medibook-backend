from typing import Optional


SPECIALTY_KEYWORDS: dict[str, list[str]] = {
    "Cardiology": [
        "chest pain", "chest tightness", "chest pressure",
        "heart attack", "heart pain", "palpitations", "irregular heartbeat",
        "rapid heartbeat", "slow heartbeat", "shortness of breath",
        "breathlessness", "swollen ankles", "swollen legs", "high blood pressure",
        "hypertension", "low blood pressure", "hypotension", "fainting",
        "dizziness", "lightheadedness", "bluish lips", "bluish fingertips",
        "heart failure", "arrhythmia", "angina",
    ],

    "Dermatology": [
        "skin rash", "rash", "itchy skin", "itching", "hives", "eczema",
        "psoriasis", "acne", "pimples", "blackheads", "dry skin", "oily skin",
        "skin peeling", "blistering", "boils", "cysts", "warts", "moles",
        "skin discoloration", "pigmentation", "dark spots", "white patches",
        "vitiligo", "ringworm", "fungal infection", "hair loss", "alopecia",
        "dandruff", "nail discoloration", "brittle nails", "skin lesion",
        "sunburn", "skin cancer", "melanoma",
    ],

    "Neurology": [
        "headache", "migraine", "severe headache", "chronic headache",
        "brain", "seizure", "epilepsy", "convulsions", "tremors", "shaking",
        "numbness", "tingling", "weakness in limbs", "paralysis",
        "memory loss", "forgetfulness", "confusion", "dementia",
        "alzheimer", "stroke", "slurred speech", "difficulty speaking",
        "blurred vision", "double vision", "loss of balance", "vertigo",
        "fainting", "unconsciousness", "multiple sclerosis", "parkinson",
        "nerve pain", "neuropathy", "spinal cord",
    ],

    "Gastroenterology": [
        "stomach pain", "stomach ache", "abdominal pain", "abdominal cramps",
        "gas", "bloating", "indigestion", "heartburn", "acid reflux", "gerd",
        "nausea", "vomiting", "diarrhea", "constipation", "loose stools",
        "blood in stool", "black stool", "rectal bleeding", "difficulty swallowing",
        "loss of appetite", "jaundice", "yellow skin", "yellow eyes",
        "liver pain", "gallbladder", "gallstones", "pancreatitis",
        "irritable bowel", "ibs", "crohn", "colitis", "ulcer", "stomach ulcer",
        "hemorrhoids", "piles", "anal pain",
    ],

    "Orthopedics": [
        "joint pain", "knee pain", "back pain", "lower back pain", "neck pain",
        "shoulder pain", "hip pain", "elbow pain", "wrist pain", "ankle pain",
        "bone pain", "fracture", "broken bone", "sprain", "strain",
        "muscle pain", "muscle weakness", "stiff joints", "swollen joints",
        "arthritis", "osteoporosis", "scoliosis", "slipped disc",
        "herniated disc", "carpal tunnel", "tendonitis", "bursitis",
        "sports injury", "ligament tear", "acl", "rotator cuff", "joint swelling", "swollen joint",
    ],

    "Pulmonology": [
        "cough", "chronic cough", "dry cough", "wet cough", "blood in cough",
        "coughing blood", "wheezing", "asthma", "shortness of breath",
        "difficulty breathing", "rapid breathing", "chest congestion",
        "lung pain", "pneumonia", "bronchitis", "tuberculosis", "tb",
        "sleep apnea", "snoring", "copd", "emphysema", "pulmonary",
        "pleural effusion", "collapsed lung", "oxygen levels low",
    ],

    "ENT (Ear, Nose & Throat)": [
        "ear pain", "earache", "ear infection", "hearing loss", "ringing ears",
        "tinnitus", "blocked ears", "ear discharge", "nose bleed", "nosebleed",
        "blocked nose", "runny nose", "sinusitis", "sinus pain", "sinus pressure",
        "sore throat", "throat pain", "difficulty swallowing", "hoarseness",
        "loss of voice", "tonsil", "tonsillitis", "adenoids", "nasal polyps",
        "sneezing", "allergic rhinitis", "vertigo", "balance problem",
        "smell loss", "taste loss",
    ],

    "Ophthalmology": [
        "eye pain", "eye redness", "red eyes", "itchy eyes", "watery eyes",
        "eye discharge", "blurred vision", "double vision", "vision loss",
        "sudden vision loss", "floaters", "flashes of light", "night blindness",
        "sensitivity to light", "photophobia", "cataracts", "glaucoma",
        "conjunctivitis", "pink eye", "dry eyes", "eye swelling",
        "bulging eyes", "crossed eyes", "squinting",
    ],

    "Endocrinology": [
        "diabetes", "high blood sugar", "low blood sugar", "hypoglycemia",
        "hyperglycemia", "thyroid", "hypothyroidism", "hyperthyroidism",
        "weight gain", "sudden weight gain", "weight loss", "sudden weight loss",
        "excessive thirst", "frequent urination", "excessive hunger",
        "fatigue", "extreme tiredness", "adrenal", "cushing", "addison",
        "hormonal imbalance", "hot flashes", "excessive sweating", "cold intolerance",
        "heat intolerance", "swollen neck", "goiter", "pituitary",
    ],

    "Urology": [
        "urinary pain", "painful urination", "burning urination", "frequent urination",
        "blood in urine", "cloudy urine", "dark urine", "kidney pain", "burning sensation",
        "kidney stone", "urinary tract infection", "uti", "bladder infection",
        "bladder pain", "incontinence", "urine leakage", "prostate",
        "prostate pain", "erectile dysfunction", "testicular pain",
        "scrotal swelling", "penile discharge", "difficulty urinating",
        "weak urine stream",
    ],

    "Gynecology": [
        "period pain", "menstrual cramps", "irregular periods", "heavy bleeding",
        "missed period", "no period", "vaginal discharge", "vaginal itching",
        "vaginal odor", "pelvic pain", "lower abdominal pain", "ovarian cyst",
        "pcod", "pcos", "endometriosis", "fibroids", "pregnancy", "miscarriage",
        "fertility issues", "menopause", "hot flashes", "breast pain",
        "breast lump", "nipple discharge", "cervical pain",
    ],

    "Psychiatry": [
        "depression", "feeling sad", "hopelessness", "anxiety", "panic attack",
        "panic", "stress", "burnout", "mood swings", "bipolar",
        "schizophrenia", "hallucinations", "hearing voices", "paranoia",
        "obsessive thoughts", "ocd", "phobia", "ptsd", "trauma", "feeling sad", "feeling hopeless",
        "insomnia", "sleep problems", "can't sleep", "cannot sleep", "nightmares", "eating disorder",
        "anorexia", "bulimia", "self harm", "suicidal thoughts", "addiction",
        "substance abuse", "anger issues", "personality disorder", "adhd",
        "attention deficit",
    ],

    "Pediatrics": [
        "child fever", "baby fever", "infant", "newborn", "toddler",
        "child vomiting", "child diarrhea", "child rash", "diaper rash", "has fever", "baby sick",
        "teething", "vaccination", "growth delay", "developmental delay",
        "childhood asthma", "croup", "whooping cough", "measles", "mumps",
        "chickenpox", "child ear infection", "bedwetting",
    ],

    "Oncology": [
        "cancer", "tumor", "lump", "mass", "unexplained weight loss",
        "night sweats", "persistent fatigue", "blood in urine cancer",
        "blood in stool cancer", "abnormal bleeding", "swollen lymph nodes",
        "lymphoma", "leukemia", "breast cancer", "lung cancer",
        "colon cancer", "cervical cancer", "prostate cancer",
        "skin cancer", "chemotherapy", "radiation",
    ],

    "Nephrology": [
        "kidney failure", "chronic kidney disease", "ckd", "dialysis",
        "kidney swelling", "puffy eyes", "foamy urine", "protein in urine",
        "creatinine high", "kidney inflammation", "nephrotic syndrome",
        "nephritic syndrome", "polycystic kidney",
    ],

    "Rheumatology": [
        "rheumatoid arthritis", "lupus", "autoimmune", "joint inflammation",
        "morning stiffness", "fibromyalgia", "gout", "uric acid",
        "sjogren", "scleroderma", "vasculitis", "chronic joint pain",
        "muscle inflammation", "myositis",
    ],

    "Dentistry": [
        "toothache", "tooth pain", "cavity", "tooth decay", "gum pain",
        "bleeding gums", "swollen gums", "bad breath", "halitosis",
        "jaw pain", "tmj", "broken tooth", "chipped tooth", "sensitive teeth",
        "tooth sensitivity", "wisdom tooth", "dental abscess", "mouth ulcer",
        "canker sore", "dry mouth",
    ],

    "General Medicine": [
        "fever", "high temperature", "cold", "flu", "fatigue", "tiredness",
        "general weakness", "body ache", "chills", "sweating", "dehydration",
        "malaria", "typhoid", "dengue", "viral infection", "bacterial infection",
        "anemia", "low hemoglobin", "vitamin deficiency", "malnutrition",
    ],
}


def analyze_symptoms(symptoms: str) -> dict[str, str | list[str]]:
    """
    Analyze symptom text and return the best matching specialty
    along with all matched keywords.

    Returns:
        {
            "specialty": "Cardiology",
            "matched_keywords": ["chest pain", "palpitations"],
            "confidence": "high" | "medium" | "low"
        }
    """
    text = symptoms.lower()

    scores: dict[str, list[str]] = {}

    for specialty, keywords in SPECIALTY_KEYWORDS.items():
        matches = [kw for kw in keywords if kw in text]
        if matches:
            scores[specialty] = matches

    if not scores:
        return {
            "specialty": "General Medicine",
            "matched_keywords": [],
            "confidence": "low",
            "message": "No specific symptoms matched. Recommending General Medicine.",
        }

    # Pick specialty with most keyword matches
    best = max(scores, key=lambda k: len(scores[k]))
    match_count = len(scores[best])

    confidence = "high" if match_count >= 3 else "medium" if match_count == 2 else "low"

    return {
        "specialty": best,
        "matched_keywords": scores[best],
        "confidence": confidence,
        "all_matches": {k: v for k, v in scores.items()},
    }


# ── Quick test ──
if __name__ == "__main__":
    test_cases = [
        "I have chest pain and palpitations",
        "severe headache, blurred vision and memory loss",
        "stomach pain, bloating and acid reflux",
        "knee pain and joint swelling after sports",
        "feeling very sad, anxious and can't sleep",
        "toothache and bleeding gums",
        "child has fever and ear infection",
        "itchy skin, dry patches and hair loss",
        "frequent urination and burning sensation",
        "I feel tired",
    ]

    for symptom in test_cases:
        result = analyze_symptoms(symptom)
        print(f"\nSymptoms : {symptom}")
        print(f"Specialty: {result['specialty']}  [{result['confidence']} confidence]")
        print(f"Matched  : {result['matched_keywords']}")