# Compiling tcpdump for embedded targets

* Cross-compile libpcap first and point `PCAP_ROOT` at it.
* Pass `-DCMAKE_TOOLCHAIN_FILE=<file>` to CMake.
* A static build needs `-DBUILD_SHARED_LIBS=OFF` in libpcap.
