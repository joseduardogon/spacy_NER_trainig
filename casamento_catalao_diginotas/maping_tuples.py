import json

def label_studio_to_spacy_format(label_studio_json_path, output_path):
    """
    Converts a JSON file exported from Label Studio to a SpaCy training format.
    :param label_studio_json_path: Path to the Label Studio JSON file.
    :param output_path: Path to save the converted SpaCy training data.
    """
    with open(label_studio_json_path, 'r', encoding='utf-8') as f:
        label_studio_data = json.load(f)

    training_data = []

    for entry in label_studio_data:
        # Garantindo que os dados e anotações estão presentes
        if 'data' not in entry or 'annotations' not in entry:
            print(f"Warning: Entry missing 'data' or 'annotations': {entry}")
            continue

        text = entry['data'].get('text', "")
        if not text:
            print("Warning: Entry text is missing or empty.")
            continue

        if not entry['annotations']:
            print("Warning: No annotations found in entry.")
            continue

        annotations = entry['annotations'][0].get('result', [])
        entities = []

        for annotation in annotations:
            if annotation.get('type') == 'labels':
                try:
                    start = annotation['value']['start']
                    end = annotation['value']['end']
                    label = annotation['value']['labels'][0].upper()
                    entities.append((start, end, label))
                except KeyError as e:
                    print(f"Warning: Missing key in annotation {annotation}, error: {e}")
                    continue

        training_data.append((text, {"entities": entities}))

    # Save the training data in the output path
    with open(output_path, 'w', encoding='utf-8') as out_f:
        json.dump(training_data, out_f, ensure_ascii=False, indent=2)

    print(f"Training data successfully saved to {output_path}")

# Example usage
label_studio_to_spacy_format("C:\\Users\\josed\\Downloads\\project-2-at-2024-10-25-14-53-36231f51.json",
                             'C:\\Users\\josed\\codes\\spacy_NER_trainig\\maped_data.json')