# Flag Reader

The chall was a Python script that took a .tar file, made sure its contents were safe, and then ran `tar -xf` on the file to extract it. The goal was to create a tar file that appeared differently to Python and `tar`.

I explained my solve to others on Discord, so these are my messages from there :P.

> my solution for flag reader
> made a bzip2 tar file, then set that as a filename inside of an uncompressed USTAR tar, corrupted the tar a bit to make file say it's bzip2 - python read the USTAR tar and tar command read the bzip2 filename as a bzip2 tar file

> here's the solve file if anyone wants to reference, also the process for creating it:
> first i made a link and then messed around with tar/bz params until i could get it down to 101 bytes

```bash
ln -s /flag.txt flag.txt
BZIP=-9 tar --no-xattrs --no-acls --owner=0 --group=0 --numeric-owner --mtime='@2' --bzip2 -cvf test3.tar.gz flag.txt
```

> the @2 for the time is just because it offered a better 101th character
> filenames are limited to 100 chars so when i made the tar i just changed the 101th char lol
> the checksum ends with `\x1d\x1d` because it gets stripped by python but confuses `file`
> also i edited the ustar thing because otherwise file still picked it up

the `intended_solution_org.py` file has the intended solution by the organizers