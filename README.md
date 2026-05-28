# Awesome Multimodal Deep Research

> A curated list of papers, benchmarks, and methods for **Multimodal Deep Research**: agents that *search, browse, and reason* over both text and visual information to answer open-ended, knowledge-intensive questions.

If you find this list helpful, please give it a ⭐ and **join us in maintaining it**. This is a community effort, and contributions of any size are very welcome.

## How to Contribute

We want this to be the most complete, up-to-date map of multimodal deep research, and we can't do it alone. Found a paper that's missing? A broken link? A TL;DR you'd phrase better? Please jump in.

### Ways to contribute

- **Quick (no setup):** open an [issue](../../issues) with the arXiv link (and code repo, if any). A maintainer will add it.
- **Direct:** open a Pull Request adding your entry under the right section, following the format below.

### Entry format

Every entry keeps a one-line **TL;DR** visible by default and folds the full abstract. Entries not yet filled in show `_pending_` and are backfilled over time.

````markdown
#### [Paper Title](https://arxiv.org/abs/XXXX.XXXXX)
`Affiliation` · `Venue` · YYYY-MM · Base: `Model` · [PDF](...) · [Code](...) [![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=social)](...)

> **TL;DR.** One short, crisp sentence.

<details><summary>Abstract</summary>

The full paper abstract.
</details>
````

### Generate an entry automatically

Don't hand-write the boilerplate. [`fetch_arxiv.py`](fetch_arxiv.py) (arXiv-first, stdlib-only, no dependencies) builds the entry for you:

```bash
# 1) Preview without writing (recommended first step):
python3 fetch_arxiv.py --id 2409.12959 --section "(Multi-)Image + Text" --dry-run

# 2) Insert it. Add the metadata arXiv can't give and a hand-written TL;DR:
python3 fetch_arxiv.py --id 2409.12959 --section "(Multi-)Image + Text" \
    --affiliation "CUHK MMLab" --venue "ICLR 2025" --base "GPT-4o" \
    --code https://github.com/owner/repo --tldr "One crisp sentence."

# You can also resolve a paper by URL or by title search:
python3 fetch_arxiv.py --url https://arxiv.org/abs/2409.12959 --section "(Multi-)Image + Text"
python3 fetch_arxiv.py --title "MMSearch: Benchmarking ..." --section "(Multi-)Image + Text"
```

### Conventions

- **arXiv-first.** The script uses the Atom API and falls back to the more lenient HTML abstract page on a `429` rate limit. It never retries a `429` (that only extends the ban).
- **No auto-push.** The script only edits `README.md` — review the diff and commit yourself, then open a PR.
- **Affiliation / venue** are rarely available from arXiv. If you don't have them, leave them out (no placeholder); add them later when you do.
- **TL;DR** should be a single short sentence. The script's auto first-sentence fallback is flagged with `<!-- TLDR: refine -->` so you can rewrite it into something crisp.
- **Stars.** For entries with code, include a `![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=social)` badge (the script adds it automatically when `--code` is a GitHub URL). It updates on its own.

## Contents

- [Data and Benchmark](#data-and-benchmark) — Training Data; Benchmarks (Text / (Multi-)Image + Text / Video + Text)
- [Models & Methods](#models--methods) — Text; Multimodal; Proprietary Models; Open Data Synthesis; Generation; Perception; Misc
- [Survey](#survey)

## Data and Benchmark

### Training Data

#### InfoSeek

> **TL;DR.** _pending._

#### Encyclopedic VQA: Visual Questions About Detailed Properties of Fine-grained Categories
`ICCV 2023`

> **TL;DR.** _pending._

#### OK-VQA & A-OKVQA

> **TL;DR.** _pending._

#### FVQA
`ACL 2026` · `from MM-Search-R1`

> **TL;DR.** _pending._

### Benchmarks: Text

#### [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516)
`OpenAI` · 2025-04 · [PDF](https://arxiv.org/pdf/2504.12516) · [Code](https://github.com/openai/simple-evals) [![Stars](https://img.shields.io/github/stars/openai/simple-evals?style=social)](https://github.com/openai/simple-evals)

> **TL;DR.** 1,266 hard-to-find-information questions testing an agent's web-browsing persistence, with short, easily verifiable answers (text-only).

<details><summary>Abstract</summary>

We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. BrowseComp comprises 1,266 questions that require persistently navigating the internet in search of hard-to-find, entangled information. Despite the difficulty of the questions, BrowseComp is simple and easy-to-use, as predicted answers are short and easily verifiable against reference answers. BrowseComp for browsing agents can be seen as analogous to how programming competitions are an incomplete but useful benchmark for coding agents. While BrowseComp sidesteps challenges of a true user query distribution, like generating long answers or resolving ambiguity, it measures the important core capability of exercising persistence and creativity in finding information. BrowseComp can be found at https://github.com/openai/simple-evals.

</details>

#### [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/abs/2508.06600)
2025-08 · [PDF](https://arxiv.org/pdf/2508.06600)

> **TL;DR.** A reproducible BrowseComp variant over a fixed, curated corpus with human-verified supporting documents and mined hard negatives, disentangling deep-research LLMs from their retrievers.

<details><summary>Abstract</summary>

Deep-Research agents, which integrate large language models (LLMs) with search tools, have shown success in improving the effectiveness of handling complex queries that require iterative search planning and reasoning over search results. Evaluations on current benchmarks like BrowseComp relies on black-box live web search APIs, have notable limitations in (1) fairness: dynamic and opaque web APIs hinder fair comparisons and reproducibility of deep research methods; (2) transparency: lack of control over the document corpus makes it difficult to isolate retriever contributions. In other words, the current evaluations may compare a complete deep research system at a given time, but they do not foster well-controlled experiments to provide insights into the capability of underlying deep research LLMs. To address these challenges, we introduce BrowseComp-Plus, a benchmark derived from BrowseComp, employing a fixed, carefully curated corpus. Each query in BrowseComp-Plus includes human-verified supporting documents and mined challenging negatives, enabling controlled experimentation. The benchmark is shown to be effective in distinguishing the performance of deep research systems. For instance, the open-source model Search-R1, when paired with the BM25 retriever, achieves 3.86% accuracy, whereas the GPT-5 achieves 55.9%. Integrating the GPT-5 with the Qwen3-Embedding-8B retriever further enhances its accuracy to 70.1% with fewer search calls. This benchmark allows comprehensive evaluation and disentangled analysis of deep research agents and retrieval methods, fostering insights into retrieval effectiveness, citation accuracy, and context engineering in Deep-Research system.

</details>

#### BrowseComp-ZH

> **TL;DR.** _pending._

#### [BrowseComp-V3: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2602.12876)
2026-02 · [PDF](https://arxiv.org/pdf/2602.12876)

> **TL;DR.** A 300-question multimodal browsing benchmark with cross-modal multi-hop reasoning over publicly searchable evidence and subgoal-level process evaluation; introduces the OmniSeeker agent (SOTA models reach only 36%).

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs), equipped with increasingly advanced planning and tool-use capabilities, are evolving into autonomous agents capable of performing multimodal web browsing and deep search in open-world environments. However, existing benchmarks for multimodal browsing remain limited in task complexity, evidence accessibility, and evaluation granularity, hindering comprehensive and reproducible assessments of deep search capabilities. To address these limitations, we introduce BrowseComp-$V^3$, a novel benchmark consisting of 300 carefully curated and challenging questions spanning diverse domains. The benchmark emphasizes deep, multi-level, and cross-modal multi-hop reasoning, where critical evidence is interleaved across textual and visual modalities within and across web pages. All supporting evidence is strictly required to be publicly searchable, ensuring fairness and reproducibility. Beyond final-answer accuracy, we incorporate an expert-validated, subgoal-driven process evaluation mechanism that enables fine-grained analysis of intermediate reasoning behaviors and systematic characterization of capability boundaries. In addition, we propose OmniSeeker, a unified multimodal browsing agent framework integrating diverse web search and visual perception tools. Comprehensive experiments demonstrate that even state-of-the-art models achieve only 36% accuracy on our benchmark, revealing critical bottlenecks in multimodal information integration and fine-grained perception. Our results highlight a fundamental gap between current model capabilities and robust multimodal deep search in real-world settings.

</details>

#### xbench: Tracking Agents Productivity Scaling with Profession-Aligned Real-World Evaluations

> **TL;DR.** _pending._

#### DeepSearch QA

> **TL;DR.** _pending._

#### DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation

> **TL;DR.** _pending._

#### GAIA2
`Meta`

> **TL;DR.** _pending._

#### GAIA
`Meta`

> **TL;DR.** _pending._

#### DeepResearch Bench

> **TL;DR.** _pending._

#### WebWalkerQA

> **TL;DR.** _pending._

### Benchmarks: (Multi-)Image + Text

#### LiveVQA
`HUST` · `UW`

> **TL;DR.** Tests model performance using knowledge from after the training cutoff date.

#### [SimpleVQA: Multimodal Factuality Evaluation for Multimodal Large Language Models](https://arxiv.org/abs/2502.13059)
`MAP` · 2025-02 · [PDF](https://arxiv.org/pdf/2502.13059)

> **TL;DR.** The first multimodal factuality benchmark for short-answer VQA, scored by LLM-as-judge across 9 tasks and 9 topics, evaluating 18 MLLMs and 8 text-only LLMs.

<details><summary>Abstract</summary>

The increasing application of multi-modal large language models (MLLMs) across various sectors have spotlighted the essence of their output reliability and accuracy, particularly their ability to produce content grounded in factual information (e.g. common and domain-specific knowledge). In this work, we introduce SimpleVQA, the first comprehensive multi-modal benchmark to evaluate the factuality ability of MLLMs to answer natural language short questions. SimpleVQA is characterized by six key features: it covers multiple tasks and multiple scenarios, ensures high quality and challenging queries, maintains static and timeless reference answers, and is straightforward to evaluate. Our approach involves categorizing visual question-answering items into 9 different tasks around objective events or common knowledge and situating these within 9 topics. Rigorous quality control processes are implemented to guarantee high-quality, concise, and clear answers, facilitating evaluation with minimal variance via an LLM-as-a-judge scoring system. Using SimpleVQA, we perform a comprehensive assessment of leading 18 MLLMs and 8 text-only LLMs, delving into their image comprehension and text generation abilities by identifying and analyzing error cases.

</details>

#### [MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines](https://arxiv.org/abs/2409.12959)
`MMLab` · `ICLR 2025` · 2024-09 · [PDF](https://arxiv.org/pdf/2409.12959)

> **TL;DR.** Benchmark plus pipeline (MMSearch-Engine) testing whether large multimodal models can serve as end-to-end multimodal search engines (300 instances, 14 subfields).

<details><summary>Abstract</summary>

The advent of Large Language Models (LLMs) has paved the way for AI search engines, e.g., SearchGPT, showcasing a new paradigm in human-internet interaction. However, most current AI search engines are limited to text-only settings, neglecting the multimodal user queries and the text-image interleaved nature of website information. Recently, Large Multimodal Models (LMMs) have made impressive strides. Yet, whether they can function as AI search engines remains under-explored, leaving the potential of LMMs in multimodal search an open question. To this end, we first design a delicate pipeline, MMSearch-Engine, to empower any LMMs with multimodal search capabilities. On top of this, we introduce MMSearch, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs. The curated dataset contains 300 manually collected instances spanning 14 subfields, which involves no overlap with the current LMMs' training data, ensuring the correct answer can only be obtained within searching. By using MMSearch-Engine, the LMMs are evaluated by performing three individual tasks (requery, rerank, and summarization), and one challenging end-to-end task with a complete searching process. We conduct extensive experiments on closed-source and open-source LMMs. Among all tested models, GPT-4o with MMSearch-Engine achieves the best results, which surpasses the commercial product, Perplexity Pro, in the end-to-end task, demonstrating the effectiveness of our proposed pipeline. We further present error analysis to unveil current LMMs still struggle to fully grasp the multimodal search tasks, and conduct ablation study to indicate the potential of scaling test-time computation for AI search engine. We hope MMSearch may provide unique insights to guide the future development of multimodal AI search engine. Project Page: https://mmsearch.github.io

</details>

#### MMSearch-Plus (MSP)
`HKU` · `ICLR 2026` · Multi-Image Input

> **TL;DR.** _pending._

#### HLE (Humanity's Last Exam)
`Nature`

> **TL;DR.** _pending._

#### RealX-Bench
`ICLR 2026` · `from DeepEyesV2`

> **TL;DR.** _pending._

#### VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents
`Ant`

> **TL;DR.** _pending._

#### MM-DR-Bench
`OSU & Amazon`

> **TL;DR.** _pending._

#### MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains
`ICLR 2026 Oral`

> **TL;DR.** _pending._

#### InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search

> **TL;DR.** _pending._

#### HyperEyes (IMEB Benchmark)

> **TL;DR.** _Benchmark introduced by the HyperEyes method (see Models & Methods); no open-source release yet (2026-05-11)._

#### [From Web to Pixels: Bringing Agentic Search into Visual Perception](https://arxiv.org/abs/2605.12497)
2026-05 · [PDF](https://arxiv.org/pdf/2605.12497)

> **TL;DR.** Formalizes Perception Deep Research (resolving a target's identity from external facts before localizing it) with the WebEye benchmark and the Pixel-Searcher search-to-pixel agent.

<details><summary>Abstract</summary>

Visual perception connects high-level semantic understanding to pixel-level perception, but most existing settings assume that the decisive evidence for identifying a target is already in the image or frozen model knowledge. We study a more practical yet harder open-world case where a visible object must first be resolved from external facts, recent events, long-tail entities, or multi-hop relations before it can be localized. We formalize this challenge as Perception Deep Research and introduce WebEye, an object-anchored benchmark with verifiable evidence, knowledge-intensive queries, precise box/mask annotations, and three task views: Search-based Grounding, Search-based Segmentation, and Search-based VQA. WebEyes contains 120 images, 473 annotated object instances, 645 unique QA pairs, and 1,927 task samples. We further propose Pixel-Searcher, an agentic search-to-pixel workflow that resolves hidden target identities and binds them to boxes, masks, or grounded answers. Experiments show that Pixel-Searcher achieves the strongest open-source performance across all three task views, while failures mainly arise from evidence acquisition, identity resolution, and visual instance binding.

</details>

<!-- The three entries below were in the original README but are not in the latest source list; kept pending confirmation. -->

#### VDR-Bench
`MMLab`

> **TL;DR.** _pending._

#### BC-VL (BrowseComp-VL)
`Alibaba`

> **TL;DR.** _Introduced by WebWatcher (see Models & Methods); confirm whether it has a standalone paper._

#### MM-BrowseComp
`Seed`

> **TL;DR.** _pending._

### Benchmarks: Video + Text

#### Video BrowseComp

> **TL;DR.** _pending._

### Benchmarks: TBD

#### DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation
`HF Daily Paper`

> **TL;DR.** _pending._

#### AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery

> **TL;DR.** _pending._

#### Agent-MME

> **TL;DR.** _pending._

#### [VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild](https://arxiv.org/abs/2605.27882)
2026-05 · [PDF](https://arxiv.org/pdf/2605.27882)

> **TL;DR.** A bilingual 200-task benchmark for multi-turn "vibe search" where agents must proactively refine vague user intent, scored against schema-free ground-truth knowledge graphs.

<details><summary>Abstract</summary>

LLM-based agents score well on search benchmarks, yet real users consistently find results unsatisfying, revealing a persistent evaluation-experience gap. We attribute this gap to existing benchmarks' reliance on over-specified queries, single-turn interactions, and fixed-schema evaluation, none of which reflect real search behavior where users and agents collaboratively refine vague intent through multi-turn dialogue. We term this paradigm VibeSearch and introduce VibeSearchBench, a benchmark comprising 200 manually curated bilingual (Chinese and English) tasks across 20 domains, split into VibeSearch-Pro (professional) and VibeSearch-Daily (daily-life) subsets. Each task pairs a user persona with a schema-free ground-truth knowledge graph, and is evaluated through a progressive-disclosure user simulator and a graph-matching evaluation framework. We benchmark seven frontier models under both the ReAct framework and the OpenClaw agent harness. Results show that all models remain substantially inadequate for VibeSearch (best F1: 30.30), highlighting the need for fundamental advances in long-context reasoning, proactive intent elicitation, and structured knowledge construction.

</details>

#### [LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?](https://arxiv.org/abs/2605.28721)
2026-05 · [PDF](https://arxiv.org/pdf/2605.28721)

> **TL;DR.** Shows search agents often answer from intrinsic memory rather than retrieval, and introduces a 335-question benchmark whose answers depend on facts published within the prior 90 days.

<details><summary>Abstract</summary>

Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines when answer-supporting evidence is removed. These results suggest that static search benchmarks can reward memory-backed verification rather than evidence-driven discovery, conflating what agents already know with what they can find. We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage. It contains 335 human-authored questions whose answers depend on facts published within the 90 days preceding benchmark construction, drawn from six updated sources and filtered to exclude globally salient events. On LiveBrowseComp, all evaluated agents fall below 2% closed-book accuracy, search-augmented scores drop by 25-40 points relative to BrowseComp, and prior model rankings no longer reliably predict performance. LiveBrowseComp is available at https://huggingface.co/datasets/Forival/LiveBrowseComp.

</details>

#### [AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661)
2026-05 · [PDF](https://arxiv.org/pdf/2605.18661)

> **TL;DR.** An end-to-end survey/roadmap of AI across the research lifecycle (Creation, Writing, Validation, Dissemination), mapping where AI is reliable assistance versus unreliable autonomy.

<details><summary>Abstract</summary>

AI-assisted research is crossing a threshold: fully automated systems can now generate research papers for as little as $15, while long-horizon agents can execute experiments, draft manuscripts, and simulate critique with minimal human input. Yet this productivity frontier exposes a deeper integrity problem: under scientific pressure, even frontier LLMs still fabricate results, miss hidden errors, and fail to judge novelty reliably. Studying developments through April 2026, we present an end-to-end analysis of AI across the complete research lifecycle, organized into four epistemological phases: Creation (idea generation, literature review, coding & experiments, tables & figures), Writing (paper writing), Validation (peer review, rebuttal & revision), and Dissemination (posters, slides, videos, social media, project pages, and interactive agents). We identify a sharp, stage-dependent boundary between reliable assistance and unreliable autonomy: AI excels at structured, retrieval-grounded, and tool-mediated tasks, but remains fragile for genuinely novel ideas, research-level experiments, and scientific judgment. Generated ideas often degrade after implementation, research code lags far behind pattern-matching benchmarks, and end-to-end autonomous systems have not yet consistently reached major-venue acceptance standards. We further show that greater automation can obscure rather than eliminate failure modes, making human-governed collaboration the most credible deployment paradigm. Finally, we provide a structured taxonomy, benchmark suite, and tool inventory, cross-stage design principles, and a practitioner-oriented playbook, with resources maintained at our project page.

</details>

## Models & Methods

### Methods: Text

#### [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516)
`COLM 2025 Oral` · 2025-03 · [PDF](https://arxiv.org/pdf/2503.09516)

> **TL;DR.** An RL framework where an LLM learns to autonomously issue multi-turn search queries during step-by-step reasoning (with retrieved-token masking and outcome-based rewards), improving QA by 20-41% over RAG baselines.

<details><summary>Abstract</summary>

Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact optimally with the search engine. This paper introduces Search-R1, an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval. Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions, leveraging retrieved token masking for stable RL training and a simple outcome-based reward function. Experiments on seven question-answering datasets show that Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines under the same setting. This paper further provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning. The code and model checkpoints are available at this https URL.

</details>

#### Dr. Tulu

> **TL;DR.** _pending._

#### [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)
[Code](https://github.com/TIGER-AI-Lab/OpenResearcher) [![Stars](https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=social)](https://github.com/TIGER-AI-Lab/OpenResearcher)

> **TL;DR.** Data-synthesis pipeline; SFT + distillation only, with GPT-OSS as the teacher.

#### [WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization](https://arxiv.org/abs/2507.15061)
2025-07 · [PDF](https://arxiv.org/pdf/2507.15061)

> **TL;DR.** A formalization-driven information-seeking data synthesis framework that uses set-theoretic Knowledge Projections to control reasoning structure; SOTA among open IS agents on GAIA and WebWalkerQA.

<details><summary>Abstract</summary>

The advent of Large Language Model (LLM)-powered agents has revolutionized artificial intelligence by enabling solutions to complex, open-ended tasks through web-based information-seeking (IS) capabilities. The scarcity of high-quality training data has limited the development of IS agents. Existing approaches typically adopt an information-driven paradigm that first collects web data and then generates questions based on the retrieval. However, this may lead to inconsistency between information structure and reasoning structure, question and answer. To mitigate, we propose a formalization-driven IS data synthesis framework WebShaper to construct a dataset. WebShaper systematically formalizes IS tasks through set theory. Central to the formalization is the concept of Knowledge Projections (KP), which enables precise control over reasoning structure by KP operation compositions. During synthesis, we begin by creating seed tasks, then use a multi-step expansion process. At each step, an agentic Expander expands the current formal question more complex with retrieval and validation tools based on our formalization. We train our model on the synthesized dataset. Experiment results demonstrate that WebShaper achieves state-of-the-art performance among open-sourced IS agents on GAIA and WebWalkerQA benchmarks.

</details>

#### [WebSailor: Navigating Super-human Reasoning for Web Agent](https://arxiv.org/abs/2507.02592)
2025-07 · [PDF](https://arxiv.org/pdf/2507.02592)

> **TL;DR.** A post-training pipeline (high-uncertainty task synthesis, RFT cold start, and DUPO agentic RL) that gives open-source web agents the uncertainty-reduction reasoning of proprietary deep-research systems, closing the gap on BrowseComp.

<details><summary>Abstract</summary>

Transcending human cognitive limitations represents a critical frontier in LLM training. Proprietary agentic systems like DeepResearch have demonstrated superhuman capabilities on extremely complex information-seeking benchmarks such as BrowseComp, a feat previously unattainable. We posit that their success hinges on a sophisticated reasoning pattern absent in open-source models: the ability to systematically reduce extreme uncertainty when navigating vast information landscapes. Based on this insight, we introduce WebSailor, a complete post-training methodology designed to instill this crucial capability. Our approach involves generating novel, high-uncertainty tasks through structured sampling and information obfuscation, RFT cold start, and an efficient agentic RL training algorithm, Duplicating Sampling Policy Optimization (DUPO). With this integrated pipeline, WebSailor significantly outperforms all opensource agents in complex information-seeking tasks, matching proprietary agents' performance and closing the capability gap.

</details>

#### [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
2025-05 · [PDF](https://arxiv.org/pdf/2505.22648)

> **TL;DR.** An end-to-end recipe for ReAct-style information-seeking agents (browsing-data construction, trajectory sampling, SFT cold start, RL); strong on GAIA and WebWalkerQA.

<details><summary>Abstract</summary>

Addressing intricate real-world problems necessitates in-depth information seeking and multi-step reasoning. Recent progress in agentic systems, exemplified by Deep Research, underscores the potential for autonomous multi-step research. In this work, we present a cohesive paradigm for building end-to-end agentic information seeking agents from a data-centric and training-stage perspective. Our approach consists of four key stages: (1) browsing data construction, (2) trajectories sampling, (3) supervised fine-tuning for effective cold start, and (4) reinforcement learning for enhanced generalisation. We instantiate this framework in a web agent based on the ReAct, WebDancer. Empirical evaluations on the challenging information seeking benchmarks, GAIA and WebWalkerQA, demonstrate the strong performance of WebDancer, achieving considerable results and highlighting the efficacy of our training paradigm. Further analysis of agent training provides valuable insights and actionable, systematic pathways for developing more capable agentic models. The codes and demo will be released in this https URL.

</details>

#### [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/abs/2504.21776)
2025-04 · [PDF](https://arxiv.org/pdf/2504.21776)

> **TL;DR.** A deep-research agent that lets large reasoning models autonomously search, navigate, and draft reports mid-reasoning (Deep Web Explorer + Think-Search-and-Draft), trained with iterative online DPO.

<details><summary>Abstract</summary>

Large reasoning models (LRMs), such as OpenAI-o1 and DeepSeek-R1, demonstrate impressive long-horizon reasoning capabilities. However, their reliance on static internal knowledge limits their performance on complex, knowledge-intensive tasks and hinders their ability to produce comprehensive research reports requiring synthesis of diverse web information. To address this, we propose WebThinker, a deep research agent that empowers LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process. WebThinker integrates a Deep Web Explorer module, enabling LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps. It also employs an Autonomous Think-Search-and-Draft strategy, allowing the model to seamlessly interleave reasoning, information gathering, and report writing in real time. To further enhance research tool utilization, we introduce an RL-based training strategy via iterative online Direct Preference Optimization (DPO). Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate that WebThinker significantly outperforms existing methods and strong proprietary systems. Our approach enhances LRM reliability and applicability in complex scenarios, paving the way for more capable and versatile deep research systems. The code is available at this https URL.

</details>

#### DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data
`HF Daily Paper`

> **TL;DR.** _pending._

### Methods: Multimodal

#### [MMSearch-R1: Incentivizing LMMs to Search](https://arxiv.org/abs/2506.20670)
`ACL 2026` · 2025-06 · [PDF](https://arxiv.org/pdf/2506.20670)

> **TL;DR.** The first end-to-end RL framework for on-demand multi-turn multimodal search (image + text tools) with a search-penalty reward; matches a larger RAG model while cutting search calls by 30%+.

<details><summary>Abstract</summary>

Robust deployment of large multimodal models (LMMs) in real-world scenarios requires access to external knowledge sources, given the complexity and dynamic nature of real-world information. Existing approaches such as retrieval-augmented generation (RAG) and prompt engineered search agents rely on rigid pipelines, often leading to inefficient or excessive search behaviors. We present MMSearch-R1, the first end-to-end reinforcement learning framework that enables LMMs to perform on-demand, multi-turn search in real-world Internet environments. Our framework integrates both image and text search tools, allowing the model to reason about when and how to invoke them guided by an outcome-based reward with a search penalty. To support training, We collect a multimodal search VQA dataset through a semi-automated pipeline that covers diverse visual and textual knowledge needs and curate a search-balanced subset with both search-required and search-free samples, which proves essential for shaping efficient and on-demand search behavior. Extensive experiments on knowledge-intensive and info-seeking VQA tasks show that our model not only outperforms RAG-based baselines of the same model size, but also matches the performance of a larger RAG-based model while reducing search calls by over 30%. We further analyze key empirical findings to offer actionable insights for advancing research in multimodal search.

</details>

#### Deep-MM-Search-R1
`arXiv 2510`

> **TL;DR.** _pending._

#### DeepEyesV2: Toward Agentic Multimodal Model
`ICLR 2026 Poster` · `HF Daily Paper` · [Code](https://github.com/Visual-Agent)

> **TL;DR.** _pending._

#### Tongyi DR
`Alibaba` · Base: `Qwen2.5`

> **TL;DR.** _pending._

#### OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

> **TL;DR.** _pending._

#### Vision-DeepResearch
`MMLab` · Base: `Qwen3-VL` · rllm + VeRL

> **TL;DR.** _pending._

#### [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/abs/2508.05748)
`Alibaba` · `ICLR 2026` · 2025-08 · Base: `Qwen2.5-VL` · LLaMA-Factory + VeRL · [PDF](https://arxiv.org/pdf/2508.05748)

> **TL;DR.** A vision-language deep-research agent (synthetic-trajectory cold start plus RL) that also introduces the BrowseComp-VL benchmark.

<details><summary>Abstract</summary>

Web agents such as Deep Research have demonstrated superhuman cognitive abilities, capable of solving highly challenging information-seeking problems. However, most research remains primarily text-centric, overlooking visual information in the real world. This makes multimodal Deep Research highly challenging, as such agents require much stronger reasoning abilities in perception, logic, knowledge, and the use of more sophisticated tools compared to text-based agents. To address this limitation, we introduce WebWatcher, a multi-modal Agent for Deep Research equipped with enhanced visual-language reasoning capabilities. It leverages high-quality synthetic multimodal trajectories for efficient cold start training, utilizes various tools for deep reasoning, and further enhances generalization through reinforcement learning. To better evaluate the capabilities of multimodal agents, we propose BrowseComp-VL, a benchmark with BrowseComp-style that requires complex information retrieval involving both visual and textual information. Experimental results show that WebWatcher significantly outperforms proprietary baseline, RAG workflow and open-source agents in four challenging VQA benchmarks, which paves the way for solving complex multimodal information-seeking tasks.

</details>

#### [MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline](https://arxiv.org/abs/2603.01050)
2026-03 · LLaMA-Factory + VeRL · eval-only release · [PDF](https://arxiv.org/pdf/2603.01050) · [Code](https://github.com/HJYao00/MM-DeepResearch) [![Stars](https://img.shields.io/github/stars/HJYao00/MM-DeepResearch?style=social)](https://github.com/HJYao00/MM-DeepResearch)

> **TL;DR.** A multimodal deep-research agent built from hypergraph-generated search-intensive QA (Hyper-Search) and tree-searched tool-expert trajectories (DR-TTS) over an offline multi-tool search engine for agentic RL.

<details><summary>Abstract</summary>

We aim to develop a multimodal research agent capable of explicit reasoning and planning, multi-tool invocation, and cross-modal information synthesis, enabling it to conduct deep research tasks. However, we observe three main challenges in developing such agents: (1) scarcity of search-intensive multimodal QA data, (2) lack of effective search trajectories, and (3) prohibitive cost of training with online search APIs. To tackle them, we first propose Hyper-Search, a hypergraph-based QA generation method that models and connects visual and textual nodes within and across modalities, enabling to generate search-intensive multimodal QA pairs that require invoking various search tools to solve. Second, we introduce DR-TTS, which first decomposes search-involved tasks into several categories according to search tool types, and respectively optimize specialized search tool experts for each tool. It then recomposes tool experts to jointly explore search trajectories via tree search, producing trajectories that successfully solve complex tasks using various search tools. Third, we build an offline search engine supporting multiple search tools, enabling agentic reinforcement learning without using costly online search APIs. With the three designs, we develop MM-DeepResearch, a powerful multimodal deep research agent, and extensive results shows its superiority across benchmarks. Code is available at https://github.com/HJYao00/MM-DeepResearch

</details>

#### [Towards Long-horizon Agentic Multimodal Search](https://arxiv.org/abs/2604.12890)
2026-04 · [PDF](https://arxiv.org/pdf/2604.12890)

> **TL;DR.** A long-horizon multimodal search framework (LMM-Searcher) that offloads visual assets to a file system with UID references plus on-demand image fetching; 12K distilled trajectories fine-tune Qwen3-VL-30B, scaling to 100-turn search.

<details><summary>Abstract</summary>

Multimodal deep search agents have shown great potential in solving complex tasks by iteratively collecting textual and visual evidence. However, managing the heterogeneous information and high token costs associated with multimodal inputs over long horizons remains a critical challenge, as existing methods often suffer from context explosion or the loss of crucial visual signals. To address this, we propose a novel Long-horizon MultiModal deep search framework, named LMM-Searcher, centered on a file-based visual representation mechanism. By offloading visual assets to an external file system and mapping them to lightweight textual identifiers (UIDs), our approach mitigates context overhead while preserving multimodal information for future access. We equip the agent with a tailored fetch-image tool, enabling a progressive, on-demand visual loading strategy for active perception. Furthermore, we introduce a data synthesis pipeline designed to generate queries requiring complex cross-modal multi-hop reasoning. Using this pipeline, we distill 12K high-quality trajectories to fine-tune Qwen3-VL-Thinking-30A3B into a specialized multimodal deep search agent. Extensive experiments across four benchmarks demonstrate that our method successfully scales to 100-turn search horizons, achieving state-of-the-art performance among open-source models on challenging long-horizon benchmarks like MM-BrowseComp and MMSearch-Plus, while also exhibiting strong generalizability across different base models. Our code will be released in this https URL.

</details>

#### REDSearcher: A Scalable and Cost-Efficient Framework for Long-Horizon Search Agents

> **TL;DR.** SFT + RL; covers both textual and multimodal search.

#### [Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports From Scratch with Agentic Framework](https://github.com/rickyang1114/multimodal-deepresearcher)
`AAAI 2026 Oral` · [Code](https://github.com/rickyang1114/multimodal-deepresearcher) [![Stars](https://img.shields.io/github/stars/rickyang1114/multimodal-deepresearcher?style=social)](https://github.com/rickyang1114/multimodal-deepresearcher)

> **TL;DR.** _pending._

#### OmniSearch: Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent
`ICLR 2025`

> **TL;DR.** A model-agnostic agentic search framework for multimodal RAG with a dynamic VQA dataset and self-adaptive planning.

#### HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents
`IMEB Benchmark`

> **TL;DR.** Parallel multimodal search agents trained with dual-grained efficiency-aware RL; no open-source release yet (2026-05-11).

#### [Seg-ReSearch: Segmentation with Interleaved Reasoning and External Search](https://arxiv.org/abs/2602.04454)
`ICML 2026` · 2026-02 · [PDF](https://arxiv.org/pdf/2602.04454)

> **TL;DR.** A segmentation paradigm that interleaves reasoning with external search so MLLM segmenters can handle open-world queries needing up-to-date or domain knowledge; introduces the OK-VOS benchmark.

<details><summary>Abstract</summary>

Segmentation based on language has been a popular topic in computer vision. While recent advances in multimodal large language models (MLLMs) have endowed segmentation systems with reasoning capabilities, these efforts remain confined by the frozen internal knowledge of MLLMs, which limits their potential for real-world scenarios that involve up-to-date information or domain-specific concepts. In this work, we propose Seg-ReSearch, a novel segmentation paradigm that overcomes the knowledge bottleneck of existing approaches. By enabling interleaved reasoning and external search, Seg-ReSearch empowers segmentation systems to handle dynamic, open-world queries that extend beyond the frozen knowledge of MLLMs. To effectively train this capability, we introduce a hierarchical reward design that harmonizes initial guidance with progressive incentives, mitigating the dilemma between sparse outcome signals and rigid step-wise supervision. For evaluation, we construct OK-VOS, a challenging benchmark that explicitly requires outside knowledge for video object segmentation. Experiments on OK-VOS and two existing reasoning segmentation benchmarks demonstrate that our Seg-ReSearch improves state-of-the-art approaches by a substantial margin. Code and data will be released at this https URL.

</details>

#### [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/abs/2605.16217)
2026-05 · [PDF](https://arxiv.org/pdf/2605.16217)

> **TL;DR.** A Searcher+Navigator system that treats deep research as assembling complementary evidence on a shared graph; the RL-trained Navigator scales from one to many parallel Searchers, reaching 86.2 on BrowseComp.

<details><summary>Abstract</summary>

Deep research agents have achieved remarkable progress on complex information seeking tasks. Even long ReAct style rollouts explore only a single trajectory, while recent state of the art systems scale inference time compute via parallel search and aggregation. Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit. We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel. The Searcher collects evidence traces for a given sub-query through ReAct-style interaction. The Navigator maintains a shared evidence graph, verifying which pieces are still missing, dispatching Searchers to gather them, and reasoning over the completed graph to produce a source-traced final answer. We train the Navigator with reinforcement learning to verify, dispatch, and synthesize, while independently training the Searcher to remain a standard ReAct agent. The resulting Navigator supports rollouts with a single Searcher or many in parallel without retraining. With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks. With 64 Searchers it reaches 86.2 on BrowseComp, surpassing every proprietary agent we benchmark, while the Navigator's reasoning context stays under 21.5K tokens.

</details>

#### [VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation](https://arxiv.org/abs/2605.16079)
2026-05 · [PDF](https://arxiv.org/pdf/2605.16079)

> **TL;DR.** Instance-level video understanding via visual prompts and native agentic tool calls that retrieve relevant segments on demand; cold-start + RL training yields +13.7% over baselines, beating GPT-4o and Gemini-2.5-Pro.

<details><summary>Abstract</summary>

Large Vision-Language Models (LVLMs) have shown significant progress in video understanding, yet they face substantial challenges in tasks requiring precise spatiotemporal localization at the instance level. Existing methods primarily rely on text prompts for human-model interaction, but these prompts struggle to provide precise spatial and temporal references, resulting in poor user experience. Furthermore, current approaches typically decouple visual perception from language reasoning, centering reasoning around language rather than visual content, which limits the model's ability to proactively perceive fine-grained visual evidence. To address these challenges, we propose VideoSeeker, a novel paradigm for instance-level video understanding through visual prompts. VideoSeeker seamlessly integrates agentic reasoning with instance-level video understanding tasks, enabling the model to proactively perceive and retrieve relevant video segments on demand. We construct a four-stage fully automated data synthesis pipeline to efficiently generate large-scale, high-quality instance-level video data. We internalize tool-calling and proactive perception capabilities into the model via cold-start supervision and RL training, building a powerful video understanding model. Experiments demonstrate that our model achieves an average improvement of +13.7% over baselines on instance-level video understanding tasks, surpassing powerful closed-source models such as GPT-4o and Gemini-2.5-Pro, while also showing effective transferability on general video understanding benchmarks. The relevant datasets and code will be released publicly.

</details>

#### [Watching, Reasoning, and Searching: A Video Deep Research Benchmark on Open Web for Agentic Video Reasoning](https://arxiv.org/abs/2601.06943)
2026-01 · [PDF](https://arxiv.org/pdf/2601.06943)

> **TL;DR.** Introduces VideoDR, the first video deep-research benchmark requiring cross-frame anchor extraction, web retrieval, and multi-hop verification; finds agentic isn't consistently better than workflow, with goal drift the core bottleneck.

<details><summary>Abstract</summary>

In real-world video question answering scenarios, videos often provide only localized visual cues, while verifiable answers are distributed across the open web; models therefore need to jointly perform cross-frame clue extraction, iterative retrieval, and multi-hop reasoning-based verification. To bridge this gap, we construct the first video deep research benchmark, VideoDR. VideoDR centers on video-conditioned open-domain video question answering, requiring cross-frame visual anchor extraction, interactive web retrieval, and multi-hop reasoning over joint video-web evidence; through rigorous human annotation and quality control, we obtain high-quality video deep research samples spanning six semantic domains. We evaluate multiple closed-source and open-source multimodal large language models under both the Workflow and Agentic paradigms, and the results show that Agentic is not consistently superior to Workflow: its gains depend on a model's ability to maintain the initial video anchors over long retrieval chains. Further analysis indicates that goal drift and long-horizon consistency are the core bottlenecks. In sum, VideoDR provides a systematic benchmark for studying video agents in open-web settings and reveals the key challenges for next-generation video deep research agents.

</details>

### Proprietary Models

#### OpenAI Deep Research

> **TL;DR.** _Proprietary product._

#### Google Deep Research

> **TL;DR.** _Proprietary product._

#### Seed 1.8

> **TL;DR.** _Proprietary product._

#### Salesforce Deep Research

> **TL;DR.** _Proprietary product._

#### Perplexity

> **TL;DR.** _Proprietary product._

#### Grok DeepSearch

> **TL;DR.** _Proprietary product._

### Open Data Synthesis for Deep Research

#### DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search

> **TL;DR.** _pending._

#### [MiroThinker](https://github.com/MiroMindAI/MiroThinker)
[Code](https://github.com/MiroMindAI/MiroThinker) [![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social)](https://github.com/MiroMindAI/MiroThinker)

> **TL;DR.** _pending._

#### ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

> **TL;DR.** _pending._

#### [Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design](https://arxiv.org/abs/2603.28376)
2026-03 · [PDF](https://arxiv.org/pdf/2603.28376)

> **TL;DR.** A verification-centric deep-research agent that injects explicit verification into QA synthesis, trajectory construction, and test-time scaling; an 8B model rivals 30B agents on BrowseComp and BrowseComp-ZH.

<details><summary>Abstract</summary>

Deep research agents autonomously conduct open-ended investigations, integrating complex information retrieval with multi-step reasoning across diverse sources to solve real-world problems. To sustain this capability on long-horizon tasks, reliable verification is critical during both training and inference. A major bottleneck in existing paradigms stems from the lack of explicit verification mechanisms in QA data synthesis, trajectory construction, and test-time scaling. Errors introduced at each stage propagate downstream and degrade the overall agent performance. To address this, we present Marco DeepResearch, a deep research agent optimized with a verification-centric framework design at three levels: **(1) QA Data Synthesis:** We introduce verification mechanisms to graph-based and agent-based QA synthesis to control question difficulty while ensuring answers are unique and correct; **(2) Trajectory Construction:** We design a verification-driven trajectory synthesis method that injects explicit verification patterns into training trajectories; and **(3) Test-time scaling:** We use Marco DeepResearch itself as a verifier at inference time and effectively improve performance on challenging questions. Extensive experimental results demonstrate that our proposed Marco DeepResearch agent significantly outperforms 8B-scale deep research agents on most challenging benchmarks, such as BrowseComp and BrowseComp-ZH. Crucially, under a maximum budget of 600 tool calls, Marco DeepResearch even surpasses or approaches several 30B-scale agents, like Tongyi DeepResearch-30B.

</details>

#### LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents

> **TL;DR.** _pending._

#### DLLM-Searcher: Adapting Diffusion Large Language Model for Search Agents

> **TL;DR.** _pending._

### Generation (Search-Enhanced Generation)

#### Gen-Searcher: Reinforcing Agentic Search for Image Generation

> **TL;DR.** _pending._

#### Unify-Agent: A Unified Multimodal Agent for World-Grounded Image Synthesis

> **TL;DR.** _pending._

### Perception (Search-Enhanced Perception)

_None yet._

### Misc

#### AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking in Large Language Models

> **TL;DR.** _pending._

#### CityRAG: Stepping Into a City via Spatially-Grounded Video Generation

> **TL;DR.** _pending._

#### PlugMem: Transforming Raw Agent Interactions into Reusable Knowledge

> **TL;DR.** _pending._

#### GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization

> **TL;DR.** _pending._

#### Memento: Teaching LLMs to Manage Their Own Context

> **TL;DR.** _pending._

#### Beyond Retrieval: A Multitask Benchmark and Model for Code Search

> **TL;DR.** _pending._

### Methods: TBD

#### A Tale of Two Graphs: Separating Knowledge Exploration from Outline Structure for Open-Ended Deep Research

> **TL;DR.** _pending._

#### Step-DR

> **TL;DR.** _pending._

#### Skywork-R1V4: Toward Agentic Multimodal Intelligence through Interleaved Thinking with Images and DeepResearch

> **TL;DR.** _Closed-source._

#### W&D: Scaling Parallel Tool Calling for Efficient Deep Research Agents

> **TL;DR.** _pending._

#### [OpenDeepResearcher](https://github.com/mshumer/OpenDeepResearcher)
[Code](https://github.com/mshumer/OpenDeepResearcher) [![Stars](https://img.shields.io/github/stars/mshumer/OpenDeepResearcher?style=social)](https://github.com/mshumer/OpenDeepResearcher)

> **TL;DR.** _pending._

#### Mind DeepResearch Technical Report

> **TL;DR.** _pending._

#### s1-Deep Research

> **TL;DR.** _pending._

#### MemEvolve: Meta-Evolution of Agent Memory Systems

> **TL;DR.** _pending._

#### Dr. Zero
`Meta`

> **TL;DR.** _pending._

#### [General Agentic Memory Via Deep Research](https://arxiv.org/abs/2511.18423)
`HF #1 Paper` · 2025-11 · [PDF](https://arxiv.org/pdf/2511.18423)

> **TL;DR.** A "just-in-time" agent memory framework (GAM) pairing a lightweight Memorizer with a Researcher that retrieves and integrates from a full page-store at runtime, optimized end-to-end with RL.

<details><summary>Abstract</summary>

Memory is critical for AI agents, yet the widely-adopted static memory, aiming to create readily available memory in advance, is inevitably subject to severe information loss. To address this limitation, we propose a novel framework called **general agentic memory (GAM)**. GAM follows the principle of "**just-in time (JIT) compilation**" where it focuses on creating optimized contexts for its client at runtime while keeping only simple but useful memory during the offline stage. To this end, GAM employs a duo-design with the following components. 1) **Memorizer**, which highlights key historical information using a lightweight memory, while maintaining complete historical information within a universal page-store. 2) **Researcher**, which retrieves and integrates useful information from the page-store for its online request guided by the pre-constructed memory. This design allows GAM to effectively leverage the agentic capabilities and test-time scalability of frontier large language models (LLMs), while also facilitating end-to-end performance optimization through reinforcement learning. In our experimental study, we demonstrate that GAM achieves substantial improvement on various memory-grounded task completion scenarios against existing memory systems.

</details>

#### [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](https://arxiv.org/abs/2511.15593)
`HF #3 Paper` · 2025-11 · [PDF](https://arxiv.org/pdf/2511.15593)

> **TL;DR.** Studies ideation diversity as a driver of AI research-agent performance on MLE-bench: higher-performing agents show more diverse ideas, and a controlled experiment confirms more diversity yields stronger results.

<details><summary>Abstract</summary>

AI research agents offer the promise to accelerate scientific progress by automating the design, implementation, and training of machine learning models. However, the field is still in its infancy, and the key factors driving the success or failure of agent trajectories are not fully understood. We examine the role that ideation diversity plays in agent performance. First, we analyse agent trajectories on MLE-bench, a well-known benchmark to evaluate AI research agents, across different models and agent scaffolds. Our analysis reveals that different models and agent scaffolds yield varying degrees of ideation diversity, and that higher-performing agents tend to have increased ideation diversity. Further, we run a controlled experiment where we modify the degree of ideation diversity, demonstrating that higher ideation diversity results in stronger performance. Finally, we strengthen our results by examining additional evaluation metrics beyond the standard medal-based scoring of MLE-bench, showing that our findings still hold across other agent performance metrics.

</details>

#### Chart Deep Research in LVLMs via Parallel Relative Policy Optimization

> **TL;DR.** _pending._

#### NanoResearch

> **TL;DR.** _pending._

#### Search-o1

> **TL;DR.** _pending._

#### OpenSeeker

> **TL;DR.** _pending._

#### OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories

> **TL;DR.** _pending._

#### Karpathy Autoresearch

> **TL;DR.** _pending._

#### AutoResearchClaw

> **TL;DR.** _pending._

#### Dr. Claw

> **TL;DR.** _pending._

## Survey

#### [A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications](https://arxiv.org/abs/2506.12594)
2025-06 · [PDF](https://arxiv.org/pdf/2506.12594)

> **TL;DR.** A survey of 80+ Deep Research systems since 2023 with a hierarchical taxonomy across four dimensions: foundation/reasoning models, tool use, task planning/execution, and knowledge synthesis.

<details><summary>Abstract</summary>

This survey examines the rapidly evolving field of Deep Research systems -- AI-powered applications that automate complex research workflows through the integration of large language models, advanced information retrieval, and autonomous reasoning capabilities. We analyze more than 80 commercial and non-commercial implementations that have emerged since 2023, including OpenAI/Deep Research, Gemini/Deep Research, Perplexity/Deep Research, and numerous open-source alternatives. Through comprehensive examination, we propose a novel hierarchical taxonomy that categorizes systems according to four fundamental technical dimensions: foundation models and reasoning engines, tool utilization and environmental interaction, task planning and execution control, and knowledge synthesis and output generation. We explore the architectural patterns, implementation approaches, and domain-specific adaptations that characterize these systems across academic, scientific, business, and educational applications. Our analysis reveals both the significant capabilities of current implementations and the technical and ethical challenges they present regarding information accuracy, privacy, intellectual property, and accessibility. The survey concludes by identifying promising research directions in advanced reasoning architectures, multimodal integration, domain specialization, human-AI collaboration, and ecosystem standardization that will likely shape the future evolution of this transformative technology. By providing a comprehensive framework for understanding Deep Research systems, this survey contributes to both the theoretical understanding of AI-augmented knowledge work and the practical development of more capable, responsible, and accessible research technologies. The paper resources can be viewed at https://github.com/scienceaix/deepresearch.

</details>
