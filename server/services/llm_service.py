import google.generativeai as genai
from config import Settings

settings = Settings()


class LLMService:
    def __init__(self):
        try:
            print(f"Initializing Gemini with API key: {settings.GEMINI_API_KEY}")
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-2.0-flash-exp")
            print("Gemini model initialized successfully")
        except Exception as e:
            print(f"Error initializing Gemini: {e}")
            self.model = None

    def generate_response(self, query: str, search_results: list[dict]):
        try:
            if not self.model:
                yield "Error: Gemini model was not initialized properly. Please check your API key."
                return

            print(f"Generating response for query: {query}")
            print(f"Using {len(search_results)} search results")

            context_text = "\n\n".join(
                [
                    f"Source {i+1} ({result['url']}):\n{result['content']}"
                    for i, result in enumerate(search_results)
                ]
            )

            full_prompt = f"""
            Context from web search:
            {context_text}

            Query: {query}

            Please provide a comprehensive, detailed, well-cited accurate response using the above context. 
            Think and reason deeply. Ensure it answers the query the user is asking. Do not use your knowledge until it is absolutely necessary.
            """

            print("Sending prompt to Gemini")
            response = self.model.generate_content(full_prompt, stream=True)
            print("Response stream started")

            for chunk in response:
                print(f"Received chunk: {chunk.text[:50]}...")
                yield chunk.text

        except Exception as e:
            print(f"Error generating response: {e}")
            yield f"Sorry, I encountered an error while generating a response: {str(e)}"
