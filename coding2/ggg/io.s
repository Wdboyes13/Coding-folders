.global _start
.align 2
_start: 
        mov x0, #0              // File descriptor 0 (stdin)
        adr x1, input           // Address of the buffer to store input
        mov x2, #100            // Number of bytes to read
        mov x16, #3             // System call for read
        svc #0                  // Trigger the system call

        cmp x0, #0              // Compare the number of bytes read with 0
        beq no_input            // If 0 bytes were read, branch to no_input

        mov x1, input           // Address of the buffer to write
        mov x2, x0              // Number of bytes read
        mov x0, #1              // File descriptor 1 (stdout)
        mov x16, #4             // System call for write
        svc #0                  // Trigger the system call

        b exit                  // Skip to exit

no_input:
        adr x1, no_data_msg     // Address of the "No input" message
        mov x2, #8              // Length of the message
        mov x0, #1              // File descriptor 1 (stdout)
        mov x16, #4             // System call for write
        svc #0                  // Trigger the system call

exit:
        mov x0, #0              // Exit code 0
        mov x16, #1             // System call for exit
        svc #0                  // Trigger the system call

input: 
        .skip 100               // Reserve 100 bytes for input
no_data_msg:
        .asciz "No input\n"     // Message to display if no input is provided