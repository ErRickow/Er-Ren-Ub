import re
import asyncio
import os
import sys
import shutil
import subprocess

from git import Repo
from git.exc import InvalidGitRepositoryError

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.tools import initialize_git
from utils.handler import *
from utils.scripts import format_exc, restart
from config import CMD_HANDLER

@Akeno(
    ~filters.scheduled
    & filters.command(["up", "update"], CMD_HANDLER)
    & filters.me
    & ~filters.forwarded
)