from utils.config_loader import load_config

source_finder_config = load_config("configs/source_finder_config.yaml")

class SourceFinder:
    def __init__(self, config=source_finder_config):
        self.config = config

    def get_available_sources(self):
        return self.config.get("available_sources", [])
    
    def _find_from_youtube(self, query):
        # Placeholder for YouTube source finding logic
        return ["YouTube Source 1", "YouTube Source 2"]

    def _find_from_tiktok(self, query):
        # Placeholder for TikTok source finding logic
        return ["TikTok Source 1", "TikTok Source 2"]
    
    def _get_from_yt_urls(self, urls):
        # Placeholder for getting sources from YouTube URLs
        return ["YouTube URL Source 1", "YouTube URL Source 2"]
    
    def _get_from_tt_urls(self, urls):
        # Placeholder for getting sources from TikTok URLs
        return ["TikTok URL Source 1", "TikTok URL Source 2"]