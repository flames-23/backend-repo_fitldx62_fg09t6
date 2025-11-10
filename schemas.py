"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
The collection name is the lowercase of the class name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Project(BaseModel):
    """
    Projects collection schema
    Collection name: "project"
    """
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Short description of the work and outcome")
    tags: List[str] = Field(default_factory=list, description="Key technologies or themes")
    impact: Optional[str] = Field(None, description="Impact metric or highlight")
    link: Optional[str] = Field(None, description="External link or case study")

class ContactMessage(BaseModel):
    """
    Contact messages from the website
    Collection name: "contactmessage"
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., description="Message body")

# Example schemas kept for reference
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
