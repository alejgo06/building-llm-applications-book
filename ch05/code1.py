from typing import List, Dict, Any, TypedDict, Optional
from prompts import (
    ASSISTANT_SELECTION_PROMPT_TEMPLATE,
    WEB_SEARCH_PROMPT_TEMPLATE,

)
from llm_models import get_llm

class AssistantInfo(TypedDict):  #1
    assistant_type: str
    assistant_instructions: str
    user_question: str

class SearchQuery(TypedDict):  #1
    search_query: str
    user_question: str

class SearchResult(TypedDict):  #1
    result_url: str
    search_query: str
    user_question: str
    is_fallback: Optional[bool]

class SearchSummary(TypedDict):  #1
    summary: str
    result_url: str
    user_question: str
    is_fallback: Optional[bool]

class ResearchReport(TypedDict):  #1
    report: str

class ResearchState(TypedDict):  #2
    user_question: str
    assistant_info: Optional[AssistantInfo]
    search_queries: Optional[List[SearchQuery]]
    search_results: Optional[List[SearchResult]]
    search_summaries: Optional[List[SearchSummary]]
    research_summary: Optional[str]
    final_report: Optional[str]
    used_fallback_search: Optional[bool]
    relevance_evaluation: Optional[Dict[str, Any]]
    should_regenerate_queries: Optional[bool]
    iteration_count: Optional[int]

def select_assistant(state: dict) -> dict:
    """Select the appropriate research assistant."""
    user_question = state["user_question"]

    # Use the LLM to select an assistant
    prompt = ASSISTANT_SELECTION_PROMPT_TEMPLATE.format(
        user_question=user_question
    )
    response = get_llm().invoke(prompt)

    assistant_info = parse_assistant_info(
        response.content)  #1

    return {"assistant_info": assistant_info}  #2

def generate_search_queries(state: dict) -> dict:
    """Generate search queries based on the question."""
    assistant_info = state["assistant_info"]
    user_question = state["user_question"]

    prompt = WEB_SEARCH_PROMPT_TEMPLATE.format( #3
        assistant_instructions=assistant_info["assistant_instructions"],
        user_question=user_question,
        num_search_queries=3
    )
    response = get_llm().invoke(prompt)

    search_queries = parse_search_queries(
        response.content)  #4

    return {"search_queries": search_queries}  #5


from langgraph.graph import StateGraph, END
graph = StateGraph(ResearchState)   #1

graph.add_node("select_assistant",  select_assistant)  #2
graph.add_node("generate_search_queries", generate_search_queries)   #2
graph.add_node("perform_web_searches", perform_web_searches)   #2
graph.add_node("summarize_search_results",  summarize_search_results)   #2
graph.add_node("evaluate_search_relevance",  evaluate_search_relevance)   #2
graph.add_node("write_research_report", write_research_report)   #2


def route_based_on_relevance(state):  #3
    iteration_count = state.get("iteration_count", 0) + 1
    state["iteration_count"] = iteration_count

    if iteration_count >= 3:
        return "write_research_report"
    if state.get("should_regenerate_queries", False):
        return "generate_search_queries"
    return "write_research_report"

graph.add_edge("select_assistant", "generate_search_queries")   #4
graph.add_edge("generate_search_queries",  "perform_web_searches")   #4
graph.add_edge("perform_web_searches",  "summarize_search_results")   #4
graph.add_edge("summarize_search_results","evaluate_search_relevance")  #4
graph.add_edge("write_research_report", END)   #4


graph.add_conditional_edges(  #5
    "evaluate_search_relevance",
    route_based_on_relevance,
    {
        "generate_search_queries": "generate_search_queries",
        "write_research_report": "write_research_report"
    }
)

graph.set_entry_point("select_assistant")  #6

app = graph.compile()  #1
initial_state = {  #2
    "user_question": " What can you tell me about Astorga's roman spas?",
    "assistant_info": None,
    "search_queries": None,
    "search_results": None,
    "search_summaries": None,
    "research_summary": None,
    "final_report": None,
    "used_fallback_search": False,
    "relevance_evaluation": None,
    "should_regenerate_queries": None,
    "iteration_count": 0
}
result = app.invoke(initial_state)  #3

final_report = result["final_report"]  #4