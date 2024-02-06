0x0B-python-input_output

Python Read File and Python Write to File

Python Access Methods
```
Mode	Function
r	Open a file for reading. This is the default mode.
w	Open a file for writing. If the file already exists, overwrite its contents. Create a new file if the file does not exist.
a	Open a file for appending. Preserve the file’s contents, add new data to the end of the file.
r+	Open a file for reading and writing.
w+	Allows to write as well as read from the file.
a+	
```

Python file Methods
```
Method	What it does
close()	Closes the file.
flush()	Flushes the internal buffer.
fileno()	Returns the file descriptor of the file.
next()	Returns the next line from the file.
read(size)	Reads size number of bytes from the file. Reads the entire file if you don’t pass any argument value.
readline(size)	Reads one line from a file. 
readlines()	Reads the entire file and returns a list of the lines.
seek(offset, whence)	Lets us control the position of the file pointer.
tell()	Returns the current position of the file pointer.
truncate(size)	It truncates the file to the specified size.
writable()	Returns True if we can write into the file.
write(string)	Writes string into the file.
writelines(list_of_strings)	Writes each element of the list_of_strings into the file.
```
