import os


def main():

    print("=" * 80)
    print("AI RESEARCH ASSISTANT")
    print("=" * 80)

    # TODO: Initialize genai client

    # Sample research queries
    sample_query = "How does machine learning improve code review efficiency?"

    # check for custom query via environment variable
    custom_query = os.getenv("RESEARCH_QUERY")

    if custom_query:
        selected_query = custom_query
        print("\n Running custom research query...")
    else:
        selected_query = sample_query
        print("\n Running research workflow for sample query...")

    print(f"\n User query : {selected_query}")


if __name__ == "__main__":
    main()
