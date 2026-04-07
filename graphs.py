import matplotlib.pyplot as plt
import tempfile
import os
import uuid  #helps generate temporary random ids for storing graphs with unique names randomly and save them

def create_graphs(chunk_lengths, retrieved_len, summary_len, stage_times):
    temp_dir = tempfile.gettempdir()
    uid = str(uuid.uuid4())

    # Graph 1
    plt.figure()
    plt.bar(stage_times.keys(), stage_times.values())
    plt.title("Pipeline Stage Execution Time")
    g1 = os.path.join(temp_dir, f"g1_{uid}.png")
    plt.savefig(g1)
    plt.close()

    # Graph 2
    plt.figure()
    plt.hist(chunk_lengths, bins=20)
    plt.title("Chunk Length Distribution")
    g2 = os.path.join(temp_dir, f"g2_{uid}.png")
    plt.savefig(g2)
    plt.close()

    # Graph 3
    plt.figure()
    plt.bar(["Retrieved", "Summary"], [retrieved_len, summary_len])
    plt.title("Retrieved vs Summary Length")
    g3 = os.path.join(temp_dir, f"g3_{uid}.png")
    plt.savefig(g3)
    plt.close()

    return g1, g2, g3