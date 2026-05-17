from typing import Dict

class Config:
    def __init__(self):
        self.features = {}

    def add_feature(self, feature_name: str, feature_config: Dict):
        """
        Add a new feature to the configuration.

        Args:
            feature_name (str): The name of the feature.
            feature_config (Dict): The configuration for the feature.
        """
        self.features[feature_name] = feature_config

    def get_feature(self, feature_name: str) -> Dict:
        """
        Get the configuration for a specific feature.

        Args:
            feature_name (str): The name of the feature.

        Returns:
            Dict: The configuration for the feature.
        """
        return self.features.get(feature_name)

config = Config()