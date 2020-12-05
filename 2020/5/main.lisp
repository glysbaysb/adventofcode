; https://stackoverflow.com/questions/3813895/how-can-i-read-the-contents-of-a-file-into-a-list-in-lisp
(defun get-file (filename)
  (with-open-file (stream filename)
      (loop for line = (read-line stream nil)
			while line
		    collect line)))
(defun bsp (str to front back)
  (let ((res (list 0 to)))
	  (loop for c across str do
		(cond ((EQ c front) (setf res (list 
										(car res)
										(FLOOR (/ (+ (car res) (car (cdr res))) 2)))))
			  ((EQ c back) (setf res (list 
										(CEILING (/ (+ (car res) (car (cdr res))) 2))
										(car (cdr res)))))
			  )
		)
	(car res)))
(defun id-from-boarding-pass (boarding-pass)
	(+ 
	  (* 8 (BSP (subseq boarding-pass 0 7) 127.0 #\F #\B))
	  (BSP (subseq boarding-pass 7) 7.0 #\L #\R)))
(print (id-from-boarding-pass "FBFBBFFRLR"))
(loop for boarding-pass in (get-file "input")
	  do (print (id-from-boarding-pass boarding-pass)))
