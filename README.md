# AI News Infiltration Detector

#### -- Project Status: Active

## Project Objective
This project centers around the increasing utilization of generative AI, especially Large Language Models in generating content, and the subsequent erosion of public trust in news sources. The primary motivation is to address the challenge posed by the growing presence of these technologies; which often blurs the line between human and AI-generated content, leading to potential misinformation and trust issues in media consumption.

### Methods Used
* Machine Learning
* Data Visualization
* Reinforcment Learning

### Technologies
* Python, Pytorch
* BeautifulSoup
* Pandas, NumPy, jupyter
* GPT 3.5 API

## Project Description
Over the past few years, AI has transitioned from a niche concept confined to science fiction and academic circles to a ubiquitous presence in our daily lives. The release of ChatGPT has played a significant role in democratizing AI, making it accessible to anyone with an internet connection. However, this accessibility comes with challenges, particularly in terms of content moderation. While AI tools like ChatGPT have demonstrated their ability to enhance productivity, they have also contributed to a growing distrust in traditional news outlets.

In recent years, trust in news sources has eroded due to the rampant spread of misinformation online. In response to this concerning trend, this project aims to develop a multi-modal LLM detector capable of distinguishing between human written and AI-generated news articles. News articles serve as an ideal testbed for this endeavor, offering a large amount of text and images for analysis.
Balancing the potential of AI technology with the need for regulation and oversight is paramount. While previous research, such as [DetectGPT](https://arxiv.org/abs/2301.11305) and [Ghostbuster](https://arxiv.org/abs/2305.15047), has made significant strides in AI detection, these efforts have primarily focused on analyzing text alone. In reality, news content often includes multimedia elements such as images, videos, and hyperlinks. Our project addresses this gap by developing a multi-modal model capable of detecting AI-generated content in news articles using both text and images.

By advancing this technology, we aim to contribute to restoration of public confidence in authentic news sources and mitigate the dissemination of misinformation by AI. While our initial focus is on news articles, our long-term vision includes expanding the application of our multi-modal LLM detector to various platforms. Ultimately, we envision integrating this tool as an API for social media platforms, providing users with real-time alerts about potentially AI-generated content.


## Needs of this project for future work

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical/AI modeling
- writeup/reporting

## Getting Started

clone the repo

poetry shell
poetry install
python rewrite_articles.py

### Working with Poetry for project dependencies

This guide provides an overview of how to use Poetry for managing the dependencies of the project.

### Prerequisites

Before you start, ensure you have Python installed on your system. Poetry supports Python 3.7 and newer versions.

### Installing Poetry

To install Poetry, run the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

This command downloads and executes the Poetry installation script.

### Installing Dependencies

Navigate to the project directory and install project dependencies as follows:

1. **Install All Dependencies**:

   ```bash
   poetry install
   ```

   This command installs all the dependencies listed in `pyproject.toml`.

### Updating Dependencies

To update your project's dependencies to their latest versions, use:

```bash
poetry update
```

This command updates all dependencies to the latest compatible versions and updates the `poetry.lock` file to reflect these changes.

### Setting the Python Interpreter to Poetry's Virtual Environment

Poetry creates a virtual environment for your project to manage dependencies separately from your global Python installation. To configure your IDE (e.g., Visual Studio Code) to use the Poetry-managed virtual environment:

1. **Find the Virtual Environment**: First, find the path to the virtual environment created by Poetry with:

   ```bash
   poetry env info --path
   ```

2. **Configure Your IDE**: In your IDE's settings, set the Python interpreter to the path provided by the above command. This ensures that your IDE uses the correct Python version and has access to all the dependencies installed by Poetry.


#### Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Samuel Vasserman](https://github.com/[[github handle](https://github.com/samvass)])| @samvass        |
|[Adam Geenen](https://github.com/[[github handle]](https://github.com/Geener)) |     @adam    |
