"""Credential-safe GenAI homework examples.

Set OPENAI_API_KEY before running the live examples. The functions keep the
prompt and response contract local so the assignment can be tested offline.
"""
import json
import os
import secrets
import string
from pathlib import Path


def password_generator(length=16):
    if length < 8:
        raise ValueError("password length must be at least 8")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return {"password": password, "explanation": "Generated with the cryptographically secure secrets module."}


def generate_password_and_explain(length, requirements):
    result = password_generator(length)
    result["requirements"] = requirements
    return result


def review_sentiment(review):
    positive = {"good", "great", "excellent", "love", "fast", "helpful"}
    negative = {"bad", "poor", "slow", "hate", "broken", "late"}
    words = set(review.lower().split())
    score = len(words & positive) - len(words & negative)
    label = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return {"sentiment": label, "score": score, "review": review}


def analyze_reviews(reviews_list):
    reviews = [review_sentiment(review) for review in reviews_list]
    positive = sum(review["sentiment"] == "positive" for review in reviews)
    negative = sum(review["sentiment"] == "negative" for review in reviews)
    overall_score = round(5 + 5 * (positive - negative) / max(len(reviews), 1))
    return {"reviews": reviews, "overall_score": max(1, min(10, overall_score)), "summary": f"{positive} positive, {negative} negative, and {len(reviews) - positive - negative} neutral reviews."}


def run_python_quiz(answers=None):
    questions = ["What keyword defines a function?", "What data type stores key-value pairs?", "What does len([1, 2, 3]) return?"]
    expected = ["def", "dict", "3"]
    if answers is None:
        return {"questions": questions, "message": "Provide three answers to receive a score."}
    score = sum(str(answer).strip().lower() == value for answer, value in zip(answers, expected))
    return {"score": f"{score}/3", "feedback": "Review the questions marked incorrect." if score < 3 else "Excellent work."}


def expert_chat(topic, question):
    if not os.getenv("OPENAI_API_KEY"):
        return {"topic": topic, "answer": "Offline demo: configure OPENAI_API_KEY to call the model.", "question": question}
    from openai import OpenAI
    response = OpenAI().chat.completions.create(model="gpt-4o-mini", messages=[
        {"role": "system", "content": f"You are an expert in {topic}. Answer clearly and mention uncertainty."},
        {"role": "user", "content": question},
    ])
    usage = response.usage.model_dump() if response.usage else {}
    return {"answer": response.choices[0].message.content, "token_usage": usage}


def generate_image(prompt, output_path, model="dall-e-3"):
    if not os.getenv("OPENAI_API_KEY"):
        return {"status": "offline", "message": "Set OPENAI_API_KEY to generate an image.", "prompt": prompt}
    from urllib.request import urlopen
    from openai import OpenAI
    response = OpenAI().images.generate(model=model, prompt=prompt, size="1024x1024", quality="standard", n=1)
    Path(output_path).write_bytes(urlopen(response.data[0].url).read())
    return {"status": "saved", "path": str(output_path), "prompt": prompt}


def generate_style_gallery(topic, output_dir="generated_images"):
    styles = {"photorealistic": "photorealistic", "oil_painting": "oil painting", "pixel_art": "pixel art"}
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    return [generate_image(f"{topic}, {style}", output / f"{topic.replace(' ', '_')}_{name}.png") for name, style in styles.items()]


def generate_logo(company_name, industry, colors, output_path="logo.png"):
    prompt = f"{company_name}, {industry}, colors {colors}, minimalist logo design, vector style, white background"
    return generate_image(prompt, output_path)


def story_with_illustration(theme, output_dir="generated_images"):
    story = expert_chat("creative writing", f"Write a short 100-word story about {theme}.")
    if story.get("answer", "").startswith("Offline demo"):
        return {"story": story["answer"], "image": generate_image(theme, Path(output_dir) / "story.png")}
    return {"story": story["answer"], "image": generate_image(story["answer"], Path(output_dir) / "story.png")}


if __name__ == "__main__":
    print(json.dumps(password_generator(), indent=2))
    print(json.dumps(review_sentiment("The service was fast and helpful"), indent=2))
