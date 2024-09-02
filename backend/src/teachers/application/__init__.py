import importlib

from lato import ApplicationModule

teachers_module = ApplicationModule("teachers")
importlib.import_module("tasks.application.command")
importlib.import_module("tasks.application.query")
