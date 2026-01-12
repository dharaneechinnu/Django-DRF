from algoliasearch_django import algolia_engine
from django.conf import settings


def perform_Search(query, **kwargs):
    try:
        if not query:
            return []

        # Build the index name from settings prefix (matches reindex behavior)
        prefix = settings.ALGOLIA.get('INDEX_PREFIX', '').rstrip('_')
        index_name = f"{prefix}_Product" if prefix else "Product"

        client = algolia_engine.client

        # Perform search on a single index
        results = client.search_single_index(index_name, {
            "query": query
        })

        # Extract hits safely
        if not results:
            hits = []
        elif hasattr(results, 'hits'):
            hits = results.hits
        elif isinstance(results, dict):
            hits = results.get('hits', [])
        else:
            try:
                hits = dict(results).get('hits', [])
            except Exception:
                hits = []

        print(f"Algolia search for '{query}' returned {len(hits)} results")

        # Make results JSON-serializable
        serializable_hits = []
        for h in hits:
            try:
                if hasattr(h, 'dict'):
                    serializable_hits.append(h.dict())
                else:
                    serializable_hits.append(h)
            except Exception:
                serializable_hits.append(h)

        return serializable_hits

    except Exception as e:
        print(f"Search error: {str(e)}")
        import traceback
        traceback.print_exc()
        return []
