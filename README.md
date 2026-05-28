# Awesome Multimodal Deep Research

> A curated list of papers, benchmarks, and methods for **Multimodal Deep Research**: agents that *search, browse, and reason* over both text and visual information to answer open-ended, knowledge-intensive questions.

If you find this list helpful, please give it a ⭐ and **join us in maintaining it**. This is a community effort, and contributions of any size are very welcome.

## How to Contribute

We want this to be the most complete, up-to-date map of multimodal deep research, and we can't do it alone. Found a paper that's missing? A broken link? A TL;DR you'd phrase better? Please jump in.

### Ways to contribute

- **Quick (no setup):** open an [issue](../../issues) with the arXiv link (and code repo, if any). A maintainer will add it.
- **Direct:** open a Pull Request adding your entry under the right section, following the format below.

### Entry format

Every entry keeps a one-line **TL;DR** visible by default and folds the full abstract:

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
python3 fetch_arxiv.py --id 2409.12959 --section "Benchmarks" --dry-run

# 2) Insert it. Add the metadata arXiv can't give and a hand-written TL;DR:
python3 fetch_arxiv.py --id 2409.12959 --section "Benchmarks" \
    --affiliation "CUHK MMLab" --venue "ICLR 2025" --base "GPT-4o" \
    --code https://github.com/owner/repo --tldr "One crisp sentence."

# You can also resolve a paper by URL or by title search:
python3 fetch_arxiv.py --url https://arxiv.org/abs/2409.12959 --section "Benchmarks"
python3 fetch_arxiv.py --title "MMSearch: Benchmarking ..." --section "Benchmarks"
```

### Conventions

- **arXiv-first.** The script uses the Atom API and falls back to the more lenient HTML abstract page on a `429` rate limit. It never retries a `429` (that only extends the ban).
- **No auto-push.** The script only edits `README.md` — review the diff and commit yourself, then open a PR.
- **Affiliation / venue** are rarely available from arXiv. If you don't have them, leave them out (no placeholder); add them later when you do.
- **TL;DR** should be a single short sentence. The script's auto first-sentence fallback is flagged with `<!-- TLDR: refine -->` so you can rewrite it into something crisp.
- **Stars.** For entries with code, include a `![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=social)` badge (the script adds it automatically when `--code` is a GitHub URL). It updates on its own.

## Contents

- [Benchmarks](#benchmarks)
- [Method Papers](#method-papers)
- [Language-based Deep Research](#language-based-deep-research)
  - [Benchmarks](#benchmarks-1)
  - [Method Papers](#method-papers-1)
  - [Survey Papers](#survey-papers)

## Benchmarks

#### VDR-Bench
`MMLab`
<!-- TODO: arXiv id + abstract + TL;DR. Backfill: python3 fetch_arxiv.py --id <id> --section Benchmarks --dry-run -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### MMDR-Bench
`OSU`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### BC-VL
`Alibaba`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### [SimpleVQA: Multimodal Factuality Evaluation for Multimodal Large Language Models](https://arxiv.org/abs/2502.13059)
`MAP` · 2025-02 · [PDF](https://arxiv.org/pdf/2502.13059)

> **TL;DR.** The first multimodal factuality benchmark for short-answer VQA, scored by LLM-as-judge across 9 tasks and 9 topics, evaluating 18 MLLMs and 8 text-only LLMs.

<details><summary>Abstract</summary>

The increasing application of multi-modal large language models (MLLMs) across various sectors have spotlighted the essence of their output reliability and accuracy, particularly their ability to produce content grounded in factual information (e.g. common and domain-specific knowledge). In this work, we introduce SimpleVQA, the first comprehensive multi-modal benchmark to evaluate the factuality ability of MLLMs to answer natural language short questions. SimpleVQA is characterized by six key features: it covers multiple tasks and multiple scenarios, ensures high quality and challenging queries, maintains static and timeless reference answers, and is straightforward to evaluate. Our approach involves categorizing visual question-answering items into 9 different tasks around objective events or common knowledge and situating these within 9 topics. Rigorous quality control processes are implemented to guarantee high-quality, concise, and clear answers, facilitating evaluation with minimal variance via an LLM-as-a-judge scoring system. Using SimpleVQA, we perform a comprehensive assessment of leading 18 MLLMs and 8 text-only LLMs, delving into their image comprehension and text generation abilities by identifying and analyzing error cases.

</details>

#### [MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines](https://arxiv.org/abs/2409.12959)
`MMLab` · 2024-09 · [PDF](https://arxiv.org/pdf/2409.12959)

> **TL;DR.** Benchmark plus pipeline (MMSearch-Engine) testing whether large multimodal models can serve as end-to-end multimodal search engines (300 instances, 14 subfields).

<details><summary>Abstract</summary>

The advent of Large Language Models (LLMs) has paved the way for AI search engines, e.g., SearchGPT, showcasing a new paradigm in human-internet interaction. However, most current AI search engines are limited to text-only settings, neglecting the multimodal user queries and the text-image interleaved nature of website information. Recently, Large Multimodal Models (LMMs) have made impressive strides. Yet, whether they can function as AI search engines remains under-explored, leaving the potential of LMMs in multimodal search an open question. To this end, we first design a delicate pipeline, MMSearch-Engine, to empower any LMMs with multimodal search capabilities. On top of this, we introduce MMSearch, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs. The curated dataset contains 300 manually collected instances spanning 14 subfields, which involves no overlap with the current LMMs' training data, ensuring the correct answer can only be obtained within searching. By using MMSearch-Engine, the LMMs are evaluated by performing three individual tasks (requery, rerank, and summarization), and one challenging end-to-end task with a complete searching process. We conduct extensive experiments on closed-source and open-source LMMs. Among all tested models, GPT-4o with MMSearch-Engine achieves the best results, which surpasses the commercial product, Perplexity Pro, in the end-to-end task, demonstrating the effectiveness of our proposed pipeline. We further present error analysis to unveil current LMMs still struggle to fully grasp the multimodal search tasks, and conduct ablation study to indicate the potential of scaling test-time computation for AI search engine. We hope MMSearch may provide unique insights to guide the future development of multimodal AI search engine. Project Page: https://mmsearch.github.io

</details>

#### MMSearch-Plus
`HKU` · `ICLR 2026`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### MM-BrowseComp
`Seed`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### LiveVQA
`HUST` · `UW`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

## Method Papers

#### [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/abs/2508.05748)
`Alibaba` · 2025-08 · Base: `Qwen2.5-VL` · [PDF](https://arxiv.org/pdf/2508.05748)

> **TL;DR.** A vision-language deep-research agent (synthetic-trajectory cold start plus RL) that also introduces the BrowseComp-VL benchmark.

<details><summary>Abstract</summary>

Web agents such as Deep Research have demonstrated superhuman cognitive abilities, capable of solving highly challenging information-seeking problems. However, most research remains primarily text-centric, overlooking visual information in the real world. This makes multimodal Deep Research highly challenging, as such agents require much stronger reasoning abilities in perception, logic, knowledge, and the use of more sophisticated tools compared to text-based agents. To address this limitation, we introduce WebWatcher, a multi-modal Agent for Deep Research equipped with enhanced visual-language reasoning capabilities. It leverages high-quality synthetic multimodal trajectories for efficient cold start training, utilizes various tools for deep reasoning, and further enhances generalization through reinforcement learning. To better evaluate the capabilities of multimodal agents, we propose BrowseComp-VL, a benchmark with BrowseComp-style that requires complex information retrieval involving both visual and textual information. Experimental results show that WebWatcher significantly outperforms proprietary baseline, RAG workflow and open-source agents in four challenging VQA benchmarks, which paves the way for solving complex multimodal information-seeking tasks.

</details>

#### Vision-DeepResearch
`MMLab` · Base: `Qwen3-VL`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

#### [MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline](https://arxiv.org/abs/2603.01050)
2026-03 · [PDF](https://arxiv.org/pdf/2603.01050) · [Code](https://github.com/HJYao00/MM-DeepResearch) [![Stars](https://img.shields.io/github/stars/HJYao00/MM-DeepResearch?style=social)](https://github.com/HJYao00/MM-DeepResearch)

> **TL;DR.** A multimodal deep-research agent built from hypergraph-generated search-intensive QA (Hyper-Search) and tree-searched tool-expert trajectories (DR-TTS) over an offline multi-tool search engine for agentic RL.

<details><summary>Abstract</summary>

We aim to develop a multimodal research agent capable of explicit reasoning and planning, multi-tool invocation, and cross-modal information synthesis, enabling it to conduct deep research tasks. However, we observe three main challenges in developing such agents: (1) scarcity of search-intensive multimodal QA data, (2) lack of effective search trajectories, and (3) prohibitive cost of training with online search APIs. To tackle them, we first propose Hyper-Search, a hypergraph-based QA generation method that models and connects visual and textual nodes within and across modalities, enabling to generate search-intensive multimodal QA pairs that require invoking various search tools to solve. Second, we introduce DR-TTS, which first decomposes search-involved tasks into several categories according to search tool types, and respectively optimize specialized search tool experts for each tool. It then recomposes tool experts to jointly explore search trajectories via tree search, producing trajectories that successfully solve complex tasks using various search tools. Third, we build an offline search engine supporting multiple search tools, enabling agentic reinforcement learning without using costly online search APIs. With the three designs, we develop MM-DeepResearch, a powerful multimodal deep research agent, and extensive results shows its superiority across benchmarks. Code is available at https://github.com/HJYao00/MM-DeepResearch

</details>

## Language-based Deep Research

Text-only deep research, included here for reference and lineage.

### Benchmarks

#### [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516)
`OpenAI` · 2025-04 · [PDF](https://arxiv.org/pdf/2504.12516) · [Code](https://github.com/openai/simple-evals) [![Stars](https://img.shields.io/github/stars/openai/simple-evals?style=social)](https://github.com/openai/simple-evals)

> **TL;DR.** 1,266 hard-to-find-information questions testing an agent's web-browsing persistence, with short, easily verifiable answers (text-only).

<details><summary>Abstract</summary>

We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. BrowseComp comprises 1,266 questions that require persistently navigating the internet in search of hard-to-find, entangled information. Despite the difficulty of the questions, BrowseComp is simple and easy-to-use, as predicted answers are short and easily verifiable against reference answers. BrowseComp for browsing agents can be seen as analogous to how programming competitions are an incomplete but useful benchmark for coding agents. While BrowseComp sidesteps challenges of a true user query distribution, like generating long answers or resolving ambiguity, it measures the important core capability of exercising persistence and creativity in finding information. BrowseComp can be found at https://github.com/openai/simple-evals.

</details>

### Method Papers

#### Tongyi-DeepResearch
`Alibaba` · Base: `Qwen2.5`
<!-- TODO: arXiv id + abstract + TL;DR -->

> **TL;DR.** _Abstract & TL;DR pending backfill._

### Survey Papers

_None yet._
