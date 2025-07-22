import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
import os
from serpapi import GoogleSearch

class WebSearchFallback:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
        self.serpapi_key = os.getenv('SERPAPI_API_KEY')
    
    def assess_answer_quality(self, answer, question):
        """Assess the quality of the retrieved answer"""[19]
        try:
            quality_prompt = f"""
            Assess the quality and completeness of the following answer to the given question.
            Rate the quality on a scale of 0.0 to 1.0, where:
            - 1.0 = Complete, accurate, and fully answers the question
            - 0.7 = Good answer but may lack some details
            - 0.5 = Partial answer, missing important information
            - 0.3 = Poor answer, mostly irrelevant
            - 0.0 = No relevant information
            
            Question: {question}
            Answer: {answer}
            
            Respond with only a number between 0.0 and 1.0:
            """
            
            response = self.llm.invoke(quality_prompt)
            quality_score = float(response.content.strip())
            return max(0.0, min(1.0, quality_score))
        
        except Exception as e:
            print(f"Error assessing answer quality: {e}")
            return 0.5  # Default to medium quality if assessment fails
    
    def search_web(self, query):
        """Search the web for additional information"""
        try:
            if self.serpapi_key:
                return self._search_with_serpapi(query)
            else:
                return self._search_with_requests(query)
        except Exception as e:
            print(f"Error in web search: {e}")
            return None
    
    def _search_with_serpapi(self, query):
        """Search using SerpAPI (recommended)"""
        try:
            search = GoogleSearch({
                "q": query,
                "api_key": self.serpapi_key,
                "num": 3
            })
            results = search.get_dict()
            
            if "organic_results" in results:
                snippets = []
                for result in results["organic_results"][:3]:
                    if "snippet" in result:
                        snippets.append(result["snippet"])
                
                combined_info = "\n\n".join(snippets)
                
                # Use LLM to format the web search results
                format_prompt = f"""
                Based on the following web search results, provide a comprehensive answer to the question: {query}
                
                Web search results:
                {combined_info}
                
                Provide a clear, informative answer:
                """
                
                response = self.llm.invoke(format_prompt)
                return response.content
        
        except Exception as e:
            print(f"SerpAPI search error: {e}")
            return None
    
    def _search_with_requests(self, query):
        """Fallback search using requests (less reliable)"""
        try:
            # Simple web search using DuckDuckGo instant answer API
            url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('AbstractText'):
                    return data['AbstractText']
                elif data.get('Answer'):
                    return data['Answer']
            
            return "Unable to fetch additional information from web search."
        
        except Exception as e:
            print(f"Requests search error: {e}")
            return None
