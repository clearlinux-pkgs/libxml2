#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v27
# autospec commit: 6aaa12f
#
Name     : libxml2
Version  : 2.14.3
Release  : 136
URL      : https://download.gnome.org/sources/libxml2/2.14/libxml2-2.14.3.tar.xz
Source0  : https://download.gnome.org/sources/libxml2/2.14/libxml2-2.14.3.tar.xz
Source1  : http://localhost/cgit/projects/libxml2-profile/snapshot/libxml2-profile-1.tar.bz2
Summary  : libXML library version2.
Group    : Development/Tools
License  : MIT
Requires: libxml2-bin = %{version}-%{release}
Requires: libxml2-lib = %{version}-%{release}
Requires: libxml2-license = %{version}-%{release}
Requires: libxml2-man = %{version}-%{release}
Requires: libxml2-python = %{version}-%{release}
Requires: libxml2-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : bzip2-dev
BuildRequires : file
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : icu4c-dev
BuildRequires : icu4c-dev32
BuildRequires : pkg-config
BuildRequires : python3-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: stateless.patch

%description
Module libxml2-python
=====================
This is the libxml2 python module, providing access to the
libxml2 and libxslt (if available) libraries. For general
informationss on those XML and XSLT libraries check their
web pages at:
https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home
and
https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home

%package bin
Summary: bin components for the libxml2 package.
Group: Binaries
Requires: libxml2-license = %{version}-%{release}

%description bin
bin components for the libxml2 package.


%package dev
Summary: dev components for the libxml2 package.
Group: Development
Requires: libxml2-lib = %{version}-%{release}
Requires: libxml2-bin = %{version}-%{release}
Provides: libxml2-devel = %{version}-%{release}
Requires: libxml2 = %{version}-%{release}

%description dev
dev components for the libxml2 package.


%package dev32
Summary: dev32 components for the libxml2 package.
Group: Default
Requires: libxml2-lib32 = %{version}-%{release}
Requires: libxml2-bin = %{version}-%{release}
Requires: libxml2-dev = %{version}-%{release}

%description dev32
dev32 components for the libxml2 package.


%package doc
Summary: doc components for the libxml2 package.
Group: Documentation
Requires: libxml2-man = %{version}-%{release}

%description doc
doc components for the libxml2 package.


%package lib
Summary: lib components for the libxml2 package.
Group: Libraries
Requires: libxml2-license = %{version}-%{release}

%description lib
lib components for the libxml2 package.


%package lib32
Summary: lib32 components for the libxml2 package.
Group: Default
Requires: libxml2-license = %{version}-%{release}

%description lib32
lib32 components for the libxml2 package.


%package license
Summary: license components for the libxml2 package.
Group: Default

%description license
license components for the libxml2 package.


%package man
Summary: man components for the libxml2 package.
Group: Default

%description man
man components for the libxml2 package.


%package python
Summary: python components for the libxml2 package.
Group: Default
Requires: libxml2-python3 = %{version}-%{release}

%description python
python components for the libxml2 package.


%package python3
Summary: python3 components for the libxml2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libxml2 package.


%prep
%setup -q -n libxml2-2.14.3
cd %{_builddir}
tar xf %{_sourcedir}/libxml2-profile-1.tar.bz2
cd %{_builddir}/libxml2-2.14.3
mkdir -p ../libxml2-profile
cp -r %{_builddir}/libxml2-profile-1/. %{_builddir}/libxml2-2.14.3/../libxml2-profile
%patch -P 1 -p1
pushd ..
cp -a libxml2-2.14.3 build32
popd
pushd ..
cp -a libxml2-2.14.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1748900785
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dicu=enabled \
-Dlegacy=enabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dicu=enabled \
-Dlegacy=enabled  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dicu=enabled \
-Dlegacy=enabled -Dpython=disabled builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../build32;
meson test -C builddir --print-errorlogs || : || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libxml2
cp %{_builddir}/libxml2-%{version}/Copyright %{buildroot}/usr/share/package-licenses/libxml2/f8e4e1e2a6be883608f0336e455f84155a3acb41 || :
cp %{_builddir}/libxml2-%{version}/result/html-tokenizer/NOTICE %{buildroot}/usr/share/package-licenses/libxml2/cd90d4fdec204501b3f17d48389036c5ff36a585 || :
cp %{_builddir}/libxml2-%{version}/test/html-tokenizer/NOTICE %{buildroot}/usr/share/package-licenses/libxml2/cd90d4fdec204501b3f17d48389036c5ff36a585 || :
cp %{_builddir}/libxml2-profile-1/Copyright %{buildroot}/usr/share/package-licenses/libxml2/8b8a61fcd505743acbe94866f4f73b2fdf1f359f || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xmlcatalog
/V3/usr/bin/xmllint
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint

%files dev
%defattr(-,root,root,-)
/usr/include/libxml2/libxml/HTMLparser.h
/usr/include/libxml2/libxml/HTMLtree.h
/usr/include/libxml2/libxml/SAX.h
/usr/include/libxml2/libxml/SAX2.h
/usr/include/libxml2/libxml/c14n.h
/usr/include/libxml2/libxml/catalog.h
/usr/include/libxml2/libxml/chvalid.h
/usr/include/libxml2/libxml/debugXML.h
/usr/include/libxml2/libxml/dict.h
/usr/include/libxml2/libxml/encoding.h
/usr/include/libxml2/libxml/entities.h
/usr/include/libxml2/libxml/globals.h
/usr/include/libxml2/libxml/hash.h
/usr/include/libxml2/libxml/list.h
/usr/include/libxml2/libxml/nanoftp.h
/usr/include/libxml2/libxml/nanohttp.h
/usr/include/libxml2/libxml/parser.h
/usr/include/libxml2/libxml/parserInternals.h
/usr/include/libxml2/libxml/pattern.h
/usr/include/libxml2/libxml/relaxng.h
/usr/include/libxml2/libxml/schemasInternals.h
/usr/include/libxml2/libxml/schematron.h
/usr/include/libxml2/libxml/threads.h
/usr/include/libxml2/libxml/tree.h
/usr/include/libxml2/libxml/uri.h
/usr/include/libxml2/libxml/valid.h
/usr/include/libxml2/libxml/xinclude.h
/usr/include/libxml2/libxml/xlink.h
/usr/include/libxml2/libxml/xmlIO.h
/usr/include/libxml2/libxml/xmlautomata.h
/usr/include/libxml2/libxml/xmlerror.h
/usr/include/libxml2/libxml/xmlexports.h
/usr/include/libxml2/libxml/xmlmemory.h
/usr/include/libxml2/libxml/xmlmodule.h
/usr/include/libxml2/libxml/xmlreader.h
/usr/include/libxml2/libxml/xmlregexp.h
/usr/include/libxml2/libxml/xmlsave.h
/usr/include/libxml2/libxml/xmlschemas.h
/usr/include/libxml2/libxml/xmlschemastypes.h
/usr/include/libxml2/libxml/xmlstring.h
/usr/include/libxml2/libxml/xmlunicode.h
/usr/include/libxml2/libxml/xmlversion.h
/usr/include/libxml2/libxml/xmlwriter.h
/usr/include/libxml2/libxml/xpath.h
/usr/include/libxml2/libxml/xpathInternals.h
/usr/include/libxml2/libxml/xpointer.h
/usr/lib64/cmake/libxml2/libxml2-config.cmake
/usr/lib64/libxml2.so
/usr/lib64/pkgconfig/libxml-2.0.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/libxml2/libxml2-config.cmake
/usr/lib32/libxml2.so
/usr/lib32/pkgconfig/32libxml-2.0.pc
/usr/lib32/pkgconfig/libxml-2.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libxml2/*
/usr/share/gtk-doc/html/libxml2/general.html
/usr/share/gtk-doc/html/libxml2/home.png
/usr/share/gtk-doc/html/libxml2/index.html
/usr/share/gtk-doc/html/libxml2/left.png
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLparser.html
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLtree.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX2.html
/usr/share/gtk-doc/html/libxml2/libxml2-c14n.html
/usr/share/gtk-doc/html/libxml2/libxml2-catalog.html
/usr/share/gtk-doc/html/libxml2/libxml2-chvalid.html
/usr/share/gtk-doc/html/libxml2/libxml2-debugXML.html
/usr/share/gtk-doc/html/libxml2/libxml2-dict.html
/usr/share/gtk-doc/html/libxml2/libxml2-encoding.html
/usr/share/gtk-doc/html/libxml2/libxml2-entities.html
/usr/share/gtk-doc/html/libxml2/libxml2-globals.html
/usr/share/gtk-doc/html/libxml2/libxml2-hash.html
/usr/share/gtk-doc/html/libxml2/libxml2-list.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanoftp.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanohttp.html
/usr/share/gtk-doc/html/libxml2/libxml2-parser.html
/usr/share/gtk-doc/html/libxml2/libxml2-parserInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-pattern.html
/usr/share/gtk-doc/html/libxml2/libxml2-relaxng.html
/usr/share/gtk-doc/html/libxml2/libxml2-schemasInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-schematron.html
/usr/share/gtk-doc/html/libxml2/libxml2-threads.html
/usr/share/gtk-doc/html/libxml2/libxml2-tree.html
/usr/share/gtk-doc/html/libxml2/libxml2-uri.html
/usr/share/gtk-doc/html/libxml2/libxml2-valid.html
/usr/share/gtk-doc/html/libxml2/libxml2-xinclude.html
/usr/share/gtk-doc/html/libxml2/libxml2-xlink.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlIO.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlautomata.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlerror.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlexports.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmemory.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmodule.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlreader.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlregexp.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlsave.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemas.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemastypes.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlstring.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlunicode.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlversion.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlwriter.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpath.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpathInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpointer.html
/usr/share/gtk-doc/html/libxml2/libxml2.devhelp2
/usr/share/gtk-doc/html/libxml2/right.png
/usr/share/gtk-doc/html/libxml2/style.css
/usr/share/gtk-doc/html/libxml2/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libxml2.so.16.0.3
/usr/lib64/libxml2.so.16
/usr/lib64/libxml2.so.16.0.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libxml2.so.16
/usr/lib32/libxml2.so.16.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libxml2/8b8a61fcd505743acbe94866f4f73b2fdf1f359f
/usr/share/package-licenses/libxml2/cd90d4fdec204501b3f17d48389036c5ff36a585
/usr/share/package-licenses/libxml2/f8e4e1e2a6be883608f0336e455f84155a3acb41

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xml2-config.1
/usr/share/man/man1/xmlcatalog.1
/usr/share/man/man1/xmllint.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
