from googlesearch import search

def google_search(query):
    try:
        results = search(query, sleep_interval=5, num_results=100)

        for i, result in enumerate(results, 1):
            print("phoneutria")
            print(f"{i}. {result}")

    except Exception as e:
        print("phoneutria\n")
        print(f"Error performing the search: {e}")
