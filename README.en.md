# Repository Purpose
[![ch](https://img.shields.io/badge/lang-ch-green.svg)](https://github.com/I-Sheng/Traveling-Planner-With-LLM/blob/main/README.md)

This GitHub repository is dedicated to the research project "A GPT-Centric Travel Itinerary Planning System," funded by the National Science and Technology Council. Initially, the project aimed to leverage GPT (a customized ChatGPT model) as its core system. However, with advancements in technology and increasing customization needs, LangChain is now being used for implementation.

## Project Architecture
![旅遊規劃架構圖 (1)](https://github.com/user-attachments/assets/64bbf934-b35a-4844-98da-70401c7f85de)


## User Workflow
1. Users input their preferences based on a given prompt:
    ```
    # Prompt Example
    # I like __ types of attractions, planning to travel for __ days, please recommend some attractions for me.
    # e.g.
    I like historical attractions, planning to travel for 2 days, please recommend some attractions for me.
    ```
2. The LLM (Language Learning Model) recommends potential attractions.
3. Users select their preferred attractions and accommodations.
4. The LLM returns a detailed itinerary based on the user's choices.

## Project Implementation Detail
Based on the project architecture, the implementation is divided into four main components, focusing on Chiayi as the travel destination:

1. **Data Collection**: Collect information on Chiayi tourism, including attractions, restaurants, and hotels.
   → Directory: `/webcrab`

2. **Duration Calculation**: Calculate the recommended duration for each attraction.
   → Directory: `/waiting_time`

3. **Information Retrieval**: Once the user selects attractions, retrieve detailed information for each location.
   → Script: `/langchain/distance_matrix.py`

4. **Itinerary Planning**: Utilize the retrieved information and apply algorithms to generate a planned itinerary.
   *(Note: This step is still under development)*

## Environment Setup

1. **Create a `.env` file**
   In the root directory, create a `.env` file with the following variables:
    ```env
    # Generative AI
    OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
    ANTHROPIC_API_KEY='YOUR_ANTHROPIC_API_KEY'
    GOOGLE_API_KEY='YOUR_GOOGLE_API_KEY'

    # Google Maps API
    GOOGLE_MAP_API_KEY='YOUR_GOOGLE_MAP_API_KEY'

    # LangChain
    LANGCHAIN_HUB_API_KEY='YOUR_LANGCHAIN_HUB_API_KEY'
    LANGCHAIN_API_KEY='YOUR_LANGCHAIN_API_KEY'
    ```

