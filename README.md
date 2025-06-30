# 🌍 Planet Earth Markov Text Generator

This project is the third task from my Prodigy InfoTech Generative AI internship. It demonstrates a simple but effective text generation approach using **Markov chains**, trained on a custom 10,000-word corpus about Earth (fetched from Wikipedia).

The app generates Earth-themed prose based on probabilistic state transitions using a 2-gram (order=2) model, and is deployed live as a Hugging Face Space using **Gradio**.

---

## 🚀 Live Demo

Check it out here 👉 [Hugging Face Space](https://huggingface.co/spaces/heramb04/Markov-Earth)  
_Just click **Generate** to produce fresh, random Earth-text every time!_

---


---

## ⚙️ How It Works

1. **Text Corpus**: A 10k-word dataset on planet Earth, generated via a local Python script.
2. **Markov Chain**: The model builds a `dict[state] = [possible_next_words]` mapping.
3. **Generation**: Starting from a random 2-word seed, it generates 200-word output sequences.
4. **No Deep Learning**: Just statistics, randomness, and cool old-school NLP!

---

## 🧪 Running Locally

Clone the repo and run the app:

```bash
git clone https://github.com/your-username/PRODIGY_GA_3.git
cd PRODIGY_GA_3
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python app.py
