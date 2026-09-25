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

- [Data and Benchmark](#data-and-benchmark) — Training Data; Benchmarks (Text / (Multi-)Image + Text / Video + Text / Knowledge-Intensive Image Generation)
- [Models & Methods](#models--methods) — Text; Multimodal; Proprietary Models; Open Data Synthesis; Generation; Perception; Misc
- [Survey](#survey)

## Data and Benchmark

### Training Data

#### [FVQA (from MMSearch-R1)](https://arxiv.org/abs/2506.20670)
`ACL 2026` · `from MMSearch-R1`

> **TL;DR.** The factual, search-intensive VQA training set introduced in MMSearch-R1 (see Models & Methods → Multimodal) for RL-based on-demand multimodal search.

#### [Encyclopedic VQA: Visual questions about detailed properties of fine-grained categories](https://arxiv.org/abs/2306.09224)
`ICCV 2023` · 2023-06 · [PDF](https://arxiv.org/pdf/2306.09224)

> **TL;DR.** A 1M-sample VQA dataset (221k unique Q+A) about fine-grained categories, paired with a Wikipedia knowledge base marking supporting evidence; SOTA VLMs score ~13%, but retrieval augmentation helps greatly.

<details><summary>Abstract</summary>

We propose Encyclopedic-VQA, a large scale visual question answering (VQA) dataset featuring visual questions about detailed properties of fine-grained categories and instances. It contains 221k unique question+answer pairs each matched with (up to) 5 images, resulting in a total of 1M VQA samples. Moreover, our dataset comes with a controlled knowledge base derived from Wikipedia, marking the evidence to support each answer. Empirically, we show that our dataset poses a hard challenge for large vision+language models as they perform poorly on our dataset: PaLI is state-of-the-art on OK-VQA, yet it only achieves 13.0% accuracy on our dataset. Moreover, we experimentally show that progress on answering our encyclopedic questions can be achieved by augmenting large models with a mechanism that retrieves relevant information from the knowledge base. An oracle experiment with perfect retrieval achieves 87.0% accuracy on the single-hop portion of our dataset, and an automatic retrieval-augmented prototype yields 48.8%. We believe that our dataset enables future research on retrieval-augmented vision+language models.

</details>

#### [Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?](https://arxiv.org/abs/2302.11713)
2023-02 · [PDF](https://arxiv.org/pdf/2302.11713)

> **TL;DR.** A visual information-seeking VQA dataset whose answers need fine-grained knowledge beyond commonsense; SOTA VLMs (PaLI-X, BLIP-2) struggle, while fine-tuning plus visual entity recognition and retrieval help.

<details><summary>Abstract</summary>

Pre-trained vision and language models have demonstrated state-of-the-art capabilities over existing tasks involving images and texts, including visual question answering. However, it remains unclear whether these models possess the capability to answer questions that are not only querying visual content but knowledge-intensive and information-seeking. In this study, we introduce InfoSeek, a visual question answering dataset tailored for information-seeking questions that cannot be answered with only common sense knowledge. Using InfoSeek, we analyze various pre-trained visual question answering models and gain insights into their characteristics. Our findings reveal that state-of-the-art pre-trained multi-modal models (e.g., PaLI-X, BLIP2, etc.) face challenges in answering visual information-seeking questions, but fine-tuning on the InfoSeek dataset elicits models to use fine-grained knowledge that was learned during their pre-training. Furthermore, we show that accurate visual entity recognition can be used to improve performance on InfoSeek by retrieving relevant documents, showing a significant space for improvement.

</details>

#### [A-OKVQA: A Benchmark for Visual Question Answering using World Knowledge](https://arxiv.org/abs/2206.01718)
2022-06 · [PDF](https://arxiv.org/pdf/2206.01718)

> **TL;DR.** A crowdsourced ~25K-question VQA benchmark requiring commonsense and world knowledge that can't be answered by a simple knowledge-base lookup, but instead need reasoning about the scene.

<details><summary>Abstract</summary>

The Visual Question Answering (VQA) task aspires to provide a meaningful testbed for the development of AI models that can jointly reason over visual and natural language inputs. Despite a proliferation of VQA datasets, this goal is hindered by a set of common limitations. These include a reliance on relatively simplistic questions that are repetitive in both concepts and linguistic structure, little world knowledge needed outside of the paired image, and limited reasoning required to arrive at the correct answer. We introduce A-OKVQA, a crowdsourced dataset composed of a diverse set of about 25K questions requiring a broad base of commonsense and world knowledge to answer. In contrast to the existing knowledge-based VQA datasets, the questions generally cannot be answered by simply querying a knowledge base, and instead require some form of commonsense reasoning about the scene depicted in the image. We demonstrate the potential of this new dataset through a detailed analysis of its contents and baseline performance measurements over a variety of state-of-the-art vision-language models. Project page: this http URL

</details>

#### [OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge](https://arxiv.org/abs/1906.00067)
2019-05 · [PDF](https://arxiv.org/pdf/1906.00067)

> **TL;DR.** A knowledge-based VQA benchmark of 14K+ questions whose answers require external knowledge beyond the image; SOTA VQA models degrade sharply.

<details><summary>Abstract</summary>

Visual Question Answering (VQA) in its ideal form lets us study reasoning in the joint space of vision and language and serves as a proxy for the AI task of scene understanding. However, most VQA benchmarks to date are focused on questions such as simple counting, visual attributes, and object detection that do not require reasoning or knowledge beyond what is in the image. In this paper, we address the task of knowledge-based visual question answering and provide a benchmark, called OK-VQA, where the image content is not sufficient to answer the questions, encouraging methods that rely on external knowledge resources. Our new dataset includes more than 14,000 questions that require external knowledge to answer. We show that the performance of the state-of-the-art VQA models degrades drastically in this new setting. Our analysis shows that our knowledge-based VQA task is diverse, difficult, and large compared to previous knowledge-based VQA datasets. We hope that this dataset enables researchers to open up new avenues for research in this domain. See this http URL to download and browse the dataset.

</details>

### Benchmarks: Text

#### [BrowseComp-V3: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2602.12876)
2026-02 · [PDF](https://arxiv.org/pdf/2602.12876)

> **TL;DR.** A 300-question multimodal browsing benchmark with cross-modal multi-hop reasoning over publicly searchable evidence and subgoal-level process evaluation; introduces the OmniSeeker agent (SOTA models reach only 36%).

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs), equipped with increasingly advanced planning and tool-use capabilities, are evolving into autonomous agents capable of performing multimodal web browsing and deep search in open-world environments. However, existing benchmarks for multimodal browsing remain limited in task complexity, evidence accessibility, and evaluation granularity, hindering comprehensive and reproducible assessments of deep search capabilities. To address these limitations, we introduce BrowseComp-$V^3$, a novel benchmark consisting of 300 carefully curated and challenging questions spanning diverse domains. The benchmark emphasizes deep, multi-level, and cross-modal multi-hop reasoning, where critical evidence is interleaved across textual and visual modalities within and across web pages. All supporting evidence is strictly required to be publicly searchable, ensuring fairness and reproducibility. Beyond final-answer accuracy, we incorporate an expert-validated, subgoal-driven process evaluation mechanism that enables fine-grained analysis of intermediate reasoning behaviors and systematic characterization of capability boundaries. In addition, we propose OmniSeeker, a unified multimodal browsing agent framework integrating diverse web search and visual perception tools. Comprehensive experiments demonstrate that even state-of-the-art models achieve only 36% accuracy on our benchmark, revealing critical bottlenecks in multimodal information integration and fine-grained perception. Our results highlight a fundamental gap between current model capabilities and robust multimodal deep search in real-world settings.

</details>

#### [Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments](https://arxiv.org/abs/2602.11964)
`Meta` · 2026-02 · [PDF](https://arxiv.org/pdf/2602.11964)

> **TL;DR.** A benchmark for LLM agents in dynamic, asynchronous environments (time pressure, noisy events, ambiguity, multi-agent), with action-level write-verifiers usable for RLVR; GPT-5 leads at 42% pass@1.

<details><summary>Abstract</summary>

We introduce Gaia2, a benchmark for evaluating large language model agents in realistic, asynchronous environments. Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the "sim2real" gap. Gaia2 is built on a consumer environment with the open-source Agents Research Environments platform and designed to be easy to extend. By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems.

</details>

#### [DeepSearchQA: Bridging the Comprehensiveness Gap for Deep Research Agents](https://arxiv.org/abs/2601.20975)
2026-01 · [PDF](https://arxiv.org/pdf/2601.20975)

> **TL;DR.** A 900-prompt benchmark across 17 fields testing exhaustive multi-step search: collating fragmented info, de-duplication/entity resolution, and reasoning about when to stop; agents struggle to balance recall and precision.

<details><summary>Abstract</summary>

We introduce DeepSearchQA, a 900-prompt benchmark for evaluating agents on difficult multi-step information-seeking tasks across 17 different fields. Unlike traditional benchmarks that target single answer retrieval or broad-spectrum factuality, DeepSearchQA features a dataset of challenging, handcrafted tasks designed to evaluate an agent's ability to execute complex search plans to generate exhaustive answer lists. This shift in design explicitly tests three critical, yet under-evaluated capabilities: 1) systematic collation of fragmented information from disparate sources, 2) de-duplication and entity resolution to ensure precision, and 3) the ability to reason about stopping criteria within an open-ended search space. Each task is structured as a causal chain, where discovering information for one step is dependent on the successful completion of the previous one, stressing long-horizon planning and context retention. All tasks are grounded in the open web with objectively verifiable answer sets. Our comprehensive evaluation of state-of-the-art agent architectures reveals significant performance limitations: even the most advanced models struggle to balance high recall with precision. We observe distinct failure modes ranging from premature stopping (under-retrieval) to hedging behaviors, where agents cast an overly wide net of low-confidence answers to artificially boost recall. These findings highlight critical headroom in current agent designs and position DeepSearchQA as an essential diagnostic tool for driving future research toward more robust, deep-research capabilities.

</details>

#### [DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation](https://arxiv.org/abs/2601.09688)
2026-01 · [PDF](https://arxiv.org/pdf/2601.09688)

> **TL;DR.** An automated framework that builds persona-driven deep-research tasks and scores reports via adaptive point-wise quality evaluation plus active fact-checking (verifying claims by web search even without citations).

<details><summary>Abstract</summary>

Deep research systems are widely used for multi-step web research, analysis, and cross-source synthesis, yet their evaluation remains challenging. Existing benchmarks often require annotation-intensive task construction, rely on static evaluation dimensions, or fail to reliably verify facts when citations are missing. To bridge these gaps, we introduce DeepResearchEval, an automated framework for deep research task construction and agentic evaluation. For task construction, we propose a persona-driven pipeline generating realistic, complex research tasks anchored in diverse user profiles, applying a two-stage filter Task Qualification and Search Necessity to retain only tasks requiring multi-source evidence integration and external retrieval. For evaluation, we propose an agentic pipeline with two components: an Adaptive Point-wise Quality Evaluation that dynamically derives task-specific evaluation dimensions, criteria, and weights conditioned on each generated task, and an Active Fact-Checking that autonomously extracts and verifies report statements via web search, even when citations are missing.

</details>

#### [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/abs/2508.06600)
2025-08 · [PDF](https://arxiv.org/pdf/2508.06600)

> **TL;DR.** A reproducible BrowseComp variant over a fixed, curated corpus with human-verified supporting documents and mined hard negatives, disentangling deep-research LLMs from their retrievers.

<details><summary>Abstract</summary>

Deep-Research agents, which integrate large language models (LLMs) with search tools, have shown success in improving the effectiveness of handling complex queries that require iterative search planning and reasoning over search results. Evaluations on current benchmarks like BrowseComp relies on black-box live web search APIs, have notable limitations in (1) fairness: dynamic and opaque web APIs hinder fair comparisons and reproducibility of deep research methods; (2) transparency: lack of control over the document corpus makes it difficult to isolate retriever contributions. In other words, the current evaluations may compare a complete deep research system at a given time, but they do not foster well-controlled experiments to provide insights into the capability of underlying deep research LLMs. To address these challenges, we introduce BrowseComp-Plus, a benchmark derived from BrowseComp, employing a fixed, carefully curated corpus. Each query in BrowseComp-Plus includes human-verified supporting documents and mined challenging negatives, enabling controlled experimentation. The benchmark is shown to be effective in distinguishing the performance of deep research systems. For instance, the open-source model Search-R1, when paired with the BM25 retriever, achieves 3.86% accuracy, whereas the GPT-5 achieves 55.9%. Integrating the GPT-5 with the Qwen3-Embedding-8B retriever further enhances its accuracy to 70.1% with fewer search calls. This benchmark allows comprehensive evaluation and disentangled analysis of deep research agents and retrieval methods, fostering insights into retrieval effectiveness, citation accuracy, and context engineering in Deep-Research system.

</details>

#### [xbench: Tracking Agents Productivity Scaling with Profession-Aligned Real-World Evaluations](https://arxiv.org/abs/2506.13651)
2025-06 · [PDF](https://arxiv.org/pdf/2506.13651)

> **TL;DR.** A profession-aligned, continuously-updated agent evaluation suite tied to real economic value, with initial Recruitment and Marketing benchmarks defined by industry professionals.

<details><summary>Abstract</summary>

We introduce xbench, a dynamic, profession-aligned evaluation suite designed to bridge the gap between AI agent capabilities and real-world productivity. While existing benchmarks often focus on isolated technical skills, they may not accurately reflect the economic value agents deliver in professional settings. To address this, xbench targets commercially significant domains with evaluation tasks defined by industry professionals. Our framework creates metrics that strongly correlate with productivity value, enables prediction of Technology-Market Fit (TMF), and facilitates tracking of product capabilities over time. As our initial implementations, we present two benchmarks: Recruitment and Marketing. For Recruitment, we collect 50 tasks from real-world headhunting business scenarios to evaluate agents' abilities in company mapping, information retrieval, and talent sourcing. For Marketing, we assess agents' ability to match influencers with advertiser needs, evaluating their performance across 50 advertiser requirements using a curated pool of 836 candidate influencers. We present initial evaluation results for leading contemporary agents, establishing a baseline for these professional domains. Our continuously updated evalsets and evaluations are available at this https URL.

</details>

#### [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](https://arxiv.org/abs/2506.11763)
2025-06 · [PDF](https://arxiv.org/pdf/2506.11763)

> **TL;DR.** 100 PhD-level research tasks across 22 fields for evaluating deep-research agents on report quality and citation accuracy, with two human-aligned evaluation methodologies.

<details><summary>Abstract</summary>

Deep Research Agents are a prominent category of LLM-based agents. By autonomously orchestrating multistep web exploration, targeted retrieval, and higher-order synthesis, they transform vast amounts of online information into analyst-grade, citation-rich reports--compressing hours of manual desk research into minutes. However, a comprehensive benchmark for systematically evaluating the capabilities of these agents remains absent. To bridge this gap, we present DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks, each meticulously crafted by domain experts across 22 distinct fields. Evaluating DRAs is inherently complex and labor-intensive. We therefore propose two novel methodologies that achieve strong alignment with human judgment. The first is a reference-based method with adaptive criteria to assess the quality of generated research reports. The other framework is introduced to evaluate DRA's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy. We have open-sourced DeepResearch Bench and key components of these frameworks at this https URL to accelerate the development of practical LLM-based agents.

</details>

#### [BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese](https://arxiv.org/abs/2504.19314)
2025-04 · [PDF](https://arxiv.org/pdf/2504.19314)

> **TL;DR.** 289 multi-hop questions across 11 domains evaluating LLM agents on the Chinese web; most models score below 10-20%, and the best (OpenAI DeepResearch) reaches only 42.9%.

<details><summary>Abstract</summary>

As large language models (LLMs) evolve into tool-using agents, the ability to browse the web in real-time has become a critical yardstick for measuring their reasoning and retrieval competence. Existing benchmarks such as BrowseComp concentrate on English and overlook the linguistic, infrastructural, and censorship-related complexities of other major information ecosystems -- most notably Chinese. To address this gap, we introduce BrowseComp-ZH, a high-difficulty benchmark purpose-built to comprehensively evaluate LLM agents on the Chinese web. BrowseComp-ZH consists of 289 multi-hop questions spanning 11 diverse domains. Each question is reverse-engineered from a short, objective, and easily verifiable answer (e.g., a date, number, or proper noun). A two-stage quality control protocol is applied to strive for high question difficulty and answer uniqueness. We benchmark over 20 state-of-the-art language models and agentic search systems on our proposed BrowseComp-ZH. Despite their strong conversational and retrieval capabilities, most models struggle severely: a large number achieve accuracy rates below 10%, and only a handful exceed 20%. Even the best-performing system, OpenAI's DeepResearch, reaches just 42.9%. These results demonstrate the considerable difficulty of BrowseComp-ZH, where success demands not only effective retrieval strategies, but also sophisticated reasoning and information reconciliation -- capabilities that current models still struggle to master. Our dataset, construction guidelines, and benchmark results have been publicly released.

</details>

#### [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516)
`OpenAI` · 2025-04 · [PDF](https://arxiv.org/pdf/2504.12516) · [Code](https://github.com/openai/simple-evals) [![Stars](https://img.shields.io/github/stars/openai/simple-evals?style=social)](https://github.com/openai/simple-evals)

> **TL;DR.** 1,266 hard-to-find-information questions testing an agent's web-browsing persistence, with short, easily verifiable answers (text-only).

<details><summary>Abstract</summary>

We present BrowseComp, a simple yet challenging benchmark for measuring the ability for agents to browse the web. BrowseComp comprises 1,266 questions that require persistently navigating the internet in search of hard-to-find, entangled information. Despite the difficulty of the questions, BrowseComp is simple and easy-to-use, as predicted answers are short and easily verifiable against reference answers. BrowseComp for browsing agents can be seen as analogous to how programming competitions are an incomplete but useful benchmark for coding agents. While BrowseComp sidesteps challenges of a true user query distribution, like generating long answers or resolving ambiguity, it measures the important core capability of exercising persistence and creativity in finding information. BrowseComp can be found at https://github.com/openai/simple-evals.

</details>

#### [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
2025-01 · [PDF](https://arxiv.org/pdf/2501.07572)

> **TL;DR.** Introduces WebWalkerQA, a benchmark for traversing a website's subpages to systematically extract deep, multi-layered info, plus WebWalker, a multi-agent explore-critic navigation framework.

<details><summary>Abstract</summary>

Retrieval-augmented generation (RAG) demonstrates remarkable performance across tasks in open-domain question-answering. However, traditional search engines may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information. To address it, we introduce WebWalkerQA, a benchmark designed to assess the ability of LLMs to perform web traversal. It evaluates the capacity of LLMs to traverse a website's subpages to extract high-quality data systematically. We propose WebWalker, which is a multi-agent framework that mimics human-like web navigation through an explore-critic paradigm. Extensive experimental results show that WebWalkerQA is challenging and demonstrates the effectiveness of RAG combined with WebWalker, through the horizontal and vertical integration in real-world scenarios.

</details>

#### [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)
`Meta` · 2023-11 · [PDF](https://arxiv.org/pdf/2311.12983)

> **TL;DR.** 466 real-world questions needing reasoning, multimodality, web browsing, and tool use; conceptually simple for humans (92%) but hard for AI (15% for GPT-4 with plugins).

<details><summary>Abstract</summary>

We introduce GAIA, a benchmark for General AI Assistants that, if solved, would represent a milestone in AI research. GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency. GAIA questions are conceptually simple for humans yet challenging for most advanced AIs: we show that human respondents obtain 92% vs. 15% for GPT-4 equipped with plugins. This notable performance disparity contrasts with the recent trend of LLMs outperforming humans on tasks requiring professional skills in e.g. law or chemistry. GAIA's philosophy departs from the current trend in AI benchmarks suggesting to target tasks that are ever more difficult for humans. We posit that the advent of Artificial General Intelligence (AGI) hinges on a system's capability to exhibit similar robustness as the average human does on such questions. Using GAIA's methodology, we devise 466 questions and their answer. We release our questions while retaining answers to 300 of them to power a leader-board available at this https URL.

</details>

### Benchmarks: (Multi-)Image + Text

#### [From Web to Pixels: Bringing Agentic Search into Visual Perception](https://arxiv.org/abs/2605.12497)
2026-05 · [PDF](https://arxiv.org/pdf/2605.12497)

> **TL;DR.** Formalizes Perception Deep Research (resolving a target's identity from external facts before localizing it) with the WebEye benchmark and the Pixel-Searcher search-to-pixel agent.

<details><summary>Abstract</summary>

Visual perception connects high-level semantic understanding to pixel-level perception, but most existing settings assume that the decisive evidence for identifying a target is already in the image or frozen model knowledge. We study a more practical yet harder open-world case where a visible object must first be resolved from external facts, recent events, long-tail entities, or multi-hop relations before it can be localized. We formalize this challenge as Perception Deep Research and introduce WebEye, an object-anchored benchmark with verifiable evidence, knowledge-intensive queries, precise box/mask annotations, and three task views: Search-based Grounding, Search-based Segmentation, and Search-based VQA. WebEyes contains 120 images, 473 annotated object instances, 645 unique QA pairs, and 1,927 task samples. We further propose Pixel-Searcher, an agentic search-to-pixel workflow that resolves hidden target identities and binds them to boxes, masks, or grounded answers. Experiments show that Pixel-Searcher achieves the strongest open-source performance across all three task views, while failures mainly arise from evidence acquisition, identity resolution, and visual instance binding.

</details>

#### [InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search](https://arxiv.org/abs/2605.07510)
2026-05 · [PDF](https://arxiv.org/pdf/2605.07510)

> **TL;DR.** 2,061 examples for interleaved language-vision agentic search across three levels, where textual and visual evidence repeatedly conditions later search; best model below 50% accuracy. Ships InterLV-Agent.

<details><summary>Abstract</summary>

Existing benchmarks for multimodal agentic search evaluate multimodal search and visual browsing, but visual evidence is either confined to the input or treated as an answer endpoint rather than part of an interleaved search trajectory. We introduce InterLV-Search, a benchmark for Interleaved Language-Vision Agentic Search, in which textual and visual evidence is repeatedly used to condition later search. It contains 2,061 examples across three levels: active visual evidence seeking, controlled offline interleaved multimodal search, and open-web interleaved multimodal search. Beyond existing benchmarks, it also includes multimodal multi-branch samples that involve comparison between multiple entities during the evidence search. We construct Level 1 and Level 2 with automated pipelines and Level 3 with a machine-led, human-supervised open-web pipeline. We further provide InterLV-Agent for standardized tool use, trajectory logging, and evaluation. Experiments on proprietary and open-source multimodal agents show that current systems remain far from solving interleaved multimodal search, with the best model below 50% overall accuracy, highlighting challenges in visual evidence seeking, search control, and multimodal evidence integration. We release the benchmark data and evaluation code at this https URL

</details>

#### [IMEB (from HyperEyes)](https://arxiv.org/abs/2605.07177)
`from HyperEyes` · 2026-05 · [PDF](https://arxiv.org/pdf/2605.07177)

> **TL;DR.** A 300-instance benchmark that jointly scores multimodal search capability and inference efficiency; introduced with the HyperEyes method (see Models & Methods).

#### [VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents](https://arxiv.org/abs/2603.16289)
`Ant` · 2026-03 · [PDF](https://arxiv.org/pdf/2603.16289)

> **TL;DR.** 169 expert-built VQA instances for visual-native search, requiring cross-validation of text-image evidence and reasoning over webpages' native visuals; best model (Claude-4.6-Opus) reaches only 47.6%.

<details><summary>Abstract</summary>

The rapid advancement of Multimodal Large Language Models (MLLMs) has enabled browsing agents to acquire and reason over multimodal information in the real world. But existing benchmarks suffer from two limitations: insufficient evaluation of visual reasoning ability and the neglect of native visual information of web pages in the reasoning chains. To address these challenges, we introduce a new benchmark for visual-native search, VisBrowse-Bench. It contains 169 VQA instances covering multiple domains and evaluates the models' visual reasoning capabilities during the search process through multimodal evidence cross-validation via text-image retrieval and joint reasoning. These data were constructed by human experts using a multi-stage pipeline and underwent rigorous manual verification. We additionally propose an agent workflow that can effectively drive the browsing agent to actively collect and reason over visual information during the search process. We comprehensively evaluated both open-source and closed-source models in this workflow. Experimental results show that even the best-performing model, Claude-4.6-Opus only achieves an accuracy of 47.6%, while the proprietary Deep Research model, o3-deep-research only achieves an accuracy of 41.1%. The code and data can be accessed at: this https URL

</details>

#### [MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains](https://arxiv.org/abs/2603.00873)
`ICLR 2026 Oral` · 2026-03 · [PDF](https://arxiv.org/pdf/2603.00873)

> **TL;DR.** The first agentic MM-RAG benchmark with long step-wise reasoning-chain annotations (3,333 examples, avg 3.7 hops, 5 reasoning structures) plus process-level metrics; also introduces the Search-Align fine-tuning framework.

<details><summary>Abstract</summary>

With the increasing demand for step-wise, cross-modal, and knowledge-grounded reasoning, multimodal large language models (MLLMs) are evolving beyond the traditional fixed retrieve-then-generate paradigm toward more sophisticated agentic multimodal retrieval-augmented generation (MM-RAG). Existing benchmarks, however, mainly focus on simplified QA with short retrieval chains, leaving adaptive planning and multimodal reasoning underexplored. We present MC-Search, the first benchmark for agentic MM-RAG with long, step-wise annotated reasoning chains spanning five representative reasoning structures. Each example specifies sub-questions, retrieval modalities, supporting facts, and intermediate answers, with fidelity ensured by HAVE (Hop-wise Attribution and Verification of Evidence), resulting in 3,333 high-quality examples averaging 3.7 hops. Beyond answer accuracy, MC-Search introduces new process-level metrics for reasoning quality, stepwise retrieval and planning accuracy. By developing a unified agentic MM-RAG pipeline, we benchmark six leading MLLMs and reveal systematic issues such as over- and under-retrieval and modality-misaligned planning. Finally, we introduce Search-Align, a process-supervised fine-tuning framework leveraging verified reasoning chains, showing that our data not only enables faithful evaluation but also improves planning and retrieval fidelity in open-source MLLMs.

</details>

#### [Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models](https://arxiv.org/abs/2602.02185)
`MMLab` · 2026-02 · [PDF](https://arxiv.org/pdf/2602.02185)

> **TL;DR.** A 2,000-instance benchmark for Vision-DeepResearch that removes cross-text answer leakage and over-idealized image matching so questions truly require visual search; proposes a multi-round cropped-search workflow.

<details><summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have advanced VQA and now support Vision-DeepResearch systems that use search engines for complex visual-textual fact-finding. However, evaluating these visual and textual search abilities is still difficult, and existing benchmarks have two major limitations. First, existing benchmarks are not visual search-centric: answers that should require visual search are often leaked through cross-textual cues in the text questions or can be inferred from the prior world knowledge in current MLLMs. Second, overly idealized evaluation scenario: On the image-search side, the required information can often be obtained via near-exact matching against the full image, while the text-search side is overly direct and insufficiently challenging. To address these issues, we construct the Vision-DeepResearch benchmark (VDR-Bench) comprising 2,000 VQA instances. All questions are created via a careful, multi-stage curation pipeline and rigorous expert review, designed to assess the behavior of Vision-DeepResearch systems under realistic real-world conditions. Moreover, to address the insufficient visual retrieval capabilities of current MLLMs, we propose a simple multi-round cropped-search workflow. This strategy is shown to effectively improve model performance in realistic visual retrieval scenarios. Overall, our results provide practical guidance for the design of future multimodal deep-research systems. The code will be released in this https URL.

</details>

#### [MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents](https://arxiv.org/abs/2601.12346)
`OSU & Amazon` · 2026-01 · [PDF](https://arxiv.org/pdf/2601.12346)

> **TL;DR.** 140 expert-crafted image-text tasks across 21 domains for multimodal citation-grounded report generation, evaluated by FLAE/TRACE/MOSAIC; multimodal integrity is the key bottleneck across 25 models.

<details><summary>Abstract</summary>

Deep Research Agents (DRAs) generate citation-rich reports via multi-step search and synthesis, yet existing benchmarks mainly target text-only settings or short-form multimodal QA, missing end-to-end multimodal evidence use. We introduce MMDeepResearch-Bench (MMDR-Bench), a benchmark of 140 expert-crafted tasks across 21 domains, where each task provides an image-text bundle to evaluate multimodal understanding and citation-grounded report generation. Compared to prior setups, MMDR-Bench emphasizes report-style synthesis with explicit evidence use, where models must connect visual artifacts to sourced claims and maintain consistency across narrative, citations, and visual references. We further propose a unified, interpretable evaluation pipeline: Formula-LLM Adaptive Evaluation (FLAE) for report quality, Trustworthy Retrieval-Aligned Citation Evaluation (TRACE) for citation-grounded evidence alignment, and Multimodal Support-Aligned Integrity Check (MOSAIC) for text-visual integrity, each producing fine-grained signals that support error diagnosis beyond a single overall score. Experiments across 25 state-of-the-art models reveal systematic trade-offs between generation quality, citation discipline, and multimodal grounding, highlighting that strong prose alone does not guarantee faithful evidence use and that multimodal integrity remains a key bottleneck for deep research agents.

</details>

#### [RealX-Bench](https://arxiv.org/abs/2511.05271)
`ICLR 2026` · `from DeepEyesV2` · 2025-11 · [PDF](https://arxiv.org/pdf/2511.05271)

> **TL;DR.** A benchmark for real-world multimodal reasoning that jointly requires perception, search, and reasoning; introduced with DeepEyesV2 (see Models & Methods).

#### [MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents (MSP)](https://arxiv.org/abs/2508.21475)
`HKU` · `ICLR 2026` · Multi-Image Input · 2025-08 · [PDF](https://arxiv.org/pdf/2508.21475)

> **TL;DR.** A 311-task benchmark forcing genuine multimodal reasoning by propagating fine-grained visual cues through iterative image-text retrieval; adds a set-of-mark agent module (top system reaches 36%).

<details><summary>Abstract</summary>

Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by requiring extraction and propagation of fine-grained visual cues through iterative image-text retrieval and cross-validation under retrieval noise. Our curation procedure seeds questions whose answers require extrapolating from spatial cues and temporal traces to out-of-image facts such as events, dates, and venues. Beyond the dataset, we provide a model-agnostic agent framework with standard browsing tools and a set-of-mark (SoM) module, which lets the agent place marks, crop subregions, and launch targeted image/text searches. SoM enables provenance-aware zoom-and-retrieve and improves robustness in multi-step reasoning. We evaluated closed- and open-source MLLMs in this framework. The strongest system achieves an end-to-end accuracy of 36.0%, and integrating SoM produces consistent gains in multiple settings, with improvements up to +3.9 points. From failure analysis, we observe recurring errors in locating relevant webpages and distinguishing between visually similar events. These results underscore the challenges of real-world multimodal search and establish MMSearch-Plus as a rigorous benchmark for advancing agentic MLLMs.

</details>

#### [MM-BrowseComp: A Comprehensive Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2508.13186)
`Seed` · 2025-08 · [PDF](https://arxiv.org/pdf/2508.13186)

> **TL;DR.** 224 hand-crafted multimodal browsing questions where key evidence is embedded in webpage images/videos, defeating text-only methods; even OpenAI o3 with tools reaches only 29%.

<details><summary>Abstract</summary>

AI agents with advanced reasoning and tool use capabilities have demonstrated impressive performance in web browsing for deep search. While existing benchmarks such as BrowseComp evaluate these browsing abilities, they primarily focus on textual information, overlooking the prevalence of multimodal content. To bridge this gap, we introduce MM-BrowseComp, a novel benchmark comprising 224 challenging, hand-crafted questions specifically designed to assess agents' multimodal retrieval and reasoning capabilities. These questions often incorporate images in prompts, and crucial information encountered during the search and reasoning process may also be embedded within images or videos on webpages. Consequently, methods relying solely on text prove insufficient for our benchmark. Additionally, we provide a verified checklist for each question, enabling fine-grained analysis of multimodal dependencies and reasoning paths. Our comprehensive evaluation of state-of-the-art models on MM-BrowseComp reveals that even top models like OpenAI o3 with tools achieve only 29.02% accuracy, highlighting the suboptimal multimodal capabilities and lack of native multimodal reasoning in current models.

</details>

#### [BC-VL (BrowseComp-VL)](https://arxiv.org/abs/2508.05748)
`Alibaba Tongyi Lab` · `ICLR 2026` · `from WebWatcher` · 2025-08 · [PDF](https://arxiv.org/pdf/2508.05748)

> **TL;DR.** The BrowseComp-style vision-and-language information-retrieval benchmark introduced by WebWatcher (see Models & Methods → Multimodal); requires complex retrieval over interleaved visual and textual evidence.

#### [Seeking and Updating with Live Visual Knowledge (LiveVQA)](https://arxiv.org/abs/2504.05288)
`HUST` · `UW` · 2025-04 · [PDF](https://arxiv.org/pdf/2504.05288)

> **TL;DR.** A 107K-sample, 12-category dataset for evaluating and updating MLLMs on visual knowledge from after their training cutoff; tool-use / agentic visual seeking yields ~327% average gains.

<details><summary>Abstract</summary>

The visual world around us constantly evolves, from real-time news and social media trends to global infrastructure changes visible through satellite imagery and augmented reality enhancements. However, Multimodal Large Language Models (MLLMs), which automate many tasks, struggle to stay current, limited by the cutoff dates in their fixed training datasets. To quantify this stagnation, we introduce LiveVQA, the first-of-its-kind dataset featuring 107,143 samples and 12 categories data specifically designed to support research in both seeking and updating with live visual knowledge. Drawing from recent news articles, video platforms, and academic publications in April 2024-May 2025, LiveVQA enables evaluation of how models handle latest visual information beyond their knowledge boundaries and how current methods help to update them. Our comprehensive benchmarking of 17 state-of-the-art MLLMs reveals significant performance gaps on content beyond knowledge cutoff, and tool-use or agentic visual seeking framework drastically gain an average of 327% improvement. Furthermore, we explore parameter-efficient fine-tuning (PEFT) methods to update MLLMs with new visual knowledge. We dive deeply to the critical balance between adapter capacity and model capability when updating MLLMs with new visual knowledge. All the experimental dataset and source code are publicly available at: this https URL.

</details>

#### [SimpleVQA: Multimodal Factuality Evaluation for Multimodal Large Language Models](https://arxiv.org/abs/2502.13059)
`MAP` · 2025-02 · [PDF](https://arxiv.org/pdf/2502.13059)

> **TL;DR.** The first multimodal factuality benchmark for short-answer VQA, scored by LLM-as-judge across 9 tasks and 9 topics, evaluating 18 MLLMs and 8 text-only LLMs.

<details><summary>Abstract</summary>

The increasing application of multi-modal large language models (MLLMs) across various sectors have spotlighted the essence of their output reliability and accuracy, particularly their ability to produce content grounded in factual information (e.g. common and domain-specific knowledge). In this work, we introduce SimpleVQA, the first comprehensive multi-modal benchmark to evaluate the factuality ability of MLLMs to answer natural language short questions. SimpleVQA is characterized by six key features: it covers multiple tasks and multiple scenarios, ensures high quality and challenging queries, maintains static and timeless reference answers, and is straightforward to evaluate. Our approach involves categorizing visual question-answering items into 9 different tasks around objective events or common knowledge and situating these within 9 topics. Rigorous quality control processes are implemented to guarantee high-quality, concise, and clear answers, facilitating evaluation with minimal variance via an LLM-as-a-judge scoring system. Using SimpleVQA, we perform a comprehensive assessment of leading 18 MLLMs and 8 text-only LLMs, delving into their image comprehension and text generation abilities by identifying and analyzing error cases.

</details>

#### [Humanity's Last Exam (HLE)](https://arxiv.org/abs/2501.14249)
`Nature` · 2025-01 · [PDF](https://arxiv.org/pdf/2501.14249)

> **TL;DR.** A 2,500-question, multi-modal, expert-written benchmark at the frontier of human knowledge, with verifiable answers that can't be found by quick web retrieval; SOTA LLMs score low.

<details><summary>Abstract</summary>

Benchmarks are important tools for tracking the rapid advancements in large language model (LLM) capabilities. However, benchmarks are not keeping pace in difficulty: LLMs now achieve over 90% accuracy on popular benchmarks like MMLU, limiting informed measurement of state-of-the-art LLM capabilities. In response, we introduce Humanity's Last Exam (HLE), a multi-modal benchmark at the frontier of human knowledge, designed to be the final closed-ended academic benchmark of its kind with broad subject coverage. HLE consists of 2,500 questions across dozens of subjects, including mathematics, humanities, and the natural sciences. HLE is developed globally by subject-matter experts and consists of multiple-choice and short-answer questions suitable for automated grading. Each question has a known solution that is unambiguous and easily verifiable, but cannot be quickly answered via internet retrieval. State-of-the-art LLMs demonstrate low accuracy and calibration on HLE, highlighting a significant gap between current LLM capabilities and the expert human frontier on closed-ended academic questions. To inform research and policymaking upon a clear understanding of model capabilities, we publicly release HLE at this https URL.

</details>

#### [MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines](https://arxiv.org/abs/2409.12959)
`MMLab` · `ICLR 2025` · 2024-09 · [PDF](https://arxiv.org/pdf/2409.12959)

> **TL;DR.** Benchmark plus pipeline (MMSearch-Engine) testing whether large multimodal models can serve as end-to-end multimodal search engines (300 instances, 14 subfields).

<details><summary>Abstract</summary>

The advent of Large Language Models (LLMs) has paved the way for AI search engines, e.g., SearchGPT, showcasing a new paradigm in human-internet interaction. However, most current AI search engines are limited to text-only settings, neglecting the multimodal user queries and the text-image interleaved nature of website information. Recently, Large Multimodal Models (LMMs) have made impressive strides. Yet, whether they can function as AI search engines remains under-explored, leaving the potential of LMMs in multimodal search an open question. To this end, we first design a delicate pipeline, MMSearch-Engine, to empower any LMMs with multimodal search capabilities. On top of this, we introduce MMSearch, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs. The curated dataset contains 300 manually collected instances spanning 14 subfields, which involves no overlap with the current LMMs' training data, ensuring the correct answer can only be obtained within searching. By using MMSearch-Engine, the LMMs are evaluated by performing three individual tasks (requery, rerank, and summarization), and one challenging end-to-end task with a complete searching process. We conduct extensive experiments on closed-source and open-source LMMs. Among all tested models, GPT-4o with MMSearch-Engine achieves the best results, which surpasses the commercial product, Perplexity Pro, in the end-to-end task, demonstrating the effectiveness of our proposed pipeline. We further present error analysis to unveil current LMMs still struggle to fully grasp the multimodal search tasks, and conduct ablation study to indicate the potential of scaling test-time computation for AI search engine. We hope MMSearch may provide unique insights to guide the future development of multimodal AI search engine. Project Page: https://mmsearch.github.io

</details>

#### [WorldVQA: Measuring Atomic World Knowledge in Multimodal Large Language Models](https://arxiv.org/abs/2602.02537)
`Moonshot AI` · `arXiv 2602` · 2026-01 · [PDF](https://arxiv.org/pdf/2602.02537)

> **TL;DR.** 3,500 atomic visual-knowledge VQA pairs that decouple memorized world knowledge from reasoning to measure MLLM factuality and hallucination.

<details><summary>Abstract</summary>

We introduce WorldVQA, a benchmark designed to evaluate the atomic visual world knowledge of Multimodal Large Language Models (MLLMs). Unlike current evaluations, which often conflate visual knowledge retrieval with reasoning, WorldVQA decouples these capabilities to strictly measure "what the model memorizes." The benchmark assesses the atomic capability of grounding and naming visual entities across a stratified taxonomy, spanning from common head-class objects to long-tail rarities. We expect WorldVQA to serve as a rigorous test for visual factuality, thereby establishing a standard for assessing the encyclopedic breadth and hallucination rates of current and next-generation frontier models.

</details>

#### [TVIR: Building Deep Research Agents Towards Text-Visual Interleaved Report Generation](https://arxiv.org/abs/2606.02320)
`NJU` · `arXiv 2606` · 2026-06 · [PDF](https://arxiv.org/pdf/2606.02320)

> **TL;DR.** TVIR-Bench: 100 expert-curated tasks for text-visual interleaved report generation with dual textual + visual assessment; TVIR-Agent as baseline.

<details><summary>Abstract</summary>

Deep Research Agents have shown strong capability in multi-step information retrieval, reasoning, and long-form report generation, but existing benchmarks and systems remain predominantly text-centric, with limited evaluation of whether visual elements are factually reliable and well aligned with the surrounding analysis. To address this gap, we introduce TVIR (Text-Visual Interleaved Report Generation), which includes TVIR-Bench, a benchmark of 100 expert-curated multimodal deep research tasks that require visual elements to serve specific analytical sub-goals, and TVIR-Agent, a hierarchical multi-agent framework that serves as a strong baseline for constructing outlines, retrieving images, generating charts with traceable sources, and composing reports through context-aware sequential writing. We further develop a dual-path evaluation framework that combines Textual Assessment and Visual Assessment. Experiments across nine deep research systems show that TVIR-Agent achieves strong overall performance, underscoring the importance of explicit multimodal design and evaluation for evidence-driven report generation.

</details>

### Benchmarks: Video + Text

#### [Video-Browser: Towards Agentic Open-web Video Browsing](https://arxiv.org/abs/2512.23044)
2025-12 · [PDF](https://arxiv.org/pdf/2512.23044)

> **TL;DR.** Formalizes agentic video browsing and introduces Video-BrowseComp (tasks that mandate video); Video-Browser uses Pyramidal Perception (cheap-metadata filtering, zoom only when needed) for +37.5% at 58% fewer tokens.

<details><summary>Abstract</summary>

The evolution of autonomous agents is redefining information seeking, transitioning from passive retrieval to proactive, open-ended web research. However, a significant modality gap remains in processing the web's most dynamic and information-dense modality: video. In this paper, we first formalize the task of Agentic Video Browsing and introduce Video-BrowseComp, a benchmark evaluating open-ended agentic browsing tasks that enforce a mandatory dependency on videos. We observe that current paradigms struggle to reconcile the scale of open-ended video exploration with the need for fine-grained visual verification. Direct visual inference (e.g., RAG) maximizes perception but incurs prohibitive context costs, while text-centric summarization optimizes efficiency but often misses critical visual details required for accurate grounding. To address this, we propose Video-Browser, a novel agent leveraging Pyramidal Perception, filtering with cheap metadata and zooming in with expensive visual perception only when necessary. Experiments demonstrate that our approach achieves a 37.5% relative improvement while reducing token consumption by 58.3% compared to Direct visual inference, establishing a foundation for verifiable open-web video research. We open-source all codes, benchmark at {this https URL} and {this https URL}.

</details>

### Benchmarks: Knowledge-Intensive Image Generation

#### [T2I-FactualBench: Benchmarking the Factuality of Text-to-Image Models with Knowledge-Intensive Concepts](https://arxiv.org/abs/2412.04300)
`ZJU` · `ACL 2025` · 2024-12 · [PDF](https://arxiv.org/pdf/2412.04300)

> **TL;DR.** 1,704 knowledge-intensive concept prompts scoring T2I factuality with a multi-round VQA judge.

<details><summary>Abstract</summary>

Evaluating the quality of synthesized images remains a significant challenge in the development of text-to-image (T2I) generation. Most existing studies in this area primarily focus on evaluating text-image alignment, image quality, and object composition capabilities, with comparatively fewer studies addressing the evaluation of the factuality of T2I models, particularly when the concepts involved are knowledge-intensive. To mitigate this gap, we present T2I-FactualBench in this work - the largest benchmark to date in terms of the number of concepts and prompts specifically designed to evaluate the factuality of knowledge-intensive concept generation. T2I-FactualBench consists of a three-tiered knowledge-intensive text-to-image generation framework, ranging from the basic memorization of individual knowledge concepts to the more complex composition of multiple knowledge concepts. We further introduce a multi-round visual question answering (VQA) based evaluation framework to assess the factuality of three-tiered knowledge-intensive text-to-image generation tasks. Experiments on T2I-FactualBench indicate that current state-of-the-art (SOTA) T2I models still leave significant room for improvement.

</details>

#### [WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation](https://arxiv.org/abs/2503.07265)
`PKU` · `ICML 2026` · 2025-03 · [PDF](https://arxiv.org/pdf/2503.07265) · [Code](https://github.com/PKU-YuanGroup/WISE) [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/WISE?style=social)](https://github.com/PKU-YuanGroup/WISE)

> **TL;DR.** 1,000 world-knowledge prompts across culture, spatio-temporal reasoning, and science, scored by WiScore beyond shallow text-image alignment.

<details><summary>Abstract</summary>

Text-to-Image (T2I) models are capable of generating high-quality artistic creations and visual content. However, existing research and evaluation standards predominantly focus on image realism and shallow text-image alignment, lacking a comprehensive assessment of complex semantic understanding and world knowledge integration in text-to-image generation. To address this challenge, we propose WISE, the first benchmark specifically designed for World Knowledge-Informed Semantic Evaluation. WISE moves beyond simple word-pixel mapping by challenging models with 1000 meticulously crafted prompts across 25 subdomains in cultural common sense, spatio-temporal reasoning, and natural science. To overcome the limitations of traditional CLIP metric, we introduce WiScore, a novel quantitative metric for assessing knowledge-image alignment. Through comprehensive testing of 20 models (10 dedicated T2I models and 10 unified multimodal models) using 1,000 structured prompts spanning 25 subdomains, our findings reveal significant limitations in their ability to effectively integrate and apply world knowledge during image generation, highlighting critical pathways for enhancing knowledge incorporation and application in next-generation T2I models. Code and data are available at \href{this https URL}{PKU-YuanGroup/WISE}.

</details>

#### [WorldGenBench: A World-Knowledge-Integrated Benchmark for Reasoning-Driven Text-to-Image Generation](https://arxiv.org/abs/2505.01490)
`arXiv 2505` · 2025-05 · [PDF](https://arxiv.org/pdf/2505.01490)

> **TL;DR.** Evaluates world-knowledge grounding and implicit reasoning of T2I models with a structured Knowledge Checklist Score.

<details><summary>Abstract</summary>

Recent advances in text-to-image (T2I) generation have achieved impressive results, yet existing models still struggle with prompts that require rich world knowledge and implicit reasoning: both of which are critical for producing semantically accurate, coherent, and contextually appropriate images in real-world scenarios. To address this gap, we introduce WorldGenBench, a benchmark designed to systematically evaluate T2I models' world knowledge grounding and implicit inferential capabilities, covering both the humanities and nature domains. We propose the Knowledge Checklist Score, a structured metric that measures how well generated images satisfy key semantic expectations. Experiments across 21 state-of-the-art models reveal that while diffusion models lead among open-source methods, proprietary auto-regressive models like GPT-4o exhibit significantly stronger reasoning and knowledge integration. Our findings highlight the need for deeper understanding and inference capabilities in next-generation T2I systems. Project Page: \href{this https URL}{this https URL}

</details>

### Benchmarks: TBD

#### [LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?](https://arxiv.org/abs/2605.28721)
2026-05 · [PDF](https://arxiv.org/pdf/2605.28721)

> **TL;DR.** Shows search agents often answer from intrinsic memory rather than retrieval, and introduces a 335-question benchmark whose answers depend on facts published within the prior 90 days.

<details><summary>Abstract</summary>

Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines when answer-supporting evidence is removed. These results suggest that static search benchmarks can reward memory-backed verification rather than evidence-driven discovery, conflating what agents already know with what they can find. We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage. It contains 335 human-authored questions whose answers depend on facts published within the 90 days preceding benchmark construction, drawn from six updated sources and filtered to exclude globally salient events. On LiveBrowseComp, all evaluated agents fall below 2% closed-book accuracy, search-augmented scores drop by 25-40 points relative to BrowseComp, and prior model rankings no longer reliably predict performance. LiveBrowseComp is available at https://huggingface.co/datasets/Forival/LiveBrowseComp.

</details>

#### [VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild](https://arxiv.org/abs/2605.27882)
2026-05 · [PDF](https://arxiv.org/pdf/2605.27882)

> **TL;DR.** A bilingual 200-task benchmark for multi-turn "vibe search" where agents must proactively refine vague user intent, scored against schema-free ground-truth knowledge graphs.

<details><summary>Abstract</summary>

LLM-based agents score well on search benchmarks, yet real users consistently find results unsatisfying, revealing a persistent evaluation-experience gap. We attribute this gap to existing benchmarks' reliance on over-specified queries, single-turn interactions, and fixed-schema evaluation, none of which reflect real search behavior where users and agents collaboratively refine vague intent through multi-turn dialogue. We term this paradigm VibeSearch and introduce VibeSearchBench, a benchmark comprising 200 manually curated bilingual (Chinese and English) tasks across 20 domains, split into VibeSearch-Pro (professional) and VibeSearch-Daily (daily-life) subsets. Each task pairs a user persona with a schema-free ground-truth knowledge graph, and is evaluated through a progressive-disclosure user simulator and a graph-matching evaluation framework. We benchmark seven frontier models under both the ReAct framework and the OpenClaw agent harness. Results show that all models remain substantially inadequate for VibeSearch (best F1: 30.30), highlighting the need for fundamental advances in long-context reasoning, proactive intent elicitation, and structured knowledge construction.

</details>

#### [AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661)
2026-05 · [PDF](https://arxiv.org/pdf/2605.18661)

> **TL;DR.** An end-to-end survey/roadmap of AI across the research lifecycle (Creation, Writing, Validation, Dissemination), mapping where AI is reliable assistance versus unreliable autonomy.

<details><summary>Abstract</summary>

AI-assisted research is crossing a threshold: fully automated systems can now generate research papers for as little as $15, while long-horizon agents can execute experiments, draft manuscripts, and simulate critique with minimal human input. Yet this productivity frontier exposes a deeper integrity problem: under scientific pressure, even frontier LLMs still fabricate results, miss hidden errors, and fail to judge novelty reliably. Studying developments through April 2026, we present an end-to-end analysis of AI across the complete research lifecycle, organized into four epistemological phases: Creation (idea generation, literature review, coding & experiments, tables & figures), Writing (paper writing), Validation (peer review, rebuttal & revision), and Dissemination (posters, slides, videos, social media, project pages, and interactive agents). We identify a sharp, stage-dependent boundary between reliable assistance and unreliable autonomy: AI excels at structured, retrieval-grounded, and tool-mediated tasks, but remains fragile for genuinely novel ideas, research-level experiments, and scientific judgment. Generated ideas often degrade after implementation, research code lags far behind pattern-matching benchmarks, and end-to-end autonomous systems have not yet consistently reached major-venue acceptance standards. We further show that greater automation can obscure rather than eliminate failure modes, making human-governed collaboration the most credible deployment paradigm. Finally, we provide a structured taxonomy, benchmark suite, and tool inventory, cross-stage design principles, and a practitioner-oriented playbook, with resources maintained at our project page.

</details>

#### [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://arxiv.org/abs/2604.25256)
2026-04 · [PDF](https://arxiv.org/pdf/2604.25256)

> **TL;DR.** A benchmark for autonomous scientific literature discovery with Deep Research (track down a target paper) and Wide Research (collect all qualifying papers) tasks; top LLMs reach only ~9% despite acing BrowseComp.

<details><summary>Abstract</summary>

Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a research problem, or to acquire evidence for verifying assumptions and supporting claims. To assess AI agents' capability in driving this process, we present AutoResearchBench, a dedicated benchmark for autonomous scientific literature discovery. AutoResearchBench consists of two complementary task types: (1) Deep Research, which requires tracking down a specific target paper through a progressive, multi-step probing process, and (2) Wide Research, which requires comprehensively collecting a set of papers satisfying given conditions. Compared to previous benchmarks on agentic web browsing, AutoResearchBench is distinguished along three dimensions: it is research-oriented, calling for in-depth comprehension of scientific concepts; literature-focused, demanding fine-grained utilization of detailed information; and open-ended, involving an unknown number of qualified papers and thus requiring deliberate reasoning and search throughout. These properties make AutoResearchBench uniquely suited for evaluating autonomous research capabilities, and extraordinarily challenging. Even the most powerful LLMs, despite having largely conquered general agentic web-browsing benchmarks such as BrowseComp, achieve only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, while many other strong baselines fall below 5%. We publicly release the dataset and evaluation pipeline to facilitate future research in this direction. We publicly release the dataset, evaluation pipeline, and code at this https URL.

</details>

#### [DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)
`HF Daily Paper` · 2026-04 · [PDF](https://arxiv.org/pdf/2604.14683)

> **TL;DR.** A reproducible benchmark for multimodal, multi-file deep-research report generation built from real user materials with a per-task static sandbox (supportive docs + distractors + noise) and a 5-dimension, human-aligned evaluation.

<details><summary>Abstract</summary>

Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR³-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR³-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR³-Agent based on multiple state-of-the-art language models demonstrate that DR³-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

</details>

#### [Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?](https://arxiv.org/abs/2604.03016)
2026-04 · [PDF](https://arxiv.org/pdf/2604.03016)

> **TL;DR.** A process-verified benchmark (418 tasks, 6 domains, 2000+ stepwise checkpoints) auditing whether multimodal agents actually invoke visual and search tools correctly and efficiently; best model Gemini3-pro 56.3%, falling to 23% at Level-3.

<details><summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) are evolving from passive observers into active agents, solving problems through Visual Expansion (invoking visual tools) and Knowledge Expansion (open-web search). However, existing evaluations fall short: they lack flexible tool integration, test visual and search tools separately, and evaluate primarily by final answers. Consequently, they cannot verify if tools were actually invoked, applied correctly, or used efficiently. To address this, we introduce Agentic-MME, a process-verified benchmark for Multimodal Agentic Capabilities. It contains 418 real-world tasks across 6 domains and 3 difficulty levels to evaluate capability synergy, featuring over 2,000 stepwise checkpoints that average 10+ person-hours of manual annotation per task. Each task includes a unified evaluation framework supporting sandboxed code and APIs, alongside a human reference trajectory annotated with stepwise checkpoints along dual-axis: S-axis and V-axis. To enable true process-level verification, we audit fine-grained intermediate states rather than just final answers, and quantify efficiency via an overthinking metric relative to human trajectories. Experimental results show the best model, Gemini3-pro, achieves 56.3% overall accuracy, which falls significantly to 23.0% on Level-3 tasks, underscoring the difficulty of real-world multimodal agentic problem solving.

</details>

## Models & Methods

### Methods: Text

#### [DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data](https://arxiv.org/abs/2604.19859)
2026-04 · [PDF](https://arxiv.org/pdf/2604.19859)

> **TL;DR.** A 4B edge-scale deep-research agent trained on only ~10K open data (agentic SFT + IGPO-based RL with information-gain turn rewards); beats sub-9B agents and narrows the gap to 30B-class systems.

<details><summary>Abstract</summary>

Edge-scale deep research agents based on small language models are attractive for real-world deployment due to their advantages in cost, latency, and privacy. In this work, we study how to train a strong small deep research agent under limited open-data by improving both data quality and data utilization. We present DR-Venus, a frontier 4B deep research agent for edge-scale deployment, built entirely on open data. Our training recipe consists of two stages. In the first stage, we use agentic supervised fine-tuning (SFT) to establish basic agentic capability, combining strict data cleaning with resampling of long-horizon trajectories to improve data quality and utilization. In the second stage, we apply agentic reinforcement learning (RL) to further improve execution reliability on long-horizon deep research tasks. To make RL effective for small agents in this setting, we build on IGPO and design turn-level rewards based on information gain and format-aware regularization, thereby enhancing supervision density and turn-level credit assignment. Built entirely on roughly 10K open-data, DR-Venus-4B significantly outperforms prior agentic models under 9B parameters on multiple deep research benchmarks, while also narrowing the gap to much larger 30B-class systems. Our further analysis shows that 4B agents already possess surprisingly strong performance potential, highlighting both the deployment promise of small models and the value of test-time scaling in this setting. We release our models, code, and key recipes to support reproducible research on edge-scale deep research agents.

</details>

#### [DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research](https://arxiv.org/abs/2511.19399)
2025-11 · [PDF](https://arxiv.org/pdf/2511.19399)

> **TL;DR.** The first fully-open model trained directly for long-form deep research, via Reinforcement Learning with Evolving Rubrics (RLER); DR Tulu-8B beats open agents by 15.6% and matches OpenAI DR at ~1000x lower cost per query.

<details><summary>Abstract</summary>

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with Reinforcement Learning with Evolving Rubrics (RLER), where rubrics are constructed and maintained to co-evolve with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop Deep Research Tulu (DR Tulu-8B), the first fully open model that is directly trained for open-ended, long-form deep research. Across four long-form deep research benchmarks in science, healthcare, and general domains, DR Tulu substantially outperforms existing open deep research agents (by 15.6% over Tongyi DR on average) and matches or exceeds proprietary deep research agents (by 0.7% over OpenAI DR on average), while being significantly smaller and cheaper per query (1000x cheaper than OpenAI DR per query).

</details>

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

#### [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516)
`COLM 2025 Oral` · 2025-03 · [PDF](https://arxiv.org/pdf/2503.09516)

> **TL;DR.** An RL framework where an LLM learns to autonomously issue multi-turn search queries during step-by-step reasoning (with retrieved-token masking and outcome-based rewards), improving QA by 20-41% over RAG baselines.

<details><summary>Abstract</summary>

Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact optimally with the search engine. This paper introduces Search-R1, an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval. Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions, leveraging retrieved token masking for stable RL training and a simple outcome-based reward function. Experiments on seven question-answering datasets show that Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines under the same setting. This paper further provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning. The code and model checkpoints are available at this https URL.

</details>

#### [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)
[Code](https://github.com/TIGER-AI-Lab/OpenResearcher) [![Stars](https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=social)](https://github.com/TIGER-AI-Lab/OpenResearcher)

> **TL;DR.** Data-synthesis pipeline; SFT + distillation only, with GPT-OSS as the teacher.

### Methods: Multimodal

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

#### [HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177)
2026-05 · [PDF](https://arxiv.org/pdf/2605.07177)

> **TL;DR.** A parallel multimodal search agent that fuses grounding and retrieval into one atomic action (search wider, not longer), trained with dual-grained efficiency-aware RL; introduces the IMEB benchmark; HyperEyes-30B beats the best open agent by 9.9% with 5.3x fewer tool rounds.

<details><summary>Abstract</summary>

Existing multimodal search agents process target entities sequentially, issuing one tool call per entity and accumulating redundant interaction rounds whenever a query decomposes into independent sub-retrievals. We argue that effective multimodal agents should search wider rather than longer: dispatching multiple grounded queries concurrently within a round. To this end, we present HyperEyes, a parallel multimodal search agent that fuses visual grounding and retrieval into a single atomic action, enabling concurrent search across multiple entities while treating inference efficiency as a first-class training objective. HyperEyes is trained in two stages. For cold-start supervision, we develop a Parallel-Amenable Data Synthesis Pipeline covering visual multi-entity and textual multi-constraint queries, curating efficiency-oriented trajectories via Progressive Rejection Sampling. Building on this, our central contribution, a Dual-Grained Efficiency-Aware Reinforcement Learning framework, operates at two levels. At the macro level, we propose TRACE (Tool-use Reference-Adaptive Cost Efficiency), a trajectory-level reward whose reference is monotonically tightened during training to suppress superfluous tool calls without restricting genuine multi-hop search. At the micro level, we adapt On-Policy Distillation to inject dense token-level corrective signals from an external teacher on failed rollouts, mitigating the credit-assignment deficiency of sparse outcome rewards. Since existing benchmarks evaluate accuracy as the sole metric, omitting inference cost, we introduce IMEB, a human-curated benchmark of 300 instances that jointly evaluates search capability and efficiency. Across six benchmarks, HyperEyes-30B surpasses the strongest comparable open-source agent by 9.9% in accuracy with 5.3x fewer tool-call rounds on average.

</details>

#### [OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents](https://arxiv.org/abs/2605.05185)
2026-05 · [PDF](https://arxiv.org/pdf/2605.05185)

> **TL;DR.** A fully open recipe for multimodal deep-search agents: Wikipedia-path data synthesis (SFT-36k + RL-8k), a unified text/image/OCR/crop/super-res tool environment, and fatal-aware GRPO; +10 points average across seven benchmarks.

<details><summary>Abstract</summary>

Deep search has become a crucial capability for frontier multimodal agents, enabling models to solve complex questions through active search, evidence verification, and multi-step reasoning. Despite rapid progress, top-tier multimodal search agents remain difficult to reproduce, largely due to the absence of open high-quality training data, transparent trajectory synthesis pipelines, or detailed training recipes. To this end, we introduce OpenSearch-VL, a fully open-source recipe for training frontier multimodal deep search agents with agentic reinforcement learning. First, we curated a dedicated pipeline to construct high-quality training data through Wikipedia path sampling, fuzzy entity rewriting, and source-anchor visual grounding, which jointly reduce shortcuts and one-step retrieval collapse. Based on this pipeline, we curate two training datasets, SearchVL-SFT-36k for SFT and SearchVL-RL-8k for RL. Besides, we design a diverse tool environment that unifies text search, image search, OCR, cropping, sharpening, super-resolution, and perspective correction, enabling agents to combine active perception with external knowledge acquisition. Finally, we propose a multi-turn fatal-aware GRPO training algorithm that handles cascading tool failures by masking post-failure tokens while preserving useful pre-failure reasoning through one-sided advantage clamping. Built on this recipe, OpenSearch-VL delivers substantial performance gains, with over 10-point average improvements across seven benchmarks, and achieves results comparable to proprietary commercial models on several tasks. We will release all data, code, and models to support open research on multimodal deep search agents.

</details>

#### [Towards Long-horizon Agentic Multimodal Search](https://arxiv.org/abs/2604.12890)
2026-04 · [PDF](https://arxiv.org/pdf/2604.12890)

> **TL;DR.** A long-horizon multimodal search framework (LMM-Searcher) that offloads visual assets to a file system with UID references plus on-demand image fetching; 12K distilled trajectories fine-tune Qwen3-VL-30B, scaling to 100-turn search.

<details><summary>Abstract</summary>

Multimodal deep search agents have shown great potential in solving complex tasks by iteratively collecting textual and visual evidence. However, managing the heterogeneous information and high token costs associated with multimodal inputs over long horizons remains a critical challenge, as existing methods often suffer from context explosion or the loss of crucial visual signals. To address this, we propose a novel Long-horizon MultiModal deep search framework, named LMM-Searcher, centered on a file-based visual representation mechanism. By offloading visual assets to an external file system and mapping them to lightweight textual identifiers (UIDs), our approach mitigates context overhead while preserving multimodal information for future access. We equip the agent with a tailored fetch-image tool, enabling a progressive, on-demand visual loading strategy for active perception. Furthermore, we introduce a data synthesis pipeline designed to generate queries requiring complex cross-modal multi-hop reasoning. Using this pipeline, we distill 12K high-quality trajectories to fine-tune Qwen3-VL-Thinking-30A3B into a specialized multimodal deep search agent. Extensive experiments across four benchmarks demonstrate that our method successfully scales to 100-turn search horizons, achieving state-of-the-art performance among open-source models on challenging long-horizon benchmarks like MM-BrowseComp and MMSearch-Plus, while also exhibiting strong generalizability across different base models. Our code will be released in this https URL.

</details>

#### [MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline](https://arxiv.org/abs/2603.01050)
2026-03 · LLaMA-Factory + VeRL · eval-only release · [PDF](https://arxiv.org/pdf/2603.01050) · [Code](https://github.com/HJYao00/MM-DeepResearch) [![Stars](https://img.shields.io/github/stars/HJYao00/MM-DeepResearch?style=social)](https://github.com/HJYao00/MM-DeepResearch)

> **TL;DR.** A multimodal deep-research agent built from hypergraph-generated search-intensive QA (Hyper-Search) and tree-searched tool-expert trajectories (DR-TTS) over an offline multi-tool search engine for agentic RL.

<details><summary>Abstract</summary>

We aim to develop a multimodal research agent capable of explicit reasoning and planning, multi-tool invocation, and cross-modal information synthesis, enabling it to conduct deep research tasks. However, we observe three main challenges in developing such agents: (1) scarcity of search-intensive multimodal QA data, (2) lack of effective search trajectories, and (3) prohibitive cost of training with online search APIs. To tackle them, we first propose Hyper-Search, a hypergraph-based QA generation method that models and connects visual and textual nodes within and across modalities, enabling to generate search-intensive multimodal QA pairs that require invoking various search tools to solve. Second, we introduce DR-TTS, which first decomposes search-involved tasks into several categories according to search tool types, and respectively optimize specialized search tool experts for each tool. It then recomposes tool experts to jointly explore search trajectories via tree search, producing trajectories that successfully solve complex tasks using various search tools. Third, we build an offline search engine supporting multiple search tools, enabling agentic reinforcement learning without using costly online search APIs. With the three designs, we develop MM-DeepResearch, a powerful multimodal deep research agent, and extensive results shows its superiority across benchmarks. Code is available at https://github.com/HJYao00/MM-DeepResearch

</details>

#### [REDSearcher: A Scalable and Cost-Efficient Framework for Long-Horizon Search Agents](https://arxiv.org/abs/2602.14234)
2026-02 · [PDF](https://arxiv.org/pdf/2602.14234)

> **TL;DR.** A unified framework co-designing complex task synthesis (graph-topology difficulty control), mid-training of atomic skills, and post-training; SOTA on text and multimodal search, releasing 10K text + 5K multimodal trajectories.

<details><summary>Abstract</summary>

Large language models are transitioning from general-purpose knowledge engines to real-world problem solvers, yet optimizing them for deep search tasks remains challenging. The central bottleneck lies in the extreme sparsity of high-quality search trajectories and reward signals, arising from the difficulty of scalable long-horizon task construction and the high cost of interaction-heavy rollouts involving external tool calls. To address these challenges, we propose REDSearcher, a unified framework that co-designs complex task synthesis, mid-training, and post-training for scalable search-agent optimization. Specifically, REDSearcher introduces the following improvements: (1) We frame task synthesis as a dual-constrained optimization, where task difficulty is precisely governed by graph topology and evidence dispersion, allowing scalable generation of complex, high-quality tasks. (2) We introduce tool-augmented queries to encourage proactive tool use rather than passive recall. (3) During mid-training, we strengthen core atomic capabilities (knowledge, planning, and function calling), substantially reducing the cost of collecting high-quality trajectories for downstream training. (4) We build a local simulated environment that enables rapid, low-cost algorithmic iteration for reinforcement learning experiments. Across both text-only and multimodal search-agent benchmarks, our approach achieves state-of-the-art performance. To facilitate future research on long-horizon search agents, we will release 10K high-quality complex text search trajectories, 5K multimodal trajectories and 1K text RL query set, together with code and model checkpoints.

</details>

#### [Seg-ReSearch: Segmentation with Interleaved Reasoning and External Search](https://arxiv.org/abs/2602.04454)
`ICML 2026` · 2026-02 · [PDF](https://arxiv.org/pdf/2602.04454)

> **TL;DR.** A segmentation paradigm that interleaves reasoning with external search so MLLM segmenters can handle open-world queries needing up-to-date or domain knowledge; introduces the OK-VOS benchmark.

<details><summary>Abstract</summary>

Segmentation based on language has been a popular topic in computer vision. While recent advances in multimodal large language models (MLLMs) have endowed segmentation systems with reasoning capabilities, these efforts remain confined by the frozen internal knowledge of MLLMs, which limits their potential for real-world scenarios that involve up-to-date information or domain-specific concepts. In this work, we propose Seg-ReSearch, a novel segmentation paradigm that overcomes the knowledge bottleneck of existing approaches. By enabling interleaved reasoning and external search, Seg-ReSearch empowers segmentation systems to handle dynamic, open-world queries that extend beyond the frozen knowledge of MLLMs. To effectively train this capability, we introduce a hierarchical reward design that harmonizes initial guidance with progressive incentives, mitigating the dilemma between sparse outcome signals and rigid step-wise supervision. For evaluation, we construct OK-VOS, a challenging benchmark that explicitly requires outside knowledge for video object segmentation. Experiments on OK-VOS and two existing reasoning segmentation benchmarks demonstrate that our Seg-ReSearch improves state-of-the-art approaches by a substantial margin. Code and data will be released at this https URL.

</details>

#### [Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models](https://arxiv.org/abs/2601.22060)
`MMLab` · Base: `Qwen3-VL` · rllm + VeRL · 2026-01 · [PDF](https://arxiv.org/pdf/2601.22060)

> **TL;DR.** A multimodal deep-research paradigm doing multi-turn, multi-entity, multi-scale visual + textual search robust to real-world noise (dozens of reasoning steps, hundreds of engine calls); cold-start + RL beats workflows on GPT-5 / Gemini-2.5-Pro / Claude-4-Sonnet.

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs) have achieved remarkable success across a broad range of vision tasks. However, constrained by the capacity of their internal world knowledge, prior work has proposed augmenting MLLMs by "reasoning-then-tool-call" for visual and textual search engines to obtain substantial gains on tasks requiring extensive factual information. However, these approaches typically define multimodal search in a naive setting, assuming that a single full-level or entity-level image query and few text query suffices to retrieve the key evidence needed to answer the question, which is unrealistic in real-world scenarios with substantial visual noise. Moreover, they are often limited in the reasoning depth and search breadth, making it difficult to solve complex questions that require aggregating evidence from diverse visual and textual sources. Building on this, we propose Vision-DeepResearch, which proposes one new multimodal deep-research paradigm, i.e., performs multi-turn, multi-entity and multi-scale visual and textual search to robustly hit real-world search engines under heavy noise. Our Vision-DeepResearch supports dozens of reasoning steps and hundreds of engine interactions, while internalizing deep-research capabilities into the MLLM via cold-start supervision and RL training, resulting in a strong end-to-end multimodal deep-research MLLM. It substantially outperforming existing multimodal deep-research MLLMs, and workflows built on strong closed-source foundation model such as GPT-5, Gemini-2.5-pro and Claude-4-Sonnet. The code will be released in this https URL.

</details>

#### [Watching, Reasoning, and Searching: A Video Deep Research Benchmark on Open Web for Agentic Video Reasoning](https://arxiv.org/abs/2601.06943)
2026-01 · [PDF](https://arxiv.org/pdf/2601.06943)

> **TL;DR.** Introduces VideoDR, the first video deep-research benchmark requiring cross-frame anchor extraction, web retrieval, and multi-hop verification; finds agentic isn't consistently better than workflow, with goal drift the core bottleneck.

<details><summary>Abstract</summary>

In real-world video question answering scenarios, videos often provide only localized visual cues, while verifiable answers are distributed across the open web; models therefore need to jointly perform cross-frame clue extraction, iterative retrieval, and multi-hop reasoning-based verification. To bridge this gap, we construct the first video deep research benchmark, VideoDR. VideoDR centers on video-conditioned open-domain video question answering, requiring cross-frame visual anchor extraction, interactive web retrieval, and multi-hop reasoning over joint video-web evidence; through rigorous human annotation and quality control, we obtain high-quality video deep research samples spanning six semantic domains. We evaluate multiple closed-source and open-source multimodal large language models under both the Workflow and Agentic paradigms, and the results show that Agentic is not consistently superior to Workflow: its gains depend on a model's ability to maintain the initial video anchors over long retrieval chains. Further analysis indicates that goal drift and long-horizon consistency are the core bottlenecks. In sum, VideoDR provides a systematic benchmark for studying video agents in open-web settings and reveals the key challenges for next-generation video deep research agents.

</details>

#### [DeepEyesV2: Toward Agentic Multimodal Model](https://arxiv.org/abs/2511.05271)
`ICLR 2026 Poster` · `HF Daily Paper` · 2025-11 · [PDF](https://arxiv.org/pdf/2511.05271) · [Code](https://github.com/Visual-Agent)

> **TL;DR.** An agentic multimodal model trained with a cold-start + RL two-stage pipeline for robust tool use (code execution, web search, image ops); introduces RealX-Bench for real-world perception + search + reasoning.

<details><summary>Abstract</summary>

Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive benchmark designed to evaluate real-world multimodal reasoning, which inherently requires the integration of multiple capabilities, including perception, search, and reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative benchmarks, demonstrating its effectiveness across real-world understanding, mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2 exhibits task-adaptive tool invocation, tending to use image operations for perception tasks and numerical computations for reasoning tasks. Reinforcement learning further enables complex tool combinations and allows model to selectively invoke tools based on context. We hope our study can provide guidance for community in developing agentic multimodal models.

</details>

#### [Tongyi DeepResearch Technical Report](https://arxiv.org/abs/2510.24701)
`Alibaba` · 2025-10 · [PDF](https://arxiv.org/pdf/2510.24701) · [Code](https://github.com/Alibaba-NLP/DeepResearch) [![Stars](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=social)](https://github.com/Alibaba-NLP/DeepResearch) · [Model](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B)

> **TL;DR.** An agentic 30.5B-A3B (3.3B active) MoE LLM for long-horizon deep research, trained via agentic mid- and post-training on fully-synthetic data; SOTA on HLE, BrowseComp/-ZH, WebWalkerQA, and xbench.

<details><summary>Abstract</summary>

We present Tongyi DeepResearch, an agentic large language model, which is specifically designed for long-horizon, deep information-seeking research tasks. To incentivize autonomous deep research agency, Tongyi DeepResearch is developed through an end-to-end training framework that combines agentic mid-training and agentic post-training, enabling scalable reasoning and information seeking across complex tasks. We design a highly scalable data synthesis pipeline that is fully automatic, without relying on costly human annotation, and empowers all training stages. By constructing customized environments for each stage, our system enables stable and consistent interactions throughout. Tongyi DeepResearch, featuring 30.5 billion total parameters, with only 3.3 billion activated per token, achieves state-of-the-art performance across a range of agentic deep research benchmarks, including Humanity's Last Exam, BrowseComp, BrowseComp-ZH, WebWalkerQA, xbench-DeepSearch, FRAMES and xbench-DeepSearch-2510. We open-source the model, framework, and complete solutions to empower the community.

</details>

#### [DeepMMSearch-R1: Empowering Multimodal LLMs in Multimodal Web Search](https://arxiv.org/abs/2510.12801)
2025-10 · [PDF](https://arxiv.org/pdf/2510.12801)

> **TL;DR.** An MLLM doing on-demand multi-turn web search that crops the input image to drive image search and iteratively rewrites text queries with self-correction; trained via SFT cold-start + online RL on DeepMMSearchVQA.

<details><summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) in real-world applications require access to external knowledge sources and must remain responsive to the dynamic and ever-changing real-world information in order to address information-seeking and knowledge-intensive user queries. Existing approaches, such as retrieval augmented generation (RAG) methods, search agents, and search equipped MLLMs, often suffer from rigid pipelines, excessive search calls, and poorly constructed search queries, which result in inefficiencies and suboptimal outcomes. To address these limitations, we present DeepMMSearch-R1, the first multimodal LLM capable of performing on-demand, multi-turn web searches and dynamically crafting queries for both image and text search tools. Specifically, DeepMMSearch-R1 can initiate web searches based on relevant crops of the input image making the image search more effective, and can iteratively adapt text search queries based on retrieved information, thereby enabling self-reflection and self-correction. Our approach relies on a two-stage training pipeline: a cold start supervised finetuning phase followed by an online reinforcement learning optimization. For training, we introduce DeepMMSearchVQA, a novel multimodal VQA dataset created through an automated pipeline intermixed with real-world information from web search tools. This dataset contains diverse, multi-hop queries that integrate textual and visual information, teaching the model when to search, what to search for, which search tool to use and how to reason over the retrieved information. We conduct extensive experiments across a range of knowledge-intensive benchmarks to demonstrate the superiority of our approach. Finally, we analyze the results and provide insights that are valuable for advancing multimodal web-search.

</details>

#### [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/abs/2508.05748)
`Alibaba` · `ICLR 2026` · 2025-08 · Base: `Qwen2.5-VL` · LLaMA-Factory + VeRL · [PDF](https://arxiv.org/pdf/2508.05748)

> **TL;DR.** A vision-language deep-research agent (synthetic-trajectory cold start plus RL) that also introduces the BrowseComp-VL benchmark.

<details><summary>Abstract</summary>

Web agents such as Deep Research have demonstrated superhuman cognitive abilities, capable of solving highly challenging information-seeking problems. However, most research remains primarily text-centric, overlooking visual information in the real world. This makes multimodal Deep Research highly challenging, as such agents require much stronger reasoning abilities in perception, logic, knowledge, and the use of more sophisticated tools compared to text-based agents. To address this limitation, we introduce WebWatcher, a multi-modal Agent for Deep Research equipped with enhanced visual-language reasoning capabilities. It leverages high-quality synthetic multimodal trajectories for efficient cold start training, utilizes various tools for deep reasoning, and further enhances generalization through reinforcement learning. To better evaluate the capabilities of multimodal agents, we propose BrowseComp-VL, a benchmark with BrowseComp-style that requires complex information retrieval involving both visual and textual information. Experimental results show that WebWatcher significantly outperforms proprietary baseline, RAG workflow and open-source agents in four challenging VQA benchmarks, which paves the way for solving complex multimodal information-seeking tasks.

</details>

#### [MMSearch-R1: Incentivizing LMMs to Search](https://arxiv.org/abs/2506.20670)
`ACL 2026` · 2025-06 · [PDF](https://arxiv.org/pdf/2506.20670)

> **TL;DR.** The first end-to-end RL framework for on-demand multi-turn multimodal search (image + text tools) with a search-penalty reward; matches a larger RAG model while cutting search calls by 30%+.

<details><summary>Abstract</summary>

Robust deployment of large multimodal models (LMMs) in real-world scenarios requires access to external knowledge sources, given the complexity and dynamic nature of real-world information. Existing approaches such as retrieval-augmented generation (RAG) and prompt engineered search agents rely on rigid pipelines, often leading to inefficient or excessive search behaviors. We present MMSearch-R1, the first end-to-end reinforcement learning framework that enables LMMs to perform on-demand, multi-turn search in real-world Internet environments. Our framework integrates both image and text search tools, allowing the model to reason about when and how to invoke them guided by an outcome-based reward with a search penalty. To support training, We collect a multimodal search VQA dataset through a semi-automated pipeline that covers diverse visual and textual knowledge needs and curate a search-balanced subset with both search-required and search-free samples, which proves essential for shaping efficient and on-demand search behavior. Extensive experiments on knowledge-intensive and info-seeking VQA tasks show that our model not only outperforms RAG-based baselines of the same model size, but also matches the performance of a larger RAG-based model while reducing search calls by over 30%. We further analyze key empirical findings to offer actionable insights for advancing research in multimodal search.

</details>

#### [Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports From Scratch with Agentic Framework](https://arxiv.org/abs/2506.02454)
`AAAI 2026 Oral` · 2025-06 · [PDF](https://arxiv.org/pdf/2506.02454) · [Code](https://github.com/rickyang1114/multimodal-deepresearcher) [![Stars](https://img.shields.io/github/stars/rickyang1114/multimodal-deepresearcher?style=social)](https://github.com/rickyang1114/multimodal-deepresearcher)

> **TL;DR.** An agentic framework that writes text-chart interleaved reports via a Formal Description of Visualization (FDV) representation; 82% win rate over the baseline, with a new MultimodalReportBench.

<details><summary>Abstract</summary>

Visualizations play a crucial part in effective communication of concepts and information. Recent advances in reasoning and retrieval augmented generation have enabled Large Language Models (LLMs) to perform deep research and generate comprehensive reports. Despite its progress, existing deep research frameworks primarily focus on generating text-only content, leaving the automated generation of interleaved texts and visualizations underexplored. This novel task poses key challenges in designing informative visualizations and effectively integrating them with text reports. To address these challenges, we propose Formal Description of Visualization (FDV), a structured textual representation of charts that enables LLMs to learn from and generate diverse, high-quality visualizations. Building on this representation, we introduce Multimodal DeepResearcher, an agentic framework that decomposes the task into four stages: (1) researching, (2) exemplar report textualization, (3) planning, and (4) multimodal report generation. For the evaluation of generated multimodal reports, we develop MultimodalReportBench, which contains 100 diverse topics served as inputs along with 5 dedicated metrics. Extensive experiments across models and evaluation methods demonstrate the effectiveness of Multimodal DeepResearcher. Notably, utilizing the same Claude 3.7 Sonnet model, Multimodal DeepResearcher achieves an 82% overall win rate over the baseline method.

</details>

#### [OmniSearch: Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent](https://arxiv.org/abs/2411.02937)
`ICLR 2025` · 2024-11 · [PDF](https://arxiv.org/pdf/2411.02937)

> **TL;DR.** Introduces the Dyn-VQA dataset (rapidly-changing, multimodal, multi-hop questions) and OmniSearch, a self-adaptive planning agent that decomposes multimodal questions into retrieval sub-question chains.

<details><summary>Abstract</summary>

Multimodal Retrieval Augmented Generation (mRAG) plays an important role in mitigating the "hallucination" issue inherent in multimodal large language models (MLLMs). Although promising, existing heuristic mRAGs typically predefined fixed retrieval processes, which causes two issues: (1) Non-adaptive Retrieval Queries. (2) Overloaded Retrieval Queries. However, these flaws cannot be adequately reflected by current knowledge-seeking visual question answering (VQA) datasets, since the most required knowledge can be readily obtained with a standard two-step retrieval. To bridge the dataset gap, we first construct Dyn-VQA dataset, consisting of three types of "dynamic" questions, which require complex knowledge retrieval strategies variable in query, tool, and time: (1) Questions with rapidly changing answers. (2) Questions requiring multi-modal knowledge. (3) Multi-hop questions. Experiments on Dyn-VQA reveal that existing heuristic mRAGs struggle to provide sufficient and precisely relevant knowledge for dynamic questions due to their rigid retrieval processes. Hence, we further propose the first self-adaptive planning agent for multimodal retrieval, OmniSearch. The underlying idea is to emulate the human behavior in question solution which dynamically decomposes complex multimodal questions into sub-question chains with retrieval action. Extensive experiments prove the effectiveness of our OmniSearch, also provide direction for advancing mRAG. The code and dataset will be open-sourced at this https URL.

</details>

#### [Visual Agentic Reinforcement Fine-Tuning](https://arxiv.org/abs/2505.14246)
`Shanghai AI Lab` · `arXiv 2505` · 2025-05 · Base: `Qwen2.5-VL` · [PDF](https://arxiv.org/pdf/2505.14246) · [Code](https://github.com/Liuziyu77/Visual-RFT) [![Stars](https://img.shields.io/github/stars/Liuziyu77/Visual-RFT?style=social)](https://github.com/Liuziyu77/Visual-RFT)

> **TL;DR.** Agentic RL fine-tuning that teaches LVLMs to browse the web and write image-processing code, plus the MAT bench (MAT-Search / MAT-Coding).

<details><summary>Abstract</summary>

A key trend in Large Reasoning Models (e.g., OpenAI's o3) is the native agentic ability to use external tools such as web browsers for searching and writing/executing code for image manipulation to think with images. In the open-source research community, while significant progress has been made in language-only agentic abilities such as function calling and tool integration, the development of multi-modal agentic capabilities that involve truly thinking with images, and their corresponding benchmarks, are still less explored. This work highlights the effectiveness of Visual Agentic Reinforcement Fine-Tuning (Visual-ARFT) for enabling flexible and adaptive reasoning abilities for Large Vision-Language Models (LVLMs). With Visual-ARFT, open-source LVLMs gain the ability to browse websites for real-time information updates and write code to manipulate and analyze input images through cropping, rotation, and other image processing techniques. We also present a Multi-modal Agentic Tool Bench (MAT) with two settings (MAT-Search and MAT-Coding) designed to evaluate LVLMs' agentic search and coding abilities. Our experimental results demonstrate that Visual-ARFT outperforms its baseline by +18.6% F1 / +13.0% EM on MAT-Coding and +10.3% F1 / +8.7% EM on MAT-Search, ultimately surpassing GPT-4o. Visual-ARFT also achieves +29.3 F1% / +25.9% EM gains on existing multi-hop QA benchmarks such as 2Wiki and HotpotQA, demonstrating strong generalization capabilities. Our findings suggest that Visual-ARFT offers a promising path toward building robust and generalizable multimodal agents.

</details>

#### [SenseNova-MARS: Empowering Multimodal Agentic Reasoning and Search via Reinforcement Learning](https://arxiv.org/abs/2512.24330)
`SenseTime` · `CVPR 2026` · 2025-12 · Base: `Qwen3-VL` · [PDF](https://arxiv.org/pdf/2512.24330) · [Code](https://github.com/OpenSenseNova/SenseNova-MARS) [![Stars](https://img.shields.io/github/stars/OpenSenseNova/SenseNova-MARS?style=social)](https://github.com/OpenSenseNova/SenseNova-MARS)

> **TL;DR.** Interleaves visual reasoning with search and crop tools via BN-GSPO RL, and ships the high-resolution HR-MMSearch benchmark.

<details><summary>Abstract</summary>

While Vision-Language Models (VLMs) can solve complex tasks through agentic reasoning, their capabilities remain largely constrained to text-oriented chain-of-thought or isolated tool invocation. They fail to exhibit the human-like proficiency required to seamlessly interleave dynamic tool manipulation with continuous reasoning, particularly in knowledge-intensive and visually complex scenarios that demand coordinated external tools such as search and image cropping. In this work, we introduce SenseNova-MARS, a novel Multimodal Agentic Reasoning and Search framework that empowers VLMs with interleaved visual reasoning and tool-use capabilities via reinforcement learning (RL). Specifically, SenseNova-MARS dynamically integrates the image search, text search, and image crop tools to tackle fine-grained and knowledge-intensive visual understanding challenges. In the RL stage, we propose the Batch-Normalized Group Sequence Policy Optimization (BN-GSPO) algorithm to improve the training stability and advance the model's ability to invoke tools and reason effectively. To comprehensively evaluate the agentic VLMs on complex visual tasks, we introduce the HR-MMSearch benchmark, the first search-oriented benchmark composed of high-resolution images with knowledge-intensive and search-driven questions. Experiments demonstrate that SenseNova-MARS achieves state-of-the-art performance on open-source search and fine-grained image understanding benchmarks. Specifically, on search-oriented benchmarks, SenseNova-MARS-32B scores 74.3 on MMSearch and 54.4 on HR-MMSearch, surpassing proprietary models such as Gemini-3-Pro and GPT-5.2. SenseNova-MARS represents a promising step toward agentic VLMs by providing effective and robust tool-use capabilities. To facilitate further research in this field, we will release all code, models, and datasets.

</details>

#### [VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning](https://arxiv.org/abs/2603.02795)
`IDEA` · `arXiv 2603` · 2026-03 · Base: `Qwen3-VL-8B` · [PDF](https://arxiv.org/pdf/2603.02795) · [Code](https://github.com/Ruiyang-061X/VSearcher) [![Stars](https://img.shields.io/github/stars/Ruiyang-061X/VSearcher?style=social)](https://github.com/Ruiyang-061X/VSearcher)

> **TL;DR.** Long-horizon multimodal search agent trained with SFT-then-RL on iteratively injected synthetic multimodal QA.

<details><summary>Abstract</summary>

Large models are increasingly becoming autonomous agents that interact with real-world environments and use external tools to augment their static capabilities. However, most recent progress has focused on text-only large language models, which are limited to a single modality and therefore have narrower application scenarios. On the other hand, multimodal large models, while offering stronger perceptual capabilities, remain limited to static knowledge and lack the ability to access and leverage up-to-date web information. In this paper, we propose VSearcher, turning static multimodal model into multimodal search agent capable of long-horizon, multi-turn tool use in real-world web environments, including text search, image search, and web browsing, via reinforcement learning. Specifically, we introduce Iterative Injection Data Synthesis pipeline to generate large-scale, complex multimodal QA questions, which are further filtered with comprehensive metrics to ensure high quality and sufficient difficulty. We then adopt an SFT-then-RL training pipeline to turn base multimodal models to agent capable of multi-turn tool calling in real-world web environments. Besides, we propose a multimodal search benchmark MM-SearchExam dedicated to evaluating search capabilities of multimodal search agents, which proves highly challenging for recent proprietary models. Extensive evaluations across multiple multimodal search benchmarks reveal effectiveness of our method. VSearcher achieves superior performance compared to recent multimodal search agents and even surpasses several proprietary models on multimodal web search tasks.

</details>

#### [MTA-Agent: An Open Recipe for Multimodal Deep Search Agents](https://arxiv.org/abs/2604.06376)
`Salesforce` · `arXiv 2604` · 2026-04 · [PDF](https://arxiv.org/pdf/2604.06376) · [Code](https://github.com/SalesforceAIResearch/MTA-Agent) [![Stars](https://img.shields.io/github/stars/SalesforceAIResearch/MTA-Agent?style=social)](https://github.com/SalesforceAIResearch/MTA-Agent)

> **TL;DR.** Tool-augmented synthesis agent that builds the verified 21K MTA-Vision-DeepSearch corpus (and MTA-Test) for training multimodal deep-search agents.

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs) have demonstrated strong capabilities in visual understanding, yet they remain limited in complex, multi-step reasoning that requires deep searching and integrating visual evidence with external knowledge. In this work, we address this challenge by constructing high-quality, verified multi-hop vision-language training data for multimodal deep-search agents. We propose a Multi-hop Tool-Augmented Agent for Evidence-based QA Synthesis (MTA-Agent), which automatically selects tools and their parameters to retrieve and validate evidence from both visual and textual sources and generates structured multi-hop question-answer trajectories. Starting from diverse VQA seed datasets, our pipeline produces a large-scale training dataset, MTA-Vision-DeepSearch, containing 21K high-quality multi-hop examples. The data is filtered through a multi-stage verification process to ensure factual consistency and answer uniqueness. Using MTA-Vision-DeepSearch, a 32B open-source multimodal search agent achieves state-of-the-art performance, reaching an average of 54.63% across six challenging benchmarks, outperforming GPT-5 (51.86%), Gemini-2.5-Pro (50.98%), and Gemini-3-Pro (54.46%) under the same tool settings. We further show that training on our data improves both reasoning depth and tool-use behavior, increasing the average number of steps from 2.27 to 4.28, and leading to more systematic and persistent search strategies. Additionally, we demonstrate that training can be performed without real-time tool calls by replaying cached interactions, significantly reducing training cost. Importantly, we present MTA-Agent as a fully open recipe for multimodal deep search: we release the entire dataset, training trajectories, and implementation details to enable reproducibility and future research on open multimodal search agents.

</details>

#### [POINTS-Seeker: An Open Recipe for Multimodal Search Agents with Visual Memory Management](https://arxiv.org/abs/2604.14029)
`SJTU` · `arXiv 2604` · 2026-04 · Base: `Qwen3-VL-8B` · [PDF](https://arxiv.org/pdf/2604.14029)

> **TL;DR.** Open recipe with Agentic Seeding cold-start and V-Fold memory that folds stale context into the visual space to fight context explosion.

<details><summary>Abstract</summary>

Large Multimodal Models (LMMs) excel at visual perception but struggle with real-time, knowledge-intensive queries due to their reliance on static parametric knowledge. While multimodal search agents offer a promising solution, developing them from vanilla LMMs presents two major challenges: the lack of open recipes to cultivate search agency from scratch, and the severe context explosion (attention dilution) that occurs during long-horizon multi-turn investigations. In this paper, we address both challenges by developing a native multimodal search agent. First, we introduce an open training recipe featuring Agentic Seeding, a formative training stage that bootstraps tool-use and planning abilities directly from a non-agentic foundation. Second, to overcome the context bottleneck, we propose V-Fold, an adaptive memory management mechanism. V-Fold retains recent interactions as high-fidelity text while folding stale historical context into the visual space via rendering, exploiting the model's cross-modal alignment to preserve raw evidence without text token redundancy. Combining these innovations, we present POINTS-Seeker-8B, which achieves state-of-the-art performance among models of comparable scale across six multimodal search benchmarks.

</details>

#### [Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents](https://arxiv.org/abs/2605.10832)
`HKUST` · `arXiv 2605` · 2026-05 · Base: `Qwen3-VL` · [PDF](https://arxiv.org/pdf/2605.10832) · [Code](https://github.com/JoeYing1019/ODE) [![Stars](https://img.shields.io/github/stars/JoeYing1019/ODE?style=social)](https://github.com/JoeYing1019/ODE)

> **TL;DR.** Visual-native harness with an image-bank reference protocol plus on-policy data evolution that regenerates training data from the current policy's failures.

<details><summary>Abstract</summary>

Multimodal deep search requires an agent to solve open-world problems by chaining search, tool use, and visual reasoning over evolving textual and visual context. Two bottlenecks limit current systems. First, existing tool-use harnesses treat images returned by search, browsing, or transformation as transient outputs, so intermediate visual evidence cannot be re-consumed by later tools. Second, training data is usually built by fixed curation recipes that cannot track the target agent's evolving capability. To address these challenges, we first introduce a visual-native agent harness centered on an image bank reference protocol, which registers every tool-returned image as an addressable reference and makes intermediate visual evidence reusable by later tools. On top of this harness, On-policy Data Evolution (ODE) runs a closed-loop data generator that refines itself across rounds from rollouts of the policy being trained. This per-round refinement makes each round's data target what the current policy still needs to learn. The same framework supports both diverse supervised fine-tuning data and policy-aware reinforcement learning data curation, covering the full training lifecycle of the target agent. Across 8 multimodal deep search benchmarks, ODE improves the Qwen3-VL-8B agent from 24.9% to 39.0% on average, surpassing Gemini-2.5 Pro in standard agent-workflow setting (37.9%). At 30B, ODE raises the average score from 30.6% to 41.5%. Further analyses validate the effectiveness of image-bank reuse, especially on complex tasks requiring iterative visual refinement, while rollout-feedback evolution yields more grounded SFT traces and better policy-matched RL tasks than static synthesis.

</details>

#### [Visual-Seeker: Towards Visual-Native Multimodal Agentic Search via Active Visual Reasoning](https://arxiv.org/abs/2606.15231)
`Ant Group` · `arXiv 2606` · 2026-06 · Base: `Qwen3-VL-8B` · [PDF](https://arxiv.org/pdf/2606.15231)

> **TL;DR.** Visual-native deep-search agent that actively harvests fine-grained visual evidence, trained on 5K synthesized active-visual-reasoning trajectories.

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs) have demonstrated impressive capabilities in many visual tasks, but they often struggle with factual grounding when confronted with complex, open-world scenarios. While recent multimodal deep search agents attempt to address this issue by utilizing external tools, the visual-native search paradigm remains underexplored. Existing methods primarily rely on simple images with explicit semantics and text-only evidence trajectories, limiting the agent's ability to perform multi-hop, cross-modal reasoning and search. To address these limitations, we propose Visual-Seeker, a visual-native multimodal deep search agent via active visual reasoning. Rather than treating vision as a static input, our agent actively attends to fine-grained visual details, dynamically harvests visual evidence throughout the search process. To unlock its visual-native potential, we design an active visual reasoning data pipeline and synthesize 5K high-quality multimodal trajectories for model training. Extensive experiments demonstrate the state-of-the-art performance across five challenging multimodal search benchmarks, even surpassing several proprietary models, validating robust visual-native reasoning and search in real-world web environments. The code and data can be accessed at: this https URL.

</details>

#### [TAPO: Tool-Aware Policy Optimization via Credit Transfer for Multimodal Search Agents](https://arxiv.org/abs/2606.05784)
`USTC` · `arXiv 2606` · 2026-06 · Base: `Qwen3-VL` · [PDF](https://arxiv.org/pdf/2606.05784)

> **TL;DR.** Fixes GRPO credit misassignment for tool calls via counterfactual witnesses and confidence-gated advantage correction.

<details><summary>Abstract</summary>

We identify and formally characterize credit misassignment as a systematic failure mode of GRPO in tool-augmented multimodal search agents: its uniform broadcast of trajectory-level advantages to all tokens causes valuable tool-use steps in failing trajectories to be penalized no differently from valueless ones. We further empirically quantify the scale of this phenomenon. Over half of failing trajectories and failing tool-use actions exhibit correctable credit misassignment, demonstrating that the wasted training signal is both substantial and structurally exploitable. Building on this insight, we propose Tool-Aware Policy Optimization (TAPO), which exploits the parameter-determinism property of information-acquisition tools: similar call parameters define equivalent information-acquisition actions and should therefore share comparable action credit. TAPO constructs counterfactual witnesses within the current training batch and compensates misassigned negative credit via confidence-gated conservative advantage correction. It requires no additional annotation, models, or sampling, and introduces negligible computational overhead. Across multiple multimodal search benchmarks, TAPO delivers consistent, plug-and-play improvements over strong baselines for three mainstream RL algorithms (GRPO, GSPO, and SAPO). Our code and models will be publicly released upon acceptance.

</details>

#### [SimpleSearch-VL: A Simple Recipe for Multimodal Agentic Deep Search](https://arxiv.org/abs/2606.31504)
`Ant Group` · `arXiv 2606` · 2026-06 · Base: `Qwen3-VL-8B/30B-A3B` · [PDF](https://arxiv.org/pdf/2606.31504) · [Code](https://github.com/AQ-MedAI/SimpleSearch-VL) [![Stars](https://img.shields.io/github/stars/AQ-MedAI/SimpleSearch-VL?style=social)](https://github.com/AQ-MedAI/SimpleSearch-VL)

> **TL;DR.** Simple recipe (5K SFT + 2K RL) with factorized adaptive rollout and evidence-verified reasoning; no extra tools or auxiliary models.

<details><summary>Abstract</summary>

We present SimpleSearch-VL, an efficient, reliable, and practical framework for multimodal agentic search. Its core idea is to improve the agent's own search-and-verification process rather than scaling data, tools, or auxiliary model components. For efficiency, Factorized Adaptive Rollout (FAR) improves sampling efficiency by forming more informative training groups while using redundant samples to mitigate long-tail latency and expose hard samples. For reliability, SimpleSearch-VL performs evidence-verified reasoning, explicitly using chain-of-thought verification to assess the relevance of retrieved visual and textual cues to the original context. For practicality, SimpleSearch-VL keeps a lightweight tool interface and performs webpage self-summary within the agent, requiring no additional external dependencies. With only 5K supervised tool-interleaved trajectories and 2K RL data, SimpleSearch-VL improves Qwen3-VL agentic baselines by 15.8 and 16.0 average points for the 8B and 30B-A3B variants, respectively. The SimpleSearch-VL-30B-A3B model further achieves performance competitive with agentic Gemini-3-Pro.

</details>

#### [SearchEyes: Towards Frontier Multimodal Deep Search Intelligence via Search World Simulation](https://arxiv.org/abs/2607.05943)
`CUHK` · `arXiv 2607` · 2026-07 · Base: `Qwen3.5-VL-9B/27B` · [PDF](https://arxiv.org/pdf/2607.05943) · [Code](https://github.com/Frostlinx/SearchEyes) [![Stars](https://img.shields.io/github/stars/Frostlinx/SearchEyes?style=social)](https://github.com/Frostlinx/SearchEyes)

> **TL;DR.** Simulates a reproducible search world over a typed knowledge graph and anchors step-level RL credit on hop metadata (HaPO); ships VisSearch-Bench.

<details><summary>Abstract</summary>

Training multimodal search agents to perform multi-hop reasoning remains challenging due to a fundamental structural disconnect: existing pipelines construct training data, search environments, and reward signals independently, causing synthesized structural metadata to be discarded, environments to rely on irreproducible external engines, and RL rewards to remain sparse at the trajectory level. We present SearchEyes, which uses a typed knowledge graph as the backbone of a simulated search world that unifies all three components. We propose Perception-Knowledge Chains (PKC) to sample constrained multi-hop paths over the visual-knowledge intersection of Wikidata5M, retaining hop-level entity metadata that simultaneously defines a self-contained search world and step-level reward anchors. We further propose Hop-Anchored Policy Optimization (HaPO), which reuses these anchors for step-level credit assignment without a separately trained process reward model. Experiments on six multimodal knowledge-intensive benchmarks show that SearchEyes achieves state-of-the-art performance among open-source multimodal search agents, with SearchEyes-27B improving over the strongest open-source baseline by 6.2 points on average.%

</details>

#### [DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal Agents](https://arxiv.org/abs/2608.01827)
`PKU` · `arXiv 2608` · 2026-08 · Base: `Qwen3-VL-8B/30B` · [PDF](https://arxiv.org/pdf/2608.01827) · [Code](https://github.com/Halcyon-Zhang/DeepVoyager-VL) [![Stars](https://img.shields.io/github/stars/Halcyon-Zhang/DeepVoyager-VL?style=social)](https://github.com/Halcyon-Zhang/DeepVoyager-VL)

> **TL;DR.** Vision-in-the-loop long-horizon search: a multimodal event graph drives data synthesis so intermediate visual evidence keeps driving retrieval.

<details><summary>Abstract</summary>

Multimodal large language models (MLLMs) have advanced visual understanding and reasoning, yet their static parametric knowledge limits their ability to address knowledge-intensive and dynamically evolving open-world problems. To move beyond this limitation, multimodal deep search has emerged as a key direction for open-world information access, evolving from single-turn factual retrieval toward long-horizon, multi-turn search guided by visual evidence. However, existing methods typically confine vision to the input or answer stage, overlooking its role in intermediate reasoning, and lack designs tailored to long-horizon interaction. Consequently, visual evidence rarely drives continued retrieval, constraining both interaction depth and reasoning span. To address these limitations, we propose DeepVoyager-VL, a long-horizon multimodal deep-search framework for vision-in-the-loop search. Specifically, we construct a multimodal event graph to drive data synthesis, yielding problems with intermediate visual dependencies and long reasoning chains. We then design an agent framework for active visual acquisition and on-demand image loading. Finally, we fine-tune models on the synthesized data without reinforcement learning. Extensive experiments across ten multimodal search benchmarks demonstrate the effectiveness of our method.

</details>

#### [Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent](https://arxiv.org/abs/2608.03979)
`USTC` · `arXiv 2608` · 2026-08 · Base: `Qwen3-VL-30B / 35B-A3B` · [PDF](https://arxiv.org/pdf/2608.03979) · [Code](https://github.com/Osilly/Vision-DeepResearch) [![Stars](https://img.shields.io/github/stars/Osilly/Vision-DeepResearch?style=social)](https://github.com/Osilly/Vision-DeepResearch)

> **TL;DR.** Extends deep research to video with a decoupled perception-exploration pipeline and stage-wise tool unlocking; ships Video-DR-Bench.

<details><summary>Abstract</summary>

We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address these challenges, we propose Video-DR, featuring a decoupled perception-exploration pipeline with stage-wise tool unlocking that compels exhaustive cross-frame visual grounding prior to web retrieval. Our framework adopts a two-stage training recipe: supervised fine-tuning followed by Group Relative Policy Optimization (GRPO), enabling autonomous exploration that breaks the imitation-learning ceiling. Furthermore, we curate Video-DR-Bench, a human-AI collaborative benchmark comprising 200 complex, multi-hop VQA instances. Empirical results demonstrate that our Video-DeepResearch-35B-A3B establishes a new state-of-the-art of 64.0% average accuracy, surpassing proprietary Claude-4.5-Sonnet (59.0%) by 5.0 points and significantly outperforming GPT-5 (52.5%) and Gemini 2.5 Pro (57.5%). The 30B-A3B variant achieves 59.3%, competitive with Claude-4.5-Sonnet and demonstrating the effectiveness of our training paradigm even at compact scale. Code: this https URL.

</details>

#### [WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents](https://arxiv.org/abs/2608.28062)
`WeChat` · `arXiv 2608` · 2026-08 · Base: `Qwen3-VL-30B` · [PDF](https://arxiv.org/pdf/2608.28062)

> **TL;DR.** WeAgent-Harness gives retrieved images persistent disk references for native text-vision interaction, with runtime recovery for long-horizon rollouts.

<details><summary>Abstract</summary>

Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as text and omit tool-returned images from subsequent context, reducing visually grounded trajectories to text-only reasoning. Long-horizon interaction also compounds tool-call, response-length, timeout, and budget failures, which can discard salvageable trajectories, waste rollout computation, and disturb policy updates. To address these issues, we introduce WeAgent-Harness, a multimodal agentic harness that supports native text-vision interaction and runtime recovery. Retrieved images receive persistent disk references, allowing the model to inspect, process, and cite them throughout the trajectory. Based on this harness, we develop WeAgent-MMSearch, an integrated system spanning data construction, agentic post-training, and multimodal rollout. For data construction, a strong MLLM uses WeAgent-Harness to discover, synthesize, and verify MMSearch-style tasks and collect expert trajectories. During post-training, our Failure-Aware GSPO (FA-GSPO) recovers salvageable abnormal rollouts and filters invalid ones to improve bounded multimodal planning and search. We also introduce VisTarget-Bench, a 150-task human-verified benchmark that pairs each question with a held-out target image, distinguishing image-retrieval failures from visual-perception failures. Evaluation on VisTarget-Bench and seven public benchmarks shows that agentic post-training improves the average score by 19.22 points, enabling our model to outperform similarly sized open-source models and rival models with roughly ten times its parameter count.

</details>

#### [OmniGAIA: Towards Native Omni-Modal AI Agents](https://arxiv.org/abs/2602.22897)
`RUC` · `arXiv 2602` · 2026-02 · Base: `Qwen3.5-Omni` · [PDF](https://arxiv.org/pdf/2602.22897) · [Code](https://github.com/RUC-NLPIR/OmniGAIA) [![Stars](https://img.shields.io/github/stars/RUC-NLPIR/OmniGAIA?style=social)](https://github.com/RUC-NLPIR/OmniGAIA)

> **TL;DR.** Omni-modal agent benchmark (video / audio / image, 360 tasks) plus OmniAtlas, a native omni-modal agent trained with hindsight-guided trees and OmniDPO.

<details><summary>Abstract</summary>

Human intelligence naturally intertwines omni-modal perception -- spanning vision, audio, and language -- with complex reasoning and tool usage to interact with the world. However, current multi-modal LLMs are primarily confined to bi-modal interactions (e.g., vision-language), lacking the unified cognitive capabilities required for general AI assistants. To bridge this gap, we introduce OmniGAIA, a comprehensive benchmark designed to evaluate omni-modal agents on tasks necessitating deep reasoning and multi-turn tool execution across video, audio, and image modalities. Constructed via a novel omni-modal event graph approach, OmniGAIA synthesizes complex, multi-hop queries derived from real-world data that require cross-modal reasoning and external tool integration. Furthermore, we propose OmniAtlas, a native omni-modal foundation agent under tool-integrated reasoning paradigm with active omni-modal perception. Trained on trajectories synthesized via a hindsight-guided tree exploration strategy and OmniDPO for fine-grained error correction, OmniAtlas effectively enhances the tool-use capabilities of existing open-source models. This work marks a step towards next-generation native omni-modal AI assistants for real-world scenarios.

</details>

### Proprietary Models

#### [Seed1.8 Model Card: Towards Generalized Real-World Agency](https://arxiv.org/abs/2603.20633)
2026-03 · [PDF](https://arxiv.org/pdf/2603.20633)

> **TL;DR.** A foundation-model card for generalized real-world agency: strong LLM + VLM with a unified agentic interface (search, code execution, GUI) and latency/cost-aware inference modes.

<details><summary>Abstract</summary>

We present Seed1.8, a foundation model aimed at generalized real-world agency: going beyond single-turn prediction to multi-turn interaction, tool use, and multi-step execution. Seed1.8 keeps strong LLM and vision-language performance while supporting a unified agentic interface-search, code generation and execution, and GUI interaction. For deployment, it offers latency- and cost-aware inference, including configurable thinking modes and optimized visual encoding for images and video. We report evaluations on standard benchmarks and application-aligned workflows spanning foundational skills, multimodal understanding, and agentic behavior. Seed1.8 is released to support further research and development on interactive, real-world use cases.

</details>

#### [SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents](https://arxiv.org/abs/2509.06283)
`Salesforce` · 2025-09 · [PDF](https://arxiv.org/pdf/2509.06283)

> **TL;DR.** Salesforce's recipe for autonomous single-agent deep research (minimal crawling + Python tools) via continual RL on reasoning models with synthetic data; SFR-DR-20B reaches 28.7% on Humanity's Last Exam.

<details><summary>Abstract</summary>

Equipping large language models (LLMs) with complex, interleaved reasoning and tool-use capabilities has become a key focus in agentic AI research, especially with recent advances in reasoning-oriented (``thinking'') models. Such capabilities are key to unlocking a number of important applications. One such application is Deep Research (DR), which requires extensive search and reasoning over many sources. Our work in this paper focuses on the development of native Autonomous Single-Agent models for DR featuring minimal web crawling and Python tool integration. Unlike multi-agent systems, where agents take up pre-defined roles and are told what to do at each step in a static workflow, an autonomous single-agent determines its next action dynamically based on context, without manual directive. While prior work has proposed training recipes for base or instruction-tuned LLMs, we focus on continual reinforcement learning (RL) of reasoning-optimized models to further enhance agentic skills while preserving reasoning ability. Towards this end, we propose a simple RL recipe with entirely synthetic data, which we apply to various open-source LLMs. Our best variant SFR-DR-20B achieves up to 28.7% on Humanity's Last Exam benchmark. In addition, we conduct key analysis experiments to provide more insights into our methodologies.

</details>

#### [OpenAI Deep Research](https://openai.com/index/introducing-deep-research/)

> **TL;DR.** _Proprietary product (no paper); product announcement linked._

#### [Gemini Deep Research (Google)](https://gemini.google/overview/deep-research/)

> **TL;DR.** _Proprietary product (no paper); product page linked._

#### [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)

> **TL;DR.** _Proprietary product (no paper); product announcement linked._

#### [Grok DeepSearch](https://grok.com/project/deepsearch)

> **TL;DR.** _Proprietary product (no paper); product page linked._

### Open Data Synthesis for Deep Research

#### [LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents](https://arxiv.org/abs/2605.05191)
2026-05 · [PDF](https://arxiv.org/pdf/2605.05191)

> **TL;DR.** Context-ReAct, an elastic context-management paradigm (Skip/Compress/Rollback/Snippet/Delete); LongSeeker (Qwen3-30B-A3B, 10k trajectories) hits 61.5% BrowseComp / 62.5% BrowseComp-ZH, beating Tongyi DeepResearch.

<details><summary>Abstract</summary>

Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information. Naively accumulating all intermediate content can overwhelm the agent, increasing costs and the risk of errors. We propose that effective context management should be adaptive: parts of the agent's trajectory are maintained at different levels of detail depending on their current relevance to the task. To operationalize this principle, we introduce Context-ReAct, a general agentic paradigm for elastic context orchestration that integrates reasoning, context management, and tool use in a unified loop. Context-ReAct provides five atomic operations: Skip, Compress, Rollback, Snippet and Delete, which allow the agent to dynamically reshape its working context, preserving important evidence, summarizing resolved information, discarding unhelpful branches, and controlling context size. We prove that the Compress operator is expressively complete, while the other specialized operators provide efficiency and fidelity guarantees that reduce generation cost and hallucination risk. Building on this paradigm, we develop LongSeeker, a long-horizon search agent fine-tuned from Qwen3-30B-A3B on 10k synthesized trajectories. Across four representative search benchmarks, LongSeeker achieves 61.5% on BrowseComp and 62.5% on BrowseComp-ZH, substantially outperforming Tongyi DeepResearch (43.2% and 46.7%) and AgentFold (36.2% and 47.3%). These results highlight the potential of adaptive context management, showing that agents can achieve more reliable and efficient long-horizon reasoning by actively shaping their working memory.

</details>

#### [ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://arxiv.org/abs/2605.03042)
2026-05 · [PDF](https://arxiv.org/pdf/2605.03042)

> **TL;DR.** An open-source autonomous-research harness using cross-model adversarial collaboration (executor + a different-family reviewer), 65+ Markdown skills, a research wiki, and a three-stage claim-to-evidence assurance layer to catch unsupported "successes".

<details><summary>Abstract</summary>

This report describes ARIS (Auto-Research-in-sleep), an open-source research harness for autonomous research, including its architecture, assurance mechanisms, and early deployment experience. The performance of agent systems built on LLMs depends on both the model weights and the harness around them, which governs what information to store, retrieve, and present to the model. For long-horizon research workflows, the central failure mode is not a visible breakdown but a plausible unsupported success: a long-running agent can produce claims whose evidential support is incomplete, misreported, or silently inherited from the executor's framing. Therefore, we present ARIS as a research harness that coordinates machine-learning research workflows through cross-model adversarial collaboration as a default configuration: an executor model drives forward progress while a reviewer from a different model family is recommended to critique intermediate artifacts and request revisions. ARIS has three architectural layers. The execution layer provides more than 65 reusable Markdown-defined skills, model integrations via MCP, a persistent research wiki for iterative reuse of prior findings, and deterministic figure generation. The orchestration layer coordinates five end-to-end workflows with adjustable effort settings and configurable routing to reviewer models. The assurance layer includes a three-stage process for checking whether experimental claims are supported by evidence: integrity verification, result-to-claim mapping, and claim auditing that cross-checks manuscript statements against the claim ledger and raw evidence, as well as a five-pass scientific-editing pipeline, mathematical-proof checks, and visual inspection of the rendered PDF. A prototype self-improvement loop records research traces and proposes harness improvements that are adopted only after reviewer approval.

</details>

#### [Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design](https://arxiv.org/abs/2603.28376)
2026-03 · [PDF](https://arxiv.org/pdf/2603.28376)

> **TL;DR.** A verification-centric deep-research agent that injects explicit verification into QA synthesis, trajectory construction, and test-time scaling; an 8B model rivals 30B agents on BrowseComp and BrowseComp-ZH.

<details><summary>Abstract</summary>

Deep research agents autonomously conduct open-ended investigations, integrating complex information retrieval with multi-step reasoning across diverse sources to solve real-world problems. To sustain this capability on long-horizon tasks, reliable verification is critical during both training and inference. A major bottleneck in existing paradigms stems from the lack of explicit verification mechanisms in QA data synthesis, trajectory construction, and test-time scaling. Errors introduced at each stage propagate downstream and degrade the overall agent performance. To address this, we present Marco DeepResearch, a deep research agent optimized with a verification-centric framework design at three levels: **(1) QA Data Synthesis:** We introduce verification mechanisms to graph-based and agent-based QA synthesis to control question difficulty while ensuring answers are unique and correct; **(2) Trajectory Construction:** We design a verification-driven trajectory synthesis method that injects explicit verification patterns into training trajectories; and **(3) Test-time scaling:** We use Marco DeepResearch itself as a verifier at inference time and effectively improve performance on challenging questions. Extensive experimental results demonstrate that our proposed Marco DeepResearch agent significantly outperforms 8B-scale deep research agents on most challenging benchmarks, such as BrowseComp and BrowseComp-ZH. Crucially, under a maximum budget of 600 tool calls, Marco DeepResearch even surpasses or approaches several 30B-scale agents, like Tongyi DeepResearch-30B.

</details>

#### [DLLM-Searcher: Adapting Diffusion Large Language Model for Search Agents](https://arxiv.org/abs/2602.07035)
2026-02 · [PDF](https://arxiv.org/pdf/2602.07035)

> **TL;DR.** Adapts diffusion LLMs into search agents via Agentic SFT plus Variance-Reduced Preference Optimization, with a Parallel-Reasoning-and-Acting (P-ReAct) paradigm that decodes tool calls while still thinking (~15% faster inference).

<details><summary>Abstract</summary>

Recently, Diffusion Large Language Models (dLLMs) have demonstrated unique efficiency advantages, enabled by their inherently parallel decoding mechanism and flexible generation paradigm. Meanwhile, despite the rapid advancement of Search Agents, their practical deployment is constrained by a fundamental limitation, termed as 1) Latency Challenge: the serial execution of multi-round reasoning, tool calling, and tool response waiting under the ReAct agent paradigm induces severe end-to-end latency. Intuitively, dLLMs can leverage their distinctive strengths to optimize the operational efficiency of agents under the ReAct agent paradigm. Practically, existing dLLM backbones face the 2) Agent Ability Challenge. That is, existing dLLMs exhibit remarkably weak reasoning and tool-calling capabilities, preventing these advantages from being effectively realized in practice. In this paper, we propose DLLM-Searcher, an optimization framework for dLLM-based Search Agents. To solve the Agent Ability Challenge, we design a two-stage post-training pipeline encompassing Agentic Supervised Fine-Tuning (Agentic SFT) and Agentic Variance-Reduced Preference Optimization Agentic VRPO, which enhances the backbone dLLM's information seeking and reasoning capabilities. To mitigate the Latency Challenge, we leverage the flexible generation mechanism of dLLMs and propose a novel agent paradigm termed Parallel-Reasoning and Acting P-ReAct. P-ReAct guides the model to prioritize decoding tool_call instructions, thereby allowing the model to keep thinking while waiting for the tool's return. Experimental results demonstrate that DLLM-Searcher achieves performance comparable to mainstream LLM-based search agents and P-ReAct delivers approximately 15% inference acceleration. Our code is available at this https URL

</details>

#### [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search](https://arxiv.org/abs/2509.25454)
2025-09 · [PDF](https://arxiv.org/pdf/2509.25454)

> **TL;DR.** Embeds Monte Carlo Tree Search directly into RLVR training (not just inference) for systematic exploration and step-level credit assignment; new SOTA math reasoning at 5.7x fewer GPU hours.

<details><summary>Abstract</summary>

Although RLVR has become an essential component for developing advanced reasoning skills in language models, contemporary studies have documented training plateaus after thousands of optimization steps, i.e., notable decreases in performance gains despite increased computational investment. This limitation stems from the sparse exploration patterns inherent in current RLVR practices, where models rely on limited rollouts that often miss critical reasoning paths and fail to provide systematic coverage of the solution space. We present DeepSearch, a framework that integrates Monte Carlo Tree Search (MCTS) directly into RLVR training. In contrast to existing methods that rely on tree search only at inference, DeepSearch embeds structured search into the training loop, enabling systematic exploration and fine-grained credit assignment across reasoning steps. Through training-time exploration, DeepSearch addresses the fundamental bottleneck of insufficient exploration, which leads to diminishing performance gains over prolonged training. Our contributions include: (1) a global frontier selection strategy that prioritizes promising nodes across the search tree, (2) selection with entropy-based guidance that identifies confident paths for supervision, and (3) adaptive replay buffer training with solution caching for efficiency. Experiments on mathematical reasoning benchmarks show that DeepSearch achieves an average accuracy of 62.95% and establishes a new state-of-the-art reasoning model, while using 5.7x fewer GPU hours than extended training approaches. These results highlight the importance of strategic exploration over brute-force scaling and demonstrate the promise of algorithmic innovation for advancing RLVR methodologies. DeepSearch establishes a new direction for scaling reasoning capabilities through systematic search rather than prolonged computation.

</details>

#### [Open Data Synthesis For Deep Research](https://arxiv.org/abs/2509.00375)
2025-08 · [PDF](https://arxiv.org/pdf/2509.00375)

> **TL;DR.** Formalizes deep research as Hierarchical Constraint Satisfaction Problems and presents InfoSeek (a dual-agent Research-Tree synthesis framework, 50K+ tasks); 3B models trained on it beat 32B baselines on BrowseComp-Plus. (NB: this InfoSeek is a data-synthesis framework, distinct from the visual-VQA InfoSeek under Training Data.)

<details><summary>Abstract</summary>

Large language models (LLMs) are increasingly expected to go beyond simple factual queries toward Deep Research-tasks that require decomposing questions into sub-problems, coordinating multi-step reasoning, and synthesizing evidence from diverse sources. We formalize Deep Research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs), which are fundamentally different from single-constraint, multi-hop, or flat CSP formulations. However, existing benchmarks (e.g., Natural Questions, HotpotQA) fail to capture this complexity, while recent synthetic datasets often introduce shortcut reasoning, knowledge leakage, or lack sufficient structural depth. To address this gap, we introduce InfoSeek, a scalable framework for synthesizing complex Deep Research tasks. InfoSeek uses a dual-agent system to recursively build a Research Tree from large-scale webpages, blurring intermediate nodes into valid sub-problems, and converting these trees into natural language questions that require traversing the full hierarchy. It also enables rapid scaling, yielding over 50K training examples, a curated test set, and reasoning trajectories generated via reject sampling. Experiments show that models trained on InfoSeek consistently outperform strong baselines. On a challenging benchmark BrowseComp-Plus, 3B LLMs optimized with InfoSeek surpass much larger 32B models and lightweight commercial APIs (e.g., Gemini2.5-Flash), while achieving performance comparable to stronger APIs (e.g., Gemini2.5-Pro). By preserving meta-information such as intermediate steps and retrieval labels, InfoSeek further supports advanced optimization strategies, including compound reward design and trajectory-level exploration. We provide our codes and datasets in this repository.

</details>

#### [MiroThinker](https://github.com/MiroMindAI/MiroThinker)
[Code](https://github.com/MiroMindAI/MiroThinker) [![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social)](https://github.com/MiroMindAI/MiroThinker)

> **TL;DR.** _pending._

### Generation (Search-Enhanced Generation)

#### [Unify-Agent: A Unified Multimodal Agent for World-Grounded Image Synthesis](https://arxiv.org/abs/2603.29620)
2026-03 · [PDF](https://arxiv.org/pdf/2603.29620)

> **TL;DR.** Reframes image generation as an agentic pipeline (prompt understanding, multimodal evidence search, grounded recaptioning, synthesis) for world-grounded synthesis of long-tail concepts; introduces the FactIP benchmark.

<details><summary>Abstract</summary>

Unified multimodal models provide a natural and promising architecture for understanding diverse and complex real-world knowledge while generating high-quality images. However, they still rely primarily on frozen parametric knowledge, which makes them struggle with real-world image generation involving long-tail and knowledge-intensive concepts. Inspired by the broad success of agents on real-world tasks, we explore agentic modeling to address this limitation. Specifically, we present Unify-Agent, a unified multimodal agent for world-grounded image synthesis, which reframes image generation as an agentic pipeline consisting of prompt understanding, multimodal evidence searching, grounded recaptioning, and final synthesis. To train our model, we construct a tailored multimodal data pipeline and curate 143K high-quality agent trajectories for world-grounded image synthesis, enabling effective supervision over the full agentic generation process. We further introduce FactIP, a benchmark covering 12 categories of culturally significant and long-tail factual concepts that explicitly requires external knowledge grounding. Extensive experiments show that our proposed Unify-Agent substantially improves over its base unified model across diverse benchmarks and real world generation tasks, while approaching the world knowledge capabilities of the strongest closed-source models. As an early exploration of agent-based modeling for world-grounded image synthesis, our work highlights the value of tightly coupling reasoning, searching, and generation for reliable open-world agentic image synthesis.

</details>

#### [Gen-Searcher: Reinforcing Agentic Search for Image Generation](https://arxiv.org/abs/2603.28767)
2026-03 · [PDF](https://arxiv.org/pdf/2603.28767)

> **TL;DR.** The first search-augmented image-generation agent: multi-hop search gathers textual knowledge and reference images for grounded generation (SFT + agentic RL with dual text/image rewards); +16 on KnowGen, which it also introduces.

<details><summary>Abstract</summary>

Recent image generation models have shown strong capabilities in generating high-fidelity and photorealistic images. However, they are fundamentally constrained by frozen internal knowledge, thus often failing on real-world scenarios that are knowledge-intensive or require up-to-date information. In this paper, we present Gen-Searcher, as the first attempt to train a search-augmented image generation agent, which performs multi-hop reasoning and search to collect the textual knowledge and reference images needed for grounded generation. To achieve this, we construct a tailored data pipeline and curate two high-quality datasets, Gen-Searcher-SFT-10k and Gen-Searcher-RL-6k, containing diverse search-intensive prompts and corresponding ground-truth synthesis images. We further introduce KnowGen, a comprehensive benchmark that explicitly requires search-grounded external knowledge for image generation and evaluates models from multiple dimensions. Based on these resources, we train Gen-Searcher with SFT followed by agentic reinforcement learning with dual reward feedback, which combines text-based and image-based rewards to provide more stable and informative learning signals for GRPO training. Experiments show that Gen-Searcher brings substantial gains, improving Qwen-Image by around 16 points on KnowGen and 15 points on WISE. We hope this work can serve as an open foundation for search agents in image generation, and we fully open-source our data, models, and code.

</details>

#### [Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation](https://arxiv.org/abs/2606.26907)
`Qwen` · `arXiv 2606` · 2026-06 · Base: `Qwen-Image 2.0` · [PDF](https://arxiv.org/pdf/2606.26907)

> **TL;DR.** Training-free agentic framework that closes the context gap in real-world T2I via context-aware planning, search, memory, and feedback; ships IA-Bench.

<details><summary>Abstract</summary>

While text-to-image (T2I) models have achieved remarkable progress, they struggle with real-world requests that are often underspecified, implicit, or dependent on up-to-date knowledge. We identify this challenge as the Context Gap: the mismatch between the user context and the sufficient generation context for T2I models. To bridge this gap, we propose Qwen-Image-Agent, a unified agentic framework that integrates plan, reason, search, memory and feedback in a context-centric manner. Qwen-Image-Agent treats user input as partial context and progressively constructs the generation context through Context-Aware Planning and Context Grounding. Specifically, Context-Aware Planning identifies missing context and plans how it should be acquired and used, while Context Grounding gathers this context from reason, search, memory, and feedback. To evaluate agentic image generation, we further introduce Image Agent Bench (IA-Bench), a benchmark covering four core image agent capabilities: Plan, Reason, Search, and Memory. Experiments on IA-Bench, Mindbench and WISE-Verified show that Qwen-Image-Agent outperforms strong baselines and achieves state-of-the-art performance.

</details>

#### [Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](https://arxiv.org/abs/2607.05382)
`University of Waterloo` · `arXiv 2607` · 2026-07 · Base: `Qwen-Image / Bagel-7B` · [PDF](https://arxiv.org/pdf/2607.05382) · [Code](https://github.com/HaozheH3/SearchGen) [![Stars](https://img.shields.io/github/stars/HaozheH3/SearchGen?style=social)](https://github.com/HaozheH3/SearchGen)

> **TL;DR.** Models a generator-specific knowledge boundary to decide when search should aid image generation; ships SearchGen-20K, a 1M offline corpus, and SearchGen-Bench.

<details><summary>Abstract</summary>

Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed multimodal SearchGen-Corpus-1M to support offline, reproducible research. On SearchGen-Bench, frontier open generators score only 21 to 28 out of 100, a 40-point collapse invisible to existing benchmarks. The natural remedy is to employ search tools, enabling agentic visual generation. However, we find that naive search fails: it retrieves indiscriminately, injecting noise into prompts the generator already handles. We trace the root cause to a generator-specific, evolving knowledge boundary: the divide between what a generator can internalize through training and what must remain in external context. Although this boundary is hard to specify in advance, we show that it is discoverable through a teach-then-search co-training framework. Even a minimal version of this co-training recipe produces monotonic improvement, laying the foundation for recursive self-improvement in visual generation that can meet world-knowledge-grounded requests. We release the full dataset, co-training corpus, and search corpus as a replayable harness for tool-augmented, world-knowledge-grounded visual generation.

</details>

#### [JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents](https://arxiv.org/abs/2607.23588)
`CUHK` · `arXiv 2607` · 2026-07 · [PDF](https://arxiv.org/pdf/2607.23588)

> **TL;DR.** Canvas-native open harness for long-horizon creative agents that keeps drafts, edits, tool actions, and feedback as an evolving project state.

<details><summary>Abstract</summary>

Creative AI is moving from single-step asset generation toward long-horizon multimodal production. Although recent generative models can synthesize high-quality images, videos, audio clips, UI elements, storyboards, slides, and other creative assets, real-world creative work requires more than isolated prompt-output interactions. It involves references, drafts, alternatives, edits, failed attempts, version relations, tool actions, evaluation signals, and human feedback, which together form an evolving project state. Existing prompt-based, chat-based, and node-based generation systems only partially support this state, as they often discard intermediate context, rely on linear conversations, or require manually specified workflows. Recent commercial systems indicate a shift toward agent-assisted creative production, but their closed architectures make it difficult to study how agents represent context, choose tools, revise artifacts, recover from failures, and maintain consistency over time. To address this gap, we introduce JarvisHub, a canvas-native creative agent harness for long-horizon multimodal creation. JarvisHub treats an editable canvas as the user workspace, the agent's external memory, action space, and shared project state, representing multimodal artifacts, dependencies, versions, and feedback as typed canvas nodes and links. Through a three-layer architecture of canvas state, protocol bridge, and agent runtime, JarvisHub enables agents to act within an inspectable and editable creative state. This design moves creative agents beyond isolated tool use toward sustained, human-steerable creative automation, where agents can progressively plan, generate, revise, and organize multimodal projects while users remain able to inspect, guide, and intervene throughout the process.

</details>

#### [ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation](https://arxiv.org/abs/2608.04436)
`RUC` · `arXiv 2608` · 2026-08 · Base: `Emu3.5` · [PDF](https://arxiv.org/pdf/2608.04436) · [Code](https://github.com/bubble65/EMU-Agentic-PostTrain) [![Stars](https://img.shields.io/github/stars/bubble65/EMU-Agentic-PostTrain?style=social)](https://github.com/bubble65/EMU-Agentic-PostTrain)

> **TL;DR.** Post-trains a unified multimodal model so one policy coordinates reasoning, tool use, and native image generation.

<details><summary>Abstract</summary>

Text-to-image (T2I) models can produce visually compelling images, yet they remain limited on open-world tasks that require complex semantic understanding, multi-step reasoning, and the integration of external world knowledge. Existing efforts introduce agent capabilities into image generation, but they either prescribe a fixed workflow or place only a subset of the open-world image generation process under agent control. Consequently, reasoning, tool invocation, and image generation are not coordinated by a single policy. We propose ToolArtist, a fully agentic image generation model obtained by post-training a Unified Multimodal Model (UMM). ToolArtist dynamically orchestrates reasoning, external tool use, and native image generation within one unified policy. During Supervised Fine-Tuning (SFT), we equip a teacher agent with search tools alongside an image-generation tool. We then convert the collected trajectories into a UMM compatible format, where the image-generation tool is concealed while the resulting generated images are retained. During Reinforcement Learning (RL), we develop an agentic RL infrastructure for UMMs and introduce Reason-Act-Draw GRPO (RAD-GRPO), which uses complementary intent and quality rewards to jointly optimize the model. Experiments show that placing the entire open-world image-generation process under an agent policy consistently outperforms approaches with fixed pipelines or only partially agent-controlled components. We release the training data and the complete post-training infrastructure.

</details>

#### [GenRouter: Unified Workflow Routing for Agentic Image Generation](https://arxiv.org/abs/2608.16721)
`HKUST` · `arXiv 2608` · 2026-08 · [PDF](https://arxiv.org/pdf/2608.16721) · [Code](https://github.com/EnVision-Research/GenRouter) [![Stars](https://img.shields.io/github/stars/EnVision-Research/GenRouter?style=social)](https://github.com/EnVision-Research/GenRouter)

> **TL;DR.** Routes each prompt to the cheapest sufficient agentic image-generation workflow via demand profiling, experience matching, and Pareto filtering.

<details><summary>Abstract</summary>

The rapid evolution of text-to-image (T2I) generation models has effectively solved the foundational challenge of raw pixel synthesis, shifting the community's focus toward fulfilling increasingly intricate user requests. While recent agentic image generation workflows enhance static inference with advanced capabilities like external knowledge retrieval and iterative reasoning, they mostly operate in isolated silos with fixed ``one-size-fits-all" topologies. This inevitably leads to severe compute-mismatch, where simple queries are forced through computationally heavy pipelines. To bridge this gap, we present GenRouter, the first unified workflow routing framework for agentic image generation. We first formulate GenCanvas, standardizing diverse agentic pipelines into a universal set of foundational primitives and executable templates. Operating over this unified space, GenRouter adaptively routes heterogeneous prompts to their optimal workflows via (i) demand profiling, (ii) experience matching, and (iii) Pareto filtering. Extensive experiments across diverse benchmarks demonstrate that GenRouter achieves superior visual alignment while reducing execution costs by over 95% and latency by 65% compared to heavyweight static pipelines. Furthermore, the system continuously self-evolves via accumulated experience, enabling robust zero-shot generalization that boosts performance and halves computational overhead.

</details>

#### [WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing](https://arxiv.org/abs/2609.05171)
`WeChat` · `arXiv 2609` · 2026-09 · [PDF](https://arxiv.org/pdf/2609.05171)

> **TL;DR.** Full-stack recipe (harness, data pipeline, benchmark, post-training) for knowledge-grounded agentic image generation and editing.

<details><summary>Abstract</summary>

Image generation and editing models have advanced rapidly, yet remain unreliable when prompts require external world knowledge. Bounded and long-tail parametric knowledge prevents direct or reason-then-generate approaches from recovering the required facts and visual appearances. Existing agentic generation and editing methods mitigate this limitation with retrieval tools, yet remain constrained by insufficient visual verification, overloaded policy models, and weak integration of retrieved textual and visual evidence. To address these limitations, we present WeAgent-MMGenEdit, a full-stack recipe including a multimodal harness, a scalable data construction pipeline, a comprehensive benchmark, and post-training methods for the agent policy and image backend. We first introduce WeAgent-Harness, a multimodal runtime with persistent evidence management and dedicated verification and integration tools that organize retrieved multimodal evidence into a dense carrier. Upon this, we develop a scalable pipeline for prompt synthesis and agentic trajectory collection, yielding 23K supervised trajectories and 14.7K RL tasks with three-layer verifiable checklists. We further introduce WeBench-MMGenEdit, a bilingual benchmark covering both knowledge-intensive image generation and multi-image editing. Finally, a two-sided post-training recipe based on SFT and RL improves the agent policy and image backend. Together, WeAgent-MMGenEdit enables a 30B-total/3B-active policy to outperform similarly sized policy models and approach the performance of a 1T-parameter agent.

</details>

### Perception (Search-Enhanced Perception)

_None yet._

### Misc

#### [Beyond Retrieval: A Multitask Benchmark and Model for Code Search](https://arxiv.org/abs/2605.04615)
2026-05 · [PDF](https://arxiv.org/pdf/2605.04615)

> **TL;DR.** CoREB, a contamination-limited multitask code-search benchmark (text-to-code, code-to-text, code-to-code) from rewritten LiveCodeBench, plus a fine-tuned reranker; short keyword queries collapse every model.

<details><summary>Abstract</summary>

Code search has usually been evaluated as first-stage retrieval, even though production systems rely on broader pipelines with reranking and developer-style queries. Existing benchmarks also suffer from data contamination, label noise, and degenerate binary relevance. In this paper, we introduce CoREB, a contamination-limited, multitask code retrieval and reranking benchmark, together with a fine-tuned code reranker, that goes beyond retrieval to cover the full code search pipeline. CoREB is built from counterfactually rewritten LiveCodeBench problems in five programming languages and delivered as timed releases with graded relevance judgments. We benchmark eleven embedding models and five rerankers across three tasks: text-to-code, code-to-text, and code-to-code. Our experiments reveal that: \circone code-specialised embeddings dominate code-to-code retrieval (${\sim}2{\times}$ over general encoders), yet no single model wins all three tasks; \circtwo short keyword queries, the format closest to real developer search, collapse every model to near-zero nDCG@10; \circthree off-the-shelf rerankers are task-asymmetric, with a 12-point swing on code-to-code and no baseline net-positive across all tasks; \circfour our fine-tuned CoREB-Reranker is the first to achieve consistent gains across all three tasks. The data and model are released.

</details>

#### [CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741)
2026-04 · [PDF](https://arxiv.org/pdf/2604.19741)

> **TL;DR.** A spatially-grounded video generative model that uses geo-registered data as context to simulate real locations, producing minutes-long 3D-consistent navigable sequences with stable weather/lighting and loop closure.

<details><summary>Abstract</summary>

We address the problem of generating a 3D-consistent, navigable environment that is spatially grounded: a simulation of a real location. Existing video generative models can produce a plausible sequence that is consistent with a text (T2V) or image (I2V) prompt. However, the capability to reconstruct the real world under arbitrary weather conditions and dynamic object configurations is essential for downstream applications including autonomous driving and robotics simulation. To this end, we present CityRAG, a video generative model that leverages large corpora of geo-registered data as context to ground generation to the physical scene, while maintaining learned priors for complex motion and appearance changes. CityRAG relies on temporally unaligned training data, which teaches the model to semantically disentangle the underlying scene from its transient attributes. Our experiments demonstrate that CityRAG can generate coherent minutes-long, physically grounded video sequences, maintain weather and lighting conditions over thousands of frames, achieve loop closure, and navigate complex trajectories to reconstruct real-world geography.

</details>

#### [MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/abs/2604.09852)
2026-04 · [PDF](https://arxiv.org/pdf/2604.09852)

> **TL;DR.** Teaches reasoning models to segment thinking into blocks and compress each into a dense memento summary, attending only to mementos; ~2.5x KV-cache reduction at maintained accuracy, with the OpenMementos dataset (228K traces).

<details><summary>Abstract</summary>

Reasoning models think in long, unstructured streams with no mechanism for compressing or organizing their own intermediate state. We introduce MEMENTO: a method that teaches models to segment reasoning into blocks, compress each block into a memento, i.e., a dense state summary, and reason forward by attending only to mementos, reducing context, KV cache, and compute. To train MEMENTO models, we release OpenMementos, a public dataset of 228K reasoning traces derived from OpenThoughts-v3, segmented and annotated with intermediate summaries. We show that a two-stage SFT recipe on OpenMementos is effective across different model families (Qwen3, Phi-4, Olmo 3) and scales (8B--32B parameters). Trained models maintain strong accuracy on math, science, and coding benchmarks while achieving ${\sim}2.5\times$ peak KV cache reduction. We extend vLLM to support our inference method, achieving ${\sim}1.75\times$ throughput improvement while also enabling us to perform RL and further improve accuracy. Finally, we identify a dual information stream: information from each reasoning block is carried both by the memento text and by the corresponding KV states, which retain implicit information from the original block. Removing this channel drops accuracy by 15 pp on AIME24.

</details>

#### [GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization](https://arxiv.org/abs/2511.15705)
2025-11 · [PDF](https://arxiv.org/pdf/2511.15705)

> **TL;DR.** An agentic geolocalization model that interleaves an image-zoom tool and a web-search tool in its reasoning (SFT cold-start + RL with hierarchical reward); introduces GeoBench and rivals Gemini-2.5-flash and GPT-5.

<details><summary>Abstract</summary>

Current research on agentic visual reasoning enables deep multimodal understanding but primarily focuses on image manipulation tools, leaving a gap toward more general-purpose agentic models. In this work, we revisit the geolocalization task, which requires not only nuanced visual grounding but also web search to confirm or refine hypotheses during reasoning. Since existing geolocalization benchmarks fail to meet the need for high-resolution imagery and the localization challenge for deep agentic reasoning, we curate GeoBench, a benchmark that includes photos and panoramas from around the world, along with a subset of satellite images of different cities to rigorously evaluate the geolocalization ability of agentic models. We also propose GeoVista, an agentic model that seamlessly integrates tool invocation within the reasoning loop, including an image-zoom-in tool to magnify regions of interest and a web-search tool to retrieve related web information. We develop a complete training pipeline for it, including a cold-start supervised fine-tuning (SFT) stage to learn reasoning patterns and tool-use priors, followed by a reinforcement learning (RL) stage to further enhance reasoning ability. We adopt a hierarchical reward to leverage multi-level geographical information and improve overall geolocalization performance. Experimental results show that GeoVista surpasses other open-source agentic models on the geolocalization task greatly and achieves performance comparable to closed-source models such as Gemini-2.5-flash and GPT-5 on most metrics.

</details>

#### [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking in Large Language Models](https://arxiv.org/abs/2505.17312)
2025-05 · [PDF](https://arxiv.org/pdf/2505.17312)

> **TL;DR.** An LLM-agnostic, RL-trained plugin that picks per-task reasoning configs (instruction format, temperature, step count); consistently beats fixed-config baselines across six LLMs.

<details><summary>Abstract</summary>

LLMs often need effective configurations, like temperature and reasoning steps, to handle tasks requiring sophisticated reasoning and problem-solving, ranging from joke generation to mathematical reasoning. Existing prompting approaches usually adopt general-purpose, fixed configurations that work 'well enough' across tasks but seldom achieve task-specific optimality. To address this gap, we introduce AdaReasoner, an LLM-agnostic plugin designed for any LLM to automate adaptive reasoning configurations for tasks requiring different types of thinking. AdaReasoner is trained using a reinforcement learning (RL) framework, combining a factorized action space with a targeted exploration strategy, along with a pretrained reward model to optimize the policy model for reasoning configurations with only a few-shot guide. AdaReasoner is backed by theoretical guarantees and experiments of fast convergence and a sublinear policy gap. Across six different LLMs and a variety of reasoning tasks, it consistently outperforms standard baselines, preserves out-of-distribution robustness, and yield gains on knowledge-intensive tasks through tailored prompts.

</details>

### Methods: TBD

#### [OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories](https://arxiv.org/abs/2605.04036)
2026-05 · [PDF](https://arxiv.org/pdf/2605.04036)

> **TL;DR.** An academic-team search agent showing that SFT on just 10.6k informative, high-difficulty trajectories (larger knowledge graphs, more tools, low-step filtering) beats the heavy CPT+SFT+RL recipe; a 30B model tops BrowseComp/-ZH/HLE/xbench, surpassing Tongyi DeepResearch.

<details><summary>Abstract</summary>

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry recipe involves a highly resource-intensive pipeline spanning pre-training, continual pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). In this report, we show that when fueled with informative and high-difficulty trajectories, a simple SFT approach could be surprisingly powerful for training frontier search agents. By introducing three simple data synthesis modifications: scaling knowledge graph size for richer exploration, expanding the tool set size for broader functionality, and strict low-step filtering, we establish a stronger baseline. Trained on merely 10.6k data points, our OpenSeeker-v2 achieves state-of-the-art performance across 4 benchmarks (30B-sized agents with ReAct paradigm): 46.0% on BrowseComp, 58.1% on BrowseComp-ZH, 34.6% on Humanity's Last Exam, and 78.0% on xbench, surpassing even Tongyi DeepResearch trained with heavy CPT+SFT+RL pipeline, which achieves 43.4%, 46.7%, 32.9%, and 75.0%, respectively. Notably, OpenSeeker-v2 represents the first state-of-the-art search agent within its model scale and paradigm to be developed by a purely academic team using only SFT. We are excited to open-source the OpenSeeker-v2 model weights and share our simple yet effective findings to make frontier search agent research more accessible to the community.

</details>

#### [A Tale of Two Graphs: Separating Knowledge Exploration from Outline Structure for Open-Ended Deep Research](https://arxiv.org/abs/2602.13830)
2026-02 · [PDF](https://arxiv.org/pdf/2602.13830)

> **TL;DR.** DualGraph memory keeps two co-evolving graphs (an Outline Graph + a Knowledge Graph) to separate what the agent knows from how it writes, driving targeted exploration; 53.08 RACE on DeepResearch Bench with GPT-5.

<details><summary>Abstract</summary>

Open-Ended Deep Research (OEDR) pushes LLM agents beyond short-form QA toward long-horizon workflows that iteratively search, connect, and synthesize evidence into structured reports. However, existing OEDR agents largely follow either linear ``search-then-generate'' accumulation or outline-centric planning. The former suffers from lost-in-the-middle failures as evidence grows, while the latter relies on the LLM to implicitly infer knowledge gaps from the outline alone, providing weak supervision for identifying missing relations and triggering targeted exploration. We present DualGraph memory, an architecture that separates what the agent knows from how it writes. DualGraph maintains two co-evolving graphs: an Outline Graph (OG), and a Knowledge Graph (KG), a semantic memory that stores fine-grained knowledge units, including core entities, concepts, and their relations. By analyzing the KG topology together with structural signals from the OG, DualGraph generates targeted search queries, enabling more efficient and comprehensive iterative knowledge-driven exploration and refinement. Across DeepResearch Bench, DeepResearchGym, and DeepConsult, DualGraph consistently outperforms state-of-the-art baselines in report depth, breadth, and factual grounding; for example, it reaches a 53.08 RACE score on DeepResearch Bench with GPT-5. Moreover, ablation studies confirm the central role of the dual-graph design.

</details>

#### [MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/abs/2512.18746)
2025-12 · [PDF](https://arxiv.org/pdf/2512.18746)

> **TL;DR.** A meta-evolutionary framework that jointly evolves an agent's experience and its memory architecture; ships EvolveLab (12 memory systems in one design space) and improves SmolAgent/Flash-Searcher by up to 17%.

<details><summary>Abstract</summary>

Self-evolving memory systems are unprecedentedly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the staticity of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents' experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior research and foster openness in future self-evolving systems, we introduce EvolveLab, a unified self-evolving memory codebase that distills twelve representative memory systems into a modular design space (encode, store, retrieve, manage), providing both a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks demonstrate that MemEvolve achieves (I) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to $17.06%$; and (II) strong cross-task and cross-LLM generalization, designing memory architectures that transfer effectively across diverse benchmarks and backbone models.

</details>

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

#### Step-DR

> **TL;DR.** _pending._

#### [Skywork-R1V4: Toward Agentic Multimodal Intelligence through Interleaved Thinking with Images and DeepResearch](https://arxiv.org/abs/2512.02395)
`Skywork AI` · `arXiv 2512` · 2025-12 · Base: `30B-A3B` · [PDF](https://arxiv.org/pdf/2512.02395)

> **TL;DR.** SFT-only (<30K planning-consistent trajectories) agentic model unifying image manipulation and deep multimodal search with interleaved reasoning.

<details><summary>Abstract</summary>

Despite recent progress in multimodal agentic systems, existing approaches often treat image manipulation and web search as disjoint capabilities, rely heavily on costly reinforcement learning, and lack planning grounded in real tool-execution traces. To address these limitations, we present Skywork-R1V4, a 30B (A3B) parameter multimodal agentic model that unifies multimodal planning, active image manipulation ("thinking with images"), deep multimodal search, and, most critically, interleaved reasoning that dynamically alternates between visual operations and external knowledge retrieval. Trained solely via supervised fine-tuning on fewer than 30,000 high-quality, planning-execution-consistent trajectories and validated through stepwise consistency filtering, Skywork-R1V4 achieves state-of-the-art results across perception and multimodal search benchmarks: it scores 66.1 on MMSearch and 67.2 on FVQA, surpassing Gemini 2.5 Flash on all 11 metrics. Skywork-R1V4 exhibits emergent long-horizon reasoning at inference time, successfully orchestrating more than 10 tool calls to solve complex, multi-step tasks. Our results demonstrate that sophisticated agentic multimodal intelligence can be achieved through carefully curated supervised learning alone, without any reliance on reinforcement learning.

</details>

#### W&D: Scaling Parallel Tool Calling for Efficient Deep Research Agents

> **TL;DR.** _pending._

#### [OpenDeepResearcher](https://github.com/mshumer/OpenDeepResearcher)
[Code](https://github.com/mshumer/OpenDeepResearcher) [![Stars](https://img.shields.io/github/stars/mshumer/OpenDeepResearcher?style=social)](https://github.com/mshumer/OpenDeepResearcher)

> **TL;DR.** _pending._

#### Mind DeepResearch Technical Report

> **TL;DR.** _pending._

#### s1-Deep Research

> **TL;DR.** _pending._

#### Dr. Zero
`Meta`

> **TL;DR.** _pending._

#### Chart Deep Research in LVLMs via Parallel Relative Policy Optimization

> **TL;DR.** _pending._

#### NanoResearch

> **TL;DR.** _pending._

#### Search-o1

> **TL;DR.** _pending._

#### OpenSeeker

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
