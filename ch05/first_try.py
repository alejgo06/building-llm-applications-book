from typing import List, Dict, Any, TypedDict, Optional





class assistant_instructions(TypedDict): 
    assistant_type : str
    assistant_instructions : str
    user_question : str


class web_searches(TypedDict): 
    search_query : str
    user_question : str

class search_result_text_and_summary(TypedDict): 
    result_url : str
    search_query : str
    user_question : str

class search_and_summarization(TypedDict): 
    search_result_text  : str
    result_url  : str
    search_query  : str
    user_question  : str

class web_research(TypedDict): 
     report: str

class ResearchState(TypedDict):  #2
    user_question: str
    assistant_info: Optional[assistant_instructions]
    search_queries: Optional[List[web_searches]]
    search_results: Optional[List[search_result_text_and_summary]]
    search_summaries: Optional[List[web_research]]
    research_summary: Optional[str]
    