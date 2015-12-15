package main

import (
	"fmt"
	"strings"
	"log"
	"math"
	"time"
	"testing"
	"github.com/stretchr/testify/assert"
)


func PrimeFactors(n int) string {
	var pexprs []string = make([]string, 0)
	var pcount int = 0
	for i := 2; i < n + 1; i++ {
		for n % i == 0 {
			pcount += 1
			n /= i
		}
		if pcount != 0 {
			if pcount == 1 {
				pexprs = append(pexprs, fmt.Sprintf("(%d)", i))
			} else {
				pexprs = append(pexprs, fmt.Sprintf("(%d**%d)", i, pcount))
			}
			pcount = 0
		}
		if n == 1 {
			break
		}
	}
	return strings.Join(pexprs, "")
}
// 既然有python的实现，怎么能不来一个go的实现来拼拼速度呢？测5200000下来，
// 361407个素数，golang实现0.2s，python实现6.6s，有空再写一个javascript的比比
func PrimeSieve(n int) []int {
	sieve := make([]bool, n + 1)
	sieve[0] = true
	sieve[1] = true

	for i := 2; i < int(math.Sqrt(float64(n))) + 1; i++ {
		pointer := i * 2
		for pointer <= n {
			sieve[pointer] = true
			pointer += i
		}
	}

	result := make([]int, 0)
	for i, _ := range sieve {
		if sieve[i] == false {
			result = append(result, i)
		}
	}
	return result
}

func timeTrack(start time.Time) {
	elapsed := time.Since(start)
	log.Println("it took ", float64(elapsed) / float64(int(time.Second)), " seconds.")
}

func TestPrimeFactors(t *testing.T) {
	main()
	self := assert.New(t)
	self.Equal(PrimeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)", "")
	self.Equal(PrimeFactors(7919), "(7919)", "")
	self.Equal(PrimeFactors(17*17*93*677), "(3)(17**2)(31)(677)", "")
	self.Equal(PrimeFactors(933555431), "(7537)(123863)", "")
	self.Equal(PrimeFactors(342217392), "(2**4)(3)(11)(43)(15073)","")
	self.Equal(PrimeFactors(35791357), "(7)(5113051)", "")
	self.Equal(PrimeFactors(782611830), "(2)(3**2)(5)(7**2)(11)(13)(17)(73)","")
	self.Equal(PrimeFactors(775878912), "(2**8)(3**4)(17)(31)(71)","")

}

func main() {
	start := time.Now()
	v := PrimeFactors(933555431)
	timeTrack(start)
	log.Println(v)
	start = time.Now()
	r := PrimeSieve(5200000)
	timeTrack(start)
	log.Println(len(r))
	log.Println(r[len(r) - 1])
}

