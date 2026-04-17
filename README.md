# codeguardian-x
CodeGuardian-X is a multi-agent security reasoning system that detects and simulates cross-file exploit chains across a codebase. It uses adaptive routing to combine fast scanning with deep analysis, producing vulnerability reports, exploit paths, and system-level risk insights.

CodeGuardian-X
System-Level Risk Reasoning Engine for Autonomous Exploit Chain Detection

"Unlike traditional tools that detect isolated vulnerabilities, CodeGuardian-X performs cross-file causal reasoning to simulate real-world exploit paths across an entire codebase."

Show Image
Show Image
Show Image
Show Image

Overview
CodeGuardian-X is an autonomous multi-agent security reasoning system built on NVIDIA Nemotron 3 Super's 1-million-token context window. It ingests an entire GitHub repository in a single pass and performs end-to-end security analysis — without chunking, without losing cross-file context, and without missing multi-hop attack chains.
Traditional static analysis tools flag individual lines in isolation. CodeGuardian-X reasons like an attacker, tracing how a single unsanitized input in one module cascades across the entire system to expose a critical database or bypass authentication. This level of cross-file causal reasoning is only possible because of Nemotron 3 Super's unique architectural capabilities.

Core Capabilities
Cross-File Causal Reasoning
Standard vulnerability scanners report: "This file has a SQL injection."
CodeGuardian-X reports: "This function affects this module, which exposes this API endpoint, which leads to this exploit chain."
The system builds a full dependency graph across the entire codebase and reasons about multi-hop attack paths that no single-file scanner can detect.
Exploit Simulation Engine
For every vulnerability identified, CodeGuardian-X generates a step-by-step exploit scenario:
ATTACK CHAIN DETECTED — CRITICAL

  Step 1: User input at api/routes/auth.py:L47 — unsanitized string
  Step 2: Passed to db/query_builder.py:L112 — no parameterization
  Step 3: SQL injected — auth table queried directly
  Step 4: Admin credentials exposed — privilege escalation achieved
  Step 5: Full database access granted to attacker

  Severity: CRITICAL  |  CVSS Score: 9.8
  Fix Generated: Yes  |  Confidence: 91%
Visual Risk Heatmap
An interactive visualization of the entire codebase risk profile, rendered as a color-coded dependency graph. Safe modules, flagged areas, active vulnerabilities, and critical exploit paths are each represented distinctly, giving reviewers an immediate understanding of system-wide exposure.
Decision Transparency via Super + Nano Routing
Every analysis decision is logged with full transparency:
TaskModelConfidenceRationaleFile-level syntax scanNemotron 3 Nano97%Fast pattern match, low complexityCross-module attack chainNemotron 3 Super91%Multi-hop reasoning requiredExploit simulationNemotron 3 Super88%Causal chain inference neededFix suggestion (known pattern)Nemotron 3 Nano95%Standard patch, no deep reasoning needed

System Architecture
GitHub Repository URL
        |
        v
Repo Ingestion Layer (GitPython + tree-sitter)
        |
        v
+---------------------------+
|     Nemotron 3 Nano       |  -- Fast scan, file-level pattern matching
|     Tag suspicious areas  |  -- Classifies and routes flagged code
+----------+----------------+
           |
           v  (flagged areas passed forward)
+---------------------------+
|     Nemotron 3 Super      |  -- Full 1M token context (entire repo)
|     Cross-file reasoning  |  -- Builds dependency graph
|     Causal chain tracing  |  -- Detects multi-hop attack paths
+----------+----------------+
           |
     +-----+-----+
     |             |
     v             v
Exploit        Dependency
Simulation     Graph +
Engine         Risk Heatmap
     |             |
     +------+------+
            |
            v
  Final Report + Patch Suggestions

Why This Requires Nemotron 3 Super
This project is architecturally dependent on capabilities unique to Nemotron 3 Super:
1M Token Context Window — Entire repositories are ingested in a single pass. No chunking means no lost cross-file relationships, which is the foundation of accurate attack chain detection.
Latent MoE Architecture (4x experts, same compute cost) — Enables deep multi-hop reasoning across hundreds of files without proportional inference cost increases.
Multi-Token Prediction (MTP) — Provides 3x faster generation, critical for real-time exploit simulation output.
Super + Nano Routing Pattern — Intelligent cost optimization: Nano handles fast, simple scans while Super handles causal reasoning tasks. This makes the system economically viable at scale.
Native NVFP4 Pretraining — Memory-efficient deployment on real infrastructure without sacrificing reasoning quality.
No other open model enables this combination of long context, agentic reasoning, and efficient deployment simultaneously.

Tech Stack
ComponentTechnologyCore Reasoning ModelNVIDIA Nemotron 3 Super (120B, 12B active parameters)Fast Routing ModelNVIDIA Nemotron 3 NanoInference EnginevLLM / SGLangAgent OrchestrationLangGraphCode Parsingtree-sitter, GitPythonVisualizationD3.js / PlotlyFrontendStreamlitFine-tuningNVIDIA NeMo (LoRA/SFT on CVE datasets)Production DeploymentNVIDIA TensorRT-LLM

Project Structure
codeguardian-x/
├── agents/
│   ├── nano_scanner.py          # File-level scan agent (Nano)
│   ├── super_reasoner.py        # Cross-file causal agent (Super)
│   └── exploit_simulator.py     # Attack chain simulation
├── core/
│   ├── repo_ingester.py         # GitHub repository loader
│   ├── dependency_graph.py      # Cross-file graph construction
│   └── router.py                # Super + Nano routing logic
├── visualization/
│   ├── risk_heatmap.py          # Codebase risk map renderer
│   └── chain_visualizer.py      # Attack chain graph
├── deployment/
│   ├── vllm_config.yaml         # vLLM deployment configuration
│   └── tensorrt_config.yaml     # TensorRT-LLM configuration
├── app.py                       # Streamlit frontend
└── README.md

Sample Report Output
CODEGUARDIAN-X ANALYSIS REPORT
--------------------------------------------------------------
Repository     : github.com/example/webapp
Files Analyzed : 847 files  |  94,312 lines of code
Context Used   : ~380K tokens (single pass, no chunking)
Analysis Time  : 43 seconds

FINDINGS SUMMARY
  Critical : 3
  High     : 11
  Medium   : 24
  Low      : 41

ATTACK CHAIN #1 — CRITICAL
  Path     : auth.py -> query_builder.py -> admin_panel.py
  Type     : SQL Injection -> Privilege Escalation
  Simulated: Yes
  Fix      : Generated
--------------------------------------------------------------

Roadmap

 Core Super + Nano routing architecture
 Cross-file dependency graph construction
 Exploit simulation engine (in progress)
 Interactive risk heatmap visualization
 LoRA fine-tuning on NVD/CVE dataset via NeMo
 CI/CD GitHub Actions integration
 Multi-language support (Python, JavaScript, Go, Java)


Author
Sarvari Khatoon
B.Tech Student | AI/ML Developer
Presented at NVIDIA Nemotron 3 Super Workshop — IIIT Hyderabad (OSDG x HydPy)

License
MIT License
