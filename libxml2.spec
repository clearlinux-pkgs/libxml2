#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxml2
Version  : 2.9.10
Release  : 88
URL      : https://gitlab.gnome.org/GNOME/libxml2/-/archive/v2.9.10/libxml2-v2.9.10.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/libxml2/-/archive/v2.9.10/libxml2-v2.9.10.tar.gz
Summary  : libXML library version2.
Group    : Development/Tools
License  : MIT
Requires: libxml2-bin = %{version}-%{release}
Requires: libxml2-lib = %{version}-%{release}
Requires: libxml2-license = %{version}-%{release}
Requires: libxml2-man = %{version}-%{release}
Requires: libxml2-python = %{version}-%{release}
Requires: libxml2-python3 = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-gnome
BuildRequires : bzip2-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32icu-i18n)
BuildRequires : pkgconfig(32liblzma)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: libxml2-update.patch
Patch2: stateless.patch

%description
XML toolkit from the GNOME project
Full documentation is available on-line at
http://xmlsoft.org/

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
%setup -q -n libxml2-v2.9.10
cd %{_builddir}/libxml2-v2.9.10
%patch1 -p1
%patch2 -p1
pushd ..
cp -a libxml2-v2.9.10 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607987948
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %autogen --disable-static
make  %{?_smp_mflags}

make dba100000.xml
./xmllint --noout  dba100000.xml
./xmllint --stream  dba100000.xml
./xmllint --noout --valid test/valid/REC-xml-19980210.xml
./xmllint --stream --valid test/valid/REC-xml-19980210.xml
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static  --without-python --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1607987948
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libxml2
cp %{_builddir}/libxml2-v2.9.10/Copyright %{buildroot}/usr/share/package-licenses/libxml2/3c21506a45e8d0171fc92fd4ff6903c13adde660
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## install_append content
make clean
%configure --with-python=/usr/bin/python3
make %{_smp_mflags}
%make_install
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib32/xml2Conf.sh
/usr/lib64/xml2Conf.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint

%files dev
%defattr(-,root,root,-)
/usr/include/libxml2/libxml/DOCBparser.h
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
/usr/share/aclocal/*.m4
/usr/share/man/man3/libxml.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/libxml2/libxml2-config.cmake
/usr/lib32/libxml2.so
/usr/lib32/pkgconfig/32libxml-2.0.pc
/usr/lib32/pkgconfig/libxml-2.0.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libxml2/*
/usr/share/doc/libxml2-2.9.10/Copyright
/usr/share/doc/libxml2-2.9.10/examples/testHTML.c
/usr/share/doc/libxml2-2.9.10/examples/testSAX.c
/usr/share/doc/libxml2-2.9.10/examples/testXPath.c
/usr/share/doc/libxml2-2.9.10/examples/xmllint.c
/usr/share/doc/libxml2-2.9.10/html/DOM.gif
/usr/share/doc/libxml2-2.9.10/html/FAQ.html
/usr/share/doc/libxml2-2.9.10/html/Libxml2-Logo-180x168.gif
/usr/share/doc/libxml2-2.9.10/html/Libxml2-Logo-90x34.gif
/usr/share/doc/libxml2-2.9.10/html/encoding.html
/usr/share/doc/libxml2-2.9.10/html/examples.xml
/usr/share/doc/libxml2-2.9.10/html/examples.xsl
/usr/share/doc/libxml2-2.9.10/html/html/book1.html
/usr/share/doc/libxml2-2.9.10/html/html/home.png
/usr/share/doc/libxml2-2.9.10/html/html/index.html
/usr/share/doc/libxml2-2.9.10/html/html/left.png
/usr/share/doc/libxml2-2.9.10/html/html/libxml-DOCBparser.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-HTMLparser.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-HTMLtree.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-SAX.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-SAX2.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-c14n.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-catalog.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-chvalid.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-debugXML.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-dict.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-encoding.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-entities.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-globals.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-hash.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-lib.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-list.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-nanoftp.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-nanohttp.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-parser.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-parserInternals.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-pattern.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-relaxng.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-schemasInternals.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-schematron.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-threads.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-tree.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-uri.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-valid.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xinclude.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xlink.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlIO.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlautomata.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlerror.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlexports.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlmemory.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlmodule.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlreader.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlregexp.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlsave.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlschemas.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlschemastypes.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlstring.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlunicode.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlversion.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xmlwriter.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xpath.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xpathInternals.html
/usr/share/doc/libxml2-2.9.10/html/html/libxml-xpointer.html
/usr/share/doc/libxml2-2.9.10/html/html/right.png
/usr/share/doc/libxml2-2.9.10/html/html/up.png
/usr/share/doc/libxml2-2.9.10/html/index.html
/usr/share/doc/libxml2-2.9.10/html/io1.c
/usr/share/doc/libxml2-2.9.10/html/io1.res
/usr/share/doc/libxml2-2.9.10/html/io2.c
/usr/share/doc/libxml2-2.9.10/html/io2.res
/usr/share/doc/libxml2-2.9.10/html/libxml.gif
/usr/share/doc/libxml2-2.9.10/html/parse1.c
/usr/share/doc/libxml2-2.9.10/html/parse2.c
/usr/share/doc/libxml2-2.9.10/html/parse3.c
/usr/share/doc/libxml2-2.9.10/html/parse4.c
/usr/share/doc/libxml2-2.9.10/html/reader1.c
/usr/share/doc/libxml2-2.9.10/html/reader1.res
/usr/share/doc/libxml2-2.9.10/html/reader2.c
/usr/share/doc/libxml2-2.9.10/html/reader3.c
/usr/share/doc/libxml2-2.9.10/html/reader3.res
/usr/share/doc/libxml2-2.9.10/html/reader4.c
/usr/share/doc/libxml2-2.9.10/html/reader4.res
/usr/share/doc/libxml2-2.9.10/html/redhat.gif
/usr/share/doc/libxml2-2.9.10/html/smallfootonly.gif
/usr/share/doc/libxml2-2.9.10/html/structure.gif
/usr/share/doc/libxml2-2.9.10/html/test1.xml
/usr/share/doc/libxml2-2.9.10/html/test2.xml
/usr/share/doc/libxml2-2.9.10/html/test3.xml
/usr/share/doc/libxml2-2.9.10/html/testWriter.c
/usr/share/doc/libxml2-2.9.10/html/tree1.c
/usr/share/doc/libxml2-2.9.10/html/tree1.res
/usr/share/doc/libxml2-2.9.10/html/tree2.c
/usr/share/doc/libxml2-2.9.10/html/tree2.res
/usr/share/doc/libxml2-2.9.10/html/tst.xml
/usr/share/doc/libxml2-2.9.10/html/tutorial/apa.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/apb.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/apc.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/apd.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ape.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/apf.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/apg.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/aph.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/api.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s02.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s03.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s04.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s05.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s06.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s07.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s08.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ar01s09.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/customfo.xsl
/usr/share/doc/libxml2-2.9.10/html/tutorial/customhtml.xsl
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/blank.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/1.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/10.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/2.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/3.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/4.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/5.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/6.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/7.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/8.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/callouts/9.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/caution.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/draft.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/home.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/important.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/next.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/note.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/prev.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/tip.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/toc-blank.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/toc-minus.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/toc-plus.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/up.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/images/warning.png
/usr/share/doc/libxml2-2.9.10/html/tutorial/includeaddattribute.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/includeaddkeyword.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/includeconvert.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/includegetattribute.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/includekeyword.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/includestory.xml
/usr/share/doc/libxml2-2.9.10/html/tutorial/includexpath.c
/usr/share/doc/libxml2-2.9.10/html/tutorial/index.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/ix01.html
/usr/share/doc/libxml2-2.9.10/html/tutorial/xmltutorial.pdf
/usr/share/doc/libxml2-2.9.10/html/tutorial/xmltutorial.xml
/usr/share/doc/libxml2-2.9.10/html/w3c.png
/usr/share/doc/libxml2-2.9.10/html/writer.xml
/usr/share/doc/libxml2-2.9.10/html/xml.html
/usr/share/doc/libxml2-2.9.10/html/xpath1.c
/usr/share/doc/libxml2-2.9.10/html/xpath1.res
/usr/share/doc/libxml2-2.9.10/html/xpath2.c
/usr/share/doc/libxml2-2.9.10/html/xpath2.res
/usr/share/doc/libxml2-python-2.9.10/TODO
/usr/share/doc/libxml2-python-2.9.10/examples/attribs.py
/usr/share/doc/libxml2-python-2.9.10/examples/build.py
/usr/share/doc/libxml2-python-2.9.10/examples/compareNodes.py
/usr/share/doc/libxml2-python-2.9.10/examples/ctxterror.py
/usr/share/doc/libxml2-python-2.9.10/examples/cutnpaste.py
/usr/share/doc/libxml2-python-2.9.10/examples/dtdvalid.py
/usr/share/doc/libxml2-python-2.9.10/examples/error.py
/usr/share/doc/libxml2-python-2.9.10/examples/inbuf.py
/usr/share/doc/libxml2-python-2.9.10/examples/indexes.py
/usr/share/doc/libxml2-python-2.9.10/examples/input_callback.py
/usr/share/doc/libxml2-python-2.9.10/examples/invalid.xml
/usr/share/doc/libxml2-python-2.9.10/examples/nsdel.py
/usr/share/doc/libxml2-python-2.9.10/examples/outbuf.py
/usr/share/doc/libxml2-python-2.9.10/examples/push.py
/usr/share/doc/libxml2-python-2.9.10/examples/pushSAX.py
/usr/share/doc/libxml2-python-2.9.10/examples/pushSAXhtml.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader2.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader3.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader4.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader5.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader6.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader7.py
/usr/share/doc/libxml2-python-2.9.10/examples/reader8.py
/usr/share/doc/libxml2-python-2.9.10/examples/readererr.py
/usr/share/doc/libxml2-python-2.9.10/examples/readernext.py
/usr/share/doc/libxml2-python-2.9.10/examples/regexp.py
/usr/share/doc/libxml2-python-2.9.10/examples/relaxng.py
/usr/share/doc/libxml2-python-2.9.10/examples/resolver.py
/usr/share/doc/libxml2-python-2.9.10/examples/schema.py
/usr/share/doc/libxml2-python-2.9.10/examples/serialize.py
/usr/share/doc/libxml2-python-2.9.10/examples/sync.py
/usr/share/doc/libxml2-python-2.9.10/examples/test.dtd
/usr/share/doc/libxml2-python-2.9.10/examples/thread2.py
/usr/share/doc/libxml2-python-2.9.10/examples/tst.py
/usr/share/doc/libxml2-python-2.9.10/examples/tst.xml
/usr/share/doc/libxml2-python-2.9.10/examples/tstLastError.py
/usr/share/doc/libxml2-python-2.9.10/examples/tstURI.py
/usr/share/doc/libxml2-python-2.9.10/examples/tstmem.py
/usr/share/doc/libxml2-python-2.9.10/examples/tstxpath.py
/usr/share/doc/libxml2-python-2.9.10/examples/valid.xml
/usr/share/doc/libxml2-python-2.9.10/examples/validDTD.py
/usr/share/doc/libxml2-python-2.9.10/examples/validRNG.py
/usr/share/doc/libxml2-python-2.9.10/examples/validSchemas.py
/usr/share/doc/libxml2-python-2.9.10/examples/validate.py
/usr/share/doc/libxml2-python-2.9.10/examples/walker.py
/usr/share/doc/libxml2-python-2.9.10/examples/xpath.py
/usr/share/doc/libxml2-python-2.9.10/examples/xpathext.py
/usr/share/doc/libxml2-python-2.9.10/examples/xpathleak.py
/usr/share/doc/libxml2-python-2.9.10/examples/xpathns.py
/usr/share/doc/libxml2-python-2.9.10/examples/xpathret.py
/usr/share/gtk-doc/html/libxml2/general.html
/usr/share/gtk-doc/html/libxml2/home.png
/usr/share/gtk-doc/html/libxml2/index.html
/usr/share/gtk-doc/html/libxml2/left.png
/usr/share/gtk-doc/html/libxml2/libxml2-DOCBparser.html
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
/usr/share/gtk-doc/html/libxml2/libxml2.devhelp
/usr/share/gtk-doc/html/libxml2/right.png
/usr/share/gtk-doc/html/libxml2/style.css
/usr/share/gtk-doc/html/libxml2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxml2.so.2
/usr/lib64/libxml2.so.2.9.10

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libxml2.so.2
/usr/lib32/libxml2.so.2.9.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libxml2/3c21506a45e8d0171fc92fd4ff6903c13adde660

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xml2-config.1
/usr/share/man/man1/xmlcatalog.1
/usr/share/man/man1/xmllint.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
