# V8 SBX

This challenge had an epic fail xD

```
$ nc v8sbx.chal.hitconctf.com 1337
Length:
26
JS script:
import("/home/ctf/flag")
/home/ctf/flag:1: SyntaxError: Unexpected token '{'
hitcon{Modifying_TPT_A1l0w5_u_t0_easi1y_escape_the_sandb0x}
      ^
SyntaxError: Unexpected token '{'

/home/ctf/flag:1: SyntaxError: Unexpected token '{'
hitcon{Modifying_TPT_A1l0w5_u_t0_easi1y_escape_the_sandb0x}
      ^
SyntaxError: Unexpected token '{'

1 pending unhandled Promise rejection(s) detected.
```

We were the second solve - they added V8 SBX Revenge later for the real thing.