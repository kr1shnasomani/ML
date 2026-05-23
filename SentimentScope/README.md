<h1 align="center">SentimentScope</h1>

Classifies IMDb movie reviews as positive or negative using deep learning.

## Approach
- **NLP Processing**: Tokenization and sequence padding.
- **Embeddings**: Pre-trained GloVe embeddings for dense vector representations.
- **Architecture**: Sequential LSTM network.

## Performance
Achieves ~85.39% accuracy on the test set.

## Installation & Execution
```bash
cd SentimentScope
pip install pandas numpy matplotlib tensorflow scikit-learn
```
Download IMDb dataset and GloVe embeddings as specified, then run `code/main.ipynb`.
