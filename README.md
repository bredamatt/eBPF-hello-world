# eBPF hello world

This counts the number of syscall, kernel function ++ invocations used by a uid. This Python program runs in userspace, but is capable via eBPF to perform traces in kernelspace.

- Uses the BPF_HASH(name) method to create a map of key values.
- Uses the privileged function bpf_get_current_uid_gid()
