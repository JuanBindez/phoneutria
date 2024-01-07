from googlesearch import search

def google_search(query, num_results=15):
    try:
        results = search(query, num_results=num_results)

        for i, result in enumerate(results, 1):
            print("phoneutria")
            print(f"{i}. {result}")

    except Exception as e:
        print("phoneutria\n")
        print(f"Error performing the search: {e}")
