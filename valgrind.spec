Name     : valgrind
Version  : 3.13.0
Release  : 29
URL      : ftp://sourceware.org/pub/valgrind/valgrind-3.13.0.tar.bz2
Source0  : ftp://sourceware.org/pub/valgrind/valgrind-3.13.0.tar.bz2
Summary  : Valgrind Memory Debugger
Group    : Development/Tools
License  : GPL-2.0+ GFDL-1.2 GPL-2.0
Requires: valgrind-bin
Requires: valgrind-doc
BuildRequires : sed
BuildRequires : zlib-dev
BuildRequires : libxml2-dev
BuildRequires : openmpi-dev
BuildRequires : boost-dev

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
%setup -q -n valgrind-3.13.0
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
/usr/lib64/valgrind/*.xml
/usr/lib64/valgrind/vgpreload_core-*-linux.so
/usr/lib64/valgrind/vgpreload_drd-*-linux.so
/usr/lib64/valgrind/vgpreload_exp-dhat-*-linux.so
/usr/lib64/valgrind/vgpreload_exp-sgcheck-*-linux.so
/usr/lib64/valgrind/vgpreload_helgrind-*-linux.so
/usr/lib64/valgrind/vgpreload_massif-*-linux.so
/usr/lib64/valgrind/vgpreload_memcheck-*-linux.so
/usr/lib64/valgrind/cachegrind-amd64-linux
/usr/lib64/valgrind/callgrind-amd64-linux
/usr/lib64/valgrind/default.supp
/usr/lib64/valgrind/drd-amd64-linux
/usr/lib64/valgrind/exp-bbv-amd64-linux
/usr/lib64/valgrind/exp-dhat-amd64-linux
/usr/lib64/valgrind/exp-sgcheck-amd64-linux
/usr/lib64/valgrind/getoff-amd64-linux
/usr/lib64/valgrind/helgrind-amd64-linux
/usr/lib64/valgrind/lackey-amd64-linux
/usr/lib64/valgrind/libmpiwrap-amd64-linux.so
/usr/lib64/valgrind/massif-amd64-linux
/usr/lib64/valgrind/memcheck-amd64-linux
/usr/lib64/valgrind/none-amd64-linux

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
/usr/include/valgrind/pub_tool_guest.h
/usr/include/valgrind/pub_tool_transtab.h
/usr/include/valgrind/vki/vki-scnums-solaris.h
/usr/include/valgrind/vki/vki-solaris-repcache.h
/usr/include/valgrind/vki/vki-solaris.h
/usr/include/valgrind/vki/vki-xen-physdev.h
/usr/include/valgrind/vki/vki-xen-schedop.h
/usr/include/valgrind/vki/vki-xen-xsm.h
/usr/include/valgrind/pub_tool_xtmemory.h
/usr/include/valgrind/pub_tool_xtree.h

/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/valgrind/*
%doc /usr/share/man/man1/*
