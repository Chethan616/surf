from config import Settings
from tavily import TavilyClient
import trafilatura
import time

settings = Settings()
tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)


class SearchService:
    def web_search(self, query: str):
        try:
            print(f"Searching for: {query}")
            print(f"Using Tavily API key: {settings.TAVILY_API_KEY}")
            
            # Add a small delay to ensure API connection
            time.sleep(1)
            
            results = []
            response = tavily_client.search(query, max_results=5)
            print(f"Search response received: {len(response.get('results', []))} results")
            
            search_results = response.get("results", [])

            for i, result in enumerate(search_results):
                try:
                    url = result.get("url")
                    print(f"Downloading content from {url}")
                    downloaded = trafilatura.fetch_url(url)
                    content = trafilatura.extract(downloaded, include_comments=False)

                    results.append(
                        {
                            "title": result.get("title", ""),
                            "url": url,
                            "content": content or "",
                        }
                    )
                except Exception as e:
                    print(f"Error processing search result {i}: {e}")

            return results
        except Exception as e:
            print(f"Error in web search: {e}")
            # Return a fallback result so the app doesn't hang
            return [
                {
                    "title": "Error fetching search results",
                    "url": "https://example.com",
                    "content": f"There was an error fetching search results: {str(e)}. Please check your Tavily API key.",
                }
            ]
