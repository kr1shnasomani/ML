<h1 align="center">FilmFinder</h1>

Content-based Movie Recommendation Engine suggesting movies based on plot and metadata similarities.

## Approach
- **NLP Text Processing**: `TfidfVectorizer` and `CountVectorizer` to embed metadata.
- **Similarity Matrix**: `cosine_similarity` and `linear_kernel` to find matches.

## Performance
Efficiently retrieves the top 10 most similar movies across large datasets.

## Installation & Execution
```bash
cd FilmFinder
pip install numpy pandas matplotlib scikit-learn
```
Open and run `code/main.ipynb`.
