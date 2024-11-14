# ner_training/data_loader.py

def load__data_conll(file_path):
    """
    Load data in CONLL format with four columns (word, POS, chunk, NER tag).
    Input: Only consider the word and NER tag columns.
    Output: A list of sentences, where each sentence is represented by two lists:
            - words: List of words (tokens) in the sentence
            - ner_tags: List of corresponding NER tags for each word
    """
    sentences = []
    words, ner_tags = [], []

    with open(file_path, 'r') as fh:
        for line in fh:
            line = line.strip()
            
            # Check for sentence boundaries
            if not line:
                if words and ner_tags:  # Ensure both lists are non-empty before appending
                    sentences.append([words, ner_tags])
                    words, ner_tags = [], []  # Reset for the next sentence
                continue

            # Skip any document start markers
            if line.startswith("-DOCSTART-"):
                continue

            # Split the line into components and extract word and NER tag
            components = line.split()
            if len(components) == 4:
                word, ner_tag = components[0], components[3]
                words.append(word)
                ner_tags.append(ner_tag)
            else:
                print(f"Unexpected format in line: {line}")

    # Append any remaining sentence
    if words and ner_tags:
        sentences.append([words, ner_tags])
    
    return sentences
