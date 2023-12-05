f, err := os.Open(fi)
if err != nil {
    fmt.Printf("error opening file: %v\n",err)
    os.Exit(1)
}
r := bufio.NewReader(f)
s, e := Readln(r)
for e == nil {
    fmt.Println(s)
    s,e = Readln(r)
}