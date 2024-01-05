from googlesearch import search

def google_search(query, num_results=5):
    try:
        results = search(query, num_results=num_results, stop=num_results)

        for i, result in enumerate(results, 1):
            print(f"{i}. {result}")

    except Exception as e:
        print(f"Erro ao realizar a pesquisa: {e}")
