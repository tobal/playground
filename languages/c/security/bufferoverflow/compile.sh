#!/usr/bin/env bash
gcc bufferoverflow.c -fno-stack-protector -m32 -z execstack
