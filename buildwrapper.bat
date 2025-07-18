@echo off
mkdir dist


go build -o %1 src/wrapper/main.go