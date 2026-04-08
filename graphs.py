#uuid helps generate temporary random ids for storing graphs with unique names randomly and save them
import matplotlib.pyplot as plt
import tempfile
import os
import uuid

def create_graphs(chunk_lengths, retrieved_len, summary_len, stage_times):
    temp_dir = tempfile.gettempdir()
    uid = str(uuid.uuid4())

    # Graph 1: Pipeline stage execution time
    plt.figure(figsize=(8, 5))
    plt.bar(stage_times.keys(), stage_times.values())
    plt.xticks(rotation=30)
    plt.title("Pipeline Stage Execution Time", fontsize=14)
    plt.xlabel("Pipeline Stage")
    plt.ylabel("Time (seconds)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    g1 = os.path.join(temp_dir, f"g1_{uid}.png")
    plt.savefig(g1)
    plt.close()

    # Graph 2: Chunk length distribution
    plt.figure(figsize=(8, 5))
    plt.hist(chunk_lengths, bins=20)
    plt.title("Chunk Length Distribution", fontsize=14)
    plt.xlabel("Chunk Length (words)")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    g2 = os.path.join(temp_dir, f"g2_{uid}.png")
    plt.savefig(g2)
    plt.close()

    # Graph 3: Retrieved vs summary length
    plt.figure(figsize=(6, 5))
    plt.bar(["Retrieved Text", "Summary"], [retrieved_len, summary_len])
    plt.title("Retrieved vs Summary Length", fontsize=14)
    plt.xlabel("Text Type")
    plt.ylabel("Word Count")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    g3 = os.path.join(temp_dir, f"g3_{uid}.png")
    plt.savefig(g3)
    plt.close()

    return g1, g2, g3
