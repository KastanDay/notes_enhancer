# Welcome to Notes Enhancer
> True inspiration—real, transformative insight—arrives through the serendipitous collision between old ideas. -David Drysdale


## Mission

**Problem**: We have lots of notes that get stale and are forgotten. 

**Solution**: As you're writing a note, see all the ways it subtly connects to what you already know.

1. **Find "unlinked mentions"** between pages via semantic search. As a page is written, the rest of your notes are 'fuzzy' searched for synonymous (and opposite) terms, people.
2. Use content generation to **"finish your thought"** and extend your notes to make them more rich and searchable.
3. **Search the web to enrich notes.** Use Wikipedia, Google knowledge graph for topics & people mentioned in your notes. Append that content to the bottom of your notes to make notes richer, and easily searchable. This is a positive feedback loop that helps make more connections between notes, as well.

## Related work 

* There's a new project: https://mem.ai/ Their AI isn't fully implemented yet (waitlist) but it seems like they have funding and might launch soon. They are the closest to what I'm looking for.

* RemNote

* MyMind

## Install

@future `pip install .......`

## How to use

Code examples tbd

```python
import gpt-3-simple as gpt3
gpt3.download_gpt3()

notes.find_similar(gpt3)
```


## Roadmap

1. [RayCast](https://www.raycast.com/) extension w/ connection to live notion pages (and keep it fast with cacheing?)
2. Keyword -> [Stable Difusion](https://github.com/huggingface/diffusers/releases/tag/v0.2.3) extension. 
