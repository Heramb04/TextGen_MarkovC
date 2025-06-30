# app.py
import os, random
from collections import defaultdict
import gradio as gr

# ─── 1) Load & tokenize your corpus ─────────────────────────────────────────
HERE         = os.path.dirname(__file__)
DATA_DIR     = os.path.join(HERE, "training_corpus")
CORPUS_FILE  = os.path.join(DATA_DIR, "corpus_earth_10k.txt")

with open(CORPUS_FILE, "r", encoding="utf-8") as f:
    tokens = f.read().split()

# ─── 2) Build Markov chain (order = 2) ───────────────────────────────────────
k = 2
chain = defaultdict(list)
for i in range(len(tokens) - k):
    state = tuple(tokens[i : i + k])
    chain[state].append(tokens[i + k])

# ─── 3) Generation function ─────────────────────────────────────────────────
def generate_text():
    # pick a random starting state
    state = random.choice(list(chain.keys()))
    output = list(state)

    # generate 200 words total (including the k seed words)
    for _ in range(200 - k):
        nxt_choices = chain.get(state)
        if not nxt_choices:
            # dead end → pick a fresh state
            state = random.choice(list(chain.keys()))
            output.extend(state)
            continue
        nxt = random.choice(nxt_choices)
        output.append(nxt)
        state = tuple(output[-k:])
    return " ".join(output)

# ─── 4) Gradio UI ────────────────────────────────────────────────────────────
with gr.Blocks() as demo:
    gr.Markdown("## Planet Earth Markov Generator")
    output_box = gr.Textbox(label="Generated Text", lines=10)
    gr.Button("Generate").click(fn=generate_text, outputs=output_box)

if __name__ == "__main__":
    demo.launch(share=True)