// Wrapper to call the actual heyai program from the command line

package main

import (
	"fmt"
	"os"
)

func main() {
    fmt.Println(os.Args[1:])
}