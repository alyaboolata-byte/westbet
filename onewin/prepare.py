"""Publish IndexNow verification and deployed revision for 1win.westbet.ru."""
import json, os, pathlib
root=pathlib.Path(__file__).resolve().parent
(root/"7b0e06c118f4444ea3c72f81b9a849a2.txt").write_text("7b0e06c118f4444ea3c72f81b9a849a2\n",encoding="utf-8")
(root/"indexnow-deployment.json").write_text(json.dumps({"projectId":"prj_8JWDx7J3geLyDeYiyljy1amENcG6","sha":os.getenv("VERCEL_GIT_COMMIT_SHA","")}),encoding="utf-8")
