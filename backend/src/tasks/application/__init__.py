import importlib

from lato import ApplicationModule

tasks_module = ApplicationModule("tasks")
importlib.import_module("tasks.application.command")
importlib.import_module("tasks.application.query")
