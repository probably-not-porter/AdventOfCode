package main
import "fmt"
import "os"
import "bufio"

// Return single lines from input buffer
func Readln(r *bufio.Reader) (string, error) {
    var (isPrefix bool = true
         err error = nil
         line, ln []byte
        )
    for isPrefix && err == nil {
        line, isPrefix, err = r.ReadLine()
        ln = append(ln, line...)
    }
    return string(ln),err
}

// puzzle algorithm
func main() {
    // READ FILE
    f, err := os.Open("input.txt")
    if err != nil {
        fmt.Printf("error opening file: %v\n",err)
        os.Exit(1)
    }
    r := bufio.NewReader(f)
    s, e := Readln(r)

    // MAIN LOOP
    for e == nil {                  // for line in input
        fmt.Println("line: " + s)   // print input line

        for y := 0; y < len(s); y++ { // iterate over grid y-axis

            for i, c := range "abc" { // iterate over grid x-axis
                fmt.Println(i, " => ", string(c))
            }
        }
        s,e = Readln(r) // read next line
    }
}
