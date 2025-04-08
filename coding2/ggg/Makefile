Link: hi.o
	ld -o hi hi.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64
	echo "Assembled hi.s to hi.o and Linked hi.o to hi"
	echo "To run use ./hi"
Assemble: hi.s
	as -o hi.o hi.s
clean:
	rm hi
	rm hi.o