# BrandBrief AI

BrandBrief AI is a Sales Brochure Generator built as my first
Generative AI project while learning the fundamentals of LLM
application development.

The project takes a company's website, identifies useful information
from the website, and uses an LLM to generate a structured sales
brochure.

## How It Works

The project follows a two-stage LLM workflow:

Company Website
↓
Web Scraping
↓
LLM 1 — Relevant Page Selection
↓
Context Construction
↓
LLM 2 — Sales Brochure Generation
↓
Streaming Output

### Stage 1 — Website Intelligence

The first LLM analyzes the links discovered from the company's website
and identifies the pages that contain useful information such as:

- Products
- Services
- Solutions
- Industries
- Customers
- Case studies
- About the company

### Stage 2 — Brochure Generation

The relevant information collected from the selected pages is provided
as context to the second LLM.

The second LLM uses this context to generate a structured sales
brochure while staying grounded in the information collected from
the company's website.

## Technologies

- Python
- Gemini API
- LLMs
- Prompt Engineering
- Web Scraping
- Jupyter Notebook

## Files

```text
brandbrief-ai/
│
├── brandbrief_llm.ipynb
├── scraper.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example

What I Learned

This project helped me understand that building an LLM application
involves much more than simply sending a prompt to a model.

I learned about:

Working with LLM APIs
Prompt engineering
Context construction
Multi-stage LLM workflows
Web scraping
Streaming LLM responses

One of the main ideas I explored was using separate LLM steps
for different tasks rather than asking one model to perform the
entire workflow at once.

Limitations

This is an early learning project, so the current implementation
has limitations around website scraping, content extraction, and
the amount of information that can be passed to the model.

Future Improvements
More robust website crawling
Better content extraction
Improved context management
Better handling of complex websites
Further experimentation with LLM workflows