// Wrapper to call the actual heyai program from the command line

package main

import (
	"os"
	"os/exec"
	"strings"
	"fmt"
)

func get_backend() string {
	return "backend/heyai.py"
}

func main() {
    var args = os.Args[1:]

	var formattedArgs = strings.Join(args, " ")
	var backendPath = get_backend()

	exec.Command("py " + backendPath + " " + formattedArgs)
}