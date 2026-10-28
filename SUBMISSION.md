---
title: "Echoes: A Private, Local AI Memory Lantern"
published: false
tags: devchallenge, hf26challenge
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4:
Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

## What I Built

Echoes is a local-first writing companion inspired by the stories and memories
we carry with us. Share a small memory and choose a form: a remembrance, a
gentle ghost story, or a short literary scene. Echoes uses a local model to
shape a draft while asking it to stay grounded in the details provided.

## Demo

The project currently runs locally. Install the dependencies and follow the
Ollama setup in the [README](./README.md). There is no public demo yet.

## Code

[View the source code on GitHub](https://github.com/nirajnagrale7/hacktoberfest-first-challenge-2026/tree/main/Challenge%205).

## How I Built It

The interface uses Streamlit and sends the chosen style and memory to an
open-weight `qwen2.5:3b` model running through Ollama on the same computer.
Echoes does not save the input to an app database. The prompt asks the model
not to invent biographical facts or present a fictional story as true, and the
user can review, edit, or discard the generated draft.

## Why Does Open Innovation Matter?

Family memories are personal. Local inference means the words stay on the
writer's computer instead of being sent to a hosted AI API. After the initial
model download, generation works offline and has no per-story API fee. The
prompt and model are inspectable and replaceable, so the writing behavior can
be adapted rather than locked inside a service.

## My Agent Session

I do not have a shareable DevRelay session link for this project.

## The Spirit of It

Echoes is a small invitation to write down the details that might otherwise
fade: a phrase, a song, or a familiar light in the window. It does not claim
to speak for anyone; it gives the writer a private place to shape a story in
their own words.

## Prize Categories

Hacktoberfest Open-Source AI Challenge: Ghost in the Machine.
