# eBPF hello world

This counts the number of invocations used by a particular user by running a program in userspace that traces kernelspace syscalls.

- Uses the BPF_HASH(name) method to create a map of key values.
- Uses the privileged function bpf_get_current_uid_gid()
