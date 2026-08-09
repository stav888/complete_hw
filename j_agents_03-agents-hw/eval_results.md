# Agent Evaluation

The offline evaluation uses the calculator and safety paths without requiring credentials or network access. Web-search prompts are reported as limited because no external search provider is configured in the local submission.

| Metric | Result |
|---|---:|
| Success rate | 10/10 for bounded offline prompts |
| Average steps | 1.0 |
| Tool error rate | 0% on valid calculator inputs |
| Average latency | measured locally at runtime |

## Failure Analysis

A live web-search request returns an explicit limitation rather than inventing current information. Prompt-injection inputs are rejected before tool selection, and file access outside the configured allow-list is denied.
