<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">LangSmith & LangGraph Studio</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE5/00_AIM_Quicklinks)

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 16: LLM Ops: Operating RAG in Production](https://www.notion.so/Session-16-LLM-Ops-Operating-RAG-in-Production-1c8cd547af3d815795f8f2a8c626fa60?pvs=4#1c8cd547af3d81108a30c4a9db742661) | [Session 16: LLM Ops: Operating RAG in Production](https://www.notion.so/Session-16-LLM-Ops-Operating-RAG-in-Production-1c8cd547af3d815795f8f2a8c626fa60) | [Recording](https://us02web.zoom.us/rec/share/MIqBKtvqX-MVX2iVIypF2x4nburlIAX5hsleF7CUeFomG9QGUtnBcz4YVdGapmtU.iHoOvDy3lTOc0nJ-)  (FsQWwi?5) | [Session 16 Slides](https://www.canva.com/design/DAGjaXGSJVE/4o7sKV5uNEyLrFi5wTEvoA/edit?utm_content=DAGjaXGSJVE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 16: LLM Ops: Operating RAG in Production](https://forms.gle/mawQduxCRtRdzm1r8) | [AIE6 Feedback 5/22](https://forms.gle/FZnfaUQcBFawCaTT7) |


# Build 🏗️

Run the notebook and complete the following:

1. 🤝 BREAKOUT ROOM #1:
  - Task 1: Set Up HF Endpoints As in Session 15
  - Task 2: Depends and Set-Up
  - Task 3: Setting up RAG With Production in Mind
  - Task 4: RAG LCEL Chain
2. 🤝 BREAKOUT ROOM #2:
  - Clone the [open_deep_research](https://github.com/langchain-ai/open_deep_research) repository *outside* of your AIE6 Repository. 

    ```bash
    cd ~
    git clone https://github.com/langchain-ai/open_deep_research
    ```

  - Deploy LangGraph Studio for [open_deep_research](https://github.com/langchain-ai/open_deep_research) by following the instructions in that README.md

## ADVANCED BUILD:

The caching we're using is both: 

1. Ineffecient
2. Exact Match

Please produce a locally running application (through Docker) that integrates a more intelligent caching process.

In simpler terms: 

- Use a database approach (Redis, Vectordatase, SQLite, etc.) instead of plain-memory for caching
- Implement Semantic LLM Caching OR Implement E2E Caching

> NOTE: Doing the advanced build will count as your assignment for the week. If you do the advanced build, you are not required to do the notebook.

# Ship 🚢

- HF App.
- 5min. Loom Video

# Share 🚀
- Walk through your notebook and explain what you've completed in the Loom video
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned
