import gradio as gr
import joblib
import numpy as np

# Load your model (use correct file name)
model = joblib.load("Linear_SVM_model.sav")

def predict(packet_count, byte_count, duration, src_port, dst_port, protocol):
    # Convert inputs to array
    features = np.array([[packet_count, byte_count, duration, src_port, dst_port, protocol]])
    pred = model.predict(features)[0]

    if pred == 1:
        return "🚨 Malicious Traffic Detected"
    else:
        return "✅ Normal Traffic"

inputs = [
    gr.Number(label="Packet Count"),
    gr.Number(label="Byte Count"),
    gr.Number(label="Duration (sec)"),
    gr.Number(label="Source Port"),
    gr.Number(label="Destination Port"),
    gr.Number(label="Protocol (TCP=6, UDP=17)")
]

app = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs="text",
    title="Cloud Shield – Threat Detection",
    description="Enter network parameters to detect malicious traffic."
)

app.launch()
