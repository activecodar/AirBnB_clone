#!/usr/bin/python3
"""init module defines a variable storage, an instance of FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
