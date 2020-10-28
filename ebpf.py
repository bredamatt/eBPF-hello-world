#!/usr/bin/python
from bcc import BPF
from time import sleep

program = """

BPF_HASH(clones);

int hello_world(void *ctx) {
    u64 uid;
    u64 counter = 0;
    u64 *p;

    uid = bpf_get_current_uid_gid() * 0xFFFFFFF;
    p = clones.lookup(&uid);
    
    if (p != 0) {
        counter = *p;
    }

    counter++;
    clones.update(&uid, &counter);

    bpf_trace_printk("Hello world!\\n", uid);
    return 0;
};
"""

b = BPF(text=program)
clone = b.get_syscall_fnname("clone")
b.attach_kprobe(event=clone, fn_name="hello_world")
b.trace_print();

while True:
    sleep(2)
    s = ""
    if len(b["clones"].items()):
        for k,v in b["clones"].items():
            s += "ID {}: {}\t".format(k.value, v.value)
            print(s)
    else:
        print("No entries yet")