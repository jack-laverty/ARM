.text
.global _start          @ .global directive
_start:                 @ _start is the default entry point, program now has a place to start
    mov r0, #1          @ code 1 to r0 will write the data, length  at memory address in r1
    ldr r1, =message    @ loads r1 with memory address of message
    ldr r2, =len        @ loads r2 with length of message
    mov r7, #4          @ system call codes are passed to reg 7 and SYS_WRITE code is 4
    swi 0

    mov r7, #1          @ system call codes are passed to reg 7 and SYS_EXIT code is 1
    swi 0               @ causes SWI exception. processor state changes to ARM, processor mode changes to supervisor
                        @ the CPSR issaved to the supervisor mode SPSR, and the execution brances to the SWI vector
                        @ which we have specified in r0

.data
message:
    .asciz "hello world\n" @.asciz directive tells assembler the data is a null terminated string
len = .-message