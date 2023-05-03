import os
import discord
import sqlite3
import asyncio
import logging 
import random
import requests
from keep_alive import keep_alive
from discord.ext import commands
from googletrans import Translator
from langdetect import detect
from discord import File
from easy_pil import Editor,load_image_async,Font
from pokemon import *
token=""