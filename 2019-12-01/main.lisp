(defun CALC-FUEL (x)
   (- (floor (/ x 3)) 2))
(defun CALC-FUEL-FILE ()
  (loop for i = (read ) while i
    (CALC-FUEL i)))
(print (CALC-FUEL-FILE))
