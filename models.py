from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    email: str
    username: str
    tier: str = "free"
    created_at: datetime

class Payment(BaseModel):
    id: int
    user_id: int
    amount: float
    currency: str = "USD"
    status: str
    created_at: datetime

    def add_feature(self, feature_name: str, feature_value: str):
        """
        Add a new feature to the payment model.

        Args:
            feature_name (str): The name of the feature to add.
            feature_value (str): The value of the feature to add.

        Returns:
            dict: A dictionary containing the updated payment features.
        """
        # Create a dictionary to store the payment features
        payment_features = {}

        # Check if the payment features dictionary already exists
        if hasattr(self, 'features'):
            payment_features = self.features

        # Add the new feature to the dictionary
        payment_features[feature_name] = feature_value

        # Update the payment features
        self.features = payment_features

        # Return the updated payment features
        return self.features