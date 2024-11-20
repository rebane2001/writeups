# Truth of NPM

Deno chall.

I don't remember the exact details but pretty much what happens is that the `package.json` exports gets interpreted weirdly by this code in the chall:
```ts
const module = await import(`npm:${packageName}/package.json`, {
	with: {
		type: 'json'
	}
})
```
which means the
```json
  "exports": {
      ".": {},
      "./package.json": "./evilcode.js"
  }
```
in the package.json ends up executing `evilcode.js`.

The `evilcode.js` copies the `maps` file and symlinks the `mem` file so that we can mess with them even though there are supposed to be protections in place for that:
```ts
await Deno.copyFile("proc/self/maps", "/tmp/maps");
await Deno.symlink("/proc/self/mem", "/tmp/mem")
```

The payload is something I pinched from [this blogpost](https://secfault-security.com/blog/deno.html) and edited a little to work for this chall. You'll notice I uh... didn't bother to find the right offsets xD - `shellcode = "\x90".repeat(1000000) + shellcode`.