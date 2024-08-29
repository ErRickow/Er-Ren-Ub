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

from Akeno.utils.tools import initialize_git
from Akeno.utils.handler import *
from Akeno.utils.scripts import format_exc, restart
from config import CMD_HANDLER

@Akeno(
    ~filters.scheduled
    & filters.command(["up", "update"], CMD_HANDLER)
    & filters.me
    & ~filters.forwarded
)

async def ngapdate(client, message):
  pros = await message.reply(
        f"<blockquote> <b>Memeriksa pembaruan resources {client.me.mention}</b></blockquote>"
    )
  out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
  teks = f"<b>❒ Status resources :</b>\n"
  memeg = f"<b>Perubahan logs by {client.me.mention}</b>"
  if "Already up to date." in str(out):
        return await pros.edit(f"<blockquote>{teks}┖ {out}</blockquote>")
  if len(out) > 4096:
          anuk = await pros.edit(
            f"<blockquote> <b>Hasil akan dikirimkan dalam bentuk file ..</b></blockquote>"
        )
  anuk = None
  with open("output.txt", "w+") as file:
            file.write(out)

           # X = f"<blockquote> <b>Perubahan logs </b></blockquote>"
  #await client.send_document(
  #        message.chat.id,
  #        "output.txt",
  #        caption=f"{X}",
   #       reply_to_message_id=message.id,
   #       )
  os.remove("output.txt")
  format_line = [f"┣ {line}" for line in out.splitlines()]
  if format_line:
    format_line[-1] = f"┖ {format_line[-1][2:]}"
    format_output = "\n".join(format_line)
  await pros.edit(f"<blockquote>{memeg}\n\n{teks}{format_output}\n\nanuin this update by @LuciferReborns</blockquote>")
  os.execl(sys.executable, sys.executable, "python3 server.py & python3 -m Akeno")
  
