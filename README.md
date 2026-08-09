# Homework Solutions

All solutions are written in English and use the official exercise data where it was provided. Folder names follow the lesson date or the source exercise name supplied in the course links.

## Inputs and Credentials

- Put the course `landscape.jpg` next to `c_unsupervised_Fd-kmean-hw/c_unsupervised_Fd-kmean-hw.py` when running the K-Means image exercise. A deterministic fallback image keeps the script runnable without the asset.
- Put the course `tips.csv` next to `29.09.2025_18-zmatplotlib-hw/matplotlib_exercises.py` to generate the tips-analysis plots.
- Set `OPENAI_API_KEY` only in the environment when running live GenAI functions. The key is never stored in this repository.

## Assignments

- `17.11.2025_02-logistic_hw`: logistic regression classification and confidence threshold.
- `13.11.2025_07-knn_hw2`: manual and scikit-learn KNN regression.
- `20.11.2025_09-svm_hw`: distances and classification relative to a hyperplane.
- `24.11.2025_10-svm_hw2`: linear SVM for apples and bananas.
- `27.11.2025_16-dec_tree_hw`: decision-tree split comparison and rules.
- `a_supervised_21-randomf-hw`: multiclass Random Forest and OOB score.
- `c_unsupervised_Fd-kmean-hw`: K-Means image color quantization and Elbow Method.
- `d_ann_Jc-NN-hw`: linear and logistic neural-network examples.
- `09.03.2026_hw`: recursive Python exercises.
- `05.02.2026_hw`: Point class and tests.
- `05.03.2026_hw`: OOP interview exercises.
- `16.02.2026_hw`: abstract vehicle interfaces.
- `26.02.2026_hw`: hashing, equality, `*args`, and `**kwargs`.
- `12.02.2027_hw`: vehicle inheritance exercises.
- `12-pandas-hw2`: Pandas filtering, transformations, indexing, and conditions.
- `29.09.2025_18-zmatplotlib-hw`: Matplotlib line, scatter, bar, histogram, and subplot exercises.
- `26.03.2026_hw`: TDD BankAccount implementation and tests.
- `23.03.2026_hw`: pytest functions and coverage.
- `12.03.2026_hw`: in-memory FastAPI books API.
- `16.03.2026_hw`: SQLite-backed FastAPI books API.
- `j_agents_03-agents-hw`: restricted tool-using agent with JSONL evaluation logs.
- `h_genai_Lg-GenAI-hw`: GenAI examples with offline fallbacks and optional OpenAI calls.

## Verification

From the repository root:

```powershell
& '.venv\Scripts\python.exe' -m compileall -q complete_hw
& '.venv\Scripts\python.exe' -m pytest complete_hw -q
```
