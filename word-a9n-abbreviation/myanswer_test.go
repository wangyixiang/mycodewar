package main

import (
	"log"
	"regexp"
	"strconv"
	"testing"
)

func Abbreviate(s string) string {
	re := regexp.MustCompile("[a-zA-Z]{4,}")
	return re.ReplaceAllStringFunc(s,
		func(s string) string {
			return string(s[0])+ strconv.Itoa(len(s)-2) + string(s[len(s)-1])
		})
}

func mustEqual(t *testing.T, s1, s2 string) {
	if s1 != s2 {
		t.FailNow()
	}
}

func TestAbbreviate(t *testing.T){
	mustEqual(t, Abbreviate("internationalization"), "i18n")
	mustEqual(t, Abbreviate("accessibility"), "a11y")
	mustEqual(t, Abbreviate("Accessibility"), "A11y")
	mustEqual(t, Abbreviate("cat. monolithic-monolithic: double-barreled'doggy-a: mat-balloon; "),
                         "cat. m8c-m8c: d4e-b6d'd3y-a: mat-b5n; ")
}

func main() {
	log.Println(Abbreviate("internationalization"))
	log.Println(Abbreviate("cat. monolithic-monolithic: double-barreled'doggy-a: mat-balloon; "))
}