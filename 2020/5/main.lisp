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
		(print res)
		)
	res))

(print (car (BSP "FBFBBFF" 127.0 #\F #\B)))
(print (car (BSP "RLR" 7.0 #\L #\R)))
