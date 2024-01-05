from googlesearch import search
from phoneutria.version import __version__

def google_search(query, num_results=50):
    try:
        results = search(query, num_results=num_results)

        for i, result in enumerate(results, 1):
            print("phoneutria ", + __version__)
            print(f"{i}. {result}")

    except Exception as e:
        print("phoneutria ", + __version__)
        print(f"Erro ao realizar a pesquisa: {e}")
