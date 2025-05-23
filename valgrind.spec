#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
%define keepstatic 1
Name     : valgrind
Version  : 3.20.0
Release  : 45
URL      : https://sourceware.org/pub/valgrind/valgrind-3.20.0.tar.bz2
Source0  : https://sourceware.org/pub/valgrind/valgrind-3.20.0.tar.bz2
Source1  : https://sourceware.org/pub/valgrind/valgrind-3.20.0.tar.bz2.asc
Summary  : Valgrind Memory Debugger
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-2.0+
Requires: valgrind-bin = %{version}-%{release}
Requires: valgrind-libexec = %{version}-%{release}
Requires: valgrind-license = %{version}-%{release}
Requires: valgrind-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : libxml2-dev
BuildRequires : procps-ng
BuildRequires : sed
BuildRequires : zlib-dev
Patch1: glibc-2.21.patch
Patch2: 0001-Accept-glibc-2.21-as-valid.patch

%description
Release notes for Valgrind
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are building a binary package of Valgrind for distribution,

%package bin
Summary: bin components for the valgrind package.
Group: Binaries
Requires: valgrind-libexec = %{version}-%{release}
Requires: valgrind-license = %{version}-%{release}

%description bin
bin components for the valgrind package.


%package dev
Summary: dev components for the valgrind package.
Group: Development
Requires: valgrind-bin = %{version}-%{release}
Provides: valgrind-devel = %{version}-%{release}
Requires: valgrind = %{version}-%{release}

%description dev
dev components for the valgrind package.


%package doc
Summary: doc components for the valgrind package.
Group: Documentation
Requires: valgrind-man = %{version}-%{release}

%description doc
doc components for the valgrind package.


%package libexec
Summary: libexec components for the valgrind package.
Group: Default
Requires: valgrind-license = %{version}-%{release}

%description libexec
libexec components for the valgrind package.


%package license
Summary: license components for the valgrind package.
Group: Default

%description license
license components for the valgrind package.


%package man
Summary: man components for the valgrind package.
Group: Default

%description man
man components for the valgrind package.


%prep
%setup -q -n valgrind-3.20.0
cd %{_builddir}/valgrind-3.20.0
%patch1 -p1
%patch2 -p1

%build
## build_prepend content
export CFLAGS=`echo $CFLAGS | sed s,-fexceptions,,g | sed s:-Wp,-D_FORTIFY_SOURCE=2::g | sed s:-fstack-protector::g `
./autogen.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666740305
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure  || ./configure --enable-static --enable-only64bit --enable-tls
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check ||:
/usr/bin/perl tests/vg_regtest cachegrind ||:
/usr/bin/perl tests/vg_regtest callgrind ||:
/usr/bin/perl tests/vg_regtest massif ||:
/usr/bin/perl tests/vg_regtest lackey ||:
/usr/bin/perl tests/vg_regtest helgrind ||:
/usr/bin/perl tests/vg_regtest drd ||:
/usr/bin/perl tests/vg_regtest dhat ||:

%install
export SOURCE_DATE_EPOCH=1666740305
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/valgrind
cp %{_builddir}/valgrind-%{version}/COPYING %{buildroot}/usr/share/package-licenses/valgrind/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/valgrind-%{version}/COPYING.DOCS %{buildroot}/usr/share/package-licenses/valgrind/fcbf818f92ef8679a88f3778b12b4c8b5810545b
cp %{_builddir}/valgrind-%{version}/VEX/LICENSE.GPL %{buildroot}/usr/share/package-licenses/valgrind/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/valgrind-%{version}/VEX/LICENSE.README %{buildroot}/usr/share/package-licenses/valgrind/61ef372f94283a2e8909d8a5b7516abe2550fbbe
cp %{_builddir}/valgrind-%{version}/docs/html/license.gfdl.html %{buildroot}/usr/share/package-licenses/valgrind/00921e181567bf8fdfbc06375d10ed399d48b185
cp %{_builddir}/valgrind-%{version}/docs/html/license.gpl.html %{buildroot}/usr/share/package-licenses/valgrind/4b3d52fc140815bc03cbab3184a6be494eb808da
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/valgrind/libcoregrind-amd64-linux.a
/usr/lib64/valgrind/libgcc-sup-amd64-linux.a
/usr/lib64/valgrind/libreplacemalloc_toolpreload-amd64-linux.a
/usr/lib64/valgrind/libvex-amd64-linux.a
/usr/lib64/valgrind/libvexmultiarch-amd64-linux.a

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
/usr/include/valgrind/dhat.h
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
/usr/include/valgrind/libvex_inner.h
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
/usr/include/valgrind/pub_tool_guest.h
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
/usr/include/valgrind/pub_tool_transtab.h
/usr/include/valgrind/pub_tool_vki.h
/usr/include/valgrind/pub_tool_vkiscnums.h
/usr/include/valgrind/pub_tool_vkiscnums_asm.h
/usr/include/valgrind/pub_tool_wordfm.h
/usr/include/valgrind/pub_tool_xarray.h
/usr/include/valgrind/pub_tool_xtmemory.h
/usr/include/valgrind/pub_tool_xtree.h
/usr/include/valgrind/valgrind.h
/usr/include/valgrind/vki/vki-amd64-freebsd.h
/usr/include/valgrind/vki/vki-amd64-linux.h
/usr/include/valgrind/vki/vki-arm-linux.h
/usr/include/valgrind/vki/vki-arm64-linux.h
/usr/include/valgrind/vki/vki-darwin.h
/usr/include/valgrind/vki/vki-freebsd.h
/usr/include/valgrind/vki/vki-linux-drm.h
/usr/include/valgrind/vki/vki-linux-io_uring.h
/usr/include/valgrind/vki/vki-linux.h
/usr/include/valgrind/vki/vki-machine-types-amd64-freebsd.h
/usr/include/valgrind/vki/vki-machine-types-x86-freebsd.h
/usr/include/valgrind/vki/vki-mips32-linux.h
/usr/include/valgrind/vki/vki-mips64-linux.h
/usr/include/valgrind/vki/vki-nanomips-linux.h
/usr/include/valgrind/vki/vki-posixtypes-amd64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-arm-linux.h
/usr/include/valgrind/vki/vki-posixtypes-arm64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-mips32-linux.h
/usr/include/valgrind/vki/vki-posixtypes-mips64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-nanomips-linux.h
/usr/include/valgrind/vki/vki-posixtypes-ppc32-linux.h
/usr/include/valgrind/vki/vki-posixtypes-ppc64-linux.h
/usr/include/valgrind/vki/vki-posixtypes-s390x-linux.h
/usr/include/valgrind/vki/vki-posixtypes-x86-linux.h
/usr/include/valgrind/vki/vki-ppc32-linux.h
/usr/include/valgrind/vki/vki-ppc64-linux.h
/usr/include/valgrind/vki/vki-s390x-linux.h
/usr/include/valgrind/vki/vki-scnums-32bit-linux.h
/usr/include/valgrind/vki/vki-scnums-amd64-linux.h
/usr/include/valgrind/vki/vki-scnums-arm-linux.h
/usr/include/valgrind/vki/vki-scnums-arm64-linux.h
/usr/include/valgrind/vki/vki-scnums-darwin.h
/usr/include/valgrind/vki/vki-scnums-freebsd.h
/usr/include/valgrind/vki/vki-scnums-mips32-linux.h
/usr/include/valgrind/vki/vki-scnums-mips64-linux.h
/usr/include/valgrind/vki/vki-scnums-nanomips-linux.h
/usr/include/valgrind/vki/vki-scnums-ppc32-linux.h
/usr/include/valgrind/vki/vki-scnums-ppc64-linux.h
/usr/include/valgrind/vki/vki-scnums-s390x-linux.h
/usr/include/valgrind/vki/vki-scnums-shared-linux.h
/usr/include/valgrind/vki/vki-scnums-solaris.h
/usr/include/valgrind/vki/vki-scnums-x86-linux.h
/usr/include/valgrind/vki/vki-solaris-repcache.h
/usr/include/valgrind/vki/vki-solaris.h
/usr/include/valgrind/vki/vki-x86-freebsd.h
/usr/include/valgrind/vki/vki-x86-linux.h
/usr/include/valgrind/vki/vki-xen-domctl.h
/usr/include/valgrind/vki/vki-xen-evtchn.h
/usr/include/valgrind/vki/vki-xen-gnttab.h
/usr/include/valgrind/vki/vki-xen-hvm.h
/usr/include/valgrind/vki/vki-xen-memory.h
/usr/include/valgrind/vki/vki-xen-mmuext.h
/usr/include/valgrind/vki/vki-xen-physdev.h
/usr/include/valgrind/vki/vki-xen-schedop.h
/usr/include/valgrind/vki/vki-xen-sysctl.h
/usr/include/valgrind/vki/vki-xen-tmem.h
/usr/include/valgrind/vki/vki-xen-version.h
/usr/include/valgrind/vki/vki-xen-x86.h
/usr/include/valgrind/vki/vki-xen-xsm.h
/usr/include/valgrind/vki/vki-xen.h
/usr/lib64/pkgconfig/valgrind.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/valgrind/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/valgrind/32bit-core-valgrind-s1.xml
/usr/libexec/valgrind/32bit-core-valgrind-s2.xml
/usr/libexec/valgrind/32bit-core.xml
/usr/libexec/valgrind/32bit-linux-valgrind-s1.xml
/usr/libexec/valgrind/32bit-linux-valgrind-s2.xml
/usr/libexec/valgrind/32bit-linux.xml
/usr/libexec/valgrind/32bit-sse-valgrind-s1.xml
/usr/libexec/valgrind/32bit-sse-valgrind-s2.xml
/usr/libexec/valgrind/32bit-sse.xml
/usr/libexec/valgrind/64bit-avx-valgrind-s1.xml
/usr/libexec/valgrind/64bit-avx-valgrind-s2.xml
/usr/libexec/valgrind/64bit-avx.xml
/usr/libexec/valgrind/64bit-core-valgrind-s1.xml
/usr/libexec/valgrind/64bit-core-valgrind-s2.xml
/usr/libexec/valgrind/64bit-core.xml
/usr/libexec/valgrind/64bit-linux-valgrind-s1.xml
/usr/libexec/valgrind/64bit-linux-valgrind-s2.xml
/usr/libexec/valgrind/64bit-linux.xml
/usr/libexec/valgrind/64bit-sse-valgrind-s1.xml
/usr/libexec/valgrind/64bit-sse-valgrind-s2.xml
/usr/libexec/valgrind/64bit-sse.xml
/usr/libexec/valgrind/amd64-avx-coresse-valgrind.xml
/usr/libexec/valgrind/amd64-avx-coresse.xml
/usr/libexec/valgrind/amd64-avx-linux-valgrind.xml
/usr/libexec/valgrind/amd64-avx-linux.xml
/usr/libexec/valgrind/amd64-coresse-valgrind.xml
/usr/libexec/valgrind/amd64-linux-valgrind.xml
/usr/libexec/valgrind/arm-core-valgrind-s1.xml
/usr/libexec/valgrind/arm-core-valgrind-s2.xml
/usr/libexec/valgrind/arm-core.xml
/usr/libexec/valgrind/arm-vfpv3-valgrind-s1.xml
/usr/libexec/valgrind/arm-vfpv3-valgrind-s2.xml
/usr/libexec/valgrind/arm-vfpv3.xml
/usr/libexec/valgrind/arm-with-vfpv3-valgrind.xml
/usr/libexec/valgrind/arm-with-vfpv3.xml
/usr/libexec/valgrind/cachegrind-amd64-linux
/usr/libexec/valgrind/callgrind-amd64-linux
/usr/libexec/valgrind/default.supp
/usr/libexec/valgrind/dh_view.css
/usr/libexec/valgrind/dh_view.html
/usr/libexec/valgrind/dh_view.js
/usr/libexec/valgrind/dhat-amd64-linux
/usr/libexec/valgrind/drd-amd64-linux
/usr/libexec/valgrind/exp-bbv-amd64-linux
/usr/libexec/valgrind/getoff-amd64-linux
/usr/libexec/valgrind/helgrind-amd64-linux
/usr/libexec/valgrind/i386-coresse-valgrind.xml
/usr/libexec/valgrind/i386-linux-valgrind.xml
/usr/libexec/valgrind/lackey-amd64-linux
/usr/libexec/valgrind/massif-amd64-linux
/usr/libexec/valgrind/memcheck-amd64-linux
/usr/libexec/valgrind/mips-cp0-valgrind-s1.xml
/usr/libexec/valgrind/mips-cp0-valgrind-s2.xml
/usr/libexec/valgrind/mips-cp0.xml
/usr/libexec/valgrind/mips-cpu-valgrind-s1.xml
/usr/libexec/valgrind/mips-cpu-valgrind-s2.xml
/usr/libexec/valgrind/mips-cpu.xml
/usr/libexec/valgrind/mips-fpu-valgrind-s1.xml
/usr/libexec/valgrind/mips-fpu-valgrind-s2.xml
/usr/libexec/valgrind/mips-fpu.xml
/usr/libexec/valgrind/mips-linux-valgrind.xml
/usr/libexec/valgrind/mips-linux.xml
/usr/libexec/valgrind/mips64-cp0-valgrind-s1.xml
/usr/libexec/valgrind/mips64-cp0-valgrind-s2.xml
/usr/libexec/valgrind/mips64-cp0.xml
/usr/libexec/valgrind/mips64-cpu-valgrind-s1.xml
/usr/libexec/valgrind/mips64-cpu-valgrind-s2.xml
/usr/libexec/valgrind/mips64-cpu.xml
/usr/libexec/valgrind/mips64-fpu-valgrind-s1.xml
/usr/libexec/valgrind/mips64-fpu-valgrind-s2.xml
/usr/libexec/valgrind/mips64-fpu.xml
/usr/libexec/valgrind/mips64-linux-valgrind.xml
/usr/libexec/valgrind/mips64-linux.xml
/usr/libexec/valgrind/none-amd64-linux
/usr/libexec/valgrind/power-altivec-valgrind-s1.xml
/usr/libexec/valgrind/power-altivec-valgrind-s2.xml
/usr/libexec/valgrind/power-altivec.xml
/usr/libexec/valgrind/power-core-valgrind-s1.xml
/usr/libexec/valgrind/power-core-valgrind-s2.xml
/usr/libexec/valgrind/power-core.xml
/usr/libexec/valgrind/power-fpu-valgrind-s1.xml
/usr/libexec/valgrind/power-fpu-valgrind-s2.xml
/usr/libexec/valgrind/power-fpu.xml
/usr/libexec/valgrind/power-linux-valgrind-s1.xml
/usr/libexec/valgrind/power-linux-valgrind-s2.xml
/usr/libexec/valgrind/power-linux.xml
/usr/libexec/valgrind/power-vsx-valgrind-s1.xml
/usr/libexec/valgrind/power-vsx-valgrind-s2.xml
/usr/libexec/valgrind/power-vsx.xml
/usr/libexec/valgrind/power64-core-valgrind-s1.xml
/usr/libexec/valgrind/power64-core-valgrind-s2.xml
/usr/libexec/valgrind/power64-core.xml
/usr/libexec/valgrind/power64-core2-valgrind-s1.xml
/usr/libexec/valgrind/power64-core2-valgrind-s2.xml
/usr/libexec/valgrind/power64-linux-valgrind-s1.xml
/usr/libexec/valgrind/power64-linux-valgrind-s2.xml
/usr/libexec/valgrind/power64-linux.xml
/usr/libexec/valgrind/powerpc-altivec32l-valgrind.xml
/usr/libexec/valgrind/powerpc-altivec32l.xml
/usr/libexec/valgrind/powerpc-altivec64l-valgrind.xml
/usr/libexec/valgrind/powerpc-altivec64l.xml
/usr/libexec/valgrind/s390-acr-valgrind-s1.xml
/usr/libexec/valgrind/s390-acr-valgrind-s2.xml
/usr/libexec/valgrind/s390-acr.xml
/usr/libexec/valgrind/s390-fpr-valgrind-s1.xml
/usr/libexec/valgrind/s390-fpr-valgrind-s2.xml
/usr/libexec/valgrind/s390-fpr.xml
/usr/libexec/valgrind/s390-vx-valgrind-s1.xml
/usr/libexec/valgrind/s390-vx-valgrind-s2.xml
/usr/libexec/valgrind/s390-vx.xml
/usr/libexec/valgrind/s390x-core64-valgrind-s1.xml
/usr/libexec/valgrind/s390x-core64-valgrind-s2.xml
/usr/libexec/valgrind/s390x-core64.xml
/usr/libexec/valgrind/s390x-generic-valgrind.xml
/usr/libexec/valgrind/s390x-generic.xml
/usr/libexec/valgrind/s390x-linux64-valgrind-s1.xml
/usr/libexec/valgrind/s390x-linux64-valgrind-s2.xml
/usr/libexec/valgrind/s390x-linux64.xml
/usr/libexec/valgrind/s390x-vx-linux-valgrind.xml
/usr/libexec/valgrind/s390x-vx-linux.xml
/usr/libexec/valgrind/vgpreload_core-amd64-linux.so
/usr/libexec/valgrind/vgpreload_dhat-amd64-linux.so
/usr/libexec/valgrind/vgpreload_drd-amd64-linux.so
/usr/libexec/valgrind/vgpreload_helgrind-amd64-linux.so
/usr/libexec/valgrind/vgpreload_massif-amd64-linux.so
/usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/valgrind/00921e181567bf8fdfbc06375d10ed399d48b185
/usr/share/package-licenses/valgrind/4b3d52fc140815bc03cbab3184a6be494eb808da
/usr/share/package-licenses/valgrind/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/valgrind/61ef372f94283a2e8909d8a5b7516abe2550fbbe
/usr/share/package-licenses/valgrind/fcbf818f92ef8679a88f3778b12b4c8b5810545b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/callgrind_annotate.1
/usr/share/man/man1/callgrind_control.1
/usr/share/man/man1/cg_annotate.1
/usr/share/man/man1/cg_diff.1
/usr/share/man/man1/cg_merge.1
/usr/share/man/man1/ms_print.1
/usr/share/man/man1/valgrind-di-server.1
/usr/share/man/man1/valgrind-listener.1
/usr/share/man/man1/valgrind.1
/usr/share/man/man1/vgdb.1
