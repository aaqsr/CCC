#lang racket

;; A simple script to calculate the factorial

(define (fact num)
  (if (= num 2)
      2
      (* (fact (- num 1)) num)))

(fact 5)
