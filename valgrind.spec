Name     : valgrind
Version  : 3.12.0
Release  : 24
URL      : http://valgrind.org/downloads/valgrind-3.12.0.tar.bz2
Source0  : http://valgrind.org/downloads/valgrind-3.12.0.tar.bz2
Summary  : Valgrind Memory Debugger
Group    : Development/Tools
License  : GPL-2.0+ GFDL-1.2 GPL-2.0
Requires: valgrind-bin
Requires: valgrind-doc
BuildRequires : sed
Patch1: glibc-2.21.patch
Patch2: 0001-Accept-glibc-2.21-as-valid.patch

%description


%package bin
Summary: bin components for the valgrind package.
Group: Binaries

%description bin
bin components for the valgrind package.


%package dev
Summary: dev components for the valgrind package.
Group: Development
Requires: valgrind-bin

%description dev
dev components for the valgrind package.


%package doc
Summary: doc components for the valgrind package.
Group: Documentation

%description doc
doc components for the valgrind package.


%prep
%setup -q -n valgrind-3.12.0
%patch1 -p1
%patch2 -p1

%build
# -fexceptions causes memcheck link command to fail when built with GCC 5.1
export CFLAGS=`echo $CFLAGS | sed s,-fexceptions,,g | sed s:-Wp,-D_FORTIFY_SOURCE=2::g | sed s:-fstack-protector::g `
./autogen.sh
%configure --disable-static --enable-only64bit --enable-tls
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check ||:
/usr/bin/perl tests/vg_regtest cachegrind ||:
/usr/bin/perl tests/vg_regtest callgrind ||:
/usr/bin/perl tests/vg_regtest massif ||:
/usr/bin/perl tests/vg_regtest lackey ||:
/usr/bin/perl tests/vg_regtest helgrind ||:
/usr/bin/perl tests/vg_regtest drd ||:

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/valgrind/32bit-core-valgrind-s1.xml
/usr/lib64/valgrind/32bit-core-valgrind-s2.xml
/usr/lib64/valgrind/32bit-core.xml
/usr/lib64/valgrind/32bit-linux-valgrind-s1.xml
/usr/lib64/valgrind/32bit-linux-valgrind-s2.xml
/usr/lib64/valgrind/32bit-linux.xml
/usr/lib64/valgrind/32bit-sse-valgrind-s1.xml
/usr/lib64/valgrind/32bit-sse-valgrind-s2.xml
/usr/lib64/valgrind/32bit-sse.xml
/usr/lib64/valgrind/64bit-avx-valgrind-s1.xml
/usr/lib64/valgrind/64bit-avx-valgrind-s2.xml
/usr/lib64/valgrind/64bit-avx.xml
/usr/lib64/valgrind/64bit-core-valgrind-s1.xml
/usr/lib64/valgrind/64bit-core-valgrind-s2.xml
/usr/lib64/valgrind/64bit-core.xml
/usr/lib64/valgrind/64bit-linux-valgrind-s1.xml
/usr/lib64/valgrind/64bit-linux-valgrind-s2.xml
/usr/lib64/valgrind/64bit-linux.xml
/usr/lib64/valgrind/64bit-sse-valgrind-s1.xml
/usr/lib64/valgrind/64bit-sse-valgrind-s2.xml
/usr/lib64/valgrind/64bit-sse.xml
/usr/lib64/valgrind/amd64-avx-coresse-valgrind.xml
/usr/lib64/valgrind/amd64-avx-coresse.xml
/usr/lib64/valgrind/amd64-avx-linux-valgrind.xml
/usr/lib64/valgrind/amd64-avx-linux.xml
/usr/lib64/valgrind/amd64-coresse-valgrind.xml
/usr/lib64/valgrind/*-linux-valgrind.xml
/usr/lib64/valgrind/arm-core-valgrind-s1.xml
/usr/lib64/valgrind/arm-core-valgrind-s2.xml
/usr/lib64/valgrind/arm-core.xml
/usr/lib64/valgrind/arm-vfpv3-valgrind-s1.xml
/usr/lib64/valgrind/arm-vfpv3-valgrind-s2.xml
/usr/lib64/valgrind/arm-vfpv3.xml
/usr/lib64/valgrind/arm-with-vfpv3-valgrind.xml
/usr/lib64/valgrind/arm-with-vfpv3.xml
/usr/lib64/valgrind/cachegrind-*-linux
/usr/lib64/valgrind/callgrind-*-linux
/usr/lib64/valgrind/default.supp
/usr/lib64/valgrind/drd-*-linux
/usr/lib64/valgrind/exp-bbv-*-linux
/usr/lib64/valgrind/exp-dhat-*-linux
/usr/lib64/valgrind/exp-sgcheck-*-linux
/usr/lib64/valgrind/getoff-*-linux
/usr/lib64/valgrind/helgrind-*-linux
/usr/lib64/valgrind/i386-coresse-valgrind.xml
/usr/lib64/valgrind/i386-linux-valgrind.xml
/usr/lib64/valgrind/lackey-*-linux
/usr/lib64/valgrind/massif-*-linux
/usr/lib64/valgrind/memcheck-*-linux
/usr/lib64/valgrind/mips-cp0-valgrind-s1.xml
/usr/lib64/valgrind/mips-cp0-valgrind-s2.xml
/usr/lib64/valgrind/mips-cp0.xml
/usr/lib64/valgrind/mips-cpu-valgrind-s1.xml
/usr/lib64/valgrind/mips-cpu-valgrind-s2.xml
/usr/lib64/valgrind/mips-cpu.xml
/usr/lib64/valgrind/mips-fpu-valgrind-s1.xml
/usr/lib64/valgrind/mips-fpu-valgrind-s2.xml
/usr/lib64/valgrind/mips-fpu.xml
/usr/lib64/valgrind/mips-linux-valgrind.xml
/usr/lib64/valgrind/mips-linux.xml
/usr/lib64/valgrind/mips64-cp0-valgrind-s1.xml
/usr/lib64/valgrind/mips64-cp0-valgrind-s2.xml
/usr/lib64/valgrind/mips64-cp0.xml
/usr/lib64/valgrind/mips64-cpu-valgrind-s1.xml
/usr/lib64/valgrind/mips64-cpu-valgrind-s2.xml
/usr/lib64/valgrind/mips64-cpu.xml
/usr/lib64/valgrind/mips64-fpu-valgrind-s1.xml
/usr/lib64/valgrind/mips64-fpu-valgrind-s2.xml
/usr/lib64/valgrind/mips64-fpu.xml
/usr/lib64/valgrind/mips64-linux-valgrind.xml
/usr/lib64/valgrind/mips64-linux.xml
/usr/lib64/valgrind/none-*-linux
/usr/lib64/valgrind/power-altivec-valgrind-s1.xml
/usr/lib64/valgrind/power-altivec-valgrind-s2.xml
/usr/lib64/valgrind/power-altivec.xml
/usr/lib64/valgrind/power-core-valgrind-s1.xml
/usr/lib64/valgrind/power-core-valgrind-s2.xml
/usr/lib64/valgrind/power-core.xml
/usr/lib64/valgrind/power-fpu-valgrind-s1.xml
/usr/lib64/valgrind/power-fpu-valgrind-s2.xml
/usr/lib64/valgrind/power-fpu.xml
/usr/lib64/valgrind/power-linux-valgrind-s1.xml
/usr/lib64/valgrind/power-linux-valgrind-s2.xml
/usr/lib64/valgrind/power-linux.xml
/usr/lib64/valgrind/power-vsx-valgrind-s1.xml
/usr/lib64/valgrind/power-vsx-valgrind-s2.xml
/usr/lib64/valgrind/power-vsx.xml
/usr/lib64/valgrind/power64-core-valgrind-s1.xml
/usr/lib64/valgrind/power64-core-valgrind-s2.xml
/usr/lib64/valgrind/power64-core.xml
/usr/lib64/valgrind/power64-core2-valgrind-s1.xml
/usr/lib64/valgrind/power64-core2-valgrind-s2.xml
/usr/lib64/valgrind/power64-linux-valgrind-s1.xml
/usr/lib64/valgrind/power64-linux-valgrind-s2.xml
/usr/lib64/valgrind/power64-linux.xml
/usr/lib64/valgrind/powerpc-altivec32l-valgrind.xml
/usr/lib64/valgrind/powerpc-altivec32l.xml
/usr/lib64/valgrind/powerpc-altivec64l-valgrind.xml
/usr/lib64/valgrind/powerpc-altivec64l.xml
/usr/lib64/valgrind/s390-acr-valgrind-s1.xml
/usr/lib64/valgrind/s390-acr-valgrind-s2.xml
/usr/lib64/valgrind/s390-acr.xml
/usr/lib64/valgrind/s390-fpr-valgrind-s1.xml
/usr/lib64/valgrind/s390-fpr-valgrind-s2.xml
/usr/lib64/valgrind/s390-fpr.xml
/usr/lib64/valgrind/s390x-core64-valgrind-s1.xml
/usr/lib64/valgrind/s390x-core64-valgrind-s2.xml
/usr/lib64/valgrind/s390x-core64.xml
/usr/lib64/valgrind/s390x-generic-valgrind.xml
/usr/lib64/valgrind/s390x-generic.xml
/usr/lib64/valgrind/s390x-linux64-valgrind-s1.xml
/usr/lib64/valgrind/s390x-linux64-valgrind-s2.xml
/usr/lib64/valgrind/s390x-linux64.xml
/usr/lib64/valgrind/vgpreload_core-*-linux.so
/usr/lib64/valgrind/vgpreload_drd-*-linux.so
/usr/lib64/valgrind/vgpreload_exp-dhat-*-linux.so
/usr/lib64/valgrind/vgpreload_exp-sgcheck-*-linux.so
/usr/lib64/valgrind/vgpreload_helgrind-*-linux.so
/usr/lib64/valgrind/vgpreload_massif-*-linux.so
/usr/lib64/valgrind/vgpreload_memcheck-*-linux.so

%files bin
%defattr(-,root,root,-)
/usr/bin/callgrind_annotate
/usr/bin/callgrind_control
/usr/bin/cg_annotate
/usr/bin/cg_diff
/usr/bin/cg_merge
/usr/bin/ms_print
/usr/bin/valgrind
/usr/bin/valgrind-di-server
/usr/bin/valgrind-listener
/usr/bin/vgdb

%files dev
%defattr(-,root,root,-)
/usr/include/valgrind/callgrind.h
/usr/include/valgrind/config.h
/usr/include/valgrind/drd.h
/usr/include/valgrind/helgrind.h
/usr/include/valgrind/libvex.h
/usr/include/valgrind/libvex_basictypes.h
/usr/include/valgrind/libvex_emnote.h
/usr/include/valgrind/libvex_guest_amd64.h
/usr/include/valgrind/libvex_guest_arm.h
/usr/include/valgrind/libvex_guest_arm64.h
/usr/include/valgrind/libvex_guest_mips32.h
/usr/include/valgrind/libvex_guest_mips64.h
/usr/include/valgrind/libvex_guest_offsets.h
/usr/include/valgrind/libvex_guest_ppc32.h
/usr/include/valgrind/libvex_guest_ppc64.h
/usr/include/valgrind/libvex_guest_s390x.h
/usr/include/valgrind/libvex_guest_x86.h
/usr/include/valgrind/libvex_ir.h
/usr/include/valgrind/libvex_s390x_common.h
/usr/include/valgrind/libvex_trc_values.h
/usr/include/valgrind/memcheck.h
/usr/include/valgrind/pub_tool_addrinfo.h
/usr/include/valgrind/pub_tool_aspacehl.h
/usr/include/valgrind/pub_tool_aspacemgr.h
/usr/include/valgrind/pub_tool_basics.h
/usr/include/valgrind/pub_tool_basics_asm.h
/usr/include/valgrind/pub_tool_clientstate.h
/usr/include/valgrind/pub_tool_clreq.h
/usr/include/valgrind/pub_tool_debuginfo.h
/usr/include/valgrind/pub_tool_deduppoolalloc.h
/usr/include/valgrind/pub_tool_errormgr.h
/usr/include/valgrind/pub_tool_execontext.h
/usr/include/valgrind/pub_tool_gdbserver.h
/usr/include/valgrind/pub_tool_hashtable.h
/usr/include/valgrind/pub_tool_libcassert.h
/usr/include/valgrind/pub_tool_libcbase.h
/usr/include/valgrind/pub_tool_libcfile.h
/usr/include/valgrind/pub_tool_libcprint.h
/usr/include/valgrind/pub_tool_libcproc.h
/usr/include/valgrind/pub_tool_libcsetjmp.h
/usr/include/valgrind/pub_tool_libcsignal.h
/usr/include/valgrind/pub_tool_machine.h
/usr/include/valgrind/pub_tool_mallocfree.h
/usr/include/valgrind/pub_tool_options.h
/usr/include/valgrind/pub_tool_oset.h
/usr/include/valgrind/pub_tool_poolalloc.h
/usr/include/valgrind/pub_tool_rangemap.h
/usr/include/valgrind/pub_tool_redir.h
/usr/include/valgrind/pub_tool_replacemalloc.h
/usr/include/valgrind/pub_tool_seqmatch.h
/usr/include/valgrind/pub_tool_signals.h
/usr/include/valgrind/pub_tool_sparsewa.h
/usr/include/valgrind/pub_tool_stacktrace.h
/usr/include/valgrind/pub_tool_threadstate.h
/usr/include/valgrind/pub_tool_tooliface.h
/usr/include/valgrind/pub_tool_vki.h
/usr/include/valgrind/pub_tool_vkiscnums.h
/usr/include/valgrind/pub_tool_vkiscnums_asm.h
/usr/include/valgrind/pub_tool_wordfm.h
/usr/include/valgrind/pub_tool_xarray.h
/usr/include/valgrind/valgrind.h
/usr/include/valgrind/vki/vki-*-linux.h
/usr/include/valgrind/vki/vki-arm-linux.h
/usr/include/valgrind/vki/vki-arm64-linux.h
/usr/include/valgrind/vki/vki-darwin.h
/usr/include/valgrind/vki/vki-linux-drm.h
/usr/include/valgrind/vki/vki-linux.h
/usr/include/valgrind/vki/vki-mips32-linux.h
/usr/include/valgrind/vki/vki-mips64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-*-linux.h
/usr/include/valgrind/vki/vki-posixtypes-arm-linux.h
/usr/include/valgrind/vki/vki-posixtypes-arm64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-mips32-linux.h
/usr/include/valgrind/vki/vki-posixtypes-mips64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-ppc32-linux.h
/usr/include/valgrind/vki/vki-posixtypes-ppc64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-s390x-linux.h
/usr/include/valgrind/vki/vki-posixtypes-x86-linux.h
/usr/include/valgrind/vki/vki-ppc32-linux.h
/usr/include/valgrind/vki/vki-ppc64-linux.h
/usr/include/valgrind/vki/vki-s390x-linux.h
/usr/include/valgrind/vki/vki-scnums-*-linux.h
/usr/include/valgrind/vki/vki-scnums-arm-linux.h
/usr/include/valgrind/vki/vki-scnums-arm64-linux.h
/usr/include/valgrind/vki/vki-scnums-darwin.h
/usr/include/valgrind/vki/vki-scnums-mips32-linux.h
/usr/include/valgrind/vki/vki-scnums-mips64-linux.h
/usr/include/valgrind/vki/vki-scnums-ppc32-linux.h
/usr/include/valgrind/vki/vki-scnums-ppc64-linux.h
/usr/include/valgrind/vki/vki-scnums-s390x-linux.h
/usr/include/valgrind/vki/vki-scnums-x86-linux.h
/usr/include/valgrind/vki/vki-x86-linux.h
/usr/include/valgrind/vki/vki-xen-domctl.h
/usr/include/valgrind/vki/vki-xen-evtchn.h
/usr/include/valgrind/vki/vki-xen-gnttab.h
/usr/include/valgrind/vki/vki-xen-hvm.h
/usr/include/valgrind/vki/vki-xen-memory.h
/usr/include/valgrind/vki/vki-xen-mmuext.h
/usr/include/valgrind/vki/vki-xen-sysctl.h
/usr/include/valgrind/vki/vki-xen-tmem.h
/usr/include/valgrind/vki/vki-xen-version.h
/usr/include/valgrind/vki/vki-xen-x86.h
/usr/include/valgrind/vki/vki-xen.h
/usr/include/valgrind/libvex_guest_tilegx.h
/usr/include/valgrind/pub_tool_guest.h
/usr/include/valgrind/pub_tool_transtab.h
/usr/include/valgrind/vki/vki-scnums-solaris.h
/usr/include/valgrind/vki/vki-solaris-repcache.h
/usr/include/valgrind/vki/vki-solaris.h
/usr/include/valgrind/vki/vki-xen-physdev.h
/usr/include/valgrind/vki/vki-xen-schedop.h
/usr/include/valgrind/vki/vki-xen-xsm.h

/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/valgrind/*
%doc /usr/share/man/man1/*
