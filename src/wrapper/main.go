// Wrapper to call the actual heyai program from the command line

package main

import (
	"os"
	"os/exec"
	"strings"
)

func get_backend() string {
	return "heyai.py"
}

func main() {
    var args = os.Args[1:]

	exec.Command(get_backend(), strings.Join(args, " "))
}