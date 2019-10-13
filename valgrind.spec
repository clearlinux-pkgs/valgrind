%define keepstatic 1

Name     : valgrind
Version  : 3.15.0
Release  : 34
URL      : ftp://sourceware.org/pub/valgrind/valgrind-3.15.0.tar.bz2
Source0  : ftp://sourceware.org/pub/valgrind/valgrind-3.15.0.tar.bz2
Summary  : Valgrind Memory Debugger
Group    : Development/Tools
License  : GPL-2.0+ GFDL-1.2 GPL-2.0
Requires: valgrind-bin
Requires: valgrind-doc
Requires: valgrind-libexec
BuildRequires : sed
BuildRequires : zlib-dev
BuildRequires : libxml2-dev
#BuildRequires : openmpi-dev
BuildRequires : boost-dev

Patch1: glibc-2.21.patch
Patch2: 0001-Accept-glibc-2.21-as-valid.patch

%description


%package bin
Summary: bin components for the valgrind package.
Group: Binaries
Requires: valgrind-libexec = %{version}-%{release}

%description bin
bin components for the valgrind package.


%package dev
Summary: dev components for the valgrind package.
Group: Development
Requires: valgrind-bin
Requires: valgrind

%description dev
dev components for the valgrind package.


%package doc
Summary: doc components for the valgrind package.
Group: Documentation

%description doc
doc components for the valgrind package.


%package libexec
Summary: libexec components for the valgrind package.
Group: Default

%description libexec
libexec components for the valgrind package.


%prep
%setup -q -n valgrind-3.15.0
%patch1 -p1
%patch2 -p1

%build
# -fexceptions causes memcheck link command to fail when built with GCC 5.1
export CFLAGS=`echo $CFLAGS | sed s,-fexceptions,,g | sed s:-Wp,-D_FORTIFY_SOURCE=2::g | sed s:-fstack-protector::g `
./autogen.sh
%configure --enable-static --enable-only64bit --enable-tls
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check ||:
/usr/bin/perl tests/vg_regtest cachegrind ||:
/usr/bin/perl tests/vg_regtest callgrind ||:
/usr/bin/perl tests/vg_regtest massif ||:
/usr/bin/perl tests/vg_regtest lackey ||:
/usr/bin/perl tests/vg_regtest helgrind ||:
/usr/bin/perl tests/vg_regtest drd ||:
/usr/bin/perl tests/vg_regtest dhat ||:

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/valgrind/*.xml
/usr/lib64/valgrind/vgpreload_core-*-linux.so
/usr/lib64/valgrind/vgpreload_dhat-*-linux.so
/usr/lib64/valgrind/vgpreload_drd-*-linux.so
/usr/lib64/valgrind/vgpreload_exp-sgcheck-*-linux.so
/usr/lib64/valgrind/vgpreload_helgrind-*-linux.so
/usr/lib64/valgrind/vgpreload_massif-*-linux.so
/usr/lib64/valgrind/vgpreload_memcheck-*-linux.so
/usr/lib64/valgrind/cachegrind-amd64-linux
/usr/lib64/valgrind/callgrind-amd64-linux
/usr/lib64/valgrind/default.supp
/usr/lib64/valgrind/drd-amd64-linux
/usr/lib64/valgrind/exp-bbv-amd64-linux
/usr/lib64/valgrind/dhat-amd64-linux
/usr/lib64/valgrind/exp-sgcheck-amd64-linux
/usr/lib64/valgrind/getoff-amd64-linux
/usr/lib64/valgrind/helgrind-amd64-linux
/usr/lib64/valgrind/lackey-amd64-linux
#/usr/lib64/valgrind/libmpiwrap-amd64-linux.so
/usr/lib64/valgrind/massif-amd64-linux
/usr/lib64/valgrind/memcheck-amd64-linux
/usr/lib64/valgrind/none-amd64-linux
/usr/lib64/valgrind/libcoregrind-amd64-linux.a
/usr/lib64/valgrind/libreplacemalloc_toolpreload-amd64-linux.a
/usr/lib64/valgrind/libvex-amd64-linux.a
/usr/lib64/valgrind/libvexmultiarch-amd64-linux.a

%files libexec
%defattr(-,root,root,-)
/usr/libexec/valgrind/dh_view.css
/usr/libexec/valgrind/dh_view.html
/usr/libexec/valgrind/dh_view.js

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
/usr/include/valgrind/*.h
/usr/include/valgrind/vki/vki-*.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/valgrind/*
%doc /usr/share/man/man1/*
