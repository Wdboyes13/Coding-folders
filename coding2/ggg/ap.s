.global _start
.align 2
_start: mov x0, #1
        add x5, x0, #2

        mov x0, x5
        bl printf

        mov x0, #0
        mov x16, #1
        svc 0