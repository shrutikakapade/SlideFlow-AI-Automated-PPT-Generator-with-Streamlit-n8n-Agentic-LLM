
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" 
</head>  
        <h1>NEOFLUX AI — Automated PPT Generator</h1>
        <p class="lead">NEOFLUX AI converts a single text prompt into a complete, professional PowerPoint in seconds using Streamlit, Python, python-pptx, n8n, and an Agentic LLM.</p>
      </div>
    </header>
<div
    <section class="card full">
      <h2>Quick Summary</h2>
      <p class="muted">An end-to-end AI automation pipeline: prompt → agentic LLM → python-pptx code → generated .pptx. Built for speed, scale, and clean slide layouts.</p>
      <div style="margin-top:12px">
        <a class="badge">Streamlit</a>
        <a class="badge">python-pptx</a>
        <a class="badge">n8n</a>
        <a class="badge">Agentic LLM</a>
        <a class="badge">Webhooks</a>
      </div>
    </section>
<div
    <div class="grid">
      <div class="card">
        <h3>Key Features</h3>
        <ul>
          <li>One-prompt PPT generation: title, agenda, content, summary slides.</li>
          <li>Agentic LLM generates python-pptx code that follows strict layout rules.</li>
          <li>Streamlit UI for prompt input and file download.</li>
          <li>n8n workflow for orchestration (webhook → LLM → code → response).</li>
          <li>Clean spacing, no overlapping elements, download-ready .pptx.</li>
        </ul>
      </div>
<div
      <aside class="card">
        <h3>Tech Stack</h3>
        <table>
          <tr><th>Component</th><th class="muted">Role</th></tr>
          <tr><td><strong>Streamlit</strong></td><td class="muted">Frontend UI (prompt + download)</td></tr>
          <tr><td><strong>Python</strong></td><td class="muted">Backend logic & execution</td></tr>
          <tr><td><strong>python-pptx</strong></td><td class="muted">Programmatic slide creation</td></tr>
          <tr><td><strong>n8n</strong></td><td class="muted">Workflow orchestration & webhooks</td></tr>
          <tr><td><strong>Agentic LLM</strong></td><td class="muted">Autonomous content planning & code gen</td></tr>
        </table>
      </aside>
<div
      <div class="card full">
        <h3>System Architecture</h3>
        <pre class="mono">
User (Streamlit)
      │
      ▼
  Webhook (n8n)
      │
      ▼
  Agentic LLM (code generator)
      │
      ▼
python-pptx script → generated_presentation.pptx
      │
      └─ Respond to Webhook → Streamlit (download)
        </pre>
<div
        <p class="muted">The workflow exported from n8n implements this chain: Webhook → Google Gemini (LLM) → Agent Node (python-pptx code) → Respond. See workflow JSON included with the repo for exact node configuration. 


        

        

<img width="1154" height="525" alt="Screenshot 2025-12-01 163937" src="https://github.com/user-attachments/assets/731dd284-19a2-4e43-8dea-97600f5b2585" />



  


  
<div
      <div class="card">
        <h3>Installation</h3>
        <ol>
          <li>Clone the repo: <span class="mono">git clone &lt;repo-url&gt;</span></li>
          <li>Install dependencies: <span class="mono">pip install -r requirements.txt</span></li>
          <li>Import & activate n8n workflow from <span class="mono">n8n_workflow/streamlitai-workflow.json</span></li>
          <li>Update webhook URL in <span class="mono">streamlit_app/app.py</span></li>
          <li>Run app: <span class="mono">streamlit run streamlit_app/app.py</span></li>
        </ol>
      </div>
<div
      <div class="card">
        <h3>Usage</h3>
        <ol>
          <li>Open Streamlit app in your browser.</li>
          <li>Enter a prompt or topic and click <em>Generate Presentation</em>.</li>
          <li>Wait for the pipeline to run; download the generated <span class="mono">generated_presentation.pptx</span>.</li>
        </ol>
      </div>
<div
      <div class="card full">
        <h3>n8n Workflow (details)</h3>
        <p class="muted">The included n8n JSON defines the automation nodes and rules used by NEOFLUX AI. Key nodes from the exported workflow:</p>
        <ul>
          <li><strong>Webhook</strong> — receives the Streamlit POST with the user prompt.</li>
          <li><strong>Google Gemini Chat Model</strong> — optional LLM node used as a language model backend.</li>
          <li><strong>AI Agent</strong> — agentic node that generates python-pptx code following strict rules (title/content slides, bullet formatting, no overlap, final line saves as <code>generated_presentation.pptx</code>).</li>
          <li><strong>Respond to Webhook</strong> — returns the generated file/code to Streamlit for download.</li>
        </ul>
        <p class="muted">Reference: exported n8n workflow JSON (included in this repo). :contentReference[oaicite:1]{index=1}</p>
      </div>
<div
      <div class="card">
        <h3>Recommended Repo Layout</h3>
        <pre class="mono">
NEOFLUX AI/
├─ streamlit_app/
│  └─ app.py
├─ n8n_workflow/
│  └─ streamlitai-workflow.json
├─ generated_ppts/
├─ requirements.txt
└─ README.html
        </pre>
      </div>
<div
      <div class="card">
        <h3>Output</h3>
        <p class="muted">Generated presentations include:</p>
        <ul>
          <li>Title slide</li>
          <li>Agenda / outline</li>
          <li>Multiple content slides with bullets & sub-bullets</li>
          <li>Summary / closing slide</li>
        </ul>
      </div>
<div
    </div>
<div
    <section class="card full">
      <h3>Contributing</h3>
<div
    <footer>
      <div class="muted">Made with Streamlit, python-pptx, n8n & Agentic LLM — NEOFLUX AI</div>
    </footer>
  </div>

  

https://github.com/user-attachments/assets/0cda8435-5dc5-4bd8-8ee7-d49feae6c323



  ## 🚀 Why NEOFLUX AI?

**NEOFLUX AI** represents new intelligence in continuous motion.

- **Neo** stands for next-generation artificial intelligence.
- **Flux** represents the seamless flow from ideas to execution.

The name reflects how NEOFLUX AI continuously transforms user intent into structured, high-quality presentations using agentic AI workflows.

</body>
</html>
