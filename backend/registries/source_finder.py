from schemas.source_finder import Source, InputMode, SourceCapability
from registries.registry import Registry

SOURCE_CAPABILITY_REGISTRY = Registry[Source, SourceCapability]()

def register_source_capabilities():
    """Registers the capabilities of each source in the SOURCE_CAPABILITY_REGISTRY."""
    SOURCE_CAPABILITY_REGISTRY.register(
        Source.YOUTUBE,
        SourceCapability(
            supported_input_modes=[InputMode.QUERY, InputMode.URLS],
            constraints={
                "max_query_results": 10,
                "max_url_results": 5
            }
        )
    )
    SOURCE_CAPABILITY_REGISTRY.register(
        Source.TIKTOK,
        SourceCapability(
            supported_input_modes=[InputMode.QUERY, InputMode.URLS],
            constraints={
                "max_query_results": 10,
                "max_url_results": 5
            }
        )
    )