.global _start
.align 2
_start: mov x0, #1
        adr x1, hello
        mov x16, #4
        mov x2, #5
        svc 0

        mov x0, #1
        adr x1, name
        mov x16, #4
        mov x2, #20
        svc 0

        mov x0, #0
        mov x16, #1
        svc 0
hello: .asciz "Hey!\n"
name: .asciz "My name is william!\n"