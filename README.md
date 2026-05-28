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

> **TL;DR.** _pending._

#### BrowseComp-ZH

> **TL;DR.** _pending._

#### [BrowseComp-V3: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2602.12876)
2026-02 · [PDF](https://arxiv.org/pdf/2602.12876)

> **TL;DR.** _pending._

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

> **TL;DR.** _pending._

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

> **TL;DR.** _pending._

#### [LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?](https://arxiv.org/abs/2605.28721)
2026-05 · [PDF](https://arxiv.org/pdf/2605.28721)

> **TL;DR.** _pending._

#### [AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661)
2026-05 · [PDF](https://arxiv.org/pdf/2605.18661)

> **TL;DR.** _pending._

## Models & Methods

### Methods: Text

#### Search-R1
`COLM 2025 Oral`

> **TL;DR.** _pending._

#### Dr. Tulu

> **TL;DR.** _pending._

#### [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)
[Code](https://github.com/TIGER-AI-Lab/OpenResearcher) [![Stars](https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=social)](https://github.com/TIGER-AI-Lab/OpenResearcher)

> **TL;DR.** Data-synthesis pipeline; SFT + distillation only, with GPT-OSS as the teacher.

#### WebShaper

> **TL;DR.** _pending._

#### WebSailor

> **TL;DR.** _pending._

#### WebDancer

> **TL;DR.** _pending._

#### WebThinker

> **TL;DR.** _pending._

#### DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data
`HF Daily Paper`

> **TL;DR.** _pending._

### Methods: Multimodal

#### MM-Search-R1
`ACL 2026`

> **TL;DR.** _pending._

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

> **TL;DR.** SFT and data generation; introduces LMM-Searcher-30B.

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

> **TL;DR.** _pending._

#### [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/abs/2605.16217)
2026-05 · [PDF](https://arxiv.org/pdf/2605.16217)

> **TL;DR.** _pending._

#### [VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation](https://arxiv.org/abs/2605.16079)
2026-05 · [PDF](https://arxiv.org/pdf/2605.16079)

> **TL;DR.** _pending._

#### [Watching, Reasoning, and Searching: A Video Deep Research Benchmark on Open Web for Agentic Video Reasoning](https://arxiv.org/abs/2601.06943)
2026-01 · [PDF](https://arxiv.org/pdf/2601.06943)

> **TL;DR.** _pending._

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

> **TL;DR.** _pending._

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

> **TL;DR.** _pending._

#### [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](https://arxiv.org/abs/2511.15593)
`HF #3 Paper` · 2025-11 · [PDF](https://arxiv.org/pdf/2511.15593)

> **TL;DR.** _pending._

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

> **TL;DR.** _pending._
