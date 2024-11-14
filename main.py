# main.py

from ner_training.data_loader import load__data_conll
from ner_training.feature_extraction import get_feats_conll
from ner_training.model import train_seq

def main():
    train_path = 'data/train.txt'
    test_path = 'data/test.txt'

    # Load and process data
    conll_train = load__data_conll(train_path)
    conll_dev = load__data_conll(test_path)

    # Extract features and labels
    X_train, Y_train = get_feats_conll(conll_train)
    X_dev, Y_dev = get_feats_conll(conll_dev)

    # Train and evaluate model
    train_seq(X_train, Y_train, X_dev, Y_dev)

if __name__ == "__main__":
    main()
